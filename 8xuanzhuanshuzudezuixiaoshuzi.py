# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# 看到这样的旋转数组查找最小数，我们会不会潜意识里面就想到了二分查找呢。确实，这道题目就是用二分查找的思路来解决，中间用到了旋转数组的一些特性。
# 以题目中的旋转数组为例，{3,4,5,1,2}，我们可以有序数组经过旋转以后被分割为两段有序的数组，比如此处被分为{3,4,5}{1,2}这样两个数组，
# 并且前半段数组中的数字肯定大于等于后半段的数组。我们找中间元素，让其跟元素首元素比较，如果大于首元素，则中间元素属于前半段有序数组，
# 如果小于尾元素，那么中间元素就是后半段的元素。
#
# 这里我们设定两个指针start和end分别指向数组的首尾元素，然后当start指向前半段最后一个元素，end指向后半段第一个元素，
# 这是程序就找到了数组中的最小元素，就是end指向的那个数，程序的出口就是 end-start==1。

class Solution:
    # def minNumberInRotateArray(self, rotateArray):
    #     if len(rotateArray) == 0:
    #         return 0
    #     front = 0
    #     rear = len(rotateArray) - 1
    #     minVal = rotateArray[0]
    #     if rotateArray[front] < rotateArray[rear]:
    #         return rotateArray[front]
    #     else:
    #         while (rear - front) > 1:
    #             mid = (rear + front)//2
    #             if rotateArray[mid] == rotateArray[front] and rotateArray[front] == rotateArray[rear]:
    #                 for i in range(1, len(rotateArray)):
    #                     if rotateArray[i] < minVal:
    #                         minVal = rotateArray[i]
    #                         rear = i
    #             elif rotateArray[mid] >= rotateArray[front]:
    #                 front = mid
    #             elif rotateArray[mid] <= rotateArray[rear]:
    #                 rear = mid
    #         minVal = rotateArray[rear]
    #         return minVal


    # # 书上方法
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        minNumIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                minNumIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.MinInOrder(rotateArray, front, rear)

            if rotateArray[midIndex] >= rotateArray[front]:
                front = midIndex
            elif rotateArray[midIndex] <= rotateArray[rear]:
                rear = midIndex
        return rotateArray[minNumIndex]
    def MinInOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end+1]:
            if i < result:
                result = i
        return result



Test = Solution()
print(Test.minNumberInRotateArray([4, 5, 1, 2, 3]))
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))