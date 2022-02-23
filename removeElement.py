"""
题目描述：
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
示例 1: 给定 nums = [3,2,2,3], val = 3, 长度 2, 并且 nums 中的前两个元素均为 2。 
示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
链接：https://leetcode-cn.com/problems/remove-element/
"""
from ctypes.wintypes import tagRECT
from typing import List
from wsgiref.simple_server import demo_app


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        解法要点：
        通常对于数组题的解题，只是使用单一指针遍历元素操作。
        双指针——快慢指针
        则是一种使用两个指针来遍历数组元素，根据某种逻辑进行迭代。具体逻辑如下：
        * 开始阶段，两个指针指向同一元素。
        * 某个迭代，当发现特征元素时，快指针指向下一个元素，慢指针停留在特征元素上。
        * 当快指针遍历到数组尾，则结束迭代。
        解题关键点：
        * 原地移除数字。
        * 返回新数组的长度
        """
        # 定义快慢指针。
        fast, slow = 0, 0
        size = len(nums)
        # 定义迭代过程。
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


demo = Solution()
mylist = [1, 0, 9, 5, 9, 12]
a = 9
result = demo.removeElement(mylist, a)
print(result)
