class Solution:
    def sumZero(self, n: int) -> List[int]:
        num  = [i for i in range(1, int(n/2)+1)] + [-i for i in range(1, int(n/2)+1)] #取正負抵銷
        return num if n % 2 == 0 else num + [0]
