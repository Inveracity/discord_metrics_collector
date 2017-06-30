# Discord Metrics Collector

> Turnkey metrics collector for your discord community

This project builds 2 docker containers one with kairosdb 1.1.3 and one with grafana 4.3.2

![grafana](/images/image.png)

goals:
  - gain usage insights into your discord community
  - easy to deploy with minimal configuration

## prerequisites:
To test and deploy this you need

* docker-ce >= 17.03
* docker-compose


```bash
# clone the repo
git clone https://github.com/Inveracity/discord_metrics_collector.git

# change to the directory
cd discord_metrics_collector/

# build the containers
docker-compose build

# start the containers
docker-compose start

# put some testing data in the kairosdb
python bot/generate_test_data.py
```

