age = input('please input your age:')
#注意18要用''括起来，不然会报
#TypeError: '>=' not supported between instances of 'str' and 'int'
#因为input返回的是str类型，直接>=18的话18是int，为了避免格式转化的麻烦，直接用''括起来当str就行
if age >= '18':
    print('audlt')
else:
    print('teenager')