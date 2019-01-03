
import numpy as np
from datadog import initialize


def read_properties(file):
    properties = {}
    for line in file:
        parts = line.split('=')
        if len(parts) > 1:
            properties[parts[0].strip()] = parts[1].strip()
    return properties


dd_props = read_properties(open('personaldatadog.ini', 'r'))


options = {
    'api_key': dd_props['api_key'],
    'app_key': dd_props['app_key']
}


initialize(**options)


num = 100000
refdist = {'apple': 0.35, 'orange': 0.35, 'grape': 0.25, 'durian': 0.05}

from datadog import ThreadStats
stats = ThreadStats()
stats.start()
for _ in range(num):
    sampled_fruit = np.random.choice(list(refdist.keys()), p=list(refdist.values()))
    stats.increment('fruit.picked', 1, tags=['fruit:'+sampled_fruit])
