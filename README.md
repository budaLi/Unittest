##使用说明
本项目只需使用测试实践目录。其余文件可自行删除。
###项目环境搭建
>python环境 python 3.x
>基础环境 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xlrd,xlutils,json,jsonpath_rw
>发送邮件 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple smtplib,email
>测试结果可视化 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib

>###项目说明 
>run_test.py  项目入口  配置好环境后运行该文件即可启动本项目
>data_config.py Excel读取配置 
>operationExcel.py 操作Excel封装
>operationsJson.py  操作Json数据封装 本项目未用到
>runmain.py   post和get请求封装
>dependData.py  测试依赖  本项目未用到
>sendEmail.py  发送邮件
>showTables.py 测试结果可视化 目前只有饼状图
>utils.py  工具类
>testDemo.xls  Excel文件

>下图为本人理解，未完善。
>![](https://github.com/budaLi/Unittest/blob/master/%E6%B5%8B%E8%AF%95%E5%AE%9E%E8%B7%B5/images/mind.png)


>###项目运行结果
>![](https://github.com/budaLi/Unittest/blob/master/%E6%B5%8B%E8%AF%95%E5%AE%9E%E8%B7%B5/images/screen.png)
