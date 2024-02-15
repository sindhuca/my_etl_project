import configparser
import os,sys

def read_config():
    config = configparser.RawConfigParser()

    config.read("pyetl/config.ini")
    

    read_config.user = config.get("MYSQL","user")
    read_config.password = config.get("MYSQL","password")   
    read_config.host = config.get("MYSQL","host")
    read_config.authin = config.get("MYSQL","auth_plugin")