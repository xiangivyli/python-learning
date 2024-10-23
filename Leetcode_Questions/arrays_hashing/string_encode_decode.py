class Solution:

    def encode(self, strs: List[str]) -> str:
        # using length+# to connect each char
        join_strs = ""
        for char in strs:
            join_strs += str(len(char)) + "#" + char
        return join_strs


    def decode(self, s: str) -> List[str]:
        # using length+# to seperate the join_strs
        decode_list = [] # empty a list to store seperated strings
        i = 0 # starting point to read s
        while i < len(s):
            # give a read pointer
            j = i
            while s[j] != "#":
                j += 1
            # until j reaches the first "#" after length number
            # extract the length
            length = int(s[i:j])
            # extract the string from s
            decode_list.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decode_list

# trap: the length is possibly over 10, pure location method will make mistakes
# time complexity: O(n)
# space complexity: O(n)
