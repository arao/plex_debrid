import json
import os
from enum import Enum, EnumMeta

from ui import ui_print

http_proxy_endpoint = os.environ.get('CUSTOM_HTTP_PROXY')
https_proxy_endpoint = os.environ.get('CUSTOM_HTTPS_PROXY')
ftp_proxy_endpoint = os.environ.get('FTP_PROXY')

proxy_config = {key: value for key, value in {
    'http': http_proxy_endpoint,
    'https': https_proxy_endpoint,
    'ftp': ftp_proxy_endpoint
}.items() if value is not None}


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class Service(BaseEnum):
    TORRENTIO = "TORRENTIO",
    RARBG = "RARBG",
    PROWLARR = "PROWLARR",
    ORIONOID = "ORIONOID",
    NYAA = "NYAA",
    JACKETT = "JACKETT",
    X1337 = "X1337",

    ALLDEBRID = "ALLDEBRID",
    DEBRIDLINK = "DEBRIDLINK",
    PREMIUMIZE = "PREMIUMIZE",
    PUTIO = "PUTIO",
    REALDEBRID = "REALDEBRID",

    JELLYFIN = "JELLYFIN",
    OVERSEERR = "OVERSEERR",
    PLEX = "PLEX",
    TRAKT = "TRAKT",


allowed_proxy_services = [Service(x) for x in json.loads(os.environ.get('PROXY_SERVICES', "[]")) if x in Service]


def get_proxy(service: Service):
    if service in allowed_proxy_services:
        ui_print(f"Using proxy {proxy_config} for {service.value} ")
        return proxy_config
    return None

