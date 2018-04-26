class TreeNode:
    def __init__(self, x=None):
        self.val = x if x else 0
        self.left = None
        self.right = None


def main():



def list2tree(m_list):
    root = None
    if m_list:
        root = TreeNode(m_list.pop(0))
        queue = [root]
    while m_list:
        node = queue.pop(0)
        if not m_list:
            break
        node.left = TreeNode(m_list.pop(0))
        queue.append(node.left)

        if not m_list:
            break
        node.right = TreeNode(m_list.pop(0))
        queue.append(node.right)
    return root


def travel_tree(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    main()
