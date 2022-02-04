# 程序的起始
# 程序的结束
# 程序的迭代过程
# while 循环条件
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right)/2
            if nums[middle] < target:
                left = middle + 1
            if target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return -1
