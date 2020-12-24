class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            short_ele = strs[0] #找出lst中最小值並移除
            for ele in strs:
                if len(ele) < len(short_ele):
                    short_ele = ele
            strs.remove(short_ele)
            cpre = "" #用來存共同值
            n = 0 #strs中每個值的第幾字元
            for i in short_ele: #取最小值的每字元
                presame = False #預設不相同
                for str in strs: #取strs中每個值
                    presame = False
                    if str[n] == i: #如果相同
                        presame = True
                    elif presame == False: #只要一個不同就跳出迴圈
                        break;
                if presame == True: #相同就加入共同值
                    cpre += i
                else:
                    break
                n += 1
            return cpre
