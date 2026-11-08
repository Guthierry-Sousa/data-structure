from collections import deque

def level_max_sum(root):
    if root is None:
        return None

    q = deque([root])
    max_sum = float('-inf')
    nivel = 0

    nivel_temp = 0

    while q:

        size = len(q)
        sum_ = 0
        nivel_temp += 1

        for _ in range(size):
            n = q.popleft()
            sum_ += n.data

            if n.left: q.append(n.left)
            if n.right: q.append(n.right)

        if sum_ > max_sum:
            max_sum = sum_
            nivel = nivel_temp

    return max_sum, nivel