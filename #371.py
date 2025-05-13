class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0: #a, b同號, a + b的情況
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else: #a, b異號, a - b的情況
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign
'''
2023.04.10
1.failed
'''
#