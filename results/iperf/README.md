# Results

This section contains all iperf3 bandwidth tests. Native and running on docker with various mtu's set. The tests were conducted for send and receive bandwidth.

The bandwidth test was exactly the same in each case. Time t=60.

## Normal / Native

### Send

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   112 MBytes   942 Mbits/sec
[  4]   1.00-2.00   sec   113 MBytes   949 Mbits/sec
[  4]   2.00-3.00   sec   113 MBytes   949 Mbits/sec
[  4]   3.00-4.00   sec   113 MBytes   949 Mbits/sec
[  4]   4.00-5.00   sec   113 MBytes   949 Mbits/sec
[  4]   5.00-6.00   sec   113 MBytes   949 Mbits/sec
[  4]   6.00-7.00   sec   113 MBytes   949 Mbits/sec
[  4]   7.00-8.00   sec   113 MBytes   949 Mbits/sec
[  4]   8.00-9.00   sec   113 MBytes   949 Mbits/sec
[  4]   9.00-10.00  sec   113 MBytes   949 Mbits/sec
[  4]  10.00-11.00  sec   113 MBytes   949 Mbits/sec
[  4]  11.00-12.00  sec   113 MBytes   949 Mbits/sec
[  4]  12.00-13.00  sec   113 MBytes   949 Mbits/sec
[  4]  13.00-14.00  sec   113 MBytes   949 Mbits/sec
[  4]  14.00-15.00  sec   113 MBytes   949 Mbits/sec
[  4]  15.00-16.00  sec   113 MBytes   949 Mbits/sec
[  4]  16.00-17.00  sec   113 MBytes   949 Mbits/sec
[  4]  17.00-18.00  sec   113 MBytes   949 Mbits/sec
[  4]  18.00-19.00  sec   113 MBytes   949 Mbits/sec
[  4]  19.00-20.00  sec   113 MBytes   949 Mbits/sec
[  4]  20.00-21.00  sec   113 MBytes   949 Mbits/sec
[  4]  21.00-22.00  sec   113 MBytes   949 Mbits/sec
[  4]  22.00-23.00  sec   113 MBytes   949 Mbits/sec
[  4]  23.00-24.00  sec   113 MBytes   949 Mbits/sec
[  4]  24.00-25.00  sec   113 MBytes   949 Mbits/sec
[  4]  25.00-26.00  sec   113 MBytes   949 Mbits/sec
[  4]  26.00-27.00  sec   113 MBytes   949 Mbits/sec
[  4]  27.00-28.00  sec   113 MBytes   949 Mbits/sec
[  4]  28.00-29.00  sec   113 MBytes   949 Mbits/sec
[  4]  29.00-30.00  sec   113 MBytes   949 Mbits/sec
[  4]  30.00-31.00  sec   113 MBytes   949 Mbits/sec
[  4]  31.00-32.00  sec   113 MBytes   949 Mbits/sec
[  4]  32.00-33.00  sec   113 MBytes   949 Mbits/sec
[  4]  33.00-34.00  sec   113 MBytes   949 Mbits/sec
[  4]  34.00-35.00  sec   113 MBytes   949 Mbits/sec
[  4]  35.00-36.00  sec   113 MBytes   949 Mbits/sec
[  4]  36.00-37.00  sec   113 MBytes   949 Mbits/sec
[  4]  37.00-38.00  sec   113 MBytes   949 Mbits/sec
[  4]  38.00-39.00  sec   113 MBytes   949 Mbits/sec
[  4]  39.00-40.00  sec   113 MBytes   949 Mbits/sec
[  4]  40.00-41.00  sec   113 MBytes   949 Mbits/sec
[  4]  41.00-42.00  sec   113 MBytes   949 Mbits/sec
[  4]  42.00-43.00  sec   113 MBytes   949 Mbits/sec
[  4]  43.00-44.00  sec   113 MBytes   949 Mbits/sec
[  4]  44.00-45.00  sec   113 MBytes   949 Mbits/sec
[  4]  45.00-46.00  sec   113 MBytes   949 Mbits/sec
[  4]  46.00-47.00  sec   113 MBytes   949 Mbits/sec
[  4]  47.00-48.00  sec   113 MBytes   949 Mbits/sec
[  4]  48.00-49.00  sec   113 MBytes   949 Mbits/sec
[  4]  49.00-50.00  sec   113 MBytes   949 Mbits/sec
[  4]  50.00-51.00  sec   113 MBytes   948 Mbits/sec
[  4]  51.00-52.00  sec   113 MBytes   950 Mbits/sec
[  4]  52.00-53.00  sec   113 MBytes   949 Mbits/sec
[  4]  53.00-54.00  sec   113 MBytes   949 Mbits/sec
[  4]  54.00-55.00  sec   113 MBytes   949 Mbits/sec
[  4]  55.00-56.00  sec   113 MBytes   949 Mbits/sec
[  4]  56.00-57.00  sec   113 MBytes   949 Mbits/sec
[  4]  57.00-58.00  sec   113 MBytes   949 Mbits/sec
[  4]  58.00-59.00  sec   113 MBytes   949 Mbits/sec
[  4]  59.00-60.00  sec   113 MBytes   949 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-60.00  sec  6.63 GBytes   949 Mbits/sec                  sender
[  4]   0.00-60.00  sec  6.63 GBytes   949 Mbits/sec                  receiver

```

### Receive

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   113 MBytes   945 Mbits/sec
[  4]   1.00-2.00   sec   112 MBytes   942 Mbits/sec
[  4]   2.00-3.00   sec   112 MBytes   942 Mbits/sec
[  4]   3.00-4.00   sec   112 MBytes   942 Mbits/sec
[  4]   4.00-5.00   sec   112 MBytes   942 Mbits/sec
[  4]   5.00-6.00   sec   112 MBytes   942 Mbits/sec
[  4]   6.00-7.00   sec   112 MBytes   942 Mbits/sec
[  4]   7.00-8.00   sec   112 MBytes   942 Mbits/sec
[  4]   8.00-9.00   sec   112 MBytes   942 Mbits/sec
[  4]   9.00-10.00  sec   112 MBytes   942 Mbits/sec
[  4]  10.00-11.00  sec   112 MBytes   942 Mbits/sec
[  4]  11.00-12.00  sec   112 MBytes   942 Mbits/sec
[  4]  12.00-13.00  sec   112 MBytes   942 Mbits/sec
[  4]  13.00-14.00  sec   112 MBytes   942 Mbits/sec
[  4]  14.00-15.00  sec   112 MBytes   942 Mbits/sec
[  4]  15.00-16.00  sec   112 MBytes   942 Mbits/sec
[  4]  16.00-17.00  sec   112 MBytes   942 Mbits/sec
[  4]  17.00-18.00  sec   112 MBytes   942 Mbits/sec
[  4]  18.00-19.00  sec   112 MBytes   942 Mbits/sec
[  4]  19.00-20.00  sec   112 MBytes   942 Mbits/sec
[  4]  20.00-21.00  sec   112 MBytes   942 Mbits/sec
[  4]  21.00-22.00  sec   112 MBytes   942 Mbits/sec
[  4]  22.00-23.00  sec   112 MBytes   942 Mbits/sec
[  4]  23.00-24.00  sec   112 MBytes   942 Mbits/sec
[  4]  24.00-25.00  sec   112 MBytes   942 Mbits/sec
[  4]  25.00-26.00  sec   112 MBytes   942 Mbits/sec
[  4]  26.00-27.00  sec   112 MBytes   942 Mbits/sec
[  4]  27.00-28.00  sec   112 MBytes   942 Mbits/sec
[  4]  28.00-29.00  sec   112 MBytes   942 Mbits/sec
[  4]  29.00-30.00  sec   112 MBytes   942 Mbits/sec
[  4]  30.00-31.00  sec   112 MBytes   942 Mbits/sec
[  4]  31.00-32.00  sec   112 MBytes   942 Mbits/sec
[  4]  32.00-33.00  sec   112 MBytes   942 Mbits/sec
[  4]  33.00-34.00  sec   112 MBytes   942 Mbits/sec
[  4]  34.00-35.00  sec   112 MBytes   942 Mbits/sec
[  4]  35.00-36.00  sec   112 MBytes   942 Mbits/sec
[  4]  36.00-37.00  sec   112 MBytes   942 Mbits/sec
[  4]  38.00-39.00  sec   112 MBytes   942 Mbits/sec
[  4]  39.00-40.00  sec   112 MBytes   942 Mbits/sec
[  4]  40.00-41.00  sec   112 MBytes   942 Mbits/sec
[  4]  41.00-42.00  sec   112 MBytes   942 Mbits/sec
[  4]  42.00-43.00  sec   112 MBytes   942 Mbits/sec
[  4]  43.00-44.00  sec   112 MBytes   942 Mbits/sec
[  4]  44.00-45.00  sec   112 MBytes   942 Mbits/sec
[  4]  45.00-46.00  sec   112 MBytes   942 Mbits/sec
[  4]  46.00-47.00  sec   112 MBytes   942 Mbits/sec
[  4]  47.00-48.00  sec   112 MBytes   942 Mbits/sec
[  4]  48.00-49.00  sec   112 MBytes   942 Mbits/sec
[  4]  49.00-50.00  sec   112 MBytes   942 Mbits/sec
[  4]  50.00-51.00  sec   112 MBytes   942 Mbits/sec
[  4]  51.00-52.00  sec   112 MBytes   942 Mbits/sec
[  4]  52.00-53.00  sec   112 MBytes   942 Mbits/sec
[  4]  53.00-54.00  sec   112 MBytes   942 Mbits/sec
[  4]  54.00-55.00  sec   112 MBytes   942 Mbits/sec
[  4]  55.00-56.00  sec   112 MBytes   942 Mbits/sec
[  4]  56.00-57.00  sec   112 MBytes   942 Mbits/sec
[  4]  57.00-58.00  sec   112 MBytes   942 Mbits/sec
[  4]  58.00-59.00  sec   112 MBytes   942 Mbits/sec
[  4]  59.00-60.00  sec   112 MBytes   942 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-60.00  sec  6.58 GBytes   942 Mbits/sec   12             sender
[  4]   0.00-60.00  sec  6.58 GBytes   942 Mbits/sec                  receiver
```

## Docker MTU 1500

### Send

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   109 MBytes   915 Mbits/sec
[  4]   1.00-2.00   sec   109 MBytes   918 Mbits/sec
[  4]   2.00-3.00   sec   110 MBytes   925 Mbits/sec
[  4]   3.00-4.00   sec   111 MBytes   928 Mbits/sec
[  4]   4.00-5.00   sec   107 MBytes   901 Mbits/sec
[  4]   5.00-6.00   sec   107 MBytes   898 Mbits/sec
[  4]   6.00-7.00   sec   109 MBytes   914 Mbits/sec
[  4]   7.00-8.00   sec   112 MBytes   935 Mbits/sec
[  4]   8.00-9.00   sec   111 MBytes   929 Mbits/sec
[  4]   9.00-10.00  sec   109 MBytes   917 Mbits/sec
[  4]  10.00-11.00  sec   110 MBytes   920 Mbits/sec
[  4]  11.00-12.00  sec   110 MBytes   919 Mbits/sec
[  4]  12.00-13.00  sec   106 MBytes   890 Mbits/sec
[  4]  13.00-14.00  sec   106 MBytes   893 Mbits/sec
[  4]  14.00-15.00  sec   109 MBytes   912 Mbits/sec
[  4]  15.00-16.00  sec   110 MBytes   928 Mbits/sec
[  4]  16.00-17.00  sec  96.6 MBytes   811 Mbits/sec
[  4]  17.00-18.00  sec   106 MBytes   889 Mbits/sec
[  4]  18.00-19.00  sec   108 MBytes   911 Mbits/sec
[  4]  19.00-20.00  sec   109 MBytes   913 Mbits/sec
[  4]  20.00-21.00  sec   106 MBytes   889 Mbits/sec
[  4]  21.00-22.00  sec   107 MBytes   895 Mbits/sec
[  4]  22.00-23.00  sec   106 MBytes   890 Mbits/sec
[  4]  23.00-24.00  sec   107 MBytes   898 Mbits/sec
[  4]  24.00-25.00  sec   104 MBytes   870 Mbits/sec
[  4]  25.00-26.00  sec   108 MBytes   907 Mbits/sec
[  4]  26.00-27.00  sec   110 MBytes   924 Mbits/sec
[  4]  27.00-28.00  sec   110 MBytes   922 Mbits/sec
[  4]  28.00-29.00  sec   109 MBytes   915 Mbits/sec
[  4]  29.00-30.00  sec   110 MBytes   921 Mbits/sec
[  4]  30.00-31.00  sec   110 MBytes   921 Mbits/sec
[  4]  31.00-32.00  sec   107 MBytes   901 Mbits/sec
[  4]  32.00-33.00  sec   111 MBytes   930 Mbits/sec
[  4]  33.00-34.00  sec   108 MBytes   909 Mbits/sec
[  4]  34.00-35.00  sec   110 MBytes   924 Mbits/sec
[  4]  35.00-36.00  sec   111 MBytes   928 Mbits/sec
[  4]  36.00-37.00  sec   111 MBytes   933 Mbits/sec
[  4]  37.00-38.00  sec   109 MBytes   918 Mbits/sec
[  4]  38.00-39.00  sec   109 MBytes   916 Mbits/sec
[  4]  39.00-40.00  sec   107 MBytes   899 Mbits/sec
[  4]  40.00-41.00  sec   110 MBytes   923 Mbits/sec
[  4]  41.00-42.00  sec   110 MBytes   920 Mbits/sec
[  4]  42.00-43.00  sec   109 MBytes   916 Mbits/sec
[  4]  43.00-44.00  sec   111 MBytes   934 Mbits/sec
[  4]  44.00-45.00  sec   109 MBytes   915 Mbits/sec
[  4]  45.00-46.00  sec   108 MBytes   906 Mbits/sec
[  4]  46.00-47.00  sec   109 MBytes   915 Mbits/sec
[  4]  47.00-48.00  sec   107 MBytes   899 Mbits/sec
[  4]  48.00-49.00  sec   109 MBytes   915 Mbits/sec
[  4]  49.00-50.00  sec   109 MBytes   917 Mbits/sec
[  4]  50.00-51.00  sec   106 MBytes   892 Mbits/sec
[  4]  51.00-52.00  sec   108 MBytes   902 Mbits/sec
[  4]  52.00-53.00  sec   110 MBytes   926 Mbits/sec
[  4]  53.00-54.00  sec   104 MBytes   873 Mbits/sec
[  4]  54.00-55.00  sec   110 MBytes   923 Mbits/sec
[  4]  55.00-56.00  sec   109 MBytes   911 Mbits/sec
[  4]  56.00-57.00  sec   110 MBytes   925 Mbits/sec
[  4]  57.00-58.00  sec   107 MBytes   898 Mbits/sec
[  4]  58.00-59.00  sec   107 MBytes   898 Mbits/sec
[  4]  59.00-60.00  sec   109 MBytes   913 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-60.00  sec  6.36 GBytes   910 Mbits/sec                  sender
[  4]   0.00-60.00  sec  6.36 GBytes   910 Mbits/sec                  receiver

```

### Receive

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   109 MBytes   918 Mbits/sec
[  4]   1.00-2.00   sec   109 MBytes   913 Mbits/sec
[  4]   2.00-3.00   sec   108 MBytes   906 Mbits/sec
[  4]   3.00-4.00   sec   110 MBytes   921 Mbits/sec
[  4]   4.00-5.00   sec   111 MBytes   929 Mbits/sec
[  4]   5.00-6.00   sec   108 MBytes   902 Mbits/sec
[  4]   6.00-7.00   sec   109 MBytes   914 Mbits/sec
[  4]   7.00-8.00   sec   106 MBytes   889 Mbits/sec
[  4]   8.00-9.00   sec   107 MBytes   898 Mbits/sec
[  4]   9.00-10.00  sec   110 MBytes   925 Mbits/sec
[  4]  10.00-11.00  sec   112 MBytes   937 Mbits/sec
[  4]  11.00-12.00  sec   110 MBytes   926 Mbits/sec
[  4]  12.00-13.00  sec   109 MBytes   913 Mbits/sec
[  4]  13.00-14.00  sec   110 MBytes   924 Mbits/sec
[  4]  14.00-15.00  sec   110 MBytes   923 Mbits/sec
[  4]  15.00-16.00  sec   110 MBytes   922 Mbits/sec
[  4]  16.00-17.00  sec   109 MBytes   915 Mbits/sec
[  4]  17.00-18.00  sec   108 MBytes   904 Mbits/sec
[  4]  18.00-19.00  sec   109 MBytes   916 Mbits/sec
[  4]  19.00-20.00  sec   110 MBytes   924 Mbits/sec
[  4]  20.00-21.00  sec   112 MBytes   937 Mbits/sec
[  4]  21.00-22.00  sec   109 MBytes   917 Mbits/sec
[  4]  22.00-23.00  sec   108 MBytes   902 Mbits/sec
[  4]  23.00-24.00  sec   108 MBytes   903 Mbits/sec
[  4]  24.00-25.00  sec   106 MBytes   892 Mbits/sec
[  4]  25.00-26.00  sec   112 MBytes   936 Mbits/sec
[  4]  26.00-27.00  sec   112 MBytes   938 Mbits/sec
[  4]  27.00-28.00  sec   109 MBytes   918 Mbits/sec
[  4]  28.00-29.00  sec   110 MBytes   923 Mbits/sec
[  4]  29.00-30.00  sec   108 MBytes   907 Mbits/sec
[  4]  30.00-31.00  sec   110 MBytes   921 Mbits/sec
[  4]  31.00-32.00  sec   109 MBytes   918 Mbits/sec
[  4]  32.00-33.00  sec   110 MBytes   921 Mbits/sec
[  4]  33.00-34.00  sec   109 MBytes   914 Mbits/sec
[  4]  34.00-35.00  sec   109 MBytes   915 Mbits/sec
[  4]  35.00-36.00  sec   111 MBytes   928 Mbits/sec
[  4]  36.00-37.00  sec   109 MBytes   914 Mbits/sec
[  4]  37.00-38.00  sec   110 MBytes   925 Mbits/sec
[  4]  38.00-39.00  sec   111 MBytes   928 Mbits/sec
[  4]  39.00-40.00  sec   107 MBytes   897 Mbits/sec
[  4]  40.00-41.00  sec   109 MBytes   916 Mbits/sec
[  4]  41.00-42.00  sec   110 MBytes   919 Mbits/sec
[  4]  42.00-43.00  sec   109 MBytes   913 Mbits/sec
[  4]  43.00-44.00  sec   111 MBytes   928 Mbits/sec
[  4]  44.00-45.00  sec   107 MBytes   898 Mbits/sec
[  4]  45.00-46.00  sec   110 MBytes   921 Mbits/sec
[  4]  46.00-47.00  sec   109 MBytes   918 Mbits/sec
[  4]  47.00-48.00  sec   111 MBytes   929 Mbits/sec
[  4]  48.00-49.00  sec   108 MBytes   903 Mbits/sec
[  4]  49.00-50.00  sec   110 MBytes   919 Mbits/sec
[  4]  50.00-51.00  sec   110 MBytes   923 Mbits/sec
[  4]  51.00-52.00  sec   110 MBytes   921 Mbits/sec
[  4]  52.00-53.00  sec   109 MBytes   910 Mbits/sec
[  4]  53.00-54.00  sec   109 MBytes   918 Mbits/sec
[  4]  54.00-55.00  sec   108 MBytes   906 Mbits/sec
[  4]  55.00-56.00  sec   108 MBytes   906 Mbits/sec
[  4]  56.00-57.00  sec   108 MBytes   906 Mbits/sec
[  4]  57.00-58.00  sec   108 MBytes   910 Mbits/sec
[  4]  58.00-59.00  sec   110 MBytes   926 Mbits/sec
[  4]  59.00-60.00  sec   107 MBytes   901 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-60.00  sec  6.40 GBytes   916 Mbits/sec    0             sender
[  4]   0.00-60.00  sec  6.40 GBytes   916 Mbits/sec                  receiver
```

## Docker MTU 1440

### Send

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   111 MBytes   932 Mbits/sec
[  4]   1.00-2.00   sec   111 MBytes   933 Mbits/sec
[  4]   2.00-3.00   sec   110 MBytes   925 Mbits/sec
[  4]   3.00-4.00   sec   109 MBytes   917 Mbits/sec
[  4]   4.00-5.00   sec   111 MBytes   930 Mbits/sec
[  4]   5.00-6.00   sec   112 MBytes   945 Mbits/sec
[  4]   6.00-7.00   sec   112 MBytes   938 Mbits/sec
[  4]   7.00-8.00   sec   112 MBytes   936 Mbits/sec
[  4]   8.00-9.00   sec   112 MBytes   943 Mbits/sec
[  4]   9.00-10.01  sec   111 MBytes   923 Mbits/sec
[  4]  10.01-11.00  sec   112 MBytes   942 Mbits/sec
[  4]  11.00-12.00  sec   112 MBytes   937 Mbits/sec
[  4]  12.00-13.00  sec   112 MBytes   940 Mbits/sec
[  4]  13.00-14.00  sec   112 MBytes   939 Mbits/sec
[  4]  14.00-15.00  sec   111 MBytes   933 Mbits/sec
[  4]  15.00-16.00  sec   112 MBytes   939 Mbits/sec
[  4]  16.00-17.00  sec   112 MBytes   941 Mbits/sec
[  4]  17.00-18.00  sec   108 MBytes   909 Mbits/sec
[  4]  18.00-19.00  sec   111 MBytes   933 Mbits/sec
[  4]  19.00-20.00  sec   112 MBytes   937 Mbits/sec
[  4]  20.00-21.00  sec   112 MBytes   935 Mbits/sec
[  4]  21.00-22.00  sec   112 MBytes   942 Mbits/sec
[  4]  22.00-23.00  sec   110 MBytes   927 Mbits/sec
[  4]  23.00-24.00  sec   110 MBytes   925 Mbits/sec
[  4]  24.00-25.00  sec   111 MBytes   935 Mbits/sec
[  4]  25.00-26.00  sec   113 MBytes   944 Mbits/sec
[  4]  26.00-27.00  sec   112 MBytes   940 Mbits/sec
[  4]  27.00-28.00  sec   113 MBytes   946 Mbits/sec
[  4]  28.00-29.00  sec   113 MBytes   947 Mbits/sec
[  4]  29.00-30.00  sec   111 MBytes   930 Mbits/sec
[  4]  30.00-31.00  sec   111 MBytes   929 Mbits/sec
[  4]  31.00-32.00  sec   112 MBytes   942 Mbits/sec
[  4]  32.00-33.00  sec   113 MBytes   944 Mbits/sec
[  4]  33.00-34.00  sec   109 MBytes   918 Mbits/sec
[  4]  34.00-35.00  sec   111 MBytes   934 Mbits/sec
[  4]  35.00-36.00  sec   111 MBytes   933 Mbits/sec
[  4]  36.00-37.00  sec   112 MBytes   940 Mbits/sec
[  4]  37.00-38.00  sec   113 MBytes   945 Mbits/sec
[  4]  38.00-39.00  sec   111 MBytes   933 Mbits/sec
[  4]  39.00-40.00  sec   111 MBytes   932 Mbits/sec
[  4]  40.00-41.00  sec   111 MBytes   929 Mbits/sec
[  4]  41.00-42.00  sec   112 MBytes   942 Mbits/sec
[  4]  42.00-43.00  sec   112 MBytes   935 Mbits/sec
[  4]  43.00-44.00  sec   112 MBytes   945 Mbits/sec
[  4]  44.00-45.00  sec   111 MBytes   932 Mbits/sec
[  4]  45.00-46.00  sec   113 MBytes   945 Mbits/sec
[  4]  46.00-47.00  sec   112 MBytes   937 Mbits/sec
[  4]  47.00-48.00  sec   110 MBytes   920 Mbits/sec
[  4]  48.00-49.00  sec   112 MBytes   944 Mbits/sec
[  4]  49.00-50.00  sec   109 MBytes   913 Mbits/sec
[  4]  50.00-51.00  sec   111 MBytes   933 Mbits/sec
[  4]  51.00-52.00  sec   112 MBytes   940 Mbits/sec
[  4]  52.00-53.00  sec   112 MBytes   939 Mbits/sec
[  4]  53.00-54.00  sec   111 MBytes   932 Mbits/sec
[  4]  54.00-55.00  sec   110 MBytes   925 Mbits/sec
[  4]  55.00-56.00  sec   110 MBytes   926 Mbits/sec
[  4]  56.00-57.00  sec   111 MBytes   930 Mbits/sec
[  4]  57.00-58.00  sec   111 MBytes   933 Mbits/sec
[  4]  58.00-59.00  sec   112 MBytes   941 Mbits/sec
[  4]  59.00-60.00  sec   113 MBytes   944 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-60.00  sec  6.53 GBytes   935 Mbits/sec                  sender
[  4]   0.00-60.00  sec  6.53 GBytes   935 Mbits/sec                  receiver

```

### Receive

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   108 MBytes   908 Mbits/sec
[  4]   1.00-2.00   sec   109 MBytes   911 Mbits/sec
[  4]   2.00-3.00   sec   111 MBytes   934 Mbits/sec
[  4]   3.00-4.00   sec   112 MBytes   944 Mbits/sec
[  4]   4.00-5.00   sec   107 MBytes   899 Mbits/sec
[  4]   5.00-6.00   sec   110 MBytes   924 Mbits/sec
[  4]   6.00-7.00   sec   111 MBytes   932 Mbits/sec
[  4]   7.00-8.00   sec   113 MBytes   944 Mbits/sec
[  4]   8.00-9.00   sec   112 MBytes   944 Mbits/sec
[  4]   9.00-10.00  sec   113 MBytes   944 Mbits/sec
[  4]  10.00-11.00  sec   110 MBytes   923 Mbits/sec
[  4]  11.00-12.00  sec   112 MBytes   938 Mbits/sec
[  4]  12.00-13.00  sec   109 MBytes   913 Mbits/sec
[  4]  13.00-14.00  sec   112 MBytes   940 Mbits/sec
[  4]  14.00-15.00  sec   112 MBytes   939 Mbits/sec
[  4]  15.00-16.00  sec   112 MBytes   935 Mbits/sec
[  4]  16.00-17.00  sec   112 MBytes   943 Mbits/sec
[  4]  17.00-18.01  sec   111 MBytes   920 Mbits/sec
[  4]  18.01-19.00  sec   108 MBytes   916 Mbits/sec
[  4]  19.00-20.00  sec   111 MBytes   931 Mbits/sec
[  4]  20.00-21.00  sec   109 MBytes   916 Mbits/sec
[  4]  21.00-22.00  sec   111 MBytes   930 Mbits/sec
[  4]  22.00-23.00  sec   110 MBytes   926 Mbits/sec
[  4]  23.00-24.00  sec   111 MBytes   935 Mbits/sec
[  4]  24.00-25.00  sec   111 MBytes   929 Mbits/sec
[  4]  25.00-26.00  sec   111 MBytes   935 Mbits/sec
[  4]  26.00-27.00  sec   112 MBytes   937 Mbits/sec
[  4]  27.00-28.00  sec   112 MBytes   938 Mbits/sec
[  4]  28.00-29.00  sec   110 MBytes   926 Mbits/sec
[  4]  29.00-30.00  sec   112 MBytes   936 Mbits/sec
[  4]  30.00-31.00  sec   111 MBytes   933 Mbits/sec
[  4]  31.00-32.00  sec   111 MBytes   929 Mbits/sec
[  4]  32.00-33.00  sec   110 MBytes   925 Mbits/sec
[  4]  33.00-34.00  sec   112 MBytes   941 Mbits/sec
[  4]  34.00-35.00  sec   112 MBytes   942 Mbits/sec
[  4]  35.00-36.00  sec   111 MBytes   932 Mbits/sec
[  4]  36.00-37.00  sec   112 MBytes   940 Mbits/sec
[  4]  37.00-38.00  sec   112 MBytes   937 Mbits/sec
[  4]  38.00-39.00  sec   112 MBytes   939 Mbits/sec
[  4]  39.00-40.00  sec   112 MBytes   938 Mbits/sec
[  4]  40.00-41.00  sec   110 MBytes   924 Mbits/sec
[  4]  41.00-42.00  sec   112 MBytes   939 Mbits/sec
[  4]  42.00-43.00  sec   112 MBytes   940 Mbits/sec
[  4]  43.00-44.00  sec   112 MBytes   940 Mbits/sec
[  4]  44.00-45.00  sec   112 MBytes   936 Mbits/sec
[  4]  45.00-46.00  sec   110 MBytes   925 Mbits/sec
[  4]  46.00-47.00  sec   112 MBytes   937 Mbits/sec
[  4]  47.00-48.00  sec   111 MBytes   928 Mbits/sec
[  4]  48.00-49.00  sec   109 MBytes   918 Mbits/sec
[  4]  49.00-50.00  sec   112 MBytes   943 Mbits/sec
[  4]  50.00-51.00  sec   111 MBytes   933 Mbits/sec
[  4]  51.00-52.00  sec   111 MBytes   931 Mbits/sec
[  4]  52.00-53.00  sec   111 MBytes   929 Mbits/sec
[  4]  53.00-54.00  sec   111 MBytes   931 Mbits/sec
[  4]  54.00-55.00  sec   113 MBytes   944 Mbits/sec
[  4]  55.00-56.00  sec   111 MBytes   933 Mbits/sec
[  4]  56.00-57.00  sec   111 MBytes   930 Mbits/sec
[  4]  57.00-58.00  sec   112 MBytes   942 Mbits/sec
[  4]  58.00-59.00  sec   111 MBytes   935 Mbits/sec
[  4]  59.00-60.00  sec   112 MBytes   938 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-60.00  sec  6.51 GBytes   932 Mbits/sec    0             sender
[  4]   0.00-60.00  sec  6.51 GBytes   932 Mbits/sec                  receiver
```

## Docker MTU 1450

### Send

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   106 MBytes   891 Mbits/sec
[  4]   1.00-2.00   sec   108 MBytes   906 Mbits/sec
[  4]   2.00-3.00   sec   112 MBytes   940 Mbits/sec
[  4]   3.00-4.00   sec   111 MBytes   931 Mbits/sec
[  4]   4.00-5.00   sec   112 MBytes   940 Mbits/sec
[  4]   5.00-6.00   sec   110 MBytes   923 Mbits/sec
[  4]   6.00-7.00   sec   111 MBytes   930 Mbits/sec
[  4]   7.00-8.00   sec   110 MBytes   925 Mbits/sec
[  4]   8.00-9.00   sec   110 MBytes   920 Mbits/sec
[  4]   9.00-10.00  sec   111 MBytes   933 Mbits/sec
[  4]  10.00-11.00  sec   111 MBytes   932 Mbits/sec
[  4]  11.00-12.00  sec   108 MBytes   905 Mbits/sec
[  4]  12.00-13.00  sec   110 MBytes   924 Mbits/sec
[  4]  13.00-14.00  sec   111 MBytes   932 Mbits/sec
[  4]  14.00-15.00  sec   110 MBytes   920 Mbits/sec
[  4]  15.00-16.00  sec   107 MBytes   894 Mbits/sec
[  4]  16.00-17.00  sec   106 MBytes   890 Mbits/sec
[  4]  17.00-18.00  sec   109 MBytes   918 Mbits/sec
[  4]  18.00-19.00  sec   108 MBytes   909 Mbits/sec
[  4]  19.00-20.00  sec   110 MBytes   926 Mbits/sec
[  4]  20.00-21.00  sec   107 MBytes   900 Mbits/sec
[  4]  21.00-22.00  sec   108 MBytes   906 Mbits/sec
[  4]  22.00-23.00  sec   110 MBytes   924 Mbits/sec
[  4]  23.00-24.00  sec   107 MBytes   901 Mbits/sec
[  4]  24.00-25.00  sec   110 MBytes   922 Mbits/sec
[  4]  25.00-26.00  sec   111 MBytes   932 Mbits/sec
[  4]  26.00-27.00  sec   110 MBytes   924 Mbits/sec
[  4]  27.00-28.00  sec   110 MBytes   926 Mbits/sec
[  4]  28.00-29.01  sec   109 MBytes   911 Mbits/sec
[  4]  29.01-30.00  sec   110 MBytes   929 Mbits/sec
[  4]  30.00-31.00  sec   112 MBytes   936 Mbits/sec
[  4]  31.00-32.00  sec   108 MBytes   903 Mbits/sec
[  4]  32.00-33.00  sec   111 MBytes   934 Mbits/sec
[  4]  33.00-34.00  sec   108 MBytes   905 Mbits/sec
[  4]  34.00-35.00  sec   110 MBytes   925 Mbits/sec
[  4]  35.00-36.00  sec   112 MBytes   935 Mbits/sec
[  4]  36.00-37.00  sec   104 MBytes   872 Mbits/sec
[  4]  37.00-38.00  sec   102 MBytes   854 Mbits/sec
[  4]  38.00-39.00  sec   105 MBytes   884 Mbits/sec
[  4]  39.00-40.00  sec   111 MBytes   928 Mbits/sec
[  4]  40.00-41.00  sec   108 MBytes   909 Mbits/sec
[  4]  41.00-42.00  sec  96.9 MBytes   812 Mbits/sec
[  4]  42.00-43.00  sec   111 MBytes   930 Mbits/sec
[  4]  43.00-44.00  sec   102 MBytes   852 Mbits/sec
[  4]  44.00-45.00  sec   110 MBytes   924 Mbits/sec
[  4]  45.00-46.00  sec   108 MBytes   908 Mbits/sec
[  4]  46.00-47.00  sec   108 MBytes   904 Mbits/sec
[  4]  47.00-48.00  sec   106 MBytes   888 Mbits/sec
[  4]  48.00-49.00  sec   108 MBytes   906 Mbits/sec
[  4]  49.00-50.00  sec   107 MBytes   894 Mbits/sec
[  4]  50.00-51.00  sec   106 MBytes   892 Mbits/sec
[  4]  51.00-52.00  sec   109 MBytes   917 Mbits/sec
[  4]  52.00-53.00  sec   108 MBytes   905 Mbits/sec
[  4]  53.00-54.00  sec   111 MBytes   931 Mbits/sec
[  4]  54.00-55.00  sec   106 MBytes   893 Mbits/sec
[  4]  55.00-56.00  sec   107 MBytes   894 Mbits/sec
[  4]  56.00-57.00  sec   105 MBytes   882 Mbits/sec
[  4]  57.00-58.00  sec   110 MBytes   919 Mbits/sec
[  4]  58.00-59.00  sec   103 MBytes   862 Mbits/sec
[  4]  59.00-60.00  sec   108 MBytes   909 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-60.00  sec  6.35 GBytes   910 Mbits/sec                  sender
[  4]   0.00-60.00  sec  6.35 GBytes   910 Mbits/sec                  receiver

```

### Receive

```shell
[ ID] Interval           Transfer     Bandwidth
[  4]   0.00-1.00   sec   106 MBytes   891 Mbits/sec
[  4]   1.00-2.00   sec   106 MBytes   889 Mbits/sec
[  4]   2.00-3.00   sec   111 MBytes   931 Mbits/sec
[  4]   3.00-4.00   sec   111 MBytes   928 Mbits/sec
[  4]   4.00-5.00   sec   108 MBytes   903 Mbits/sec
[  4]   5.00-6.00   sec   109 MBytes   912 Mbits/sec
[  4]   6.00-7.00   sec   111 MBytes   928 Mbits/sec
[  4]   7.00-8.00   sec   109 MBytes   917 Mbits/sec
[  4]   8.00-9.00   sec   109 MBytes   911 Mbits/sec
[  4]   9.00-10.00  sec   109 MBytes   916 Mbits/sec
[  4]  10.00-11.00  sec   111 MBytes   931 Mbits/sec
[  4]  11.00-12.00  sec   110 MBytes   925 Mbits/sec
[  4]  12.00-13.00  sec   111 MBytes   930 Mbits/sec
[  4]  13.00-14.00  sec   111 MBytes   933 Mbits/sec
[  4]  14.00-15.00  sec   110 MBytes   925 Mbits/sec
[  4]  15.00-16.00  sec   109 MBytes   918 Mbits/sec
[  4]  16.00-17.00  sec   110 MBytes   924 Mbits/sec
[  4]  17.00-18.00  sec   111 MBytes   932 Mbits/sec
[  4]  18.00-19.00  sec   109 MBytes   915 Mbits/sec
[  4]  19.00-20.00  sec   106 MBytes   889 Mbits/sec
[  4]  20.00-21.00  sec   106 MBytes   892 Mbits/sec
[  4]  21.00-22.00  sec   107 MBytes   897 Mbits/sec
[  4]  22.00-23.00  sec   110 MBytes   923 Mbits/sec
[  4]  23.00-24.00  sec   111 MBytes   933 Mbits/sec
[  4]  24.00-25.00  sec   111 MBytes   928 Mbits/sec
[  4]  25.00-26.00  sec   109 MBytes   915 Mbits/sec
[  4]  26.00-27.00  sec   109 MBytes   913 Mbits/sec
[  4]  27.00-28.00  sec   104 MBytes   871 Mbits/sec
[  4]  28.00-29.00  sec   110 MBytes   923 Mbits/sec
[  4]  29.00-30.00  sec   107 MBytes   898 Mbits/sec
[  4]  30.00-31.00  sec   110 MBytes   919 Mbits/sec
[  4]  31.00-32.00  sec   108 MBytes   909 Mbits/sec
[  4]  32.00-33.00  sec   107 MBytes   899 Mbits/sec
[  4]  33.00-34.00  sec   110 MBytes   925 Mbits/sec
[  4]  34.00-35.00  sec   110 MBytes   925 Mbits/sec
[  4]  35.00-36.00  sec   109 MBytes   914 Mbits/sec
[  4]  36.00-37.00  sec   109 MBytes   912 Mbits/sec
[  4]  37.00-38.00  sec   110 MBytes   927 Mbits/sec
[  4]  38.00-39.00  sec   109 MBytes   913 Mbits/sec
[  4]  39.00-40.00  sec   108 MBytes   912 Mbits/sec
[  4]  40.00-41.00  sec   109 MBytes   915 Mbits/sec
[  4]  41.00-42.00  sec   110 MBytes   925 Mbits/sec
[  4]  42.00-43.00  sec   109 MBytes   914 Mbits/sec
[  4]  43.00-44.00  sec   109 MBytes   918 Mbits/sec
[  4]  44.00-45.00  sec   105 MBytes   875 Mbits/sec
[  4]  45.00-46.00  sec   109 MBytes   913 Mbits/sec
[  4]  46.00-47.00  sec   110 MBytes   919 Mbits/sec
[  4]  47.00-48.00  sec   107 MBytes   896 Mbits/sec
[  4]  48.00-49.00  sec   109 MBytes   913 Mbits/sec
[  4]  49.00-50.00  sec   108 MBytes   905 Mbits/sec
[  4]  50.00-51.00  sec   107 MBytes   896 Mbits/sec
[  4]  51.00-52.00  sec   109 MBytes   914 Mbits/sec
[  4]  52.00-53.00  sec   110 MBytes   923 Mbits/sec
[  4]  53.00-54.00  sec   108 MBytes   907 Mbits/sec
[  4]  54.00-55.00  sec   109 MBytes   912 Mbits/sec
[  4]  55.00-56.00  sec   110 MBytes   919 Mbits/sec
[  4]  56.00-57.00  sec   107 MBytes   900 Mbits/sec
[  4]  57.00-58.00  sec   108 MBytes   906 Mbits/sec
[  4]  58.00-59.00  sec   108 MBytes   908 Mbits/sec
[  4]  59.00-60.00  sec   107 MBytes   900 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-60.00  sec  6.38 GBytes   913 Mbits/sec    1             sender
[  4]   0.00-60.00  sec  6.38 GBytes   913 Mbits/sec                  receiver
```
