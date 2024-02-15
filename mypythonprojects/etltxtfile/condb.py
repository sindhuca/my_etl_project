import mysql.connector
from readconfig import config_read

def connection_db():

    config_read()

    connection_db.conn = mysql.connector.connect(host=config_read.host,user=config_read.user,password=config_read.password,auth_plugin=config_read.auth_plugin)


    if connection_db.conn:
        print("connected to database")
    else:
        print("failed to connect")