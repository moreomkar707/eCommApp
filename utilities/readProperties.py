import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
       url =  config.get("common info", "baseURL")
       return url

    @staticmethod
    def getUserEmail():
        useremail = config.get("common info", "useremail")
        return useremail

    @staticmethod
    def getPassword():
        passwd = config.get("common info", "password")
        return passwd




