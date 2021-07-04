        #checking odd even number using if esle from user

# num = int(input("Enter a Number : "))
# if (num%2)==0:
#     print("then nuber is even :",num)
# else:
#     print("the nmmber is Odd : ",num)

        #using for loop and list

# num=[11, 22, 33, 44, 55, 66, 77, 88 ,99]
# #itrating number form the list int i for use al element
# for i in num:
#     if i %2==0:#checking even numbers
#         print("are the even numbers :",i)
#     else :
#         print("rest of them are odd :",i)

        # SUM OFF ODD AND THE EVEN NUMBERS FROM THE GIVEN LIST
num=[11, 22, 33, 44, 55, 66, 77, 88 ,99]
sumOfEven=0
sumOfOdd=0
#itrating number form the list int i for use al element
for i in num:
    if i %2==0:#checking even numbers
        print("\n EVEN NUMBER IS :",i)
        sumOfEven=i
        # print("\n sum of even numbers :",i)
    else :
        print("\n ODD NUMBER IS  :",i)
        sumOfOdd=i
        # print("\n sum of odd numbers : ",i)
print("\n ADDITION OF FOUND EVEN NUMBER IS : ",sumOfEven+sumOfEven)
print("\n ADDITION OF FOUND ODD NUMBER IS : : ",sumOfOdd+sumOfOdd)
