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

        sides = 5
        rolls = 7
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