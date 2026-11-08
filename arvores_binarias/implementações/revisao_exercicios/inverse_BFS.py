from collections import deque

def inv_BFS(root):

    if root is None:
        return None

    q = deque([root])
    s = deque()

    while q:
        n = q.popleft()
        if n.left:
            q.append(n.left)

        if n.right:
            q.append(n.right)

        s.append(n)

    while s:
        n = s.pop()
        print(n.data)