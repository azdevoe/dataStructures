def search_tree(node, target):
    # Base cases: what if the node is None? What if the node is the target?
    if node is None:
        return False
    if node.val == target:
        return True
    # Send scout left
    left = search_tree(node.left,target)
    
    # If the left scout found it, return True IMMEDIATELY
    if left:
        return True
    
    # Otherwise, send scout right and return whatever they find
    right=search_tree(node.right,target)
    if right:
        return True
    
    return False