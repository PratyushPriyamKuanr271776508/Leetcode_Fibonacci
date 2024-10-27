class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def canCreateAlloys(machine, num_alloys):
            required_metals = [composition[machine][i] * num_alloys for i in range(n)]
            total_cost = sum(max(0, required_metals[i] - stock[i]) * cost[i] for i in range(n))
            return total_cost <= budget

        left, right = 0, 10**9  # Binary search limits
        max_alloys = 0

        for machine in range(k):
            while left < right:
                mid = left + (right - left) // 2
                if canCreateAlloys(machine, mid):
                    left = mid + 1
                else:
                    right = mid

            max_alloys = max(max_alloys, left - 1)
            left, right = 0, 10**9

        return max_alloys
        