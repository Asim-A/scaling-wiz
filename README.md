# Overview

Project is split into two parts. First part is the [setup](#Setup) part going over how to deploy different cluster configurations, both natively on linux and on docker. The second part is all the test outputs.


## Setup

[Link to cluster configuration setups](https://github.com/Asim-A/scaling-wiz/tree/master/cluster-configs)

## Testing

[Link to results](https://github.com/Asim-A/scaling-wiz/tree/master/results)

## Prerequisites

1. This repository is assuming the use of [Docker Engine 20.10.17](https://docs.docker.com/engine/release-notes/#201017) and Docker Compose v2.

2. It is also advisable to pull the image of MongoDB that was used under the tests.
   CLI:

```
docker pull mongo:5.0.9-focal
```

3. Open ports used for [Docker Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/#open-protocols-and-ports-between-the-hosts)

   - `sudo ufw allow 2377/tcp`
   - `sudo ufw allow 7946`
   - `sudo ufw allow 4789/udp`

4. Join the swarm with other host machines.
   - On one node execute in CLI: `docker swarm init`. We will receive an instruction on how to join the swarm from other hosts.\* This will become the _Manager_ node.

```
    docker swarm init
    Swarm initialized: current node (ssk6hbn2nph3bt7k94rvh3efh) is now a manager.

    docker swarm join --token SWMTKN-1-5g7jhaxyiz3o1i36rdftry1x12fuscltnkagt961pdzer2ok1x-88hthhicipd6exywd2bto8zo3 192.168.65.3:2377
```

\*If we loose this we can easily regenerate the token from Manager node by using `docker swarm join-token worker`.

5. Label each node. Labeling will allow explicit mapping of deployments.

   ```
    docker node update --label-add tierOne node-1
   ```

   Within docker compose we can use the node property, label, to assign a deployment to label added to a node.

   ```yaml
   deploy:
     replicas: 1
     placement:
       constraints:
         - node.labels.tierOne == 1
   ```

