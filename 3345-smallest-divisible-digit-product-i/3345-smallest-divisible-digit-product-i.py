class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Loop sequentially starting from n
        while True:
            if self.getDigitProduct(n) % t == 0:
                return n
            n += 1
            
    def getDigitProduct(self, num: int) -> int:
        prod = 1
        while num > 0:
            prod *= num % 10
            num //= 10
        return prod
