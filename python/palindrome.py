# def password_checker():
#     user=input("enter password")
#     if len(user)<8:
#         print("not acceptable password")
#     elif(user.isalpha() or user.isdigit()):
#         print("medium password try to mix digit and letter")
#     else:
#         print("password acceptable")
# password_checker()
i=0
while i<=100:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
      