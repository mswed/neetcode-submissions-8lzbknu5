class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            hashed_word = self._build_hash(word)
            if hashed_word in mapping:
                mapping[hashed_word].append(word)
            else:
                mapping[hashed_word] = [word]

        return list(mapping.values())

    def letter_to_number(self, letter):
        return ord(letter) - 96

    def _build_hash(self, word):
        charaters = [0 for i in range(26)]
        for char in word:
            number = self.letter_to_number(char) - 1
            charaters[number] += 1

        return str(charaters)
