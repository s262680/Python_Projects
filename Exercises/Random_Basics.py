x={1,2,3,4,5}
y={3,4,5,6,7}
print(x-y)
print(x|y)
print(x^y)
print(x&y)

dict_test={"a":"123","b":"456"}
# print (dict_test)
# dict_test.values
# print(dict_test["a"])
for key, value in dict_test.items():
    print(key, '-',value)


numList=[1,2,3,4,7]
for num in numList:
    print(num+num)

number=1
while number<6:
     number+=1
     if number==3:
         continue
     print(number)
else:
    print ("no longer less than 5")


def test_function():
    print("function ran")
test_function()

def test_function2(testPara):
    print(testPara*10)
test_function2(2)

def test_function3(number,power):
    print(number**power)
test_function3(5,3)


tempList=[1,2,3,4,5]
def test_function4(*num,power):
    for temp in num:
        print(temp**power)
test_function4(*tempList,power=2)

def test_function5(**number):
    print("The first number is "+ number["Num1"]+" and the second number is "+ number["Num2"])
test_function5(Num1="123",Num2="456")


