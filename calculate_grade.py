num1=int(input("enter the number in subject 1"))
num2=int(input("enter the number in subject 2"))
num3=int(input("enter the number in subject 3"))
num4=int(input("enter the number in subject 4"))
num5=int(input("enter the number in subject 5"))

sum=num1+num2+num3+num4+num5
percent=(sum/500)*100

if percent>=80 and percent<100:
    print("GRADE A")

elif percent>=60 and percent<80:
    print("GRADE B")

else:
    print("GRADE C")