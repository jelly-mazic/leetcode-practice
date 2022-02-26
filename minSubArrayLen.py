"""
题目描述：
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和≥s的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
from ctypes.wintypes import tagRECT
import re
from typing import List
from wsgiref.simple_server import demo_app


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        解法要点：
        * 窗口的定义，在于起始位置和结束位置的定义。
        * 即在迭代过程中，使用何种逻辑进行起始指针和结束指针的逻辑操作。
        * 使用for循环来遍历数组，使用while循环来控制目标对象的逻辑判断。
        * 注意异常情况：当target不存在的时候。
        """
        # 定义指针。
        size = len(nums)
        i,j = 0,0
        sum ,res= 0,size + 1
        # 定义迭代过程。
        for j in range(size):
            sum+=nums[j]
            while sum >= target :
                sum-=nums[i]
                resT = j-i+1
                if res > resT:
                    res = resT
                i+=1
        return 0 if res == size + 1 else res

demo = Solution()
mylist = [2,3,1,2,4,3]
print("before:")
print(mylist)
result = demo.minSubArrayLen(90,mylist)
print("after:")
print(result)
