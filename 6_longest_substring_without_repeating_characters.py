class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_length = 0
        start = 0

        for i in range(len(s)):
            char = s[i]
            # If the character is in the map and within the current window
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # Move the start pointer

            char_index[char] = i  # Update or add character index
            max_length = max(max_length, i - start + 1)  # Update max length

        return max_length
