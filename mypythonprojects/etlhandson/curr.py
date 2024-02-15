from con_mysql import conn_db
from readcsvp import read_csvp

def curr_cre():

    conn_db()
    curr = conn_db.conn.cursor()
    query = '''insert into data_warehouse.handson_pro(PID,PNAME,QTY,PRICE) values(%s,%s,%s,%s)'''
    read_csvp()
    for i in read_csvp.itr_lst:
        curr.execute(query,i)
        print("inserted row is :{}".format(i))
        conn_db.conn.commit() 

    conn_db.conn.close() 

curr_cre()