from injector import Injector

from internal.handler import AppHandler
from internal.router import Router
from internal.server import Http


def main():
    injector = Injector()

    app = Http(__name__, router=injector.get(Router))
    app.run()

if __name__ == '__main__':
    main()
