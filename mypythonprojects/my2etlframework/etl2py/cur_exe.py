from etl2py.condb import connection_db
from etl2py.query import temp,insrt_temp,dell,pre_process
from etl2py.readcsvfile import read_csvfile

def run_etl():
     
     connection_db()

     read_csvfile()

     curr = connection_db.conn.cursor()
     curr.execute(temp)
     connection_db.conn.commit()

     for val in read_csvfile.finl:
          curr.execute(insrt_temp,val)
     # row_count = curr.fetchall()
     connection_db.conn.commit()

     curr.execute(dell)
     connection_db.conn.commit()

     curr.execute(pre_process)
     connection_db.conn.commit()

     # connection_db.conn.close()
     # print("number of rows in employee details table:",row_count)

