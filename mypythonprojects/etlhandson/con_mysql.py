import mysql.connector
from readconfig import read_config

def conn_db():

    read_config()

    conn_db.conn = mysql.connector.connect(host=read_config.host,user=read_config.user,password=read_config.password,auth_plugin=read_config.authplugin)

    if conn_db.conn:
        print("connected")
    else:
        print("failed connection")

# conn_db()