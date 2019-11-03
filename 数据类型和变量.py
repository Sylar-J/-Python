#print absoIute vaIue of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
print(1.5e5)#1.5e = 150000

#字符串（在有引号的情况下如何正确输出）
print("I'm ok!")#双引号括单引号不影响
print('I\'m ok!')#单引号括单引号就要加反斜杠来转义原本是（'I'm ok!'）正确实例←
print('I\'m \nleaning \tPython')#\t 制表符 \n 回车 \\ == \
print('\\\n\\')#示例
print('\\\t\\')#示例
print(r'\\\t\\')#转义字符前面加r就是取消转义
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容↓
print('''line1>>>>???
..line2
```lin3''')#括号里面的内容全部显示且可以多行
#布尔值可以用and、or、not来运算
# (Ture and Ture = Ture)  (Ture and False = False)
# (False or False = False)  (Ture or False = Ture)
# (not Ture = False)  (not False = Ture)
x = 123 #x是整数
print(x)
c = 'ABC' # c为字符串
print(c)
#当一个变量已经定义了类型，就不能把不同类型的值赋值给它比如：
#int = a #a 是整数类型变量
#a = 'ABC'  # 错误：不能将字符串赋值给整型变量
#↑以上是静态语句
#↓是动态语句
z = 10
z = z + 2
print(z)
#如果从数学上理解  x = x + 2那无论如何是不成立的，在程序中
# 赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。
#除法有两种 /（单斜杠）取整显示为浮点型  //（双斜杠）取整数 %(百分号）自动取余
print(10 / 3,10 / 5)
print(10 // 3,10 // 2)
print(10 % 3, 10 % 2)

#例子
n = 123
f = 456.789
s1 = 'Hello Python world'
s2 = 'Hello, \'Sylar\''
s3 = r'Hello, "Sylar"'
s4 = r'''Hello,
Ezio!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
