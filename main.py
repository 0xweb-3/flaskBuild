import os

import dotenv
from injector import Injector

from config.config import Config
from internal.router import Router
from internal.server import Http


def create_app():
    # 将env加载到环境变量中
    dotenv.load_dotenv()

    injector = Injector()

    app = Http(__name__, conf=Config(), router=injector.get(Router))
    return app


def main():
    app = create_app()
    app.run(port=os.getenv("PORT"))


if __name__ == '__main__':
    main()
