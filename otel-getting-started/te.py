from opentelemetry import trace
tracer = trace.get_tracer("roll.dice")


def ss():
    with tracer.start_as_current_span("test") as roll_span:
        print('testtest')
        print('test')