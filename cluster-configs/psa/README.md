# Setup

This section contains information on how to setup Primary-Secondary-Arbiter (PSA) member set replica in MongoDB for multihost environment. It is assumed that Docker Swarm is [setup as stated earlier](https://github.com/Asim-A/scaling-wiz)

## Preliminary

Remember to add labels to nodes so it is possible to assign services to a host explicitly with docker compose.

## Native

In this edition, host one machine will host both the initial primary and arbiter node instance(s). Host two will host the initial secondary node instance of mongodb. Step 0 will be the setup of . Steps 1-x will have to be redone on each machine, twice on host one, once on host two.

The services will be started from the CLI, however in a production environment it would be more convenient to make a new systemctl service. This will not be covered.

0. Insert DNS hostnames in /etc/hosts, this has to be set on all hosts and needs further updating if new hosts are intended to be used for the cluster.

   ```txt
       192.168.0.101 mongo-primary
       192.168.0.102 mongo-secondary
       192.168.0.101 mongo-arbiter
   ```

   Repeat steps below per instance. Replace [placeholder] with name of instance or instance type, e.g. primary, secondary, arbiter.

1. Create log and data directories
   ```shell
    sudo mkdir /var/log/mongodb-[placeholder]
    sudo mkdir /var/lib/mongodb-[placeholder]
   ```
2. Copy the original conf file or download an example from the [offical mongodb repository](https://github.com/mongodb/mongo/blob/master/rpm/mongod.conf)
   ```shell
   sudo cp /etc/mongod.conf /etc/mongod-[placeholder].conf
   ```
3. Change owner of files and folders:
   ```shell
   sudo chown mongodb:mongodb /var/log/mongodb-[placeholder]
   sudo chown mongodb:mongodb /var/lib/mongodb-[placeholder]
   sudo chown mongodb:mongodb /etc/mongod-[placeholder].conf
   ```
4. Change access of files and folders:
   ```shell
   sudo chmod 777 /var/log/mongodb-[placeholder]
   sudo chmod 777 /var/lib/mongodb-[placeholder]
   sudo chmod 777 /etc/mongod-[placeholder].conf
   ```
5. Edit the conf file. Replace [placeholder] accordingly.

   - Specifically add a port that is available, one port per host machine. So Host One will have 27710 (primary), 27711 (arbiter) and Host Two (27017).
   - Edit bind ip, this configuration is about which IPs the instance will allow connection to. 0.0.0.0 means it accepts all connections. In this case we will allow local network (192.168.x.x) connect.
   - Add replication set details
     Example below is of setting up primary node.

   ```yaml
   # where to write logging data.
   systemLog:
   destination: file
   logAppend: true
   path: /var/log/mongodb-[placeholder]/mongod.log

   # Where and how to store data.
   storage:
   dbPath: /var/lib/mongodb-[placeholder]

   net:
   port: 27710 # Primary, change accordingly
   bindIp: 192.168.0.0
   replication:
     replSetName: ycsb # Important to note that the replSetName should be same across all instances.
   ```

6. Run Instance with respective conf file.
   ```shell
    mongod -f /etc/mongod-[placeholder].conf
   ```

When all the instances are running, connect to primary instance and initiate the cluster. You can initiate remotely or using scripts, all in all an rs.initiate() call has to be made from either nodes in the PSA configuration.

The rs.initiate() method provided by MongoDB API requires that the \_id property is equal to the replSetName in the conf file. We have to also add the hosts with respective ports. Additionally we have to set that the arbiter is arbiterOnly.

```js
rs.initiate({
  _id: "ycsb",
  members: [
    { _id: 0, host: "mongo-primary:27710" },
    { _id: 1, host: "mongo-secondary:27017" },
    { _id: 2, host: "mongo-arbiter:27711", arbiterOnly: true },
  ],
});
```

After about 10 secs we can check the status of the replica set with `rs.status()`. Example of this is [below](Config validation)

## Docker

We will do the exact same PSA configuration, but now hosted in containerized environment. We can easily configure the Docker Compose file to configure each instance omitting the use of conf files. Additionally since each instance is in itself isolated we can omit to create folders for logs and data and rather just point them to the default location, i.e. `/var/log/mongodb & /var/lib/mongodb`

We also have to add all instances to same overlay network and assign them their own volumes. This is done in a declarative way and is intuitive from the compose file.

Hostnames are given to each container, the resolving of hosts will be handled by Docker Swarm allowing for more versatility when new host machines are added and the cluster needs reconfiguration.

Once again it is important that the replSet name is same across all replicas. We have used `ycsbSet`as replSetName for this configuration.

Execute [docker-compose-PSA.yml](https://github.com/Asim-A/scaling-wiz/tree/master/cluster-configs/psa) by:

```shell
docker stack deploy -c /path/to/file/docker-compose-PSA.yml
```

```shell
docker stack deploy -c cluster-configs/psa/docker-compose-PSA.yml replica
$ docker stack deploy -c "cluster-configs/psa/docker-compose-PSA.yml" replica
Creating network replica_mongo-cluster
Creating service replica_mongo1
Creating service replica_mongo2
Creating service replica_mongo3
```

Below is output of the services running.

```shell
$ docker service ls
ID             NAME             MODE         REPLICAS   IMAGE               PORTS
trp8d3bj90ba   replica_mongo1   replicated   1/1        mongo:5.0.9-focal   *:27017->27017/tcp
waqz3b0ckndm   replica_mongo2   replicated   1/1        mongo:5.0.9-focal
pgg3r8mf37cq   replica_mongo3   replicated   1/1        mongo:5.0.9-focal


```

Full compose file can be found in this directory (docker-compose-PSA.yml).

We can now run initiate using the hostnames set in the compose:

```js
rs.initiate({
  _id: "ycsbSet",
  members: [
    { _id: 0, host: "mongo1" },
    { _id: 1, host: "mongo2" },
    { _id: 2, host: "mongo3", arbiterOnly: true },
  ],
});

// Res
{
  ok: 1;
}
```

### Config validation

Output rs.status(), truncated.

```js
ycsbSet [direct: other] test> rs.status()
{
  set: 'ycsbSet',
  date: ISODate("2022-06-20T16:31:00.313Z"),
  myState: 1,
  term: Long("1"),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long("2000"),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 2,
  optimes: {
    ...
  },
  electionCandidateMetrics: {
    ...
  },
  members: [
    {
      _id: 0,
      name: 'mongo1:27017',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      electionDate: ISODate("2022-06-20:30:14.000Z"),
      configVersion: 1,
      configTerm: 1,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongo2:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 56,
      pingMs: Long("0"),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongo1:27017',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    },
    {
      _id: 2,
      name: 'mongo3:27017',
      health: 1,
      state: 7,
      stateStr: 'ARBITER',
      uptime: 56,
      lastHeartbeat: ISODate("2022-06-20T16:30:58.471Z"),
      lastHeartbeatRecv: ISODate("2022-06-20T16:30:58.471Z"),
      pingMs: Long("0"),
      lastHeartbeatMessage: '',
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    }
  ],
  ok: 1,
  '$clusterTime': {
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  }
}

```

Furthermore we can check the replication status of the replica set with `rs.printSecondaryReplicationInfo()`

```js
ycsbSet [direct: primary] test> rs.printSecondaryReplicationInfo()
source: mongo2:27017
{
  syncedTo: 'Sun Jun 20 2022 18:36:44 GMT+0200 (Central European Summer Time)',
  replLag: '0 secs (0 hrs) behind the primary '
}
```

### Updating the docker-compose and replica member set with a new instance/node.

If more replica member sets are to be added, they can easily be added to the compose file. After they have been added to the compose file we can rerun the initial stack command to update the stack.

```shell
docker stack deploy -c cluster-configs/docker-compose-PSA.yml replica
```

The previous instances will be unaffected and then we can connect to the replica member set and call `rs.add()` like:

```js
rs.add({ host: mongo4 });

{
  ok: 1;
}
```
