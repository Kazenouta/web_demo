from app.utils.config import *
from app.utils.funcs import *
from flask import jsonify, request
import base64
import json
from Crypto.Cipher import AES

class UserInfo(object):
    @staticmethod
    def get_phone(req_data):
        '''
        获取用户手机号
        '''
        # 获取请求信息内容
        session_key = req_data.get('session_key')
        encrypted_data = req_data.get("encryptedData")
        iv = req_data.get("iv")
        # 解密请求信息
        try:
            sessionKey = base64.b64decode(session_key)
            encryptedData = base64.b64decode(encrypted_data)
            iv = base64.b64decode(iv)
            cipher = AES.new(session_key, AES.MODE_CBC, iv)
            s = cipher.decrypt(encrypted_data)
            decrypted = json.loads(s[:-ord(s[len(s)-1:])])
            if decrypted['watermark']['appid'] != APPID:
                raise Exception('Invalid Buffer')
            phone = decrypted['phoneNumber']
            ret = json.dumps({"phone":phone},ensure_ascii=False)
        except Exception as e:
            ret = json.dumps({'msg':f'获取phone失败 - {str(e)}'},ensure_ascii=False)

        return ret

    @staticmethod
    def get(openid):
        '''从数据库获取用户信息'''
        sql = '''SELECT  * 
                 FROM user_info 
                 WHERE openid="{openid}"
                 '''.format(openid=openid)
        ret = pd.read_sql(sql,ENGINE).reset_index(drop=True)

        return ret

    @staticmethod
    def save(req_data):
        '''向数据库保存用户信息'''
        user_info = {
            'name':req_data.get('name'),
            'phone':req_data.get('phone'),
            'openid':req_data.get('openid'),
            'floor_area':req_data.get('floor_area'),
            'window_area':req_data.get('window_area')}

        openid = user_info['openid']
        check_openid = UserInfo.get(openid)

        if len(check_openid)==0:
            user_info = pd.DataFrame([user_info])
            HandleDB.to_sql(user_info, 'user_info')
            return {'success':True}
        elif len(check_openid)==1:
            return {'success':True}
        else:
            return {'success':False,'msg':'保存失败'}

