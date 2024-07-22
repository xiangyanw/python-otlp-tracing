import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor

def post_fork(server, worker):
    trace.set_tracer_provider(TracerProvider())
    otlp_exporter = OTLPSpanExporter(
        endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT') # Replace with your ADOT Collector endpoint
    )
    span_processor = BatchSpanProcessor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    DjangoInstrumentor().instrument()

# Gunicorn configuration file
bind = "0.0.0.0:8000"
workers = 3
# Add other Gunicorn settings as needed