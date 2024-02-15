import configparser
#import os.sys

def read_config():

    x = configparser.RawConfigParser()
    x.read("./config.ini")

    read_config.host = x.get("MYSQL","host")
    # print(read_config.host)
    read_config.user = x.get("MYSQL", "user")
    read_config.password = x.get("MYSQL", "password")
    read_config.authplugin = x.get("MYSQL","authplugin")

# read_config()