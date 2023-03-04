import random

n1=random.randint(1,6)
n2=random.randint(1,6)
if n1+n2==7 or n1+n2==11:
	print("The sum of dice is", n1, "+", n2, "=", n1+n2)
	print("You won.")
elif n1+n2==2 or n1+n2==3 or n1+n2==12:
	print("The sum of dice is", n1, "+", n2, "=", n1+n2)
	print("You lose")
else:
	print("The sum of dice is", n1, "+", n2, "=", n1+n2)
	print("Now your goal number is", n1+n2)
n3=random.randint(1,6)
n4=random.randint(1,6)
while n3+n4!=n1+n2:
	print("The sum of dice is", n3, "+", n4, "=", n3+n4)
	if n3+n4==7:
		print("You lose")
		break
	n3=random.randint(1,6)
	n4=random.randint(1,6)
else: 
	print("The sum of dice is", n3, "+", n4, "=", n3+n4)
	print("You win")