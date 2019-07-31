from ..common import middleware
from . import adapter


@middleware.json_response
def bar(name):
    return adapter.bar(name)
