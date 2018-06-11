# 字符的声明可以有三种方式：
# 单引号''
# 双引号""
# 三引号 '''   '''

a = 'Hello，单引号'
b = "Hi,双引号"
c = '''哈哈，我是三引号。

                        我能换行哦！'''
print('***********************  String声明 **********************')
print('\t\t\t\t\t\t', a)
print('\n')
print('\t\t\t\t\t\t', b)
print('\n')
print('\t\t\t\t\t\t', c)
print('\n')
print('***********************  String类型检测 **********************')
a_type = type(a)
print('a的类型：', a_type)  # a的类型： <class 'str'>
print('\n')
print('***********************  String拼接 **********************')
print(a + b)  # Hello，单引号Hi,双引号
print('\n')
print('***********************  String乘法 **********************')
print(a * 3)  # Hello，单引号Hello，单引号Hello，单引号
print('\n')
print('***********************  String截取 **********************')
string = 'Hello World!'
print(string[0])  # H
print(string[-4])  # r
print(string[11:14])  # !
print(string[4:])  # o World!
print(string[:5])  # Hello
print('\n')
print('***********************  String长度 **********************')
print(len(string))
print('\n')
print('***********************  String转数字 **********************')
# 只有只包含纯数字的字符串才可以转换为数字
intString = '1234'
print('原始字符串：', intString)
print('原始字符串类型', type(intString))
print('转换后的字符串：', int(intString))
print('转换后的类型', type(int(intString)))
print('\n')
