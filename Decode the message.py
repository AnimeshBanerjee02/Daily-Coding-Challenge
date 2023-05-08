class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        sub_table = []
        
        
        for ch in key:
            if ch.isalpha() and ch.lower() not in sub_table:
                sub_table.append(ch.lower())
        
        
        for i in range(97, 123):
            ch = chr(i)
            if ch not in sub_table:
                sub_table.append(ch)
        
        
        sub_dict = {}
        for i in range(26):
            sub_dict[sub_table[i]] = chr(97+i)
        
       
        decoded_message = ''
        for ch in message:
            if ch == ' ':
                decoded_message += ' '
            elif ch in sub_dict:
                decoded_message += sub_dict[ch]
        
        return decoded_message
