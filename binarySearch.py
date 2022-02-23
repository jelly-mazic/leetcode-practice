"""
题目描述:
给定一个 n 个元素有序的（升序）整型数组 nums 和一个
目标值 target  ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 
提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
"""
from ctypes.wintypes import tagRECT
from typing import List
from wsgiref.simple_server import demo_app


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        解法要点：
        • 程序的迭代过程。
        • 初始、结束状态定义。
        • 输入的数列nums必须是有序的，不能重复。
        • 每次迭代搜索范围要分清楚，分为：全闭和半开两种解法
        通过left 和 right指针迭代，求解。
        """

        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] < target:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return -1


demo = Solution()
mylist = [-1, 0, 3, 5, 9, 12]
a = 9
result = demo.search(mylist, a)
print(result)
