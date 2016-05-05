# SoftwareEngineerLesson

## Dependency
1. python 2.7.11
2. Flask (0.10.1)
3. Jinja2 (2.8)
4. SQLAlchemy (1.0.12)
5. WTForms (2.1)
6. bootstrap(3.3.6)

## Usage

### 前端

#### html
在/aX/templates 目录下编写HTML
eg.
```HTML
<p>
    hello world
</p>
```
#### 输出变量
使用双大括号输出Python变量的值
eg.
```
{{data}}
```
#### if，for语句
使用{% %}表示逻辑控制语句
eg.
```
{%if flag%}
    do something
{% else %}
    do else
{% endif %}
```

#### 引入页面框架
帮助导入bootstrap，并处理好head
{% extends "bootstrap_base.html" %}

### 导入数据
在/aX/views/aX_models 目录下创建文件，便于在HTML中使用数据, 只需要在doc中描述清楚，让后端开发者能看懂即可。
eg.
```python
class data(object):
    """
    1. userlist: user list
        user: nickname, email
    """
    # 我觉得还不错的方法
    # 表示包含了一个list 叫做 userlist
    # userlist 中包含的是 user，每一项有昵称和邮件
    def __init__(self):
        super(data, self).__init__()
```

## 逻辑控制
在aX/views 下编写即可，注意不要重名，详细看例子
eg.
```python
from flask import render_template  # 帮助生成页面
from models import user            # 从数据库导入数据
from manager import app            # 路由管理
from a2_models import a2_index     # 页面需求的数据格式

@app.route('/a2')
def a2():
    temp_data = a2_index.data()
    temp_data.userlist = user.User.get_users()
    return render_template("a2.html", data = temp_data)
```

## 数据库
在/models 下编写即可，详细看例子
eg.
```python
from manager import db # 导入数据库

class User(db.Model): # 建立User 表
    # 建立id 字段，类型为integer 主键
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    # 提供给写逻辑的使用的查询所有用户的方法
    @staticmethod
    def get_users():
        return User.query.all()
```
**注意**
更新完成后在运行/db_migrate.py 才真的执行自动生成的SQL

## reference
[The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[中文版](http://www.pythondoc.com/flask-mega-tutorial/#)
