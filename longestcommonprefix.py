def longestCommonPrefix( strs) -> str:
    pref = ""

    for i in range(len(strs[0])):
        for string in strs:
            if i == len(string) or string[i] != strs[0][i]:
                return pref
        pref += strs[0][i]

print(longestCommonPrefix(["flower", "floe", "flows", "D"]))