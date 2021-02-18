def main():
    str1 = 'hello, world!'
    print(len(str1))             # 計算字串的長度
    print(str1.capitalize())     # 字串第一個字母變大寫
    print(str1.upper())          # 將字串字母變大寫
    print(str1.find('or'))       # 從字串中找子字串所在位置
    print(str1.find('shit'))
    print(str1.index('or'))      # 與 find 類似但找不到子字串時會異常
    print(str1.startswith('He'))  # 判斷字串是否以指定的字串為開頭
    print(str1.startswith('hel'))
    print(str1.endswith('!'))    # 判斷字串是否以指定的字串為結尾
    print(str1.center(50, '*'))  # 將字串以指定的寬度置中並在兩側用指定的字元填滿
    print(str1.rjust(50, ' '))  # 將字串以指定的寬度靠右放置左側用指定的字元填滿

    str2 = 'abc123456'
    print(str2[2])        # 從字串中取出指定位置的字元 (字串第一個元素為 str[0])

    # 字串切片 字串[起始值:結束值:間隔值(預設為 1 )]
    # 起始值如果不填就代表由最前方開始，結束值如果不填就代表算到最後
    print(str2[2:5])             # 印出 str2[2] ~ str2[4] 的元素
    print(str2[2:])              # 印出 str2[2] 後的所有元素
    print(str2[2::2])            # 印出 str2[2] 後間隔 2 的所有元素
    print(str2[::2])             # 印出從頭到尾間隔2的所有元素
    print(str2[::-1])            # 印出以尾為首開始的所有元素
    print(str2[-3:-1])           # 印出 str2[-3] ~ str2[-2] 的元素
    print(str2.isdigit())        # 判斷字串是否由數字構成
    print(str2.isalpha())        # 判斷字串是否由字母構成
    print(str2.isalnum())        # 判斷字串是否由數字和字母構成
    str3 = '  jackfrued@126.com  '
    print(str3)
    print(str3.strip())          # 將字串左右兩側空格刪除


if __name__ == '__main__':
    main()
