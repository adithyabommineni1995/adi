import functools
def nested_sum():
        t = 0
        list_n=[0,[1,2],3,[4,5]]
        for j in list_n:
                if(isinstance(j,list)):
                        t = t + functools.reduce((lambda x,y: x+y) ,j)
                else:
                        t=t+j
        print(t)
nested_sum()



