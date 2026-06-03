# # f=open("sample.txt",'r')
# # data=f.read()
# # print(data)
# # f.close()
# # f=open("sample.txt","at")
# # data=f.write("this inchdgscfuj")
# # f=open("sampl.txt",'x')
# # f.write("bhagduehd")
# # f=open("sample.txt",'r')
# # dat=f.read()
# # print(dat)
# # data=f.readline()
# # print(data)
# # data2=f.readline()
# # print(data2)
# # data3=f.readline()
# # print(data3)
# # data4=f.readline()
# # print(data4)
# # data5=f.readline()
# # print(data5)
# # f=open("sample8.txt",'r+')
# # f.write('fyuyggdiywjhu')
# # print(f.read())
# # f.close()
# # f=open("sample.txt","w+")
# # print(f.read())
# # f.write("huhui")
# # f.close ()
# # with open("sample.txt","w") as f:
#     # f.write("gkuhu")
# # import os
# # os.remove("sample2.txt")
# # class student:
# #     # @staticmethod
# #     def college(self):
# #         print("hi")
# # s1=student()
# # s1.college()
# # Defining a class
# class Student:
#     # Constructor (special method)
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
    
    
#     # Method to check pass/fail
#     def check_result(self, marks):
#         if marks >= 40:
#             print(f"{self.name} has Passed ")
#         else:
#             print(f"{self.name} has Failed ")

# # Creating objects
# student1 = Student("Shejal", 101)
# print(student1.name,student1.roll_no)
# # Calling methods
# student1.check_result(85)

# student2 = Student("Amit", 102)
# print(student2.name,student2.roll_no)
# student2.check_result(30)
# n=int(input("no"))
# def fab (n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# for i in range(n):
#     print(fab(n))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# Function to get nth Fibonacci number
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)   # recursion: f(n) = f(n-1) + f(n-2)

# # Function to print sequence up to n terms
# def print_fibonacci(n):
#     for i in range(n):
#         print(fib(i), end=" ")

# # Example run
# n = int(input("Enter number of terms: "))
# print("Fibonacci sequence:")
# print_fibonacci(n)
# def is_prime(n):
#     if n <= 1:  # 0 and 1 are not prime
#         return False
#     for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(9))


### 📝 To-Do List Project (Python)


# Simple To-Do List App

tasks = []

   
while True:
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print(" No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f" Removed: {removed}")
            else:
                print(" Invalid task number.")

    elif choice == "4":
        print(" Exiting... Have a productive day!")
        break

    else:
        print(" Invalid choice. Please enter 1-4.")
