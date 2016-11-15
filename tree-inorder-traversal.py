import sys
def inOrder(root):
    #Write your code here
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node)
            stack.append(node.left)
            node.left = None
        else:
            sys.stdout.write('{} '.format(node.data))
            
            if node.right:
                stack.append(node.right)
                node.right = None
