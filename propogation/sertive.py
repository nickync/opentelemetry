from random import randint
from flask import Flask, request
from opentelemetry import trace, baggage
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
from opentelemetry.baggage.propagation import W3CBaggagePropagator
from opentelemetry.sdk.trace import TracerProvider
from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


tracer = trace.get_tracer("roll.dice")

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

tracer = trace.get_tracer(__name__)

@app.route("/")
def roll_dice():
    headers = dict(request.headers)
    print(f"Received headers: {headers}")
    carrier ={'traceparent': headers['Traceparent']}
    ctx = TraceContextTextMapPropagator().extract(carrier=carrier)
    print(f"Received context: {ctx}")

    b2 ={'baggage': headers['Baggage']}
    ctx2 = W3CBaggagePropagator().extract(b2, context=ctx)
    print(f"Received context2: {ctx2}")

    # Start a new span
    with tracer.start_span("api2_span", context=ctx2):
       # Use propagated context
        print(baggage.get_baggage('hello', ctx2))
        return "Hello from API 2!"

if __name__ == '__main__':
    app.run(port=5001)