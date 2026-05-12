def reverseLinked(node):
    if node==None or node.next == None:return
    p = reverseLinked(node.next)
    if node ==5:print(node)
    node.next.next = node
    node.next=None
    return p
    