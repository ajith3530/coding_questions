def lengthOfLongestSubstring(s: str) -> int:

    size, max_size = 0, 0
    lookup = set()
    start, end = 0, 0
    for index, char in enumerate(s):
        if char in lookup:
            lookup.remove(s)
            start += 1
            while True:
                if char not in lookup:
                    break

        lookup.append(char)
        end += 1
        size = len(lookup)
        max_size = max(max_size, size)
    return max_size

print(lengthOfLongestSubstring("abba"))