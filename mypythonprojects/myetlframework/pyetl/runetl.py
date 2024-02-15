from pyetl.conn import conn_etl
from pyetl.querybox import query

from importlib.machinery import SourceFileLoader


def query_etl():
		    
    # x = SourceFileLoader("readfile","/home/manjiro/Desktop/readfile.py").load_module()
    
    # x.readsource()
    
    # y = x.readsource.finl
    conn_etl()
    cur = conn_etl.conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    # for i in y:
    # 	cur.execute(insert,i)
    # 	conn_etl.conn.commit()
    
    
    conn_etl.conn.close()
    print(result)
