# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''


class Solution:
    # 递归
    # def fib(n):
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return fib(n - 1) + fib(n - 2)



    def Fibonacci(self, n):
        tempArr = [0, 1]
        fibOne = 0
        fibTwo = 1
        fibCurrent = 0
        if (n<2):
            return tempArr[n]
        if n >= 2:
            for i in range(2, n+1):
                fibCurrent = fibOne + fibTwo
                fibOne =fibTwo
                fibTwo = fibCurrent
        return fibCurrent



test = Solution()
print(test.Fibonacci(5))
# print(test.fib(5))