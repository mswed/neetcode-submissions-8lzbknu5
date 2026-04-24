import collections


class Solution:
    def is_valid(self, target, search):
        for c, count in target.items():
            if search[c] < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # Figure out which letters we'll be looking for
        # Can't use a set since there may be duplicates
        target = collections.defaultdict(int)
        for c in range(len(t)):
            target[t[c]] += 1

        # Create a window, starting at 0 0 of s
        l = 0
        r = 0
        options = {}

        search = collections.defaultdict(int)
        while r < len(s):
            # Start searching right
            search[s[r]] += 1

            # For each iteration, check if we found the characters AND count we need
            if self.is_valid(target, search):
                # start minimizing the left window
                while self.is_valid(target, search):
                    # This is a valid string update the count
                    search[s[l]] -= 1
                    if search[s[l]] == 0:
                        del search[s[l]]

                    # and add it as an option
                    options[r - l + 1] = s[l : r + 1]
                    l += 1

                # We no longer have a valid string from the left start searching right again
                r += 1
            else:
                r += 1

        # If we reached the end of s and didn't find anything return an empty string
        if options:
            return options[min(options.keys())]
        else:
            return ""

