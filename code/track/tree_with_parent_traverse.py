def traverse(node):  
    # if tree if empty then just return
    if not node:
        return
    
    while(True):
        print(node.val)
        
        # if there's left child move left
        if node.left:
            node = node.left
        # if not left child but there's right child move right
        elif node.right:
            node = node.right
        # when we hit a leaf node
        else:
            while(True): 
                # stop if we hit root node i.e. no further parents available
                if node.parent is None:
                    return 
                leafNode = node
                node = node.parent
                
                # if previous node was left child of the parent
                # and right child also exists, then move to right
                # (as we've already visited left elements and current node)
                if(node.left == leafNode and node.right is not None):
                    node = node.right
                    break