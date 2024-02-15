import configparser
import os,sys

def config_read():

    read_config = configparser.RawConfigParser()
    read_config.read("config.ini")
    
    # print(read_config.get("MYSQL","host"))
    config_read.host = read_config.get("MYSQL","host")
    config_read.user = read_config.get("MYSQL","user")
    config_read.password = read_config.get("MYSQL","password")
    config_read.auth_plugin = read_config.get("MYSQL","auth_plugin")