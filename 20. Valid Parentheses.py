class Solution:
    def isValid(self, s: str) -> bool:        
        pstack = [] #存放左括號的list
        for p in s:
            if p == '(': #只要碰到左括號，就放入pstack
                pstack.append(p)
            elif p == '[':
                pstack.append(p)
            elif p == '{':
                pstack.append(p)
            elif p == ')': #如果碰到右括號，先檢查pstack是否空，如果是必定有錯，如不是則檢查是否相對應左括號，不是則有錯，是則從pstack移除最後一個左括號
                if len(pstack) == 0:
                    return False
                elif pstack[-1] != '(':
                    return False
                else:
                    pstack.pop()
            elif p == ']':
                if len(pstack) == 0:
                    return False
                elif pstack[-1] != '[':
                    return False
                else:
                    pstack.pop()
            elif p == '}':
                if len(pstack) == 0:
                    return False
                elif pstack[-1] != '{':
                    return False
                else:
                    pstack.pop()
        if len(pstack) == 0: #如果pstack為空則正確
            return True
        else:
            return False
