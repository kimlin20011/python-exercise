from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):  # 搖n個骰子
        total += randint(1, 6)
        return total


print(roll_dice())   # 如果沒有指定參數那麼使用默認值搖兩顆色子


def add(* args):  # 在參數名前面的 * 表示 args 是一個可變參數
    total = 0
    for val in args:
        total += val
    return total


# 調用 add 函數時可以傳入 0 個或多個參數
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
