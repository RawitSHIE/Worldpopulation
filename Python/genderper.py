"""%male&female"""
import pandas as pd
import pygal

total_male = pd.read_csv("../DATA/Male/Male Total Population.csv", encoding = "UTF-8")
total_female = pd.read_csv("../DATA/Female/Female Total Population.csv", encoding = "UTF-8")
country = input()
year = input()
hav = 0

for i in range(len(total_male['Country Name'])):
    if total_male['Country Name'][i] == country:
        male_per = (total_male[year][i]*100)/(total_male[year][i]+total_female[year][i])
        female_per = (total_female[year][i]*100)/(total_male[year][i]+total_female[year][i])
        male = int(total_male[year][i])
        female = int(total_female[year][i])
        hav = 1
        break
if hav == 1:
	print('Males :', male)
	print('Females :', female)
	print('Totals :', male+female)

	from pygal.style import NeonStyle
	NeonStyle = NeonStyle(
		colors=('#0000FF', '#FF0000')
		)
	pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=NeonStyle)

	pie_chart.title = 'Males and Females (in %)'
	pie_chart.add('Males : {}'.format(male), male_per)
	pie_chart.add('Females : {}'.format(female), female_per)
	pie_chart.render_to_file('Graph SVG/gender_pie_chart.svg')
else:
	print('not found')
