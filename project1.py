import random

user_choice=int(input("Enter your choice:Type 0 for Rock,1 for Paper,2 for Scissor:"))
computer_choice=random.randint(0,2)
print("Computer Choice:")
print(computer_choice)
if user_choice>=3 or user_choice<0:
    print("You Entered invalid number")
elif computer_choice==user_choice:
    print("It's a Draw")
elif computer_choice>user_choice:
    print("You Loose")
elif computer_choice<user_choice:
    print("You Win")
elif computer_choice==0 and user_choice==2:
    print("You Loose")
elif user_choice==0 and computer_choice==2:
    print("You Win")
elif user_choice>=3 or user_choice<0:
    print("You Entered invalid number")
