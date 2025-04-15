age = int(input("Enter your age: "))
if age <18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")

#if - elif - else statement:
marks = int(input('Enter your number: '))
if marks >= 95:
    print('You got A+')
elif marks >= 90:
    print('You got A')
elif marks >= 85:
    print('You got A-')
elif marks >= 80:
    print('You got B+')
elif marks >= 75:
    print('You got B')
elif marks >= 70:
    print('You got B-') 
elif marks >= 65:
    print('You got C+')
else:
    print('You are failed')