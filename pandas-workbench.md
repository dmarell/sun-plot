# My pandas workbench
```
df = pd.read_csv(r'sun_power_small.csv', parse_dates=['sampled'])
df['date'] = df['sampled'].dt.date

"""
>>> df.columns
Index(['sampled', 'solar_kw'], dtype='object')

>>> df['sampled'].min()
'2021-07-01 01:44:01.291000'

# Add columns:
>>> df['date'] = df['sampled'].dt.date
>>> df['time'] = df['sampled'].dt.time

>>> df.columns
Index(['sampled', 'solar_kw', 'date', 'time'], dtype='object')

>>> df.groupby(df['date'])['solar_kw'].mean()
date
2021-07-01    6.097505
2021-07-02    6.581586
2021-07-03    6.051809
2021-07-04    6.417115
2021-07-05    5.714314
Name: solar_kw, dtype: float64

>>> df.groupby([df['date'], df['sampled'].dt.hour])['solar_kw'].mean()
date        sampled
2021-07-01  1          0.000000
2          0.072585
3          0.343686
4          2.011563
5          3.439686
...   
2021-07-05  16         3.357324
17         2.704000
18         0.550753
19         0.036505
20         0.000000
Name: solar_kw, Length: 100, dtype: float64
>>> df.groupby([df['date'], df['sampled'].dt.hour, df['sampled'].dt.minute])['solar_kw'].mean()
date        sampled  sampled
2021-07-01  1        44         0.0
45         0.0
46         0.0
47         0.0
48         0.0
...
2021-07-05  20       8          0.0
9          0.0
10         0.0
11         0.0
12         0.0
Name: solar_kw, Length: 5746, dtype: float64
```
I think I like this output format directly from pandas:
```
dag  solar_kw per hour
365 [0,0,0,0.1,...5.0,...,0.1,0]
364 [0,0,0,0.1,...5.0,...,0.1,0]
363 [0,0,0,0.1,...5.0,...,0.1,0]
...
1   [0,0,0,0.1,...5.0,...,0.1,0]
```
But so far I've failed to find such a transformation in pandas.
An alternative I can see how it can happen is to grab an array per row/day and loop all days of the year:
```
>>> data = df.groupby([df['date'], df['sampled'].dt.hour])['solar_kw'].mean()
>>> data[date(2021,7,1)]
sampled
1      0.000000
2      0.072585
3      0.343686
4      2.011563
5      3.439686
6      3.639410
7      5.624913
8     11.259144
9     11.618750
10    12.706147
11    12.633722
12    12.488481
13    10.706402
14     9.349573
15     7.429144
16     5.670538
17     3.366337
18     1.596713
19     0.194500
20     0.000730
Name: solar_kw, dtype: float64
```