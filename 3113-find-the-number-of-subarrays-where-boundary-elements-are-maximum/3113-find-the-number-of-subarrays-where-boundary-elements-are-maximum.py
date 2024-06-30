class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # Observations:
        # 1. Larger element cannot be present in the middle
        # 2. A subarray of length > 1 is only formed if both ends are max and equal
        # 3. If number is less than or equal to top then put it in the stack else continue popping the elements
        
        st = []
        n = len(nums)
        ans = 0
        for i in range(n):
            while st and st[-1][0] < nums[i]: 
                if nums[i] != st[-1][0]: ans += st.pop()[-1]
            if st and st[-1][0] == nums[i]: st.append((nums[i], st[-1][1] + 1))
            else: st.append((nums[i], 1))
        
        while st: ans += st.pop()[1]
        
        return ans
        