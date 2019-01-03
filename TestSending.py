
from datadog import initialize


def read_properties(file):
    properties = {}
    for line in file:
        parts = line.split('=')
        if len(parts) > 1:
            properties[parts[0].strip()] = parts[1].strip()
    return properties


dd_props = read_properties(open('datadog.ini', 'r'))


options = {
    'api_key': dd_props['api_key'],
    'app_key': dd_props['app_key']
}


initialize(**options)


from datadog import statsd

statsd.histogram('kwyho.smile', 20, tags=["class0:1"])
statsd.histogram('kwyho.smile', 20, tags=["class1:1"])


from datadog import ThreadStats
stats = ThreadStats()
stats.start()
stats.increment('kwyho.laugh')