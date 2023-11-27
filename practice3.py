class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]

    for val in preorder[1:]:
        node = TreeNode(val)
        if val < stack[-1].val:
            stack[-1].left = node
        else:
            while stack and val > stack[-1].val:
                last = stack.pop()
            last.right = node
        stack.append(node)

    return root

# Preorder traversal: 15, 10, 7, 3, 9, 12, 11, 16, 25, 17, 22, 26
preorder = [15, 10, 7, 3, 9, 12, 11, 16, 25, 17, 22, 26]

root = bstFromPreorder(preorder)
print(root)
