# YCSB Results

This section contains all YCSB Workload test results for the PSA configuration.

YCSB Parameters:

- w=1
- 5000000 records
- 5000000 operations
- threads, t=12

Before starting benchmarks, we first check if the configuration is correct. This is an example of checking if the native member set replica is setup correctly:

```js
test> rs.status().members
"members" : [
                {
                        "_id" : 0,
                        "name" : "mongo-primary:27014",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "PRIMARY",
                        "uptime" : 129,
                        "optime" : {
                                "ts" : Timestamp(1655149771, 1),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("2022-06-13T19:49:31Z"),
                        "lastAppliedWallTime" : ISODate("2022-06-13T19:49:31.993Z"),
                        "lastDurableWallTime" : ISODate("2022-06-13T19:49:31.993Z"),
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "configTerm" : 0,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "mongo-secondary:27016",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 5,
                        "optime" : {
                                "ts" : Timestamp(1655149771, 1),
                                "t" : NumberLong(-1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1655149771, 1),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("2022-06-13T19:49:31Z"),
                        "optimeDurableDate" : ISODate("2022-06-13T19:49:31Z"),
                        "lastAppliedWallTime" : ISODate("2022-06-13T19:49:31.993Z"),
                        "lastDurableWallTime" : ISODate("2022-06-13T19:49:31.993Z"),
                        "lastHeartbeat" : ISODate("2022-06-13T19:49:37.116Z"),
                        "lastHeartbeatRecv" : ISODate("2022-06-13T19:49:36.867Z"),
                        "pingMs" : NumberLong(1),
                        "lastHeartbeatMessage" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "configTerm" : 0
                },
                {
                        "_id" : 2,
                        "name" : "mongo-primary:27015",
                        "health" : 1,
                        "state" : 7,
                        "stateStr" : "ARBITER",
                        "uptime" : 5,
                        "lastHeartbeat" : ISODate("2022-06-13T19:49:37.113Z"),
                        "lastHeartbeatRecv" : ISODate("2022-06-13T19:49:36.429Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "configTerm" : 0
                }

```

After each benchmark, we also check if the data has been replicated. We use the `rs.printSecondaryReplicationInfo()`

```js
test> rs.printSecondaryReplicationInfo()
source: mongo2:27017
{ syncedTo: 'Sun Jun 12 2022 20:30:15 GMT+0200 (sentraleuropeisk sommertid)',
  replLag: '0 secs (0 hrs) behind the primary ' }
```

## Normal / Native

### Workload A Load

```shell
[OVERALL], RunTime(ms), 329458
[OVERALL], Throughput(ops/sec), 15176.441306630892
[TOTAL_GCS_G1_Young_Generation], Count, 337
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 244
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07406103357635875
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 337
[TOTAL_GC_TIME], Time(ms), 244
[TOTAL_GC_TIME_%], Time(%), 0.07406103357635875
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 3962.5833333333335
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 47551
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 47551
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 785.601273
[INSERT], MinLatency(us), 220
[INSERT], MaxLatency(us), 1057791
[INSERT], 95thPercentileLatency(us), 1005
[INSERT], 99thPercentileLatency(us), 2529
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 213354
[OVERALL], Throughput(ops/sec), 23435.22971212164
[TOTAL_GCS_G1_Young_Generation], Count, 416
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 300
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.14061137827272982
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 416
[TOTAL_GC_TIME], Time(ms), 300
[TOTAL_GC_TIME_%], Time(%), 0.14061137827272982
[READ], Operations, 2498439
[READ], AverageLatency(us), 484.93966992990426
[READ], MinLatency(us), 237
[READ], MaxLatency(us), 81727
[READ], 95thPercentileLatency(us), 791
[READ], 99thPercentileLatency(us), 1947
[READ], Return=OK, 2498439
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 400.1666666666667
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 4787
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 4787
[UPDATE], Operations, 2501561
[UPDATE], AverageLatency(us), 531.1640639584643
[UPDATE], MinLatency(us), 239
[UPDATE], MaxLatency(us), 81599
[UPDATE], 95thPercentileLatency(us), 874
[UPDATE], 99thPercentileLatency(us), 2159
[UPDATE], Return=OK, 2501561
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 305139
[OVERALL], Throughput(ops/sec), 16385.974916349598
[TOTAL_GCS_G1_Young_Generation], Count, 338
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 236
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0773418016051701
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 338
[TOTAL_GC_TIME], Time(ms), 236
[TOTAL_GC_TIME_%], Time(%), 0.0773418016051701
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 304.0
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3633
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 3633
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 727.252546
[INSERT], MinLatency(us), 226
[INSERT], MaxLatency(us), 998911
[INSERT], 95thPercentileLatency(us), 1023
[INSERT], 99thPercentileLatency(us), 2369
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 229677
[OVERALL], Throughput(ops/sec), 21769.70266940094
[TOTAL_GCS_G1_Young_Generation], Count, 498
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 353
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15369410084597065
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 498
[TOTAL_GC_TIME], Time(ms), 353
[TOTAL_GC_TIME_%], Time(%), 0.15369410084597065
[READ], Operations, 4750993
[READ], AverageLatency(us), 542.9701243508463
[READ], MinLatency(us), 238
[READ], MaxLatency(us), 81855
[READ], 95thPercentileLatency(us), 913
[READ], 99thPercentileLatency(us), 2553
[READ], Return=OK, 4750993
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 212.5
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 2537
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2537
[UPDATE], Operations, 249007
[UPDATE], AverageLatency(us), 622.7053777604646
[UPDATE], MinLatency(us), 293
[UPDATE], MaxLatency(us), 81471
[UPDATE], 95thPercentileLatency(us), 1072
[UPDATE], 99thPercentileLatency(us), 2717
[UPDATE], Return=OK, 249007
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 317530
[OVERALL], Throughput(ops/sec), 15746.543633672409
[TOTAL_GCS_G1_Young_Generation], Count, 337
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 238
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07495354769628067
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 337
[TOTAL_GC_TIME], Time(ms), 238
[TOTAL_GC_TIME_%], Time(%), 0.07495354769628067
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 241.25
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2879
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 2879
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 756.622084
[INSERT], MinLatency(us), 229
[INSERT], MaxLatency(us), 1827839
[INSERT], 95thPercentileLatency(us), 1216
[INSERT], 99thPercentileLatency(us), 2821
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 242159
[OVERALL], Throughput(ops/sec), 20647.591045552716
[TOTAL_GCS_G1_Young_Generation], Count, 512
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 369
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15237922191617903
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 512
[TOTAL_GC_TIME], Time(ms), 369
[TOTAL_GC_TIME_%], Time(%), 0.15237922191617903
[READ], Operations, 5000000
[READ], AverageLatency(us), 576.2944306
[READ], MinLatency(us), 244
[READ], MaxLatency(us), 305151
[READ], 95thPercentileLatency(us), 949
[READ], 99thPercentileLatency(us), 2489
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 402.6666666666667
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 4815
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 4815
```

## Docker MTU 1500

### Workload A Load

```shell
[OVERALL], RunTime(ms), 359252
[OVERALL], Throughput(ops/sec), 13917.806998986784
[TOTAL_GCS_G1_Young_Generation], Count, 336
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 238
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0662487613151771
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 336
[TOTAL_GC_TIME], Time(ms), 238
[TOTAL_GC_TIME_%], Time(%), 0.0662487613151771
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 230.66666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 2753
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2753
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 857.2702622
[INSERT], MinLatency(us), 248
[INSERT], MaxLatency(us), 998399
[INSERT], 95thPercentileLatency(us), 1504
[INSERT], 99thPercentileLatency(us), 3163
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 238698
[OVERALL], Throughput(ops/sec), 20946.970649104725
[TOTAL_GCS_G1_Young_Generation], Count, 417
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 304
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.12735758154655674
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 417
[TOTAL_GC_TIME], Time(ms), 304
[TOTAL_GC_TIME_%], Time(%), 0.12735758154655674
[READ], Operations, 2499147
[READ], AverageLatency(us), 535.1116108816328
[READ], MinLatency(us), 260
[READ], MaxLatency(us), 208255
[READ], 95thPercentileLatency(us), 1089
[READ], 99thPercentileLatency(us), 1996
[READ], Return=OK, 2499147
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 202.83333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2419
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2419
[UPDATE], Operations, 2500853
[UPDATE], AverageLatency(us), 594.7303703976203
[UPDATE], MinLatency(us), 269
[UPDATE], MaxLatency(us), 208255
[UPDATE], 95thPercentileLatency(us), 1229
[UPDATE], 99thPercentileLatency(us), 2169
[UPDATE], Return=OK, 2500853
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 327598
[OVERALL], Throughput(ops/sec), 15262.608440832972
[TOTAL_GCS_G1_Young_Generation], Count, 337
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 235
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07173425967191498
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 337
[TOTAL_GC_TIME], Time(ms), 235
[TOTAL_GC_TIME_%], Time(%), 0.07173425967191498
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 516.0833333333334
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 6179
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 6179
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 781.2485694
[INSERT], MinLatency(us), 244
[INSERT], MaxLatency(us), 971775
[INSERT], 95thPercentileLatency(us), 1626
[INSERT], 99thPercentileLatency(us), 3243
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 242307
[OVERALL], Throughput(ops/sec), 20634.979592005184
[TOTAL_GCS_G1_Young_Generation], Count, 498
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 352
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.14527025632771648
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 498
[TOTAL_GC_TIME], Time(ms), 352
[TOTAL_GC_TIME_%], Time(%), 0.14527025632771648
[READ], Operations, 4750564
[READ], AverageLatency(us), 573.6594429629829
[READ], MinLatency(us), 260
[READ], MaxLatency(us), 209023
[READ], 95thPercentileLatency(us), 988
[READ], 99thPercentileLatency(us), 2036
[READ], Return=OK, 4750564
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 216.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2583
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2583
[UPDATE], Operations, 249436
[UPDATE], AverageLatency(us), 648.8342179957986
[UPDATE], MinLatency(us), 302
[UPDATE], MaxLatency(us), 78079
[UPDATE], 95thPercentileLatency(us), 1128
[UPDATE], 99thPercentileLatency(us), 2261
[UPDATE], Return=OK, 249436
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 333879
[OVERALL], Throughput(ops/sec), 14975.485130840814
[TOTAL_GCS_G1_Young_Generation], Count, 338
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 236
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07068428981756865
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 338
[TOTAL_GC_TIME], Time(ms), 236
[TOTAL_GC_TIME_%], Time(%), 0.07068428981756865
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 270.0833333333333
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3227
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 3227
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 793.968486
[INSERT], MinLatency(us), 250
[INSERT], MaxLatency(us), 997887
[INSERT], 95thPercentileLatency(us), 1465
[INSERT], 99thPercentileLatency(us), 2827
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 221733
[OVERALL], Throughput(ops/sec), 22549.64303915069
[TOTAL_GCS_G1_Young_Generation], Count, 522
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 348
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1569455155524888
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 522
[TOTAL_GC_TIME], Time(ms), 348
[TOTAL_GC_TIME_%], Time(%), 0.1569455155524888
[READ], Operations, 5000000
[READ], AverageLatency(us), 527.8147922
[READ], MinLatency(us), 250
[READ], MaxLatency(us), 74367
[READ], 95thPercentileLatency(us), 867
[READ], 99thPercentileLatency(us), 1885
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 231.33333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2761
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2761
```

## Docker MTU 1440

### Workload A Load

```shell
[OVERALL], RunTime(ms), 339926
[OVERALL], Throughput(ops/sec), 14709.08374175556
[TOTAL_GCS_G1_Young_Generation], Count, 337
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 233
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.06854433023658091
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 337
[TOTAL_GC_TIME], Time(ms), 233
[TOTAL_GC_TIME_%], Time(%), 0.06854433023658091
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 294.1666666666667
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3515
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 3515
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 810.1463742
[INSERT], MinLatency(us), 250
[INSERT], MaxLatency(us), 997887
[INSERT], 95thPercentileLatency(us), 1383
[INSERT], 99thPercentileLatency(us), 2647
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 234103
[OVERALL], Throughput(ops/sec), 21358.120143697433
[TOTAL_GCS_G1_Young_Generation], Count, 417
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 295
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.12601290884781485
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 417
[TOTAL_GC_TIME], Time(ms), 295
[TOTAL_GC_TIME_%], Time(%), 0.12601290884781485
[READ], Operations, 2498474
[READ], AverageLatency(us), 529.9275365683213
[READ], MinLatency(us), 270
[READ], MaxLatency(us), 103551
[READ], 95thPercentileLatency(us), 969
[READ], 99thPercentileLatency(us), 1599
[READ], Return=OK, 2498474
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 224.25
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2675
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 2675
[UPDATE], Operations, 2501526
[UPDATE], AverageLatency(us), 585.9044463259627
[UPDATE], MinLatency(us), 263
[UPDATE], MaxLatency(us), 107263
[UPDATE], 95thPercentileLatency(us), 1091
[UPDATE], 99thPercentileLatency(us), 1785
[UPDATE], Return=OK, 2501526
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 315060
[OVERALL], Throughput(ops/sec), 15869.993017203073
[TOTAL_GCS_G1_Young_Generation], Count, 339
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 249
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0790325652256713
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 339
[TOTAL_GC_TIME], Time(ms), 249
[TOTAL_GC_TIME_%], Time(%), 0.0790325652256713
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 267.5
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3195
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 3195
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 750.103517
[INSERT], MinLatency(us), 250
[INSERT], MaxLatency(us), 994303
[INSERT], 95thPercentileLatency(us), 1405
[INSERT], 99thPercentileLatency(us), 2733
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 245408
[OVERALL], Throughput(ops/sec), 20374.23392880428
[TOTAL_GCS_G1_Young_Generation], Count, 498
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 346
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1409896987873256
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 498
[TOTAL_GC_TIME], Time(ms), 346
[TOTAL_GC_TIME_%], Time(%), 0.1409896987873256
[READ], Operations, 4749843
[READ], AverageLatency(us), 580.6626595868537
[READ], MinLatency(us), 267
[READ], MaxLatency(us), 69503
[READ], 95thPercentileLatency(us), 996
[READ], 99thPercentileLatency(us), 2157
[READ], Return=OK, 4749843
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 214.16666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2551
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2551
[UPDATE], Operations, 250157
[UPDATE], AverageLatency(us), 663.673812845533
[UPDATE], MinLatency(us), 309
[UPDATE], MaxLatency(us), 30239
[UPDATE], 95thPercentileLatency(us), 1161
[UPDATE], 99thPercentileLatency(us), 2427
[UPDATE], Return=OK, 250157
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 327761
[OVERALL], Throughput(ops/sec), 15255.018138216567
[TOTAL_GCS_G1_Young_Generation], Count, 336
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 238
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07261388633791085
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 336
[TOTAL_GC_TIME], Time(ms), 238
[TOTAL_GC_TIME_%], Time(%), 0.07261388633791085
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 255.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3049
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 3049
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 781.8345742
[INSERT], MinLatency(us), 262
[INSERT], MaxLatency(us), 997887
[INSERT], 95thPercentileLatency(us), 1536
[INSERT], 99thPercentileLatency(us), 3201
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 230565
[OVERALL], Throughput(ops/sec), 21685.858651573308
[TOTAL_GCS_G1_Young_Generation], Count, 509
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 350
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15180101056101317
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 509
[TOTAL_GC_TIME], Time(ms), 350
[TOTAL_GC_TIME_%], Time(%), 0.15180101056101317
[READ], Operations, 5000000
[READ], AverageLatency(us), 549.3547048
[READ], MinLatency(us), 266
[READ], MaxLatency(us), 86783
[READ], 95thPercentileLatency(us), 870
[READ], 99thPercentileLatency(us), 1366
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 241.58333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2883
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 2883
```
