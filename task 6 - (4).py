def armstrong(num):
    if(num<10):
        print(num," is an armstrong number")
    else:
        count=len(str(num))
        sum=0
        n=num
        while(num!=0):
            sum+=(num%10)**count
            num//=10
        if(n==sum):
            print(n," is an armstrong number")
        else:
            print(n," is not an armstrong number")
        
print("EXPLANATION FOR ARMSTRONG NUMBER : \n TAKING TOTAL NUMBER OF DIGITS IN A NUMBER AS N , THEN SUM OF ITS DIGITS ,EACH WITH THE POWER OF N ,IF GIVES THE SAME NUMBER , THE NUMBER IS SAID TO BE ARMSTRONG NUMBER \n ( for example: 371 , since there are 3 digits in the number , 3^3 + 7^3 + 1^3 , will be taken according to the explanation. (3^3 + 7^3 + 1^3) gives 371 , which is the actual number . so, 371 is an armstrong number.")
num=int(input("To verify a number whether armstrong or not , please enter a number : "))
if(num!=0):
    armstrong(num)
else:
    print(" please enter positive integer !")

      
