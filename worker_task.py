# because i don't have timelines (proj2) service running, so i use this module to
# involke sandman
import logging.config
import bottle
import json
import requests
import sys
from bottle import get, post, error, abort, request, response, HTTPResponse, redirect, HTTPError


app = bottle.default_app()
app.config.load_config('./etc/gateway.ini')
logging.config.fileConfig(app.config['logging.config'])

servers_list = json.loads(app.config['proxy.upstreams'])


def worker_post_a_twitter(inputs):
    logging.debug("in worker_post_a_twitter")
    server_posts = (servers_list['posts'][0])
    headers = {}
    headers["Content-Type"] = "application/json"
    response = requests.request(
        method='POST',
        url=server_posts+'/posts/',
        data=inputs,
        headers=headers,
    )
    logging.debug('status code is: '+str(response.status_code))
    logging.debug((response.content))
    return response.content


def worker_inverted_index(inputs):
    logging.debug("worker_inverted_index")
    server_search_engine = (servers_list['search-engine'][0])
    headers = {}
    headers["Content-Type"] = "application/json"
    response = requests.request(
        method='POST',
        url=server_search_engine+'/search-engine/inverted-index/',
        data=inputs,
        headers=headers,
    )
    logging.debug('status code is: '+str(response.status_code))
    logging.debug((response.content))
