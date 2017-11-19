"""
GDP for CN, TH, JP, USA
"""
import pandas as pd
import pygal
from pygal.style import NeonStyle
def gdp():
    gdp_sheet = pd.read_csv("..\DATA\gdp\gdp.csv", encoding = 'UTF-8')
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle)
    line_chart.title = 'GDP (in %)'
    line_chart.x_labels = map(str, range(1961, 2017))
    line_chart.add('China', gdp_sheet.loc[38][5:61])
    line_chart.add('Thailand', gdp_sheet.loc[231][5:61])
    line_chart.add('Japan', gdp_sheet.loc[117][5:61])
    line_chart.add('United States', gdp_sheet.loc[249][5:61])
    line_chart.render_to_file('Graph SVG/gdp_line_chart.svg')
gdp()