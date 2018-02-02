# -*- coding:utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
        # http://www.cnblogs.com/edisonchou/p/4737944.html
        #     如果目标数等于第一行最后一个（角数）
        #         那么ok，true
        #      如果目标数不等于第一行最后一个
        #         目标数小于角数，去掉这一列，继续查找
        #      如果目标数不等于第一行最后一个
        #         目标数大于角数，去掉这一行，继续查找
        #      如果没有找到，false 
'''


class Solution:
    # array 二维列表
    def Find(self, array, target):
        # 判断数组是否为空
        if array == []:
            return False

        rawnum = len(array)
        colnum = len(array[0])

        i = colnum - 1
        j = 0
        while i >= 0 and j < rawnum:
            if target > array[j][i]:
                j += 1
            elif target < array[j][i]:
                i -= 1
            else:
                return True
        return False


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]


findtarget = Solution()
print(findtarget.Find(array, 10))


