
# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    '''
    if not(head):
        return
    cur = head
    while cur:
        new_node = Node(cur.val)
        new_node.next = cur.next
        cur.next = new_node
        cur = new_node.next
            
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
        
    cur = head
    new_head = head.next
    new_current = new_head

    while cur:
        cur.next = cur.next.next
        cur = cur.next

        if new_current.next:
            new_current.next = new_current.next.next
            new_current = new_current.next

    return new_head
    '''
    visited = {}
    def dfs(node):
        if node in visited:
            return visited[node]
        if not node:
            return None
        copy = Node(node.val)
        visited[node] = copy
        copy.next = dfs(node.next)
        copy.random = dfs(node.random)

        return copy
        
    return dfs(head)