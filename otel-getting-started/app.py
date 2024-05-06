from random import randint
from flask import Flask, request
import logging
from opentelemetry import trace, propagators, baggage
from opentelemetry import metrics
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
import te as t
from dic import dic
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.baggage.propagation import W3CBaggagePropagator
import requests


tracer = trace.get_tracer("roll.dice")
meter = metrics.get_meter("diceroller.meter")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

resource = Resource(attributes={
    SERVICE_NAME: "hello"
})

@app.route("/rolldice")
def roll_dice():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as roll_span:
        player = request.args.get('player', default = None, type = str)
        result = str(roll())
        roll_span.set_attribute("roll.value", result)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": result})
        obj = dic('', result)
        ctx = baggage.set_baggage('hi', 'hi')
        headers = {}
        W3CBaggagePropagator().inject(headers, ctx)
        TraceContextTextMapPropagator().inject(headers, ctx)
        print(headers)

        if player:
            logger.warn("{} is rolling the dice: {}", player, result)
        else:
            logger.warn("Anonymous player is rolling the dice: %s", result)

        response = requests.get('http://127.0.0.1:5001/', headers=headers)
    
    t.ss()
    return f"Hello from API 1! Response from API 2: {response.text}"
    #return result

def roll():
    return randint(1, 6)



if __name__ == '__main__':
    app.run(port=5002)