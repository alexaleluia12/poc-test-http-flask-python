
from . import controller

routes = [
    {'path': '/foo/<name>', 'methods': ['GET'], 'handler': controller.bar},
]
