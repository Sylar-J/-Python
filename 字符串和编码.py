print(ord('a'))
print(ord('中'))
print(chr(66))
print(chr(454564))
a = "djdkdkdljdadjda"
print('a一共有：', len(a),'个数！')
b = "中华人民共和国"
print(len(b))
#在Python中，才用的格式化方式和C语言一样，用 % 实现，例如：↓
print('Hello,%s' %'world')
print('Hi, %s, you have $%x.' %('Michael', 1000000))#%d 整数 %f 浮点数 %s 字符串 %x十六进制
print('Hi, #%s, you have $%d.' %('Michael', 1000000))#任意各种都可以用%+任意变量来进行格式化
print('%30d-%02d' %(3, 1))#%3d  '3'是加三个位置  '02'是在空的位置前面加一个0 更加好看
print('%.2f' % 3.1415926535775648)#%f 是浮点型  '2f'是小数点后两位
print('Hello, {0}, 成绩提升了,{1:.1f}%'.format('小明', 17.125))#format 会把方法里面的值依次替换掉
#例子
s1 = 72
s2 = 85
r = (s2 - s1) / 100
print('%2.2f' % r)