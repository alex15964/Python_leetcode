class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1, -len(digits)-1, -1): #從最後一位開始先+1
            digits[i] += 1
            if digits[i] == 10: #如果是10，則變成0
                digits[i] = 0
                if -i == len(digits): #如果是第一位(倒數跟長度會相同)，在前面插入1
                    digits.insert(0, 1)
                    break
            else: #不是10就跳出
                break
        return digits
