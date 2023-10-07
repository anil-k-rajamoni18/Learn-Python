recursive_count = 0
def printName(fname,lname): 
    global recursive_count
    print(fname+' '+lname)
    recursive_count += 1
    print(recursive_count)
    printName('Akumar' , "K") #recnestursive calls / functions 

    
printName('Kumar','R') 