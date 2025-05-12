class Solution:
    def longestCommonPrefix(self, strs):
        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Start by assuming the first word is the common prefix
        prefix = strs[0]

        # Loop through all the other strings
        for i in range(1, len(strs)):
            # Keep cutting the prefix until the current string starts with it
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]  # Remove last character

                # If prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""

        # Return the final common prefix
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: fl
