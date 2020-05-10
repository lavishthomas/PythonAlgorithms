
import time
tic = time.perf_counter()

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                print(current_num)
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

l = [5,2,101,102,98,99,100,3,4,1, 97]
a = Solution()        
toc = time.perf_counter()

print(a.longestConsecutive(l))
print(f"Downloaded the tutorial in {toc - tic} seconds")
