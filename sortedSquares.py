"""
题目描述：
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 
示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
"""
from ctypes.wintypes import tagRECT
import re
from typing import List
from wsgiref.simple_server import demo_app


class Solution:
    def sortedSquares(self,nums: List[int]) -> List[int]:
        """
        解法要点：
        * 双指针的用法。
        * 创建新的结果集。
        """
        # 定义指针。
        size = len(nums)
        i,j,n = 0,size-1,size-1
        # 定义结果数组。
        result = [-1]*size

        # 定义迭代过程。
        while i <= j:
            a = nums[i] *nums[i] 
            b = nums[j] *nums[j] 
            if a <= b :
                result[n] = b
                j-=1
            else :
                result[n] = a
                i+=1
            n-=1
        return result

demo = Solution()
mylist = [-8, 0, 3, 5, 9, 12]
print("before:")
print(mylist)
result = demo.sortedSquares(mylist)
print("after:")
print(result)
