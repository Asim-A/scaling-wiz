docker run -dit --network mongo-cluster -p 27017:27017 --hostname mongodb-primary --name mongodb-primary -e MONGODB_REPLICA_SET_MODE=primary -e MONGODB_ADVERTISED_HOSTNAME=mongodb-primary -e MONGODB_ROOT_PASSWORD=password123 -e MONGODB_REPLICA_SET_KEY=replicasetkey123  bitnami/mongodb:5.0.8

docker run -dit --network mongo-cluster --hostname mongodb-secondary-1 -p 27018:27017 --name mongodb-secondary -e MONGODB_REPLICA_SET_MODE=secondary -e MONGODB_ADVERTISED_HOSTNAME=mongodb-secondary -e MONGODB_INITIAL_PRIMARY_HOST=mongo-primary -e MONGODB_INITIAL_PRIMARY_PORT_NUMBER=27017 -e MONGODB_INITIAL_PRIMARY_ROOT_PASSWORD=password123 -e MONGODB_REPLICA_SET_KEY=replicasetkey123 bitnami/mongodb:5.0.8

docker run -dit --network mongo-cluster --hostname mongodb-secondary-2 -p 27017:27017 --name mongodb-secondary -e MONGODB_REPLICA_SET_MODE=secondary -e MONGODB_ADVERTISED_HOSTNAME=mongodb-secondary -e MONGODB_INITIAL_PRIMARY_HOST=mongodb-primary -e MONGODB_INITIAL_PRIMARY_PORT_NUMBER=27017 -e MONGODB_INITIAL_PRIMARY_ROOT_PASSWORD=password123 -e MONGODB_REPLICA_SET_KEY=replicasetkey123 bitnami/mongodb:5.0.8


docker run -d -p 27017:27017 --name mongo1 --hostname mongo1 --network mongo-cluster mongo:focal mongod --replSet myReplicaSet --bind_ip 0.0.0.0

docker run -d -p 27018:27017 --name mongo2 --hostname mongo2 --network mongo-cluster mongo:focal mongod --replSet myReplicaSet --bind_ip 0.0.0.0

docker run -d -p 27017:27017 --name mongo3 --hostname mongo3 --network mongo-cluster mongo:focal mongod --replSet myReplicaSet --bind_ip 0.0.0.0


rs.initiate({"_id": "myReplicaSet", "members": [{"_id": 0, "host": "192.168.0.102:27017"}, {"_id": 1, "host": "192.168.0.102:27017"}, {"_id": 2, "host": "192.168.0.109"}]})

rs.initiate({"_id": "ycsbSet", "members": [{"_id": 0, "host": "mongo1"}, {"_id": 1, "host": "mongo2"}, {"_id": 2, "host": "mongo3", arbiterOnly: true}]})

rs.initiate({"_id": "ycsbSet", "members": [{"_id": 0, "host": "mongo-primary:27014"}, {"_id": 1, "host": "mongo-secondary:27016"}, {"_id": 2, "host": "mongo-primary:27015", arbiterOnly: true}]})

// Config
rs.initiate({
    "_id": "configSet",
    "version": 1,
    "configsvr": true,
    "members": [ 
        { "_id": 0, "host" : "mongo-config-1:27017" },
        { "_id": 1, "host" : "mongo-config-2:27017" },
        { "_id": 2, "host" : "mongo-config-3:27017" }
    ]
});

// shard1
rs.initiate({
    "_id": "rsSh1",
    "members":[
        { "_id": 0, "host" : "shard-1a:27017" },
        { "_id": 1, "host" : "shard-1b:27017" },
        { "_id": 2, "host" : "shard-1c:27017", "arbiterOnly": true }, 
    ]
});

// shard2
rs.initiate({
    "_id": "rsSh2",
    "members":[
        { "_id": 0, "host" : "shard-2a:27017" },
        { "_id": 1, "host" : "shard-2b:27017" },
        { "_id": 2, "host" : "shard-2c:27017", "arbiterOnly": true }, 
    ]
});

// router 
sh.addShard(
    "rsSh1/shard-1a:27017",
    "rsSh1/shard-1b:27017",
    "rsSh1/shard-1c:27017",
);
sh.addShard(
    "rsSh2/shard-2a:27017",
    "rsSh2/shard-2b:27017",
    "rsSh2/shard-2c:27017",
);




docker exec -it mongo1 mongosh --eval "rs.initiate({
 _id: \"myReplicaSet\",
 members: [
   {_id: 0, host: \"mongo1\"},
   {_id: 1, host: \"mongo2\"},
 ]
})"