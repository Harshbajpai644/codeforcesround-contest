class Solution {
public:
    int numberOfSpecialChars(string word) {
        set<char> chars(word.begin(), word.end());
        int count = 0;
        for (char c = 'a'; c <= 'z'; c++) {
            if (chars.count(c) && chars.count(toupper(c)))
                count++;
        }
        return count;
    }
};
