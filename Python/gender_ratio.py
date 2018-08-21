"""%male&female"""
import pandas as pd
import pygal
def malefemale():
    """raito"""
    total_male = pd.read_csv("../DATA Update/Male age/raw/Male Total Population.csv", encoding = "UTF-8")
    total_female = pd.read_csv("../DATA Update/Female Age/raw/Female Total Population.csv", encoding = "UTF-8")
    country = input()
    year = input()
    hav = False

    for i in range(len(total_male['Country Name'])):
        if total_male['Country Name'][i] == country:
            male_per = (total_male[year][i]*100)/(total_male[year][i]+total_female[year][i])
            female_per = (total_female[year][i]*100)/(total_male[year][i]+total_female[year][i])
            male = int(total_male[year][i])
            female = int(total_female[year][i])
            hav = True
            break
    if hav:
        print('Males :', male)
        print('Females :', female)
        print('Totals :', male+female)

        from pygal.style import NeonStyle
        NeonStyle = NeonStyle(
            colors=('#0000FF', '#FF0000')
            )
        pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=NeonStyle)
        pie_chart.value_formatter = lambda x: "{:,}".format(x)
        pie_chart.title = 'Males and Females (in %)'
        pie_chart.add('Males : {:,} People'.format(male), male_per)
        pie_chart.add('Females : {:,} People'.format(female), female_per)
        pie_chart.render_to_file('Graph SVG/gender_pie_chart.svg')
    else:
        print('not found')
malefemale()

