num1 = ""
num2 = ""
op = ""

num = 2

while type(num1) != type(num):
	try:
		num1 = int(input("Enter your first number"))
	except ValueError:
		print("That isnt a number")

while 1==1:
	if op == "+":
		break
	if op == "/":
		break
	if op == "-":
		break
	if op == "*":
		break
	op = input("Enter your operation")
	


while type(num2) != type(num):
	try:
		num2 = int(input("Enter your second number"))
	except ValueError:
		print("That isnt a number")

print(str(num1)+str(op)+str(num2)+"=")
if op == "+":
	print(num1+num2)
elif op == "-":
	print(num1-num2)
elif op == "*":
	print(num1*num2)
elif op == "/":
	print(num1/num2)
