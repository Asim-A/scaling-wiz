# Setup

This section contains information on how to setup two sharded cluster. Each shard has a PSA replica member set. Config servers in Primary-Secondary-Secondary (PSS) configuration are also required so that current state of database is known. Additionally a query router (mongos) is required to route the queries to appropriate instances. Mongos achieves this by _asking_ the config servers about the shards. With the config servers, the shards and the query router will this configuration host 10 different containers.

Only the Docker setup is covered in this edition as setting up a cluster

## Docker

This setup is very close to the PSA only setup. In this case we have to create 10 different containers. 1 is for query routing (mongos), 3 of them are for config servers in same replica, and 2 \* 3 PSA for two different shards. We will call the config set for `configSet`, first shard `rsSh1`, second shard `rsSh2`. The mongos will be started with the command:

```shell
 mongos --port 27017 --configdb configSet/mongo-config-1:27017,mongo-config-2:27017,mongo-config-3:27017
```

This links up the query router with the config servers.

Execute [docker-compose-2SH-PSA.yml](https://github.com/Asim-A/scaling-wiz/tree/master/cluster-configs/2sh-psa) by:

```shell
docker stack deploy -c /path/to/file/docker-compose-2SH-PSA.yml
```

```shell
docker stack deploy -c cluster-configs/2sh-psa/docker-compose-2SH-PSA.yml sharded
$ docker stack deploy -c "cluster-configs/2sh-psa/docker-compose-2SH-PSA copy.yml" sharded
Ignoring unsupported options: links

Creating network sharded_sharded-cluster
Creating service sharded_shard-1c
Creating service sharded_shard-1a
Creating service sharded_shard-2b
Creating service sharded_mongo-config-3
Creating service sharded_mongo-config-2
Creating service sharded_mongo-router
Creating service sharded_shard-2c
Creating service sharded_shard-1b
Creating service sharded_mongo-config-1
Creating service sharded_shard-2a
```

Below is output of the services running.

```shell
 $ docker service ls
ID             NAME                     MODE         REPLICAS   IMAGE               PORTS
wozaugyf8aar   sharded_mongo-config-1   replicated   1/1        mongo:5.0.9-focal   *:27119->27017/tcp
cgjswdvy6oav   sharded_mongo-config-2   replicated   1/1        mongo:5.0.9-focal   *:27120->27017/tcp
t4nhnqflvksd   sharded_mongo-config-3   replicated   1/1        mongo:5.0.9-focal   *:27121->27017/tcp
6ab2lm56jojc   sharded_mongo-router     replicated   1/1        mongo:5.0.9-focal   *:27017->27017/tcp
qzetfsckp05k   sharded_shard-1a         replicated   1/1        mongo:5.0.9-focal   *:27170->27017/tcp
xj85wbnb5bnr   sharded_shard-1b         replicated   1/1        mongo:5.0.9-focal
r8xksxwsj3gi   sharded_shard-1c         replicated   1/1        mongo:5.0.9-focal
e1g6xph3ij7p   sharded_shard-2a         replicated   1/1        mongo:5.0.9-focal   *:27125->27017/tcp
kdfcev9omnxq   sharded_shard-2b         replicated   1/1        mongo:5.0.9-focal
qh228mxl7a18   sharded_shard-2c         replicated   1/1        mongo:5.0.9-focal
```

Full compose file can be found in this directory (docker-compose-2SH-PSA.yml).

Furthermore, we need to configure the different instances. We begin with config servers, then shards, then finally the query router.

All output is truncated.

Config Server:

```js
test> rs.initiate({
...     "_id": "configSet",
...     "version": 1,
...     "configsvr": true,
...     "members": [
...         { "_id": 0, "host" : "mongo-config-1:27017" },
...         { "_id": 1, "host" : "mongo-config-2:27017" },
...         { "_id": 2, "host" : "mongo-config-3:27017" }
...     ]
... });
{
  ok: 1,
  '$gleStats': {
  }
}
```

First shard:

```js
test> rs.initiate({
...     "_id": "rsSh1",
...     "members":[
...         { "_id": 0, "host" : "shard-1a:27017" },
...         { "_id": 1, "host" : "shard-1b:27017" },
...         { "_id": 2, "host" : "shard-1c:27017", "arbiterOnly": true },
...     ]
... });
{
  ok: 1,
  '$clusterTime': {
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  },
}

// Running rs.status().members to see if shard is operational:
rsSh1 [direct: primary] test> rs.status().members
[
  {
    _id: 0,
    electionDate: ISODate("2022-06-20T17:43:30.000Z"),
    configVersion: 1,
    configTerm: 1,
    self: true,
    lastHeartbeatMessage: ''
  },
  {
    _id: 1,
    name: 'shard-1b:27017',
    health: 1,
    state: 2,
    stateStr: 'SECONDARY',
  },
  {
    _id: 2,
    name: 'shard-1c:27017',
    health: 1,
    state: 7,
    stateStr: 'ARBITER',
  }
]
```

Second shard:

```js
test> rs.initiate({
...     "_id": "rsSh2",
...     "members":[
...         { "_id": 0, "host" : "shard-2a:27017" },
...         { "_id": 1, "host" : "shard-2b:27017" },
...         { "_id": 2, "host" : "shard-2c:27017", "arbiterOnly": true },
...     ]
... });
{ ok: 1 }

rsSh2 [direct: primary] test> rs.status().members
[
  {
    _id: 0,
    name: 'shard-2a:27017',
    health: 1,
    state: 1,
    electionDate: ISODate("2022-06-20T17:46:55.000Z"),
  },
  {
    _id: 1,
    name: 'shard-2b:27017',
    health: 1,
    state: 2,
    stateStr: 'SECONDARY',
  },
  {
    _id: 2,
    name: 'shard-2c:27017',
    health: 1,
    state: 7,
    stateStr: 'ARBITER',
  }
]
```

Query Router:

```js
mongos> sh.addShard(
...     "rsSh1/shard-1a:27017",
...     "rsSh1/shard-1b:27017",
...     "rsSh1/shard-1c:27017",
... );
{
	"shardAdded" : "rsSh1",
	"ok" : 1,
	"$clusterTime" : {
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
}
mongos> sh.addShard(
...     "rsSh2/shard-2a:27017",
...     "rsSh2/shard-2b:27017",
...     "rsSh2/shard-2c:27017",
... );
{
	"shardAdded" : "rsSh2",
	"ok" : 1,
	"$clusterTime" : {
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	}
}


// running sh.status() to see status of cluster
mongos> sh.status()
--- Sharding Status ---
  sharding version: {
  	"_id" : 1,
  	"minCompatibleVersion" : 5,
  	"currentVersion" : 6,
  	"clusterId" : ObjectId("62b89a5f9b3e5d291afdd7ea")
  }
  shards:
        {  "_id" : "rsSh1",  "host" : "rsSh1/shard-1a:27017,shard-1b:27017",  "state" : 1 }
        {  "_id" : "rsSh2",  "host" : "rsSh2/shard-2a:27017,shard-2b:27017",  "state" : 1 }
  active mongoses:
        "5.0.9" : 1
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled: yes
        Currently running: no
        Failed balancer rounds in last 5 attempts: 0
        Migration results for the last 24 hours:
                No recent migrations
  databases:
        {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
```

Everything is in order.

## Upgrade

Like the PSA configuration. We can update the docker compose file to add instances on different hosts. Further configuration is needed, this can be done by adding new shards.

## Cleanup

Clean up is very easy, just remove the stack.

```shell
$ docker stack rm sharded
Removing service sharded_mongo-config-1
Removing service sharded_mongo-config-2
Removing service sharded_mongo-config-3
Removing service sharded_mongo-router
Removing service sharded_shard-1a
Removing service sharded_shard-1b
Removing service sharded_shard-1c
Removing service sharded_shard-2a
Removing service sharded_shard-2b
Removing service sharded_shard-2c
Removing network sharded_sharded-cluster
```

## Setup for YCSB

Now that we configured the cluster, we can further configure it to shard on \_id field of usertables.

First we need to enable sharding of the database, we will make a generic ycsb database.

```js
mongos> sh.enableSharding("ycsb")
{
	"ok" : 1,
	"$clusterTime" : {
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
}
```

Then we can elaborate on the type of sharding and on which field:

```js
mongos> sh.shardCollection("ycsb.usertable", {"_id": "hashed"})
{
	"collectionsharded" : "ycsb.usertable",
	"ok" : 1,
	"$clusterTime" : {
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
}
```

Now the cluster is operational and will shard inserts appropriately.
