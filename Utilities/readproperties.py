
import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+ "\\configuration\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationurl():
        url=config.get("commoninfo","url")
        return url

    @staticmethod
    def getUseremail():
        email=config.get("commoninfo","email")
        return email

    @staticmethod
    def getUserPassword():
        password=config.get("commoninfo","password")
        return password