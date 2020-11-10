import heapq as hq

# リストをヒープ化、たぶんO(logN)?
a = [1, 6, 8, 0, -1]
hq.heapify(a)
print(a)

# 最小値を取り出す
# O(logN)
print(hq.heappop(a))
print(a)

# 最大値の取り出し方
# −1をかけてヒープに入れる
a = list(map(lambda x: -1*x, a))
hq.heapify(a)
print(-1*hq.heappop(a))

# 各要素がリストの場合は先頭要素で比較される
a = [[2, 3], [4, 1], [1, 3], [3, 5]]
hq.heapify(a)
for i in range(len(a)):
    print(hq.heappop(a))
# ->
# [1, 3]
# [2, 3]
# [3, 5]
# [4, 1]
