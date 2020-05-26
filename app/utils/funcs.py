import numpy as np
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from .config import *
import os

class HandleDB:
    '''操作数据库'''
    @staticmethod
    def run_sql(sql, engine):
        engine.execute(sql)
        # engine.dispose()

    @staticmethod
    def to_sql(df, tb_name, engine=ENGINE, if_exists='append'):
        df.to_sql(
            tb_name,
            con = engine,
            if_exists = if_exists,
            index = False,
            chunksize = 2000000)

    @staticmethod
    def read_sql(sql, engine):
        df = pd.read_sql(sql,engine)
        engine.dispose()
        return df

class HandleEnv:
    '''配置系统环境'''
    @staticmethod
    def freeze_packages():
        cmd = 'pip3 freeze >requirements.txt'
        os.system(cmd)

    @staticmethod
    def install_packages():
        os.system('pip3 install -r requirements.txt')

class HandleHTTP:
    @staticmethod
    def get(req_data):
        '''将请求数据以json形式返回'''
        print(req_data.method)
        if req_data.method == 'POST':
            data = req_data.json
        elif req_data.method == 'GET':
            data = req_data.args

        return data