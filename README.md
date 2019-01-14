# StuManSys
数据库课程设计：学生-课程-老师管理系统
## 环境
语言：python3.7.2

数据库：PostgreSQL-11.0

第三方库：web.py 0.40-dev1、psycopg2 2.7.6.1
## 文件结构
init.py:初始化程序，用于初始化数据库。

config.py:配置文件，记录配置的设定。

StuManSys.py:主程序入口

file.py:将html文件、css文件等读入到内存的程序
## Log
2019-01-07 00:00 增加了init.py和config.py。

2019-01-08 01:32 增加了StuManSys.py中用户登录的逻辑，并加入了html显示用户登录结果的页面。

2019-01-08 15:43 增加了每个用户登录以后的主界面、禁止用户访问与其权限不相同的跳转，以及登出的跳转

2019-01-09 00:51 修改了数据库的表项，在用户中增加了no列以识别其对应的学生/教师，令班级/教师/学生/课程的编号统一为
8位数字字符，并对用户暴露，以使用编号完成插入动作。同时增加了视图。

2019-01-09 13:00 更改了代码，使其可以在python3下运行。同时增加了学生查询成绩的模板，以及学生成绩的模块的空壳。

2019-01-09 17:43 开始写教师管理功能，已完成教师的显示。

2019-01-09 20:54 完成教师管理和课程管理功能。

2019-01-10 01:28 完成班级管理和学生管理功能。

2019-01-10 11:28 完成了学生选课功能，在数据库中写入了选课函数。

2019-01-10 23:46 完成了教师修改课程成绩、学生选课、教师查看课程统计信息功能，同时增加了为学生自动添加用户的触发器。

## 实例
实例已经运行在47.112.23.175:80上