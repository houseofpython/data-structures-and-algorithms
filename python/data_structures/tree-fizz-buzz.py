class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def fizz_buzz_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    new_root = TreeNode()

    if root.val % 3 == 0 and root.val % 5 == 0:
        new_root.val = "FizzBuzz"
    elif root.val % 3 == 0:
        new_root.val = "Fizz"
    elif root.val % 5 == 0:
        new_root.val = "Buzz"
    else:
        new_root.val = str(root.val)

    for child in root.children:
        new_root.children.append(fizz_buzz_tree(child))

    return new_root
