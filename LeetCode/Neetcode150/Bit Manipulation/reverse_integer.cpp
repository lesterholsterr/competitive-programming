// https://leetcode.com/problems/reverse-integer/description/
// Little confused why this was classified as "bit manipulation"

// Initial - much longer than it needs to be
#include <vector>
#include <climits> 
#include <cstdlib>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        if (x == INT_MIN) { // <-- can't absolute value this
            return 0;
        }

        vector<int> digits;
        bool isNeg = false;
        if (x < 0) {
            isNeg = true;
        }
        x = abs(x);

        while (x > 0) {
            int d = x % 10;
            if (!digits.empty() || d != 0) {
                digits.push_back(d);
            }
            x = (x - (x % 10)) / 10;
        }

        int ans = 0;
        for (int i = 0; i < digits.size(); ++i) {
            if (ans > INT_MAX / 10) {
                return 0;
            }
            ans *= 10;

            if (ans > INT_MAX - digits[i]) {
                return 0;
            }
            ans += digits[i];
        }

        if (isNeg) {
            ans *= -1;
        }

        return ans;
    }
};

// More condensed
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            int d = x % 10;
            x /= 10;
            if (ans > INT_MAX / 10 || (ans == INT_MAX / 10 && d > 7) || ans < INT_MIN / 10 || (ans == INT_MIN / 10 && d < -8)) {
                return 0;
            }
            ans = ans * 10 + d;
        }
        return ans;
    }
};