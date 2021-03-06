1.列举你了解的编码及他们之间的区别？
ascii,（American Standard Code for Information Interchange，美国标准信息交换代码）是基于拉丁字母的一套电脑编码系统，主要用于显示现代英语和其他西欧语言，其最多只能用 8 位来表示（一个字节），即：2**8 = 256，所以，ASCII码最多只能表示 256 个符号。
unicode,（统一码、万国码、单一码）是一种在计算机上使用的字符编码。Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，规定虽有的字符和符号最少由 16 位来表示（2个字节），即：2 **16 = 65536，注：此处说的的是最少2个字节，可能更多.
utf-8,是对Unicode编码的压缩和优化，他不再使用最少使用2个字节，而是将所有的字符和符号进行分类：ascii码中的内容用1个字节保存、欧洲的字符用2个字节保存，东亚的字符用3个字节保存.
 
2.列举你了解的Python2和Python3的区别？
python2默认的解释器编码ascii
python3默认的解释器编码utf-8

4. 输出
Python2 输出写法:
     print  'hello world'
python3 输出写法:
     print('hello world')



3.你了解的python都有那些数据类型？
整形
字符串
布尔
字典
列表
集合

4.补充代码，实现以下功能。

1.value =  _'51devops"niubi'____
2.print(value)  # 要求输出  51devops"niubi

5.用print打印出下面内容：

1文能提笔安天下,
2武能上⻢定乾坤.
3心存谋略何人胜,
4古今英雄唯是君。
a = '文能提笔安天下,'
s = '武能上⻢定乾坤.'
d = '心存谋略何人胜,'
f = '古今英雄唯是君。'
print(a)
print(s)
print(d)
print(f)



6.变量名的命名规范和建议？
变量名只能是 字母、数字或下划线的任意组合
变量名的第一个字符不能是数字
不能用python内置关键字
[‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
建议：
变量名建议不使用拼音和中文
变量的要具有意义
变量名不要过长
变量名要区分大小写
变量名推荐写法:
驼峰体 MeetTheGirl
下划线 meet_the_girl


7.如下那个变量名是正确的？

1 name = '51devops'   正确
2 _ = 'echo'
3 _9 = "zhangsan"     正确
4 9name = "xxx"
5 devops(edu = 666


8.简述你了解if条件语句的基本结构。
if
  else
  elif
  

9.设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
n = 66
num = int(input('请输入数字：'))
if num > n:
    print('大')
elif num < n:
    print('小')
else:
    print('正确')


10.写程序，成绩有ABCDE5个等级，与分数的对应关系如下.
1 A    90-100
2 B    80-89
3 C    60-79
4 D    40-59
5 E    0-39
要求用户输入0-100的数字后，你能正确打印他的对应成绩.

11.模拟10086客服电话（条件语句的嵌套）

1.猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
2.在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’。
3.使用两种方法实现输出 1 2 3 4 5 6 8 9 10 。
4.求1-100的所有数的和
5.输出 1-100 内的所有奇数
6.输出 1-100 内的所有偶数
7.求1-2+3-4+5 … 99的所有数的和
8.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
9.猜年龄游戏
要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。

10.猜年龄游戏升级版
要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出




