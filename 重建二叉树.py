# # -*- coding:utf-8 -*-
# '''
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# '''
#
# # 前序遍历：根节点->左子树->右子树
# #
# # 中序遍历：左子树->根节点->右子树
# #
# # 后序遍历：左子树->右子树->根节点
#         1
#     2      3
#   4      5   6
#     7          8
# 思路总结：先根据前序遍历序列的第一个数字创建根结点，接下来在中序遍历序列中找到根结点的位置，这样就能确定左、右子树结点的数量。
# 在前序遍历和中序遍历的序列中划分了左、右子树结点的值之后，就可以递归地去分别构建它的左右子树。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
            # 前序遍历的第一个结点一定是根节点
        root = TreeNode(pre[0])
        # 获取中序遍历中根节点的索引
        i = tin.index(pre[0])

        root.left = self.reConstructBinaryTree(pre[1: i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root


if __name__ == "__main__":
    a = Solution()
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]  # 前序遍历
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]  # 中序遍历
    root = a.reConstructBinaryTree(pre_order, mid_order)
    print root.val
    print root.left.val
    print root.right.val
    print root.left.left.val
    print root.left.left.right.val
    print root.right.right.left.val
    print root.right.left.val