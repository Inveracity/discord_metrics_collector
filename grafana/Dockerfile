FROM mhart/alpine-node:6

ENV GRAFANA_VERSION=4.3.2

RUN apk add --no-cache openssl
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk
RUN apk add glibc-2.23-r3.apk
RUN wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-$GRAFANA_VERSION.linux-x64.tar.gz
RUN tar -xzf grafana-$GRAFANA_VERSION.linux-x64.tar.gz
RUN mv grafana-$GRAFANA_VERSION/ grafana/
RUN sed -i 's,data = data,data = data/db,g' grafana/conf/defaults.ini
RUN rm grafana-$GRAFANA_VERSION.linux-x64.tar.gz /etc/apk/keys/sgerrand.rsa.pub glibc-2.23-r3.apk


RUN apk add --no-cache unzip
RUN wget https://github.com/grafana/kairosdb-datasource/archive/master.zip
RUN unzip master.zip
RUN mkdir -p grafana/data/plugins/kairosdb
RUN mv kairosdb-datasource-master/ grafana/data/plugins/
RUN npm --prefix /grafana/data/plugins/kairosdb-datasource-master install
RUN npm --prefix /grafana/data/plugins/kairosdb-datasource-master install grunt
RUN npm install -g grunt-cli
RUN grunt --gruntfile /grafana/data/plugins/kairosdb-datasource-master/Gruntfile.js

RUN apk del openssl

VOLUME ["/grafana/conf", "/grafana/data/db", "/grafana/data/log", "/grafana/data/plugins"]

EXPOSE 3000

WORKDIR /grafana
CMD ["./bin/grafana-server"]
