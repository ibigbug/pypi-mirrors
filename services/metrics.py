from prometheus_client import Counter, Histogram


req_counter = Counter(
    'http_requests_total',
    'HTTP requests total',
    ['method', 'endpoint', 'status']
)
rt_histogram = Histogram(
    'http_response_time_seconds',
    'HTTP response time seconds',
    ['method', 'endpoint', 'status']
)
