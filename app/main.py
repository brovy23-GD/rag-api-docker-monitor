"""Observable demo API. This repo does not yet perform RAG or call a language model."""
import os
import time
from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry
from pydantic import BaseModel, Field

app=FastAPI(title="RAG API Docker Monitoring - infrastructure demo",version="0.1.0")
registry=CollectorRegistry()
REQUESTS=Counter("demo_http_requests_total","Total HTTP requests",["method","path","status"],registry=registry)
LATENCY=Histogram("demo_http_request_duration_seconds","HTTP request latency",["method","path"],registry=registry)

class EchoRequest(BaseModel):
    text: str=Field(min_length=1,max_length=2000)

@app.middleware("http")
async def metrics_middleware(request:Request,call_next):
    start=time.perf_counter()
    try:
        response=await call_next(request)
    except Exception:
        REQUESTS.labels(request.method,request.url.path,"500").inc()
        raise
    else:
        if request.url.path != "/metrics":
            REQUESTS.labels(request.method,request.url.path,str(response.status_code)).inc()
            LATENCY.labels(request.method,request.url.path).observe(time.perf_counter()-start)
        return response

@app.get("/health")
def health():return {"status":"ok","service":"monitoring-demo"}

@app.post("/echo")
def echo(payload:EchoRequest):return {"echo":payload.text,"note":"This is a monitoring demonstration; RAG is not implemented."}

@app.get("/metrics")
def metrics():return Response(content=generate_latest(registry),media_type=CONTENT_TYPE_LATEST)
