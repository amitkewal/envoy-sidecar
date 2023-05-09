FROM otel/opentelemetry-collector:latest

# Copy the configuration file into the container
COPY otel-collector-config.yaml /etc/otel-collector/
EXPOSE 55679/tcp
EXPOSE 8889/tcp

# Start the OpenTelemetry Collector with the specified configuration file
CMD ["--config", "/etc/otel-collector/otel-collector-config.yaml"]
