import math
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt_5=math.sqrt(5)
        golden_ratio=(1+sqrt_5)/2
        return int(round(((golden_ratio)**n)/sqrt_5))