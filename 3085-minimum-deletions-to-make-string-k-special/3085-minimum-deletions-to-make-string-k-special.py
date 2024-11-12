class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = Counter(word).values()
        res = inf
        for x in A:
            cur = 0
            for a in A:
                cur += a if a < x else max(0, a - (x + k))
            res = min(res, cur)
        return res