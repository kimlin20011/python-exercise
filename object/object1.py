class Student(object):

    # __init__是一個特殊方法用於創建 object 時進行初始化
    # 我們可以為學生這個 object 綁定 name 和 age 兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在學習 %s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s 只能觀看普通電影' % self.name)
        else:
            print('%s 能觀看所有電影' % self.name)


def main():

    stu1 = Student('Andy', 38)    # 創建學生並指定姓名和年齡
    stu1.study('Python 程式設計')  # 給 object 發 study 的消息
    stu1.watch_movie()            # 给 object 發 watch_movie 的消息
    stu2 = Student('Amy', 15)
    stu2.study('C 語言程式設計')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
