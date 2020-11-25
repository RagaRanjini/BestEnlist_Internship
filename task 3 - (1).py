def combine(dict1,dict2):
    return(dict1.update(dict2))
dict1={"kohli":100,"kl rahul":91,"shreyas":90}
dict2={"rahane":80,"pujara":45}
combine(dict1,dict2)
print("after combining dict1 and dict2 dictionaries , we get : ",dict1)
#dict1 is printed as dict2 is updated to dict1 
