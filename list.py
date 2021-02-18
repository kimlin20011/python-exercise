def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5  # 加入 5 個此元素置列表中
    print(list2)
    print(len(list1))     # 計算列表長度(元素個數)
    print(list1[0])       # 印出列表的指定位置的元素
    print(list1[4])
    # print(list1[5])     # 超出列表範圍會發生異常
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300        # 將指定位置元素變為指定數據
    print(list1)

    list1.append(200)     # 添加此數據元素到列表中
    list1.insert(1, 400)  # 添加此數據元素到指定位置
    list1 += [1000, 2000]  # 添加此數據元素到列表中
    print(list1)
    print(len(list1))     # 計算列表長度(元素個數)

    list1.remove(3)       # 刪除此數據元素
    if 1234 in list1:     # 判斷此數據元素是否在字串中
        list1.remove(1234)
    del list1[0]          # 刪除指定位置的元素
    print(list1)

    list1.clear()         # 清空列表元素
    print(list1)


if __name__ == '__main__':
    main()
