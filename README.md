## 使用说明 
>本项目只需使用MyAutoTest目录。其余文件可自行删除。
>### 项目环境
>1.python环境 python 3.x

>2.其他依赖包 在req.txt中 可使用 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r req.txt下载依赖

>3.目录结构如下 

![](https://github.com/budaLi/Unittest/blob/master/1.png)


>### 项目说明 

>1. Excel目录  存放Excel测试文件及生成结果的Exel

>2. Image目录  存在无关照片 
  
>3. templete目录 为特殊接口类生成数据模板 登录接口单独提出

>4. TestMain目录 

>4.1    test_data_config.py 测试用例Excel读取配置 

>4.2    res_data_config.py 测试结果Excel读取配置 

>4.3    operationExcel.py 操作Excel封装

>4.4    operationsJson.py  操作Json数据封装

>4.5    runmain.py   post和get请求封装

>4.6    dependData.py  测试依赖  

>4.7    sendEmail.py  发送邮件

>4.8    showTables.py 测试结果可视化 目前只有饼状图

>4.9    utils.py  工具类

>4.10   mockData.py 模拟数据

>4.11   headers.py  请求头生成

>### 基础流程

> 配置好依赖包后 在主文件中 输入 python run_test.py -f +测试用例所在文件夹目录 即可

>1.测试用例示图

> ![测试用例示图](https://github.com/budaLi/Unittest/blob/master/ceshi.png)

>2.测试结果示图

> ![测试结果示图](https://github.com/budaLi/Unittest/blob/master/res.png)







