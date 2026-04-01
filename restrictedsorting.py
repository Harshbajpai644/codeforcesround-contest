import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    results = []
    
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        
        sorted_a = sorted(a)
        
        if a == sorted_a:
            results.append("-1")
            continue
        
        v_min = sorted_a[0]
        v_max = sorted_a[-1]
        
        k = float('inf')
        
        for i in range(n):
            if a[i] != sorted_a[i]:
                diff = max(abs(a[i] - v_min), abs(a[i] - v_max))
                k = min(k, diff)
        
        results.append(str(k))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()