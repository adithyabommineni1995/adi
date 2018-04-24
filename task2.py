
import functools
def even_sum():
        total=0
        mylist=[]
        for i in range(100,500):
                if(i%2==0):
                        mylist.append(i)
        total+=functools.reduce((lambda x,y: x+y),mylist)
        print(total)
even_sum()
