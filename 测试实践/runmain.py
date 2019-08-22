import requests
class RunMain:
    """
    重新封装get和post方法
    """
    def get(self,url,headers=None):
        if headers:
            #verify  取消https 中ssl证书验证
            response = requests.get(url=url,headers=headers,verify=False)
        else:
            response = requests.get(url=url,verify=False)
        return response.json()

    def post(self,url,data,headers=None):
        if headers:
            response = requests.post(url=url,data=data,headers=headers).json()
        else:
            response= requests.post(url=url,data=data).json()
        return response

    def main(self,method,url,data= None,headers = None):
        if method=='POST':
            res = self.post(url,data,headers)
        else:
            res = self.get(url.headers)
        return res



