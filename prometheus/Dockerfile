# Use a minimal base image
FROM alpine:3.14

# Install Prometheus
RUN wget -O /tmp/prometheus.tar.gz https://github.com/prometheus/prometheus/releases/download/v2.33.1/prometheus-2.33.1.linux-amd64.tar.gz && \
    tar -xzvf /tmp/prometheus.tar.gz -C /tmp && \
    mv /tmp/prometheus-2.33.1.linux-amd64/prometheus /usr/local/bin/ && \
    mv /tmp/prometheus-2.33.1.linux-amd64/promtool /usr/local/bin/ && \
    rm -rf /tmp/prometheus-2.33.1.linux-amd64 /tmp/prometheus.tar.gz

COPY prometheus.yml /etc/prometheus/prometheus.yml
# Expose Prometheus' default port
EXPOSE 9090

# Set the entrypoint to the Prometheus binary
ENTRYPOINT ["/usr/local/bin/prometheus"]

# Set the command to run Prometheus with the configuration file
CMD ["--config.file=/etc/prometheus/prometheus.yml"]
