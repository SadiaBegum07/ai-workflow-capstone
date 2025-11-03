from prometheus_client import Counter, generate_latest
from fastapi import Response

REQUEST_COUNT = Counter("matrix_requests_total", "Number of matrix multiplications")

def record_request():
    REQUEST_COUNT.inc()

def metrics_endpoint():
    return Response(generate_latest(), media_type="text/plain")
