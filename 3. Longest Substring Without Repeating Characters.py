class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        my_str = ""
        for x in s:
            if x not in my_str:
                my_str += x
            else:
                if len(my_str) > max_l:
                    max_l = len(my_str)
                my_str = my_str[my_str.find(x)+1:]
                my_str += x
        max_l = max(max_l,len(my_str))
        return max_l