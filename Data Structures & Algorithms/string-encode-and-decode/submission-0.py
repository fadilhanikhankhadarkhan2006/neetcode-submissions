class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            # Find '#'
            j = i
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract string
            result.append(s[j:j + length])

            # Move to next encoded string
            i = j + length

        return result
