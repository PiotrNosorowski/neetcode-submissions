class Solution:

    def encode(self, strs):
        self.one_string = []
        self.seq = []
        for word in strs:
            self.one_string.append(word)
            self.seq.append(len(word))
        
        self.s = "".join(self.one_string)

        return self.s
        
    def decode(self, s):
        str_of_chars = []

        comma_pos = 0
        for comma in self.seq:
            str_of_chars.append(s[comma_pos:comma_pos+comma])
            comma_pos = comma_pos+comma

        return str_of_chars
            