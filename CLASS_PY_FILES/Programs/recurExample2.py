def fun(num):
    if(num>0): #base condition
        print(num ,end=" ")
        fun(num-1)
        print(num ,end = " ")

if __name__ == '__main__':
    fun(4)