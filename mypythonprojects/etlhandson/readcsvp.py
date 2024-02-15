import pandas as pd

def read_csvp():

    read_csvp.filn = pd.read_csv("product.csv")
    #print(read_csvp.filn)

    read_csvp.lst = []
    for index,row in read_csvp.filn.iterrows():
        pro1,pro2,pro3,pro4 = row["PID"],row["PNAME"],row["QTY"],row["PRICE"]
        tuple_pro = (pro1,pro2,pro3,pro4)
        #print(tuple_pro)
        read_csvp.lst.append(tuple_pro)
    #print(read_csvp.lst)

    read_csvp.itr_lst = []
    for i in read_csvp.lst:
        #print(i)
        var = list(i)
        if var[2]==0:
            var[2] = "out of stock"
            var = tuple(var)
            read_csvp.itr_lst.append(var)
            
        else:
            var = tuple(var)
            read_csvp.itr_lst.append(var)
    # print(read_csvp.itr_lst )        
        


        


read_csvp()