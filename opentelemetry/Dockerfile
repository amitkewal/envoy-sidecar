FROM otel/opentelemetry-collector:latest

# Copy the configuration file into the container
COPY otel-collector-config.yaml /etc/otel-collector/otel-collector-config.yaml
EXPOSE 55679/tcp
EXPOSE 8889/tcp
EXPOSE 4317/tcp
EXPOSE 4318/tcp
EXPOSE 16686/tcp

# Start the OpenTelemetry Collector with the specified configuration file
CMD ["--config", "/etc/otel-collector/otel-collector-config.yaml"]
