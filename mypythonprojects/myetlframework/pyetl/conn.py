import mysql.connector
from pyetl.readconfig import read_config


def conn_etl():

    read_config()

    conn_etl.conn = mysql.connector.connect(host=read_config.host,user=read_config.user,password=read_config.password,auth_plugin=read_config.authin) 
    if conn_etl.conn:
        print("Connected to MySQL Server version ")
        # print(conn)
    else:
        print("Failed to connect to the database ")
