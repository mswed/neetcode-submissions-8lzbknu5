class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        source = self._build_dict(s)
        target = self._build_dict(t)
        return source == target

    def _build_dict(self, text):
        result = {}
        for c in text:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1

        return result
