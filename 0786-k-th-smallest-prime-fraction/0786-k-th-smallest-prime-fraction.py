class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def binary(ls, lo, hi, k):
            while lo < hi:
                mi = (lo + hi) / 2
                count, val1, val2 = fractionsOnleft(ls, mi)
                if count < k: lo = mi
                elif count > k: hi = mi
                else: return (val1, val2)
            return ()

        def fractionsOnleft(ls, mi):
            N = len(ls)
            i = 0
            nu, de = ls[0], ls[-1]
            count = 0
            for j in range(N):
                while ls[i] <= ls[j] * mi: i += 1
                count += i
                if i > 0 and ls[i-1]*de > ls[j] * nu:
                    nu = ls[i-1]
                    de = ls[j]
            return (count, nu, de)
        
        return binary(arr, arr[0]//arr[-1], 1, k)
        