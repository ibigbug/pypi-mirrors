import time

from flask import g, request
from flask import Flask, render_template, Response
from utils import get_page_data, get_json_data

from prometheus_client import make_wsgi_app
from services.metrics import req_counter, rt_histogram

import cron

cron.start()

app = Flask(__name__)


@app.route('/')
def index():
    context = get_page_data()
    return render_template('index.html', **context)


@app.route('/data.json')
def json_data():
    return Response(get_json_data(), mimetype='application/json')


@app.route('/metrics')
def metrics():
    return make_wsgi_app()


@app.route('/status')
def healthcheck():
    return 'ok'


@app.before_request
def before_request():
    g.start_time = time.time()


@app.after_request
def after_request(res):
    meth = request.method
    endpoint = request.path
    status = res.status_code
    req_counter.labels(meth, endpoint, status).inc()

    delta = time.time() - g.start_time
    rt_histogram.labels(meth, endpoint, status).observe(delta)

    return res


if __name__ == '__main__':
    params = {"debug": True,
              "host": "0.0.0.0", }

    app.run(**params)
