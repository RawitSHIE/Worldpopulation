"""
GDP for CN, TH, JP, USA
"""
import pandas as pd
import pygal

def gdp():
    gdp_sheet = pd.read_csv("../DATA/Total population.csv", encoding = "UTF-8")
    gdp_sheet.index = gdp_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, x_label_rotation=90)
    line_chart.title = 'Total Population of each year'
    line_chart.x_labels = map(str, range(1960, 2017, 4))
    line_chart.value_formatter = lambda x: "{:,} People".format(int(x))
    line_chart.add('China', gdp_sheet.loc["China"][4:62:4])
    line_chart.add('Thailand', gdp_sheet.loc["Thailand"][4:62:4])
    line_chart.add('Japan', gdp_sheet.loc["Japan"][4:62:4])
    line_chart.add('United States', gdp_sheet.loc["United States"][4:62:4])
    line_chart.render_to_file('Graph SVG/country_pop_all.svg')
gdp()
