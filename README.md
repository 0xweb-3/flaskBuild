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

1. 安装flask

```
pip install flask
```

2. 构建简单的应用控制器

3. 引入路由控制，蓝图
3. Flask服务引擎构建
3. flask服务可启动

4. 使用injector管理依赖注入
5. 使用dataclasses简化路由对象`__init__`
6. 

