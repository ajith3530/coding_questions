class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        def check_palindrome(input_string):
            low, high = 0, len(input_string) - 1
            while low < high:
                if input_string[low] is not input_string[high]:
                    return False
                low += 1
                high -= 1
            return True

        max_lenght = 0
        start_index = 0
        end_index = len(s) + 1
        while end_index > start_index:
            lenght = len(s[start_index:end_index])
            if check_palindrome(s[start_index:end_index]):
                if lenght > max_lenght:
                    longest_palindrome = s[start_index:end_index]
                    max_lenght = lenght
            end_index -= 1
            start_index += 1
        return longest_palindrome


