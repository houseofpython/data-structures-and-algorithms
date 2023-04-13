def breadth_first(tree):
    if not tree:
        return []

    queue = [tree]
    values = []
    while queue:
        current_node = queue.pop(0)
        values.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return values
