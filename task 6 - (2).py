start=int(input("enter the integer to start with: "))
#here we can input 5 to get the required pattern mentioned in the question
end=1
for i in range(end,start+1,1):
    for j in range((start+1)-i,end-1,-1):
        print(j,end="")
    print("\n")
   
#if no need of that much space between lines, instead of \n , \r could be given .
