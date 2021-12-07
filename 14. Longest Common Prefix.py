class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            #get 1 char from each str and form a tuple: x in zip(*strs)
            #append current char into result when tuple has same char: len(set(x))==1

            ans=''
            for x in zip(*strs):
                if len(set(x))==1:
                    ans+=x[0]
                else:
                    break
            return ans
        