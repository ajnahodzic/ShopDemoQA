import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def getEmail():
        email = config.get('common data', 'email')
        return email