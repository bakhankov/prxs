import json

from aiohttp import web
from proxyscrape import get_collector


async def index(request):
    collector = get_collector('prxs-collector')
    return web.Response(text=json.dumps(collector.get_proxy()))
