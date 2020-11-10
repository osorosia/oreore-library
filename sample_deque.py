from collections import deque

d = deque()

# 要素を追加する
# 右側
d.append(0)
d.append(1)
d.append(2)
print(d)  # [0, 1, 2]
# 左側
d.appendleft(-1)
d.appendleft(-2)
print(d)  # [-2, -1, 0, 1, 2]

# 要素を取り出す
# 右側
print(d.pop())  # 2
# 左側
print(d.popleft())  # -2
print(d)  # [-1, 0, 1]

