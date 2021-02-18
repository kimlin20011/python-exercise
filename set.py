def main():
    set1 = {1, 2, 3, 3, 3, 2}   # 創建 set
    print(set1)
    print('Length =', len(set1))  # 印出 set 的長度
    set2 = set(range(1, 10))   # 創建 1~9 的 set
    print(set2)
    set1.add(4)                 # 加入指定數據至 set 中
    set1.add(5)
    set2.update([11, 12])        # 加入指定數據至 set 中
    print(set1)
    print(set2)

    set2.discard(5)             # 刪除中指定數據
    if 4 in set2:
        set2.remove(4)  # 刪除中指定數據(remove 的元素如果不存在會引發 KeyError)
    print(set2)

    for elem in set2:           # 索引集合中的數據
        print(elem ** 2, end=' ')
    print()

    # 將元組轉換成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())          # 刪除並取得 set 中的最後一項
    print(set3)
    # 集合的交集、聯集、差集、對稱差運算
    print(set1 & set2)     # print(set1.intersection(set2))
    print(set1 | set2)     # print(set1.union(set2))
    print(set1 - set2)     # print(set1.difference(set2))
    print(set1 ^ set2)     # print(set1.symmetric_difference(set2))
    # 判斷子集和超集
    print(set2 <= set1)    # print(set2.issubset(set1))
    print(set3 <= set1)    # print(set3.issubset(set1))
    print(set1 >= set2)    # print(set1.issuperset(set2))
    print(set1 >= set3)    # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()
