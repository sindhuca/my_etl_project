def readtxt():

    f = open("ddl", "r") 
         
    li=[]

    for i in f:
        li.append(i.strip())
        
        li = li[1:]
        print(li)
 
    readtxt.li=len(li)
    print(readtxt.li)
    
    # f.close()    

    # r = open('txtfile.txt', 'r')
    #     # tup = tuple(filehandle.read())
    # # tup = r.read()
    # readtxt.tli = []
    # for i in r:
    #     m = [i.strip()]
    #     readtxt.tli.append(tuple(m))

    # f.close()
    # r.close()

    


   
