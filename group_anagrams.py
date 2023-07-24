class Solution:
    def groupAnagrams(self, strs):
        lookup = {}
        for index, string in enumerate(strs):
            sorted_string = "".join(sorted(string))
            if sorted_string not in lookup:
                lookup[sorted_string] = [string]
            else:
                lookup[sorted_string].append(string)
        return lookup.values()


input_strings = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(input_strings))
