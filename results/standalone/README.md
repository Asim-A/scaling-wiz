# YCSB Results

This section contains all YCSB Workload test results for the standalone configuration.

### Workload A Load

### Workload A Run

YCSB Parameters:

- w=1
- 5000000 records
- 5000000 operations
- threads, t=12

## Normal / Native

### Workload A Load

```shell
[OVERALL], RunTime(ms), 173039
[OVERALL], Throughput(ops/sec), 28895.220152682345
[TOTAL_GCS_G1_Young_Generation], Count, 241
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 168
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.09708793971301267
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 241
[TOTAL_GC_TIME], Time(ms), 168
[TOTAL_GC_TIME_%], Time(%), 0.09708793971301267
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 203.33333333333334
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 2427
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2427
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 411.5780838
[INSERT], MinLatency(us), 178
[INSERT], MaxLatency(us), 805887
[INSERT], 95thPercentileLatency(us), 625
[INSERT], 99thPercentileLatency(us), 1228
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 178316
[OVERALL], Throughput(ops/sec), 28040.10857130039
[TOTAL_GCS_G1_Young_Generation], Count, 334
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 235
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.13178851028511182
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 334
[TOTAL_GC_TIME], Time(ms), 235
[TOTAL_GC_TIME_%], Time(%), 0.13178851028511182
[READ], Operations, 2501639
[READ], AverageLatency(us), 424.95265623857
[READ], MinLatency(us), 215
[READ], MaxLatency(us), 58847
[READ], 95thPercentileLatency(us), 615
[READ], 99thPercentileLatency(us), 1273
[READ], Return=OK, 2501639
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 194.33333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2317
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2317
[UPDATE], Operations, 2498361
[UPDATE], AverageLatency(us), 423.082231911241
[UPDATE], MinLatency(us), 197
[UPDATE], MaxLatency(us), 58207
[UPDATE], 95thPercentileLatency(us), 617
[UPDATE], 99thPercentileLatency(us), 1285
[UPDATE], Return=OK, 2498361
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 168189
[OVERALL], Throughput(ops/sec), 29728.460244130114
[TOTAL_GCS_G1_Young_Generation], Count, 240
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 167
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0992930572153946
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 240
[TOTAL_GC_TIME], Time(ms), 167
[TOTAL_GC_TIME_%], Time(%), 0.0992930572153946
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 281.9166666666667
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 3363
[CLEANUP], 95thPercentileLatency(us), 7
[CLEANUP], 99thPercentileLatency(us), 3363
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 399.9801944
[INSERT], MinLatency(us), 182
[INSERT], MaxLatency(us), 724479
[INSERT], 95thPercentileLatency(us), 606
[INSERT], 99thPercentileLatency(us), 1073
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 183354
[OVERALL], Throughput(ops/sec), 27269.653239089414
[TOTAL_GCS_G1_Young_Generation], Count, 426
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 291
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15870938185150038
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 426
[TOTAL_GC_TIME], Time(ms), 291
[TOTAL_GC_TIME_%], Time(%), 0.15870938185150038
[READ], Operations, 4749547
[READ], AverageLatency(us), 435.13156202054637
[READ], MinLatency(us), 209
[READ], MaxLatency(us), 205055
[READ], 95thPercentileLatency(us), 607
[READ], 99thPercentileLatency(us), 2121
[READ], Return=OK, 4749547
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 200.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2381
[CLEANUP], 95thPercentileLatency(us), 9
[CLEANUP], 99thPercentileLatency(us), 2381
[UPDATE], Operations, 250453
[UPDATE], AverageLatency(us), 454.505591867536
[UPDATE], MinLatency(us), 212
[UPDATE], MaxLatency(us), 204927
[UPDATE], 95thPercentileLatency(us), 651
[UPDATE], 99thPercentileLatency(us), 2177
[UPDATE], Return=OK, 250453
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 177122
[OVERALL], Throughput(ops/sec), 28229.130204040153
[TOTAL_GCS_G1_Young_Generation], Count, 237
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 164
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0925915470692517
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 237
[TOTAL_GC_TIME], Time(ms), 164
[TOTAL_GC_TIME_%], Time(%), 0.0925915470692517
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 170.66666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 2033
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2033
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 421.337444
[INSERT], MinLatency(us), 182
[INSERT], MaxLatency(us), 694271
[INSERT], 95thPercentileLatency(us), 676
[INSERT], 99thPercentileLatency(us), 1516
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 182968
[OVERALL], Throughput(ops/sec), 27327.182895369682
[TOTAL_GCS_G1_Young_Generation], Count, 446
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 294
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1606838354247737
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 446
[TOTAL_GC_TIME], Time(ms), 294
[TOTAL_GC_TIME_%], Time(%), 0.1606838354247737
[READ], Operations, 5000000
[READ], AverageLatency(us), 435.5175084
[READ], MinLatency(us), 214
[READ], MaxLatency(us), 306687
[READ], 95thPercentileLatency(us), 589
[READ], 99thPercentileLatency(us), 1503
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 145.66666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1733
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1733
```

## Docker MTU 1500

### Workload A Load

```shell
[OVERALL], RunTime(ms), 221038
[OVERALL], Throughput(ops/sec), 22620.544883685157
[TOTAL_GCS_G1_Young_Generation], Count, 239
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 172
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07781467439987695
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 239
[TOTAL_GC_TIME], Time(ms), 172
[TOTAL_GC_TIME_%], Time(%), 0.07781467439987695
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 158.5
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1887
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1887
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 526.1765184
[INSERT], MinLatency(us), 216
[INSERT], MaxLatency(us), 741375
[INSERT], 95thPercentileLatency(us), 1164
[INSERT], 99thPercentileLatency(us), 2601
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 227036
[OVERALL], Throughput(ops/sec), 22022.939093359644
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 252
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1109956130305326
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 333
[TOTAL_GC_TIME], Time(ms), 252
[TOTAL_GC_TIME_%], Time(%), 0.1109956130305326
[READ], Operations, 2500656
[READ], AverageLatency(us), 540.2905697544965
[READ], MinLatency(us), 237
[READ], MaxLatency(us), 206591
[READ], 95thPercentileLatency(us), 1050
[READ], 99thPercentileLatency(us), 2759
[READ], Return=OK, 2500656
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 195.75
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2333
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 2333
[UPDATE], Operations, 2499344
[UPDATE], AverageLatency(us), 538.2140793744278
[UPDATE], MinLatency(us), 220
[UPDATE], MaxLatency(us), 206591
[UPDATE], 95thPercentileLatency(us), 1065
[UPDATE], 99thPercentileLatency(us), 2749
[UPDATE], Return=OK, 2499344
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 208785
[OVERALL], Throughput(ops/sec), 23948.08056134301
[TOTAL_GCS_G1_Young_Generation], Count, 242
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 177
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08477620518715424
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 242
[TOTAL_GC_TIME], Time(ms), 177
[TOTAL_GC_TIME_%], Time(%), 0.08477620518715424
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 159.91666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1903
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1903
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 493.9681988
[INSERT], MinLatency(us), 211
[INSERT], MaxLatency(us), 753663
[INSERT], 95thPercentileLatency(us), 1023
[INSERT], 99thPercentileLatency(us), 2309
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 204592
[OVERALL], Throughput(ops/sec), 24438.88324079143
[TOTAL_GCS_G1_Young_Generation], Count, 435
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 314
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15347618675217017
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 435
[TOTAL_GC_TIME], Time(ms), 314
[TOTAL_GC_TIME_%], Time(%), 0.15347618675217017
[READ], Operations, 4749974
[READ], AverageLatency(us), 485.8048795635513
[READ], MinLatency(us), 233
[READ], MaxLatency(us), 62687
[READ], 95thPercentileLatency(us), 773
[READ], 99thPercentileLatency(us), 2129
[READ], Return=OK, 4749974
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 161.66666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1926
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1926
[UPDATE], Operations, 250026
[UPDATE], AverageLatency(us), 502.9907649604441
[UPDATE], MinLatency(us), 227
[UPDATE], MaxLatency(us), 23023
[UPDATE], 95thPercentileLatency(us), 826
[UPDATE], 99thPercentileLatency(us), 2169
[UPDATE], Return=OK, 250026
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 209125
[OVERALL], Throughput(ops/sec), 23909.145248057383
[TOTAL_GCS_G1_Young_Generation], Count, 238
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 173
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08272564255827855
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 238
[TOTAL_GC_TIME], Time(ms), 173
[TOTAL_GC_TIME_%], Time(%), 0.08272564255827855
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 183.08333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 2183
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 2183
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 496.4465192
[INSERT], MinLatency(us), 213
[INSERT], MaxLatency(us), 835583
[INSERT], 95thPercentileLatency(us), 1018
[INSERT], 99thPercentileLatency(us), 2337
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 197302
[OVERALL], Throughput(ops/sec), 25341.861714528997
[TOTAL_GCS_G1_Young_Generation], Count, 434
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 291
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.14748963517855876
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 434
[TOTAL_GC_TIME], Time(ms), 291
[TOTAL_GC_TIME_%], Time(%), 0.14748963517855876
[READ], Operations, 5000000
[READ], AverageLatency(us), 469.4188674
[READ], MinLatency(us), 234
[READ], MaxLatency(us), 70399
[READ], 95thPercentileLatency(us), 716
[READ], 99thPercentileLatency(us), 1890
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 133.5
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1587
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1587
```

## Docker MTU 1340

### Workload A Load

```shell
[OVERALL], RunTime(ms), 207467
[OVERALL], Throughput(ops/sec), 24100.218347978232
[TOTAL_GCS_G1_Young_Generation], Count, 238
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 167
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.0804947292822473
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 238
[TOTAL_GC_TIME], Time(ms), 167
[TOTAL_GC_TIME_%], Time(%), 0.0804947292822473
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 155.25
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1848
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1848
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 492.0270762
[INSERT], MinLatency(us), 205
[INSERT], MaxLatency(us), 771583
[INSERT], 95thPercentileLatency(us), 1062
[INSERT], 99thPercentileLatency(us), 2377
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 223992
[OVERALL], Throughput(ops/sec), 22322.22579377835
[TOTAL_GCS_G1_Young_Generation], Count, 333
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 228
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.10178934961962928
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 333
[TOTAL_GC_TIME], Time(ms), 228
[TOTAL_GC_TIME_%], Time(%), 0.10178934961962928
[READ], Operations, 2500477
[READ], AverageLatency(us), 531.833658537951
[READ], MinLatency(us), 242
[READ], MaxLatency(us), 312575
[READ], 95thPercentileLatency(us), 1022
[READ], 99thPercentileLatency(us), 2351
[READ], Return=OK, 2500477
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 164.41666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1960
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1960
[UPDATE], Operations, 2499523
[UPDATE], AverageLatency(us), 535.8322095855889
[UPDATE], MinLatency(us), 228
[UPDATE], MaxLatency(us), 313343
[UPDATE], 95thPercentileLatency(us), 1051
[UPDATE], 99thPercentileLatency(us), 2355
[UPDATE], Return=OK, 2499523
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 208572
[OVERALL], Throughput(ops/sec), 23972.537061542298
[TOTAL_GCS_G1_Young_Generation], Count, 242
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 170
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08150662600924381
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 242
[TOTAL_GC_TIME], Time(ms), 170
[TOTAL_GC_TIME_%], Time(%), 0.08150662600924381
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 146.75
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1747
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1747
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 492.7810884
[INSERT], MinLatency(us), 214
[INSERT], MaxLatency(us), 768511
[INSERT], 95thPercentileLatency(us), 1025
[INSERT], 99thPercentileLatency(us), 2295
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 212898
[OVERALL], Throughput(ops/sec), 23485.42494527896
[TOTAL_GCS_G1_Young_Generation], Count, 428
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 288
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1352760476848068
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 428
[TOTAL_GC_TIME], Time(ms), 288
[TOTAL_GC_TIME_%], Time(%), 0.1352760476848068
[READ], Operations, 4749751
[READ], AverageLatency(us), 505.3085702808421
[READ], MinLatency(us), 240
[READ], MaxLatency(us), 66111
[READ], 95thPercentileLatency(us), 871
[READ], 99thPercentileLatency(us), 2207
[READ], Return=OK, 4749751
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 167.66666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1998
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1998
[UPDATE], Operations, 250249
[UPDATE], AverageLatency(us), 527.248548445748
[UPDATE], MinLatency(us), 234
[UPDATE], MaxLatency(us), 57471
[UPDATE], 95thPercentileLatency(us), 928
[UPDATE], 99thPercentileLatency(us), 2245
[UPDATE], Return=OK, 250249
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 211689
[OVERALL], Throughput(ops/sec), 23619.555102060098
[TOTAL_GCS_G1_Young_Generation], Count, 238
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 162
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07652735853067472
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 238
[TOTAL_GC_TIME], Time(ms), 162
[TOTAL_GC_TIME_%], Time(%), 0.07652735853067472
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 160.16666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1907
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 1907
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 503.7452642
[INSERT], MinLatency(us), 211
[INSERT], MaxLatency(us), 798207
[INSERT], 95thPercentileLatency(us), 1042
[INSERT], 99thPercentileLatency(us), 2293
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 199170
[OVERALL], Throughput(ops/sec), 25104.18235678064
[TOTAL_GCS_G1_Young_Generation], Count, 437
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 286
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.14359592308078525
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 437
[TOTAL_GC_TIME], Time(ms), 286
[TOTAL_GC_TIME_%], Time(%), 0.14359592308078525
[READ], Operations, 5000000
[READ], AverageLatency(us), 474.0763348
[READ], MinLatency(us), 233
[READ], MaxLatency(us), 62655
[READ], 95thPercentileLatency(us), 765
[READ], 99thPercentileLatency(us), 2065
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 148.33333333333334
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1765
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1765
```

## Docker MTU 1450

### Workload A Load

```shell
[OVERALL], RunTime(ms), 207146
[OVERALL], Throughput(ops/sec), 24137.564809361513
[TOTAL_GCS_G1_Young_Generation], Count, 237
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 166
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08013671516708022
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 237
[TOTAL_GC_TIME], Time(ms), 166
[TOTAL_GC_TIME_%], Time(%), 0.08013671516708022
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 143.41666666666666
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1704
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1704
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 491.3845988
[INSERT], MinLatency(us), 211
[INSERT], MaxLatency(us), 755711
[INSERT], 95thPercentileLatency(us), 1047
[INSERT], 99thPercentileLatency(us), 2323
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 198595
[OVERALL], Throughput(ops/sec), 25176.86749414638
[TOTAL_GCS_G1_Young_Generation], Count, 334
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 231
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.11631712782295626
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 334
[TOTAL_GC_TIME], Time(ms), 231
[TOTAL_GC_TIME_%], Time(%), 0.11631712782295626
[READ], Operations, 2499530
[READ], AverageLatency(us), 471.23326985473267
[READ], MinLatency(us), 232
[READ], MaxLatency(us), 53855
[READ], 95thPercentileLatency(us), 836
[READ], 99thPercentileLatency(us), 2147
[READ], Return=OK, 2499530
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 134.08333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1595
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1595
[UPDATE], Operations, 2500470
[UPDATE], AverageLatency(us), 471.4036981047563
[UPDATE], MinLatency(us), 214
[UPDATE], MaxLatency(us), 53567
[UPDATE], 95thPercentileLatency(us), 867
[UPDATE], 99thPercentileLatency(us), 2143
[UPDATE], Return=OK, 2500470
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 227551
[OVERALL], Throughput(ops/sec), 21973.096141084854
[TOTAL_GCS_G1_Young_Generation], Count, 238
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 176
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07734529841661869
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 238
[TOTAL_GC_TIME], Time(ms), 176
[TOTAL_GC_TIME_%], Time(%), 0.07734529841661869
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 139.08333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1654
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1654
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 540.0700454
[INSERT], MinLatency(us), 215
[INSERT], MaxLatency(us), 770047
[INSERT], 95thPercentileLatency(us), 1254
[INSERT], 99thPercentileLatency(us), 2543
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 218057
[OVERALL], Throughput(ops/sec), 22929.784414166937
[TOTAL_GCS_G1_Young_Generation], Count, 425
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 296
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1357443237318683
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 425
[TOTAL_GC_TIME], Time(ms), 296
[TOTAL_GC_TIME_%], Time(%), 0.1357443237318683
[READ], Operations, 4749929
[READ], AverageLatency(us), 517.1990095009842
[READ], MinLatency(us), 242
[READ], MaxLatency(us), 212223
[READ], 95thPercentileLatency(us), 930
[READ], 99thPercentileLatency(us), 2103
[READ], Return=OK, 4749929
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 134.5
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1599
[CLEANUP], 95thPercentileLatency(us), 6
[CLEANUP], 99thPercentileLatency(us), 1599
[UPDATE], Operations, 250071
[UPDATE], AverageLatency(us), 538.6691579591396
[UPDATE], MinLatency(us), 240
[UPDATE], MaxLatency(us), 37183
[UPDATE], 95thPercentileLatency(us), 992
[UPDATE], 99thPercentileLatency(us), 2175
[UPDATE], Return=OK, 250071
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 215619
[OVERALL], Throughput(ops/sec), 23189.051057652618
[TOTAL_GCS_G1_Young_Generation], Count, 237
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 169
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.07837899257486586
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 237
[TOTAL_GC_TIME], Time(ms), 169
[TOTAL_GC_TIME_%], Time(%), 0.07837899257486586
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 141.0
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1676
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1676
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 512.5428072
[INSERT], MinLatency(us), 217
[INSERT], MaxLatency(us), 835583
[INSERT], 95thPercentileLatency(us), 1078
[INSERT], 99thPercentileLatency(us), 2243
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 196590
[OVERALL], Throughput(ops/sec), 25433.643623785545
[TOTAL_GCS_G1_Young_Generation], Count, 447
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 303
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15412788036014038
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 447
[TOTAL_GC_TIME], Time(ms), 303
[TOTAL_GC_TIME_%], Time(%), 0.15412788036014038
[READ], Operations, 5000000
[READ], AverageLatency(us), 467.4551116
[READ], MinLatency(us), 231
[READ], MaxLatency(us), 215551
[READ], 95thPercentileLatency(us), 741
[READ], 99thPercentileLatency(us), 1733
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 163.0
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1943
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1943
```

## Docker MTU 1440

### Workload A Load

```shell
[OVERALL], RunTime(ms), 204659
[OVERALL], Throughput(ops/sec), 24430.882590064448
[TOTAL_GCS_G1_Young_Generation], Count, 242
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 165
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08062191254721268
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 242
[TOTAL_GC_TIME], Time(ms), 165
[TOTAL_GC_TIME_%], Time(%), 0.08062191254721268
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 146.83333333333334
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1747
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1747
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 487.5041022
[INSERT], MinLatency(us), 217
[INSERT], MaxLatency(us), 743423
[INSERT], 95thPercentileLatency(us), 979
[INSERT], 99thPercentileLatency(us), 1998
[INSERT], Return=OK, 5000000
```

### Workload A Run

```shell
[OVERALL], RunTime(ms), 185419
[OVERALL], Throughput(ops/sec), 26965.952788009858
[TOTAL_GCS_G1_Young_Generation], Count, 334
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 230
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.12404338282484535
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 334
[TOTAL_GC_TIME], Time(ms), 230
[TOTAL_GC_TIME_%], Time(%), 0.12404338282484535
[READ], Operations, 2501077
[READ], AverageLatency(us), 440.0197219038038
[READ], MinLatency(us), 232
[READ], MaxLatency(us), 207871
[READ], 95thPercentileLatency(us), 746
[READ], 99thPercentileLatency(us), 1269
[READ], Return=OK, 2501077
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 132.25
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1573
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1573
[UPDATE], Operations, 2498923
[UPDATE], AverageLatency(us), 440.5155120826052
[UPDATE], MinLatency(us), 208
[UPDATE], MaxLatency(us), 312831
[UPDATE], 95thPercentileLatency(us), 774
[UPDATE], 99thPercentileLatency(us), 1303
[UPDATE], Return=OK, 2498923
```

### Workload B Load

```shell
[OVERALL], RunTime(ms), 201039
[OVERALL], Throughput(ops/sec), 24870.796213669986
[TOTAL_GCS_G1_Young_Generation], Count, 237
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 164
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08157621158083755
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 237
[TOTAL_GC_TIME], Time(ms), 164
[TOTAL_GC_TIME_%], Time(%), 0.08157621158083755
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 154.0
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1826
[CLEANUP], 95thPercentileLatency(us), 11
[CLEANUP], 99thPercentileLatency(us), 1826
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 475.396613
[INSERT], MinLatency(us), 210
[INSERT], MaxLatency(us), 785407
[INSERT], 95thPercentileLatency(us), 899
[INSERT], 99thPercentileLatency(us), 2257
[INSERT], Return=OK, 5000000
```

### Workload B Run

```shell
[OVERALL], RunTime(ms), 187344
[OVERALL], Throughput(ops/sec), 26688.871808010932
[TOTAL_GCS_G1_Young_Generation], Count, 426
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 280
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.1494576821248612
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 426
[TOTAL_GC_TIME], Time(ms), 280
[TOTAL_GC_TIME_%], Time(%), 0.1494576821248612
[READ], Operations, 4750609
[READ], AverageLatency(us), 445.14822015451074
[READ], MinLatency(us), 230
[READ], MaxLatency(us), 64415
[READ], 95thPercentileLatency(us), 674
[READ], 99thPercentileLatency(us), 1316
[READ], Return=OK, 4750609
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 135.91666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1620
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1620
[UPDATE], Operations, 249391
[UPDATE], AverageLatency(us), 460.41581292027377
[UPDATE], MinLatency(us), 230
[UPDATE], MaxLatency(us), 64351
[UPDATE], 95thPercentileLatency(us), 724
[UPDATE], 99thPercentileLatency(us), 1354
[UPDATE], Return=OK, 249391
```

### Workload C Load

```shell
[OVERALL], RunTime(ms), 207262
[OVERALL], Throughput(ops/sec), 24124.055543225484
[TOTAL_GCS_G1_Young_Generation], Count, 242
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 167
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.08057434551437312
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 242
[TOTAL_GC_TIME], Time(ms), 167
[TOTAL_GC_TIME_%], Time(%), 0.08057434551437312
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 155.41666666666666
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 1851
[CLEANUP], 95thPercentileLatency(us), 5
[CLEANUP], 99thPercentileLatency(us), 1851
[INSERT], Operations, 5000000
[INSERT], AverageLatency(us), 493.2720038
[INSERT], MinLatency(us), 216
[INSERT], MaxLatency(us), 787455
[INSERT], 95thPercentileLatency(us), 997
[INSERT], 99thPercentileLatency(us), 2038
[INSERT], Return=OK, 5000000
```

### Workload C Run

```shell
[OVERALL], RunTime(ms), 186294
[OVERALL], Throughput(ops/sec), 26839.297025132317
[TOTAL_GCS_G1_Young_Generation], Count, 436
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 285
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.15298399304325422
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 436
[TOTAL_GC_TIME], Time(ms), 285
[TOTAL_GC_TIME_%], Time(%), 0.15298399304325422
[READ], Operations, 5000000
[READ], AverageLatency(us), 443.6274878
[READ], MinLatency(us), 240
[READ], MaxLatency(us), 62559
[READ], 95thPercentileLatency(us), 622
[READ], 99thPercentileLatency(us), 991
[READ], Return=OK, 5000000
[CLEANUP], Operations, 12
[CLEANUP], AverageLatency(us), 139.75
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 1663
[CLEANUP], 95thPercentileLatency(us), 4
[CLEANUP], 99thPercentileLatency(us), 1663
```
