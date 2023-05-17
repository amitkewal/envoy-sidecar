from random import randint
from flask import Flask, request
import os
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Congrats!!!  Flask z running inside Docker!!!!"

@app.route("/roll")
def roll():
    with tracer.start_as_current_span(
        "server_request", 
        attributes={ "endpoint": "/roll" } 
    ):

        sides = 4
        rolls = 6
        return roll_sum(sides,rolls)

def roll_sum(sides, rolls):
    span = trace.get_current_span()
    sum = 0
    for r in range(0,rolls):
        result = randint(1,sides)
        span.add_event( "log", {
            "roll.sides": sides,
            "roll.result": result,
        })
        sum += result
    return  str(sum)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)



############

# These are the necessary import declarations
from opentelemetry import trace
from opentelemetry import metrics
import os
from random import randint
from flask import Flask, request

tracer = trace.get_tracer("diceroller.tracer")
# Acquire a meter.
meter = metrics.get_meter("diceroller.meter")

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Congrats!!!  Flask z running inside Docker!!!!"


@app.route("/roll")
def roll_dice():
    return str(do_roll())

def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)