import os

import dotenv
from flask_migrate import Migrate

from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy
from injector import Injector, Module, Binder

from config.config import Config
from internal.extension.database_extension import db
from internal.router import Router
from internal.server import Http

# 将env加载到环境变量中
dotenv.load_dotenv()


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)


def create_app():
    # injector = Injector()
    injector = Injector([ExtensionModule])

    app = Http(__name__,
               conf=Config(),
               db=injector.get(SQLAlchemy),
               migrate=injector.get(Migrate),
               router=injector.get(Router)
               )
    return app


def main():
    app = create_app()
    app.run(port=os.getenv("PORT"))


if __name__ == '__main__':
    main()
