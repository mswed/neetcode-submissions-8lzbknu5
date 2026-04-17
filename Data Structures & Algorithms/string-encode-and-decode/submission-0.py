class Solution:
    def encode(self, strs: List[str]) -> str:
        encoder = []
        for s in strs:
            encoder.append(f"{len(s)}#")
            encoder.append(s)

        return "".join(encoder)

    def decode(self, s: str) -> List[str]:
        decoded = []
        current_index = 0
        word_end = 0
        while current_index <= len(s) - 1:
            current_char = s[current_index]
            if current_char == "#":
                length = int(s[word_end:current_index])
                word = s[current_index + 1 : current_index + 1 + length]
                decoded.append(word)
                current_index = current_index + 1 + length
                word_end = current_index

            current_index += 1

        return decoded


s = Solution()
send = s.encode(["Hello", "World"])
s.decode(send)
