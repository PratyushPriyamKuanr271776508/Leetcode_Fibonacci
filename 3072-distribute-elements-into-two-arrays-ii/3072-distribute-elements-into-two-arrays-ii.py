from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize sorted lists for arr1 and arr2
        arr1, arr2 = SortedList(), SortedList()
        ans1, ans2 = [], []

        # Append the first two elements manually
        arr1.add(nums[0])
        arr2.add(nums[1])
        ans1.append(nums[0])
        ans2.append(nums[1])

        for i in range(2, len(nums)):
            # Using SortedList to find the greater count efficiently
            count1 = len(arr1) - arr1.bisect_right(nums[i])
            count2 = len(arr2) - arr2.bisect_right(nums[i])

            # Decide where to append nums[i]
            if count1 > count2:
                arr1.add(nums[i])
                ans1.append(nums[i])
            elif count1 < count2:
                arr2.add(nums[i])
                ans2.append(nums[i])
            else:
                # If counts are equal, check the sizes of arr1 and arr2
                if len(arr1) < len(arr2):
                    arr1.add(nums[i])
                    ans1.append(nums[i])
                elif len(arr2) < len(arr1):
                    arr2.add(nums[i])
                    ans2.append(nums[i])
                else:
                    # If sizes are also equal, default to arr1
                    arr1.add(nums[i])
                    ans1.append(nums[i])

        # Concatenate arr1 and arr2 for the result
        return ans1 + ans2