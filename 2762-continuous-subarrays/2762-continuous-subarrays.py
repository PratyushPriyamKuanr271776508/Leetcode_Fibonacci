class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxQ = collections.deque([])
        minQ = collections.deque([])
        n = len(nums)
        i = j = 0
        ans = 0
        def insert(j):
            while maxQ and maxQ[-1] < nums[j]:
                maxQ.pop()
            maxQ.append(nums[j])

            while minQ and minQ[-1] > nums[j]:
                minQ.pop()
            minQ.append(nums[j])

        def remove(i):
            if maxQ and maxQ[0] == nums[i]: maxQ.popleft()
            if minQ and minQ[0] == nums[i]: minQ.popleft()

        while j < n:
            insert(j)
            while maxQ and minQ and maxQ[0] - minQ[0] > 2:
                remove(i)
                i += 1
            ans += j - i + 1
            j += 1
        
        return ans


            

            