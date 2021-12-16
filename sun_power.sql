select
    sampled,
    cast(parameter_value as float) / 1000.0 as solar_kw
from
    data_sample,
    cast(parameter_value as float) value
where
    parameter_name = 'sma.power' and
    value >= 0.0 and value < 100000.0 and
    sampled > '2021-01-01' and sampled < '2021-12-31'
order by 1
