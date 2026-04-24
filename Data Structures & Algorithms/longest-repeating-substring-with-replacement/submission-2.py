class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        frequency = [0] * 26
        res = 0

        while right < len(s):
            # How big is our window?
            window_length = right - left + 1
            # Update the count here so our math is correct in the validation
            frequency[ord(s[right]) - ord("A")] += 1
            # Is our window valid (i.e. can we replace up to k characters?)
            is_valid = window_length - max(frequency) <= k

            if is_valid:
                # update our max
                res = max(window_length, res)
                # Expand to the right
                right += 1
            else:
                # We remove the count
                frequency[ord(s[left]) - ord("A")] -= 1
                # And now we can shrink from the left and expand from the right
                left += 1
                right += 1

        return res
