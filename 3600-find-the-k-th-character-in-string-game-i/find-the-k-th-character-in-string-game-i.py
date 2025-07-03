class Solution:
    def kthCharacter(self, k: int) -> str:
        curr = "a"  # Start with "a"

        # Keep building the string until length >= k
        while len(curr) < k:
            temp = ""
            for ch in curr:
                # Get the next character, wrap 'z' to 'a'
                next_ch = 'a' if ch == 'z' else chr(ord(ch) + 1)
                temp += next_ch
            curr += temp  # Append to the current string

        return curr[k - 1]  # Return the k-th character