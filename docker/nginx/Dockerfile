FROM nginx:1.21

RUN mkdir -p /var/log/nginx \
    && cd /var/log/nginx \
    && touch access.log error.log
COPY ./assets /assets
