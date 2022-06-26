# Setup

This section will be information on setting up iperf3 natively and in a docker container.

## Native

For ubuntu we can easily install it by running

```shell
sudo apt-get install -y iperf3
```

If installing through package manager is not an option, check the official website:
[https://iperf.fr/iperf-download.php#ubuntu](https://iperf.fr/iperf-download.php#ubuntu)

## Docker

We can setup a stack using Docker Compose to have a container running iperf3 on supplied port. We will be using the default 5201.

```shell
docker stack deploy -c /path/to/file/docker-compose-iperf.yml
```

```shell
docker stack deploy -c cluster-configs/iperf3/docker-compose-iperf.yml net
```

We can adjust the network settings in the docker compose.

```yaml
version: "3"
services:
  iperf:
    image: networkstatic/iperf3:latest
    command: iperf3 -s
    ports:
      - "5201:5201"
    networks:
      - iperf3
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.labels.tier == 1

networks:
  iperf3:
    driver_opts:
      com.docker.network.driver.mtu: 1500
```
