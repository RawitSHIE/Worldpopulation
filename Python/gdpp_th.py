"""
GDP TH
"""
import pandas as pd
import pygal

def gdp():
    gdp_sheet = pd.read_csv("..\DATA\gdp\gdpp.csv", encoding = 'UTF-8')
    gdp_sheet.index = gdp_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'GDP per Capita (in USD)'
    line_chart.x_labels = map(str, range(1961, 2017))
    line_chart.value_formatter = lambda x: "%.2f" %x + "$"
    line_chart.add('Thailand', gdp_sheet.loc["Thailand"][5:61])
    line_chart.render_to_file('Graph SVG/gdpp_TH_line_chart.svg')
gdp()
