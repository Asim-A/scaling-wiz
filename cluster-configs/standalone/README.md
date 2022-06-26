# Setup

This section contains information on how to setup a standalone MongoDB instance on a single host machine.

## Native

Please refer to [Install MongoDB Community Edition on Ubuntu
](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/) from the official MongoDB page.

After this you can connect to the instance.

## Docker

Execute [docker-compose-single.yml](https://github.com/Asim-A/scaling-wiz/tree/master/cluster-configs/standalone) by doing:

```shell
docker stack deploy -c /path/to/file/docker-compose-single.yml [name of stack]
```

```shell
$ docker stack deploy -c "cluster-configs/standalone/docker-compose-single.yml" standalone
Creating network standalone_single
Creating service standalone_mongo1
$ docker stack ls
NAME         SERVICES   ORCHESTRATOR
standalone   1          Swarm
```

```yaml
version: "3"
services:
  mongo1:
    image: mongo:5.0.9-focal
    hostname: mongo1
    ports:
      - "27017:27017"
    volumes:
      - "mongo-data:/data/db"
      - "mongo-config:/data/configdb"
    networks:
      - single
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.labels.tier1 == 1

networks:
  single:

volumes:
  mongo-data:
  mongo-config:
```

After this you can connect to the instance.

```shell
 $ mongosh
Current Mongosh Log ID:	62b8663fa3e54d9cddc875fb
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.0
Using MongoDB:		5.0.9
Using Mongosh:		1.5.0

For mongosh info see: https://docs.mongodb.com/mongodb-shell/
test>
```
