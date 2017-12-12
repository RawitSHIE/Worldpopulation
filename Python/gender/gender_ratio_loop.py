"""%male&female"""
import pandas as pd
import pygal
def malefemale(country, year):
    """raito"""
    total_male = pd.read_csv("../../DATA/Male/Male Total Population.csv", encoding = "UTF-8")
    total_female = pd.read_csv("../../DATA/Female/Female Total Population.csv", encoding = "UTF-8")
    hav = False

    for i in range(len(total_male['Country Name'])):
        if total_male['Country Name'][i] == country:
            male_per = (total_male[year][i]*100)/(total_male[year][i]+total_female[year][i])
            female_per = (total_female[year][i]*100)/(total_male[year][i]+total_female[year][i])
            male = int(total_male[year][i])
            female = int(total_female[year][i])
            hav = True
            break
    
#---render graph ---#
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
        pie_chart.title = 'Males and Females (in %)({0} : {1} AD)'.format(country, year)
        pie_chart.add('Males : {:,} People'.format(male), male_per)
        pie_chart.add('Females : {:,} People'.format(female), female_per)
        pie_chart.render_to_file('../Graph SVG/gender_ratio/gender_ratio_{0}.svg'.format(year))
    else:
        print('not found')
def recur():
    country = input()
    for i in range(1960, 2017):
        malefemale(country, str(i))
        print(i)
recur()
