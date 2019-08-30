import base64
class Utils:
    def __init__(self):
        pass

    def str_is_equal(self,str1,str2):
        """
        判断两个字符串变为字典是否相等
        :param str1:
        :param str2:
        :return: bool
        """
        str1=str1.replace("true","True")
        if str1 =="":
            return False
        if not isinstance(str1,dict):
            str1=eval(str1)
        if not isinstance(str2,dict):
            str2=eval(str2)
        # print(str1,type(str1))
        # print(str2,type(str2))
        try:
            return str1['returnState']['stateCode']==str2['returnState']['stateCode']
        except Exception as e:
            print("Error")
            return False

    def encrypt_by_base64(self,strs):
        """
        对字符串进行base64加密
        :param strs:
        :return:
        """
        # 编码与解码的处理对象是byte，故对原数据要先编码，使原本的str类型变成byte，解码后直接输出来的是byte对象，故要解码成str对象。
        strs=base64.b64encode(strs.encode())
        res =strs.decode()
        return res

    def encapsulate_headers(self,name,password):
        """
        对密码及headers进行封装
        :return:
        """
        tem= name+":"+password
        strs = self.encrypt_by_base64(tem)
        headers = {
               'Authorization': 'Basic '+strs, # admin:123456
            }
        return headers


if __name__=="__main__":
    util = Utils()
    dic1 ={
                "permission": {
                    "clusterManage": True,
                    "deviceControl": True,
                    "deviceManage": True,
                    "download": True,
                    "opmManage": True,
                    "playback": True,
                    "systemLog": True,
                    "tvmanager": True,
                    "userManage": True,
                    "view": True
                },
                "returnState": {
                    "errorMsg": 0,
                    "stateCode": 0
                }
            }
    dic2 ={'permission': {'clusterManage': True, 'deviceControl': True, 'deviceManage': True, 'download': True, 'opmManage': True, 'playback': True, 'systemLog': True, 'tvmanager': True, 'userManage': True, 'view': True}, 'returnState': {'errorMsg': 0, 'stateCode': 0}}
    # import json
    # print(json.dumps(dic1))
    # print(util.str_is_equal(dic1,dic2))
    print(util.encapsulate_headers('admin','123456'))


