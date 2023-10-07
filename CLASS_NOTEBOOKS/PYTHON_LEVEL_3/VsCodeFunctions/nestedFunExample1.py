def print_msg(msg):
    def printer(name):
        print(msg,name)
        def third(a):
            return a*10
        res = third(10)
        return res+10
        
    res1 = printer("Python User") #calling inner function
    print("Outside function")
    res2 = printer("AK")    ##calling inner function
    return res1*res2
    
    
final_res = print_msg("Hello")
print(final_res)
