from internal.handler import AppHandler
from internal.router import Router
from internal.server import Http


def main():
    app_handler = AppHandler()
    router = Router(app_handler)
    app = Http(__name__, router=router)
    app.run()

if __name__ == '__main__':
    main()
