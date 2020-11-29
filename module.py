def newlist(list=["english","tamil","french"]):
    a=["english","tamil","french"]
    if(list==["english","tamil","french"]):
        print("THE LANGUAGES IN LIST: ",list)
    else:
        a.extend(list)
        print("THE LANGUAGES IN LIST: ",a)
