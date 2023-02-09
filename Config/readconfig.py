#封装成别人可以使用的代码
import configparser
import os
print(os.path.dirname(os.path.dirname(__file__)))
class xxreadini():
#初始化 路径
    #参数1 file_name文件名指定文件名
    #参数2 node 指定所需要节点名
    def __init__(self,file_name=None,node=None):
        self.file_name = file_name
        self.node = node
        if self.file_name == None:
            #文件名 加r 防止自动转义
            self.file_name = os.path.dirname(os.path.dirname(__file__)) +"\Config\config.ini"
        if self.node==None:
            self.node="xiaoxinconfig"
        self.cf=self.load_ini(self.file_name)

#加载配置文件
    def load_ini(self,file_name):
        #获取解析配置对象
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding="utf-8")
        return cf

    def get_value(self,key):
        return  self.cf.get(self.node,key)

if __name__ == '__main__':
    aa = xxreadini()
    print(aa.get_value("browser"))