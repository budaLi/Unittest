import json

class OperationJson:
    """
    操作json数据
    """
    def __init__(self,file_path):
        self.file_path=file_path
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_path,'r') as f:
            data = json.load(f)
            return data

    def write_data(self,file_path,data):
        with open(file_path,'w') as f:
            f.write(json.dumps(data))

    def get_data(self,key):
        if key in self.data:
            return self.data[key]
        print("键值 %s 不存在"%key)
        return None


if __name__=="__main__":
    oper=OperationJson('user.json')
    data = oper.read_data()
    print(data)
    print(oper.get_data('user3'))