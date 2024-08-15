import code
import requests, json
from django.conf import settings
from time import time
from .config import Config

class AwsSDKConnectDB():

    def __init__(self) -> None:
        self.config = Config()

        self.aws_url_base = self.config.url
        self.path = self.config.connect_path

    def get_selectFrom(self, tableName:str = "", sql:str="", fieldsName:list=[] , whereFields1:str="", whereValues1:str="", whereFields2:str="", whereValues2:str="", whereFields3:str="", whereValues3:str="", whereFields4:str="", whereValues4:str="",orderFields1:str="",orderValues1:str="",justOneRow:bool=False, dbName:str=""):
        body = {
            "sql": sql,
            "table_name": tableName,
            "fieldsName": fieldsName,
            "whereFields1": whereFields1,
            "whereValues1": whereValues1,
            "whereFields2": whereFields2,
            "whereValues2": whereValues2,
            "whereFields3": whereFields3,
            "whereValues3": whereValues3,
            "whereFields4": whereFields4,
            "whereValues4": whereValues4,
            "orderFields1": orderFields1,
            "orderValues1": orderValues1,
            "justOneRow": justOneRow
            }
        return self._post_request(body, dbName)

    def get_selectFromLike(self, tableName:str = "", sql:str="", fieldsName:list=[] , whereFields1:str="", whereFields2:str="", whereFields3:str="", whereFields4:str="",whereFields5:str="", whereValues5:str="",whereValues1:str="",orderFields1:str="",orderValues1:str="",justOneRow:bool=False, dbName:str=""):
        body = {
            "sql": sql,
            "table_name": tableName,
            "fieldsName": fieldsName,
            "whereFields1": whereFields1,
            "whereFields2": whereFields2,
            "whereFields3": whereFields3,
            "whereFields4": whereFields4,
            "whereFields5": whereFields5,
            "whereValues5": whereValues5,
            "whereValues1":whereValues1,
            "orderFields1": orderFields1,
            "orderValues1": orderValues1,
            "justOneRow": justOneRow
            }
        return self._post_request(body, dbName)

    def post_insertInto(self, tableName:str = "", sql:str="", fieldsName:list=[], values:list=[],dbName:str=""):
        body = {
            "sql": sql,
            "table_name": tableName,
            "fieldsName": fieldsName,
            "values": values
            }
        return self._post_request(body, dbName)

    def post_updateWhere(self, tableName:str = "", sql:str="", fieldsName:str='', values:str='', fieldsName2:str='', values2:str='', fieldsName3:str='', values3:str='', fieldsName4:str='', values4:str='', whereFields1:str="", whereValues1:str="",whereFields2:str="",whereValues2:str="",justOneRow:bool=False, dbName:str=""):
        body = {
            "sql": sql,
            "table_name": tableName,
            "fieldsName": fieldsName,
            "values": values,
            "fieldsName2": fieldsName2,
            "values2": values2,
            "fieldsName3": fieldsName3,
            "values3": values3,
            "fieldsName4": fieldsName4,
            "values4": values4,
            "whereFields1": whereFields1,
            "whereValues1": whereValues1,
            "whereFields2": whereFields2,
            "whereValues2": whereValues2,
            "justOneRow": justOneRow
            }
        return self._post_request(body, dbName)

    def _post_request(self, body={}, dbName:str=""):
        payload = json.dumps(body)
        headers = {
            "Content-Type": "application/json"
            }
        base_url:str=''
        if isinstance(dbName,str) and dbName == 'gocontroldb':
            base_url = self.aws_url_base
        response = requests.post(base_url + self.path, headers=headers, data=payload)
        resp = response.json()
        if ('status_code' in resp) and resp['status_code']==200:
            body = json.loads(resp['body'])
            print(json.dumps(body, indent=4))
        return body