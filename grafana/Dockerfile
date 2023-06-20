# grafana/Dockerfile
FROM grafana/grafana:latest

USER grafana

COPY ./dashboards.yml /etc/grafana/provisioning/dashboards/
COPY ./datasources.yaml /etc/grafana/provisioning/datasources/
COPY ./default_dashboard.json /etc/grafana/provisioning/dashboards/
