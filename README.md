# flask项目工程化的一步步构建

## 环境

安装venv环境

```shell
python -m venv myenv # 创建虚拟环境

source myenv/bin/activate

```

## 包管理

安装

```
pip install --no-deps pipreqs

pip install yarg==0.1.9 docopt==0.6.2
```

使用

```
# win下
pipreqs --ignore venv --force

# mac下
pipreqs --ignore myenv --force
```

## 构建步骤

1. ✅安装flask

```
pip install flask
```

2. ✅构建简单的应用控制器

3. ✅引入路由控制，蓝图

4. ✅Flask服务引擎构建

5. ✅flask服务可启动

6. ✅使用injector管理依赖注入

   ```
   pip install injector
   ```

7. ✅使用dataclasses简化路由对象`__init__`

   ```
   pip install dataclasses
   ```

8. ✅引入`.env`环境变量

   ```
   pip install dotenv
   ```

9. ✅实现表单的验证，并关闭csrf

10. ✅统一响应数据格式

11. ✅异常与错误的统一

12. ✅pyTest测试

13. ✅Flask-SQLAlchemy

14. ✅应用ORM模型的创建与增删改查

15. ✅重写SQLAlchemy核心类实现自动提交

16.  ✅Flask-Migrate扩展使用



## pytest 用法

```shell
# 直接运行文件夹内符合规则的所有用例
 pytest folder_name
 
#执行某个 Python 文件中的用例
 pytest test_file.py
 
# 执行某个 Python 文件内的某个函数
 pytest test_file.py::test_func
 
# 执行某个 Python 文件内某个测试类的某个方法
 pytest test_file.py::TestClass::test_method
 
# 运行测试时显示标准输出(stdout),允许测试中的 print0) 语句直接输出到终端
 pytest -s
 
#运行测试时显示标准输出(stdout),允许测试中的 print() 语句直接输出到終端
 pytest -s
 
#运行测试时显示详细的信息,包括每个测试用例的名称及结果(通过/失败/跳过等), -v 代表 verbose
 pytest -v
```

## Flask-Migrate 

```shell
pip install flask-migrate
```

### 常见指令

1. 初始化迁移环境

   在开始迁移数据之前,需要先使用init命令初始化创建一个迁移环境:

   ```bash
   #当flask 的应用入口在项目根目录,且文件名为 app.py,并且实例变量名为app时 
   flask --app main.py db init
   ```

   运行好命令后，就会在 directory 指定的位置创建一个迁移环境，默认位置为 ./migrations。

2. 生成迁移脚本

   使用如下命令自动生成迁移脚本:

   ```bash
   flask --app main.py db migrate -m "create_table"
   ```

   在生成的迁移脚本中有两个函数：

   - upgrade()：把迁移中的改动应用到数据库中；
   - downgrade（）：将改动撤销；

   注意下，在生产环境中一般不使用 Flask-Migrate 迁移，一般人工生成相应的 SQL 执行迁移，如果要使用迁移，一定要仔细检查生成的迁移文件是否符合预期,确认后才可以使用。

3. 更新及回滚数据库

   生成迁移脚本后，可以使用 upgrade 命令来更新数据库，如下：

   ```bash
   flask --app app.server.app db upgrade
   ```

   每一次更新ORM模型,都需要执行migrate命令生成迁移文件,然后才可以使用upgrade命令将更新同步到数据库中。

   如果想要回滚数据库，可以使用 downgrade 命令，如下：

   ```bash
   flask --app app.server.app db downgrade
   ```

   每执行一次命令会向上回滚一个版本，如果想一次性回滚到最原始的版本，即删除所有数据库，可以使用如下命令：

   ```bash
   flask --app app.server.app db downgrade base
   ```

   如果想回滚到特定的版本，可以在 downgrade 后带上特定的版本号，如下：

   ```bash
   flask --app app.server.app db downgrade 版本号
   ```
