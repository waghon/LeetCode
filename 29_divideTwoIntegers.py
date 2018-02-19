class Solution:
    def divide(self, dividend, divisor):
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        elif dividend == MIN_INT and divisor == -1:
            return MAX_INT
        elif dividend == 0:
            return 0
        isPos = not bool(((dividend ^ divisor) >> 31) & 1)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            bitMover = 0
            while (divisor << bitMover) <= (dividend >> 1):
                bitMover += 1
            result += 1 << bitMover
            dividend -= divisor << bitMover
        return result if isPos else -result

solution = Solution()
dividend = int(input())
divisor = int(input())
print(solution.divide(dividend, divisor))
