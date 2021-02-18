def main():
    scores = {'Andy': 95, 'Amy': 78, 'Alan': 82}

    print(scores['Andy'])     # 利用鍵可以獲取字典中對應的值
    print(scores['Alan'])
    for elem in scores:       # 對字典進行索引(索引的是鍵，再利用鍵取對應的值)
        print('%s \t--->  %d ' % (elem, scores[elem]))

    # 更新字典中的元素
    scores['Alice'] = 65
    scores['Abby'] = 71
    scores.update(Adam=67, Alex=85)
    print(scores)
    if 'Albert' in scores:
        print(scores['Albert'])
    print(scores.get('Albert'))
    # get方法也是利用鍵獲取對應的值，但是可以設置默認值
    print(scores.get('Albert', 60))

    # 刪除字典中的元素
    print(scores.popitem())        # 刪除並取得最後一項
    print(scores.popitem())
    print(scores.pop('Andy', 100))  # 刪除並取得指定項的值
    print(scores)
    scores.clear()                  # 清空字典
    print(scores)


# 只執行main裡面的函數
if __name__ == '__main__':
    main()
