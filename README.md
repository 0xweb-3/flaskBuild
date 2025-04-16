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

13. Flask-SQLAlchemy

14. 应用ORM模型的创建与增删改查

15. 重写SQLAlchemy核心类实现自动提交

16.  Flask-Migrate扩展使用

