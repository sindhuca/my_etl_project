from condb import connection_db
from query import query,count,insrt_query
from readtxtfile import readtxt

def run_etl():
    connection_db()
    readtxt()


    curr = connection_db.conn.cursor()
    # query = ''' '''
    curr.execute(count)
    rows = curr.fetchall()
    # print(rows)
    for i in rows:
        for j in i:
            k = j
    print(k)
    print(readtxt.li)
    
    if k == readtxt.li:
       
        for i in readtxt.tli:
            curr.execute(insrt_query,i)

        print("validation passed allows insert")
    else:
        print("validation failed to load")