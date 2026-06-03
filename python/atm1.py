import random
list=["rock","paper","scissor"]
user_choice=input("enter ur move=rock,paper,scissor")
comp_choice=random.choice(list)
print(f"user choice={user_choice},computer choice={comp_choice}")
if user_choice==comp_choice:
    print("both chooses same:match tie")
elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper covers rock: computer win")
    else:
        print("paper covers rock: user win")
elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper,computer win")
    else:
        