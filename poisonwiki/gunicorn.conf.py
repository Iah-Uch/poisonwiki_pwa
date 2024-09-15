"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count
from os import environ


bind = "0.0.0.0:" + environ.get("PORT", "8000")
module = "core.wsgi:application"
max_requests = 1000
worker_connections = 1000
workers = cpu_count() * 2 + 1


certfile = "/etc/letsencrypt/live/pesquisa.poisonwiki.com.br/fullchain.pem"
keyfile = "/etc/letsencrypt/live/pesquisa.poisonwiki.com.br/privkey.pem"
