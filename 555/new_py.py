#
# #
# #
# # a = {x for x in 'abcrws' if x not in 'abc'}
# # print(a)
# #
# # a = {'jack': 1996, 'xiaohong': 1997, 'xiaoming': 2000}
# # a['xiaowang'] = 1999
# # print(a)
# # print(a['jack'])
# # del a['xiaoming']
# # print(a)
# # print(list(a.keys()))
# # print(list(a.values()))
# # print('jack' in a)
# #
# #
# # b = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# # print(b)
# #
# # c = {x: x**2 for x in (2, 4, 6)}
# # print(c)
# #
# # d = dict(sape=4139, guido=4127, jack=4098)
# # print(d)
#
# #
# # a = {'jack': 1996, 'xiaohong': 1997}
# # for i, j in a.items():
# #     print(i, j)
# #
# # b = (1, 2, 3, 4, 5)
# # for i, j in enumerate(b):
# #
# # import turtle
# #
# # turtle.screensize(800, 600, 'green')
# #
# #
# #
# # turtle.pensize(4)
# # turtle.pencolor('red')
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.mainloop()
#
# # # 判断是闰年则输出True
# # year = int(input('请输入年份: '))
# # a = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# # print(a)
#
#
#
#
#
#
#
#
#
#
#
#
#
# # 实例1--验证用户登录
# # username = input('请输入用户名:')
# # password = input('请输入口令: ')
# # if username == 'admin' and password == '123456':
# #     print('身份验证成功')
# # else:
# #     print('身份验证失败')
#
#
#
# # # 实例2--分段函数求值
# #
# # x = float(input('X= '))
# # if x > 5:
# #     y = 3*5+x
# # elif x < 1:
# #     y = 2**x+10
# # else:
# #     y = x+100
# # print('%.2f = %.2f' % (x, y))
# # print(f'(%.2f) = %.2f' % (x, y))
# # print('f(%.2f) = %.2f' % (x, y))
# #
#
#
# # # 实例3--掷色子决定干什么
from random import randint
face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)
#
#
# # # 成绩转换为等级
# # score = float(input('请输入成绩: '))
# # if score >= 90:
# #     grade = 'A'
# # elif score >= 80:
# #     grade = 'B'
# # elif score >= 70:
# #     grade = 'C'
# # elif score >= 60:
# #     grade = 'D'
# # else:
# #     grade = 'E'
# # print('对应的等级是:', grade)
#
#
#
# # 三角形的面积和周长
# # import math
# # a = float(input('a = '))
# # b = float(input('b = '))
# # c = float(input('c = '))
# # if a+b > c and a+c > b and b+c > a:
# #     print('"周长" : %f ' % (a+b+c))
# #     p = (a+b+c)/2
# #     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
# #     print('"mj": %f ' % (area))
# # else:
# #     print('不能构成三角形')
#
#
#
#
#
# from time import sleep
#
#
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()
#
# Grade_5 = {'Yom', 'Jim', 'Rose'}
# Grade_6 = {'Tom', 'Jim', 'Jack', 'Tom'}
#
# print(Grade_6)        # 输出的集合自动去重
# print(Grade_5 - Grade_6)  # 5与6的差集（属于5但不属于6的元素）
# print(Grade_5 | Grade_6)  # 5与6的并集
# print(Grade_5 & Grade_6)  # 5与6的交集      优先级：差集>交集>并集
# print(Grade_5 ^ Grade_6)  # 5与6中不同时存在的元素
#
# Grade_6.add('小红')
# Grade_6.update([1, 4], 'happy', (11, 31, 49))   #也可以添加元素，且参数可以是列表，元组，字典等
# Grade_6.remove('小红')     # 删除集合中的某个元素
# Grade_6.discard('小红')    # 移除集合中的元素，且如果元素不存在，不会发生错误
# Grade_6.clear()            # 清空集合
#
# print(Grade_6)



# print(a*4)
# print(a+b)
# print(78 in a)
# print(a[0], a[-1], a[1:])   # 列表截取
print('hello word')
