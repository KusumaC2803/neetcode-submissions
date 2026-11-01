class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            #Find delimiter
            while s[j] != "#":
                j += 1
            #Extract the length
            length = int(s[i:j])
            #Extract the word
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            #move to the next encoded string
            i = j + 1 + length
        
        return result
