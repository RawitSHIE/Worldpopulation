import requests as rq
import pandas as pd

df_world = pd.read_csv('fixed index total.csv', encoding = "UTF-8")
df_world.index = df_world['Country Name']


for i in df_world['Country Code']:
    if len(i) == 2:
        r = rq.get('http://flags.fmcdn.net/data/flags/w580/{0}.png'.format(i))
        with open('country_flag/{0}.png'.format(i), 'wb') as f:
            f.write(r.content)


