print("""
1. Simple func

Ex:
def fun():
  print("Welcome to GFG")
  
fun()

2. Function with Parameters

Ex: 
def add(num1: int, num2: int) -> int:
    "Add two numbers"
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
  
3. Default Arguments  

Ex:
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
 
# Driver code (We call myFun() with only argument)
myFun(10)

""")
