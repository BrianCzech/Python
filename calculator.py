num1=int(input('Enter Number 1:'))
num2=int(input('Enter Number 2:'))
action=str(input('Choose action: add(a), subtract(s),multiply(m), divide(d)->'))

print('The end result is:')
if action=="a":
    print(num1+num2)
elif action=="s":
    print(num1-num2)
elif action=="m":
    print(num1*num2)
elif action=="s":
    print(num1/num2)    