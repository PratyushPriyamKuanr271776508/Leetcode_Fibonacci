import math
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find_fib(n):
            if n == 0: return (0, 1)
            nb2, nb2p1 = find_fib(n>>1) # We got here the value of n
            even = nb2*(2*nb2p1-nb2)
            odd = nb2p1**2 + nb2**2
            if n&1: return (odd, odd+even)
            else: return (even, odd)
        return find_fib(n)[0]