import os

class Config():
    ApiKey:str=''
    ApiSec:str=''
    
    def __init__(self) -> None:
        import configparser
        lConfig = configparser.RawConfigParser()
        lConfig.read(os.path.dirname(os.path.abspath(__file__)) + '/parameters.ini')
        self.ApiKey=lConfig['KRAKEN']['API_KEY']
        self.ApiSec=lConfig['KRAKEN']['API_SEC']
