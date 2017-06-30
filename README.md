# Discord Metrics Collector

> Turnkey metrics collector for your discord community

This project builds 2 docker containers one with kairosdb 1.1.3 and one with grafana 4.3.2

![grafana](/images/image.png)

goals:
* gain usage insights into your discord community
* easy to deploy with minimal configuration

## prerequisites:
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

# usage

Navigate to http://localhost:3000

1. login with admin/admin

2. add a datasource
![grafana](/images/datasource.jpg)

If you look in the Vagrantfile, you'll notice the vm has the IP address of 192.168.56.2, in your case the IP address to enter is the IP of the host the docker containers are running on.

3. Upload the dashboard json file
![grafana](/images/uploadjson.jpg)

Click the upload button and find the Discord_starwars.json file

![grafana](/images/uploadjson2.jpg)

give the dashboard a name and select the `kairosdb` datasource

and finally click Import.

and now you should have a dashboard that you can customise to your liking.

# Todo:
* add grafana configuration file to change login easily
