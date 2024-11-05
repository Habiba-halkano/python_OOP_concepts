#static methods and attributes
class Calculator:
    count = 0

    @staticmethod
    def add(num1, num2):
        Calculator.count += 1
        return num1 + num2

res1 = Calculator.add(1, 2)
print (f"result: {res1}")
print (f"add method called: {Calculator.count} times")

res2 = Calculator.add(10,20)
print (f"result: {res1}")
print (f"add method called: {Calculator.count} times")
