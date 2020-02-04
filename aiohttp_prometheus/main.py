import logging
from aiohttp import web
from handlers.fake1_view import Fake1View
from handlers.status_handler import StatusView
from prometheus_client import start_http_server

from metrics import create_metrics

logger = logging.getLogger()


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([
        web.view('/status', StatusView),
        web.view('/api/v1/fake1', Fake1View),
    ])

    app['metrics'] = create_metrics()
    start_http_server(8000)  # Prometheus metrics server
    web.run_app(app, host="0.0.0.0", port=80)

