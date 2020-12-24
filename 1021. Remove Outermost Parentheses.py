class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        n = 0
        p = ''
        
        for i in S:
            if i == '(':
                n += 1
                
                if n > 1: #第一個(忽略
                    p += '('
                    
            if i == ')':
                n -= 1
                
                if n > 0: #最後一個)以外都忽略
                    p += ')'
                    
        return p
