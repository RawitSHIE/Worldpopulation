"""
GDP for CN, TH, JP, USA
"""
import pandas as pd
import pygal

def gdp():
    gdp_sheet = pd.read_csv("..\DATA\gdp\gdp.csv", encoding = 'UTF-8')
    gdp_sheet.index = gdp_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle)
    line_chart.title = 'Gross Domestic Products (in %)'
    line_chart.x_labels = map(str, range(1961, 2017))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add('China', gdp_sheet.loc["China"][5:61])
    line_chart.add('Thailand', gdp_sheet.loc["Thailand"][5:61])
    line_chart.add('Japan', gdp_sheet.loc["Japan"][5:61])
    line_chart.add('United States', gdp_sheet.loc["United States"][5:61])
    line_chart.render_to_file('Graph SVG/gdp_line_chart.svg')
gdp()
