from aiohttp import web
from proxyscrape import create_collector

from .routes import setup_routes


def main():
    collector = create_collector('prxs-collector', 'https')
    collector.refresh_proxies()
    app = web.Application()
    setup_routes(app)
    web.run_app(app)


if __name__ == '__main__':
    main()
