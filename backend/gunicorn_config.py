import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
# MySQL
import MySQLdb
from opentelemetry.instrumentation.dbapi import trace_integration

def post_fork(server, worker):
    trace.set_tracer_provider(TracerProvider())
    otlp_exporter = OTLPSpanExporter(
        endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT') # Replace with your common tracing backend endpoint
    )
    span_processor = BatchSpanProcessor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)
    trace_integration(MySQLdb, "connect", "mysql")

    DjangoInstrumentor().instrument()

# Gunicorn configuration file
bind = "0.0.0.0:8080"
workers = 3
# Add other Gunicorn settings as needed
