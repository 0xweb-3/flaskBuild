import os

import dotenv
from injector import Injector

from internal.router import Router
from internal.server import Http


def main():
    # 将env加载到环境变量中
    dotenv.load_dotenv()

    injector = Injector()

    app = Http(__name__, router=injector.get(Router))
    app.run(port=os.getenv("PORT"))


if __name__ == '__main__':
    main()
