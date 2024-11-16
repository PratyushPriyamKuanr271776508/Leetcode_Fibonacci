class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        st = []
        nextGreaterElement = [N] * N
        
        for i in range(N):
            while st and nums[st[-1]] < nums[i]: nextGreaterElement[st.pop()] = i
            st.append(i)
        
        dic = collections.defaultdict(list)
        
        for i in range(N): dic[nums[i]].append(i)
            
        def query(l, r, val):
            
            left = bisect.bisect_left(dic[val], l)
            right = bisect.bisect_left(dic[val], r)
            
            if right == len(dic[val]) or dic[val][right] > r: return right - left
            else: return right - left + 1
            
        ans = 0
        for i in range(N): ans += query(i, nextGreaterElement[i]-1, nums[i])
            
        return ans
            