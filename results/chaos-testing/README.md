# Results

This section contains all the chaos testing done against the 2SH-PSA cluster configuration.

The chaos tool is a simply node.js application that retreives all primary nodes using Docker API and mongo driver for node.js. It runs for several minutes and randomly shuts down containers of primary nodes.

There were three tests conducted.

- Workload b running uninterrupted against 2SH-PSA cluster.
- Workload b running with random interrupts.
- Workload c running with random interrupts.

Before any of the tests we check if the cluster configuration is setup correctly with `sh.status` like:

```js
mongos> sh.status()
--- Sharding Status ---
  sharding version: {
        "_id" : 1,
        "minCompatibleVersion" : 5,
        "currentVersion" : 6,
        "clusterId" : ObjectId("62a68f55cc5b89d51fb82eb5")
  }
  shards:
        {  "_id" : "rsSh1",  "host" : "rsSh1/shard-1a:27017,shard-1b:27017",  "state" : 1,  "topologyTime" : Timestamp(1655083767, 1) }
        {  "_id" : "rsSh2",  "host" : "rsSh2/shard-2a:27017,shard-2b:27017",  "state" : 1,  "topologyTime" : Timestamp(1655083774, 3) }
  active mongoses:
        "5.0.9" : 1
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled: yes
        Currently running: no
        Failed balancer rounds in last 5 attempts: 0
        Migration results for the last 24 hours:
                517 : Success
                17 : Failed with error 'aborted', from rsSh2 to rsSh1
                2 : Failed with error 'aborted', from rsSh1 to rsSh2
  databases:
        {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
                config.system.sessions
                        shard key: { "_id" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                rsSh1   512
                                rsSh2   512
                        too many chunks to print, use verbose if you want to force print
        {  "_id" : "ycsb_c",  "primary" : "rsSh1",  "partitioned" : true,  "version" : {  "uuid" : UUID("c2f2af6b-78eb-45f8-9753-4b48124cca03"),  "timestamp" : Timestamp(1655083792, 1),  "lastMod" : 1 } }
                ycsb_c.usertable
                        shard key: { "_id" : "hashed" }
                        unique: false
                        balancing: true
                        chunks:
                                rsSh1   32
                                rsSh2   32
                        too many chunks to print, use verbose if you want to force print
```

After every test we run `db.collection.getShardDistribution()` to see if the solution is sharding properly. E.g. Below.

```js
Shard rsSh1 at rsSh1/shard-1a:27017,shard-1b:27017
{ data: '2.22GiB',
  docs: 2044050,
  chunks: 32,
  'estimated data per chunk': '71.14MiB',
  'estimated docs per chunk': 63876 }

Shard rsSh2 at rsSh2/shard-2a:27017,shard-2b:27017
{ data: '2.22GiB',
  docs: 2044163,
  chunks: 32,
  'estimated data per chunk': '71.14MiB',
  'estimated docs per chunk': 63880 }

Totals
{ data: '22232570138.18GiB',
  docs: 4088213,
  chunks: 64,
  'Shard rsSh1':
   [ '0 % data',
     '49.99 % docs in cluster',
     '1KiB avg obj size on shard' ],
  'Shard rsSh2':
   [ '0 % data',
     '50 % docs in cluster',
     '1KiB avg obj size on shard' ] }
```

## Workload B uninterrupted

```shell
2022-06-17 23:48:56:139 10 sec: 106601 operations; 10644,13 current ops/sec; est completion in 2 minutes [READ: Count=101304, Max=314111, Min=474, Avg=1061,08, 90=1568, 99=3979, 99.9=14119, 99.99=72511
] [UPDATE: Count=5325, Max=72383, Min=590, Avg=1248,21, 90=1776, 99=4527, 99.9=14455, 99.99=72383]
2022-06-17 23:49:06:124 20 sec: 224952 operations; 11852,88 current ops/sec; est completion in 1 minute [READ: Count=112440, Max=17663, Min=487, Avg=1003, 90=1536, 99=3389, 99.9=7539, 99.99=15815] [UPD
ATE: Count=5895, Max=18079, Min=595, Avg=1152,79, 90=1719, 99=3587, 99.9=10911, 99.99=17439]
2022-06-17 23:49:16:126 30 sec: 343728 operations; 11875,22 current ops/sec; est completion in 1 minute [READ: Count=112740, Max=17791, Min=490, Avg=1001,62, 90=1529, 99=3389, 99.9=6587, 99.99=15471] [
UPDATE: Count=6027, Max=17775, Min=611, Avg=1142,16, 90=1725, 99=3545, 99.9=5879, 99.99=12879]
2022-06-17 23:49:26:131 40 sec: 462726 operations; 11893,85 current ops/sec; est completion in 1 minute [READ: Count=112967, Max=30511, Min=502, Avg=999,16, 90=1519, 99=3345, 99.9=6015, 99.99=20079] [U
PDATE: Count=6028, Max=28463, Min=609, Avg=1160,12, 90=1727, 99=3537, 99.9=7963, 99.99=28431]
2022-06-17 23:49:36:130 50 sec: 581487 operations; 11877,29 current ops/sec; est completion in 1 minute [READ: Count=112971, Max=20575, Min=498, Avg=1000,54, 90=1535, 99=3325, 99.9=5683, 99.99=14295] [
UPDATE: Count=5793, Max=20719, Min=593, Avg=1169,29, 90=1729, 99=3645, 99.9=7727, 99.99=18287]
2022-06-17 23:49:46:136 60 sec: 700391 operations; 11883,27 current ops/sec; est completion in 1 minute [READ: Count=112835, Max=15751, Min=487, Avg=1000,83, 90=1533, 99=3341, 99.9=7487, 99.99=14943] [
UPDATE: Count=6071, Max=14783, Min=597, Avg=1143,58, 90=1745, 99=3599, 99.9=5935, 99.99=14287]
2022-06-17 23:49:56:134 70 sec: 820478 operations; 12011,1 current ops/sec; est completion in 58 seconds [READ: Count=114010, Max=16415, Min=487, Avg=990,6, 90=1515, 99=3271, 99.9=4987, 99.99=8695] [UP
DATE: Count=6078, Max=15119, Min=607, Avg=1125,87, 90=1681, 99=3329, 99.9=5307, 99.99=8055]
2022-06-17 23:50:06:132 80 sec: 940175 operations; 11972,09 current ops/sec; est completion in 48 seconds [READ: Count=113781, Max=19407, Min=503, Avg=993,81, 90=1532, 99=3419, 99.9=5623, 99.99=11967]
[UPDATE: Count=5912, Max=12455, Min=587, Avg=1133,43, 90=1713, 99=3581, 99.9=5243, 99.99=6303]
2022-06-17 23:50:16:139 90 sec: 1059534 operations; 11927,55 current ops/sec; est completion in 38 seconds [READ: Count=113447, Max=16655, Min=489, Avg=996,79, 90=1538, 99=3333, 99.9=5823, 99.99=14207]
[UPDATE: Count=5915, Max=15111, Min=602, Avg=1151,26, 90=1720, 99=3631, 99.9=8035, 99.99=12823]
2022-06-17 23:50:26:138 100 sec: 1178762 operations; 11923,99 current ops/sec; est completion in 28 seconds [READ: Count=113232, Max=15463, Min=490, Avg=997,22, 90=1532, 99=3363, 99.9=5667, 99.99=14247
] [UPDATE: Count=5999, Max=7807, Min=564, Avg=1146,48, 90=1758, 99=3563, 99.9=5167, 99.99=6963]
2022-06-17 23:50:36:135 110 sec: 1296957 operations; 11823,05 current ops/sec; est completion in 18 seconds [READ: Count=112319, Max=17679, Min=484, Avg=1005,24, 90=1558, 99=3375, 99.9=6015, 99.99=1385
5] [UPDATE: Count=5875, Max=15495, Min=601, Avg=1167,72, 90=1744, 99=3757, 99.9=9783, 99.99=13111]
2022-06-17 23:50:46:134 120 sec: 1415647 operations; 11870,19 current ops/sec; est completion in 8 second [READ: Count=112676, Max=21087, Min=498, Avg=1002,06, 90=1539, 99=3375, 99.9=5995, 99.99=15375]
[UPDATE: Count=6015, Max=19647, Min=567, Avg=1146,86, 90=1743, 99=3489, 99.9=5543, 99.99=19439]
2022-06-17 23:50:53:696 127 sec: 1500000 operations; 11154,85 current ops/sec; [READ: Count=80181, Max=12735, Min=472, Avg=974,11, 90=1476, 99=3275, 99.9=5291, 99.99=9343] [CLEANUP: Count=12, Max=2631,
Min=1, Avg=220,42, 90=4, 99=2631, 99.9=2631, 99.99=2631] [UPDATE: Count=4164, Max=13079, Min=593, Avg=1122,27, 90=1686, 99=3615, 99.9=5599, 99.99=13079]
[OVERALL], RunTime(ms), 127572
[OVERALL], Throughput(ops/sec), 11758.066033298843
[TOTAL_GCS_G1_Young_Generation], Count, 148
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 117
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.09171291505973098
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 148
[TOTAL_GC_TIME], Time(ms), 117
[TOTAL_GC_TIME_%], Time(%), 0.09171291505973098
[READ], Operations, 1424903
[READ], AverageLatency(us), 1002.1452260259119
[READ], MinLatency(us), 472
[READ], MaxLatency(us), 314111
[READ], 95thPercentileLatency(us), 2083
[READ], 99thPercentileLatency(us), 3379
[READ], Return=OK, 1424903
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 220.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2631
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2631
[UPDATE], Operations, 75097
[UPDATE], AverageLatency(us), 1154.491950410802
[UPDATE], MinLatency(us), 564
[UPDATE], MaxLatency(us), 72383
[UPDATE], 95thPercentileLatency(us), 2297
[UPDATE], 99thPercentileLatency(us), 3613
[UPDATE], Return=OK, 75097
```

# Workload B interrupted

```shell
2022-06-18 00:18:00:295 10 sec: 74545 operations; 7453,01 current ops/sec; est completion in 58 seconds [READ: Count=70818, Max=316671, Min=457, Avg=1511,13, 90=2753, 99=7463, 99.9=15911, 99.99=211071]
[UPDATE: Count=3739, Max=16087, Min=580, Avg=1842,66, 90=3547, 99=8439, 99.9=15055, 99.99=16087]
2022-06-18 00:18:10:299 20 sec: 130737 operations; 5616,95 current ops/sec; est completion in 57 seconds [READ: Count=53354, Max=24447, Min=463, Avg=1442,47, 90=2793, 99=6983, 99.9=14095, 99.99=19007]
[UPDATE: Count=2826, Max=46431, Min=567, Avg=1899,28, 90=3589, 99=9751, 99.9=44575, 99.99=46431]
2022-06-18 00:18:20:296 30 sec: 148160 operations; 1742,82 current ops/sec; est completion in 1 minute [READ: Count=16569, Max=11649023, Min=488, Avg=8748,63, 90=1578, 99=3639, 99.9=15247, 99.99=116490
23] [UPDATE: Count=866, Max=11649023, Min=623, Avg=14572,58, 90=1657, 99=3867, 99.9=13663, 99.99=11649023]
2022-06-18 00:18:30:298 40 sec: 223720 operations; 7554,49 current ops/sec; est completion in 50 seconds [READ: Count=71770, Max=15679, Min=476, Avg=988,13, 90=1496, 99=3285, 99.9=7755, 99.99=15079] [U
PDATE: Count=3778, Max=737791, Min=584, Avg=7713,35, 90=1710, 99=14223, 99.9=724991, 99.99=737791]
2022-06-18 00:18:40:302 50 sec: 227516 operations; 379,45 current ops/sec; est completion in 1 minute [READ: Count=3588, Max=11051007, Min=506, Avg=38760,42, 90=1649, 99=15199, 99.9=11042815, 99.99=110
51007] [UPDATE: Count=209, Max=15631, Min=556, Avg=1203,54, 90=1798, 99=2909, 99.9=15631, 99.99=15631]
2022-06-18 00:18:50:298 60 sec: 283753 operations; 5625,95 current ops/sec; est completion in 46 seconds [READ: Count=53334, Max=23263, Min=458, Avg=1257,09, 90=2145, 99=5995, 99.9=14567, 99.99=19535]
[UPDATE: Count=2906, Max=774655, Min=510, Avg=18356,62, 90=3105, 99=668671, 99.9=763391, 99.99=774655]
2022-06-18 00:19:00:296 70 sec: 370833 operations; 8709,74 current ops/sec; est completion in 25 seconds [READ: Count=82646, Max=18895, Min=441, Avg=1356,56, 90=2565, 99=6543, 99.9=12487, 99.99=15839]
[UPDATE: Count=4435, Max=22383, Min=548, Avg=1749,08, 90=3545, 99=8663, 99.9=13431, 99.99=22383]
2022-06-18 00:19:10:295 80 sec: 457190 operations; 8636,56 current ops/sec; est completion in 8 second [READ: Count=82054, Max=21215, Min=465, Avg=1370,32, 90=2589, 99=6747, 99.9=12959, 99.99=16495] [U
PDATE: Count=4301, Max=18591, Min=558, Avg=1727,19, 90=3429, 99=8439, 99.9=14039, 99.99=18591]
2022-06-18 00:19:15:667 85 sec: 500000 operations; 7969,1 current ops/sec; [READ: Count=40634, Max=18031, Min=455, Avg=1350,1, 90=2533, 99=6627, 99.9=12311, 99.99=15903] [CLEANUP: Count=12, Max=2883, M
in=0, Avg=241,33, 90=4, 99=2883, 99.9=2883, 99.99=2883] [UPDATE: Count=2173, Max=15487, Min=551, Avg=1668,05, 90=3341, 99=7707, 99.9=12183, 99.99=15487]
[OVERALL], RunTime(ms), 85374
[OVERALL], Throughput(ops/sec), 5856.583971700987
[TOTAL_GCS_G1_Young_Generation], Count, 51
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 58
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.06793637407173145
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 51
[TOTAL_GC_TIME], Time(ms), 58
[TOTAL_GC_TIME_%], Time(%), 0.06793637407173145
[READ], Operations, 474767
[READ], AverageLatency(us), 1864.8785867594
[READ], MinLatency(us), 441
[READ], MaxLatency(us), 11649023
[READ], 95thPercentileLatency(us), 3347
[READ], 99thPercentileLatency(us), 6363
[READ], Return=OK, 474767
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 241.33333333333334
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 2883
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2883
[UPDATE], Operations, 25233
[UPDATE], AverageLatency(us), 5010.275987793762
[UPDATE], MinLatency(us), 510
[UPDATE], MaxLatency(us), 11649023
[UPDATE], 95thPercentileLatency(us), 4591
[UPDATE], 99thPercentileLatency(us), 10015
[UPDATE], Return=OK, 25233
```

## Workload C interrupted

```shell
2022-06-13 18:22:58:858 10 sec: 99746 operations; 9962,64 current ops/sec; est completion in 4 minutes [READ: Count=99762, Max=662527, Min=475, Avg=1139,97, 90=1493, 99=3207, 99.9=15351, 99.99=210431]
2022-06-13 18:23:08:857 20 sec: 216088 operations; 11635,36 current ops/sec; est completion in 4 minutes [READ: Count=116333, Max=14335, Min=456, Avg=1029,6, 90=1469, 99=2985, 99.9=5183, 99.99=13471]
2022-06-13 18:23:18:850 30 sec: 333382 operations; 11737,62 current ops/sec; est completion in 4 minutes [READ: Count=117296, Max=14759, Min=475, Avg=1020,64, 90=1452, 99=2849, 99.9=5627, 99.99=14063]
2022-06-13 18:23:28:850 40 sec: 351479 operations; 1809,7 current ops/sec; est completion in 5 minutes [READ: Count=18088, Max=14103, Min=467, Avg=1036,95, 90=1470, 99=2819, 99.9=7743, 99.99=13855]
2022-06-13 18:23:38:848 50 sec: 413828 operations; 6236,15 current ops/sec; est completion in 5 minutes [READ: Count=62354, Max=10862591, Min=750, Avg=3545,81, 90=2213, 99=4983, 99.9=13655, 99.99=10862591]
2022-06-13 18:23:48:851 60 sec: 478657 operations; 6480,96 current ops/sec; est completion in 5 minutes [READ: Count=64824, Max=22063, Min=769, Avg=1408,13, 90=2149, 99=4659, 99.9=10743, 99.99=16199]
2022-06-13 18:23:58:855 70 sec: 499103 operations; 2043,78 current ops/sec; est completion in 5 minutes [READ: Count=20447, Max=10551295, Min=493, Avg=7270,58, 90=1541, 99=3371, 99.9=11231, 99.99=10551295]
2022-06-13 18:24:08:848 80 sec: 608743 operations; 10971,68 current ops/sec; est completion in 5 minutes [READ: Count=109644, Max=36191, Min=471, Avg=1092,06, 90=1564, 99=3403, 99.9=9727, 99.99=17327]
2022-06-13 18:24:18:847 90 sec: 724441 operations; 11570,96 current ops/sec; est completion in 4 minutes [READ: Count=115693, Max=21631, Min=460, Avg=1035,57, 90=1450, 99=2939, 99.9=8495, 99.99=14959]
2022-06-13 18:24:28:852 100 sec: 840696 operations; 11619,69 current ops/sec; est completion in 4 minutes [READ: Count=116266, Max=15943, Min=465, Avg=1031,01, 90=1448, 99=2885, 99.9=6935, 99.99=14919]
2022-06-13 18:24:38:848 110 sec: 851558 operations; 1086,63 current ops/sec; est completion in 4 minutes [READ: Count=10851, Max=8975, Min=505, Avg=1058,59, 90=1497, 99=3235, 99.9=7787, 99.99=8639]
2022-06-13 18:24:48:851 120 sec: 954274 operations; 10268,52 current ops/sec; est completion in 4 minutes [READ: Count=102723, Max=10625023, Min=516, Avg=2222,82, 90=1465, 99=3061, 99.9=6107, 99.99=10625023]
2022-06-13 18:24:58:855 130 sec: 1076873 operations; 12255 current ops/sec; est completion in 3 minutes [READ: Count=122602, Max=15255, Min=520, Avg=977,58, 90=1452, 99=3075, 99.9=6175, 99.99=13895]
2022-06-13 18:25:08:852 140 sec: 1200986 operations; 12415,02 current ops/sec; est completion in 3 minutes [READ: Count=124113, Max=13807, Min=512, Avg=965,01, 90=1432, 99=2939, 99.9=4447, 99.99=13415]
2022-06-13 18:25:18:850 150 sec: 1324559 operations; 12359,77 current ops/sec; est completion in 3 minutes [READ: Count=123569, Max=16655, Min=516, Avg=969,34, 90=1452, 99=2985, 99.9=4595, 99.99=9383]
2022-06-13 18:25:28:859 160 sec: 1447705 operations; 12303,53 current ops/sec; est completion in 2 minutes [READ: Count=123145, Max=17071, Min=515, Avg=973,79, 90=1442, 99=3015, 99.9=4711, 99.99=13791]
2022-06-13 18:25:38:853 170 sec: 1452795 operations; 509,31 current ops/sec; est completion in 3 minutes [READ: Count=5085, Max=5707, Min=527, Avg=996,97, 90=1506, 99=3231, 99.9=4435, 99.99=5395]
2022-06-13 18:25:48:855 180 sec: 1550388 operations; 9757,35 current ops/sec; est completion in 2 minutes [READ: Count=97598, Max=11059199, Min=473, Avg=2405,01, 90=1496, 99=3031, 99.9=7307, 99.99=11059199]
2022-06-13 18:25:58:853 190 sec: 1667087 operations; 11672,23 current ops/sec; est completion in 2 minutes [READ: Count=116700, Max=22239, Min=449, Avg=1026,42, 90=1464, 99=2923, 99.9=6623, 99.99=13799]
2022-06-13 18:26:08:857 200 sec: 1783499 operations; 11636,55 current ops/sec; est completion in 2 minutes [READ: Count=116411, Max=16447, Min=473, Avg=1029,6, 90=1457, 99=2975, 99.9=8007, 99.99=15015]
2022-06-13 18:26:18:853 210 sec: 1902156 operations; 11870,45 current ops/sec; est completion in 2 minutes [READ: Count=118656, Max=14599, Min=472, Avg=1009,38, 90=1426, 99=2879, 99.9=4667, 99.99=13559]
2022-06-13 18:26:28:858 220 sec: 1954263 operations; 5208,1 current ops/sec; est completion in 1 minute [READ: Count=52103, Max=16895, Min=465, Avg=1031,47, 90=1463, 99=2967, 99.9=8663, 99.99=14495]
2022-06-13 18:26:38:857 230 sec: 1986189 operations; 3192,92 current ops/sec; est completion in 1 minute [READ: Count=31930, Max=11624447, Min=769, Avg=5830,51, 90=2075, 99=4503, 99.9=41503, 99.99=11616255]
2022-06-13 18:26:48:861 240 sec: 2070737 operations; 8451,42 current ops/sec; est completion in 1 minute [READ: Count=84549, Max=28159, Min=765, Avg=1418,29, 90=2177, 99=4827, 99.9=11231, 99.99=17935]
2022-06-13 18:26:58:852 250 sec: 2156282 operations; 8562,21 current ops/sec; est completion in 1 minute [READ: Count=85544, Max=23023, Min=753, Avg=1399,95, 90=2137, 99=4363, 99.9=9631, 99.99=15983]
2022-06-13 18:27:08:847 260 sec: 2241967 operations; 8572,79 current ops/sec; est completion in 1 minute [READ: Count=85685, Max=16207, Min=767, Avg=1398,22, 90=2153, 99=4339, 99.9=8043, 99.99=13951]
2022-06-13 18:27:18:855 270 sec: 2281851 operations; 3985,21 current ops/sec; est completion in 1 minute [READ: Count=39880, Max=21215, Min=774, Avg=1396,88, 90=2161, 99=4379, 99.9=7687, 99.99=15287]
2022-06-13 18:27:28:853 280 sec: 2339008 operations; 5716,84 current ops/sec; est completion in 1 minute [READ: Count=57157, Max=10280959, Min=493, Avg=3222,62, 90=1497, 99=3235, 99.9=9215, 99.99=10280959]
2022-06-13 18:27:38:853 290 sec: 2392175 operations; 5316,7 current ops/sec; est completion in 1 minute [READ: Count=53167, Max=31327, Min=473, Avg=1088,67, 90=1515, 99=3611, 99.9=13487, 99.99=26591]
2022-06-13 18:27:48:853 300 sec: 2444059 operations; 5188,4 current ops/sec; est completion in 1 minute [READ: Count=51890, Max=10821631, Min=520, Avg=3506,66, 90=1502, 99=3087, 99.9=9191, 99.99=10813439]
2022-06-13 18:27:58:851 310 sec: 2564071 operations; 12003,6 current ops/sec; est completion in 53 seconds [READ: Count=120015, Max=15759, Min=528, Avg=998,21, 90=1497, 99=3113, 99.9=5107, 99.99=13479]
2022-06-13 18:28:08:849 320 sec: 2683560 operations; 11951,29 current ops/sec; est completion in 38 seconds [READ: Count=119480, Max=14535, Min=502, Avg=1002,43, 90=1491, 99=3039, 99.9=8863, 99.99=13375]
2022-06-13 18:28:18:854 330 sec: 2781333 operations; 9772,41 current ops/sec; est completion in 26 seconds [READ: Count=97776, Max=28367, Min=523, Avg=1225,86, 90=1827, 99=7111, 99.9=16479, 99.99=24383]
2022-06-13 18:28:28:859 340 sec: 2899551 operations; 11815,89 current ops/sec; est completion in 12 seconds [READ: Count=118215, Max=22271, Min=512, Avg=1013,94, 90=1544, 99=3171, 99.9=8007, 99.99=17791]
2022-06-13 18:28:37:691 348 sec: 3000000 operations; 11373,3 current ops/sec; [READ: Count=100449, Max=17711, Min=517, Avg=996,48, 90=1508, 99=2977, 99.9=7627, 99.99=14175] [CLEANUP: Count=12, Max=2701, Min=1, Avg=226,42, 90=5, 99=2701, 99.9=2701, 99.99=2701]
[OVERALL], RunTime(ms), 348845
[OVERALL], Throughput(ops/sec), 8599.807937622727
[TOTAL_GCS_G1_Young_Generation], Count, 304
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 209
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.059911995298771656
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 304
[TOTAL_GC_TIME], Time(ms), 209
[TOTAL_GC_TIME_%], Time(%), 0.059911995298771656
[READ], Operations, 3000000
[READ], AverageLatency(us), 1389.7664433333334
[READ], MinLatency(us), 449
[READ], MaxLatency(us), 11624447
[READ], 95thPercentileLatency(us), 2021
[READ], 99thPercentileLatency(us), 3351
[READ], Return=OK, 3000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 226.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2701
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2701
```
