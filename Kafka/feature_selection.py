import pandas as pd
import country_converter as coco


def rename_15_16_columns (dt, year):
    dt.rename(columns={'Economy (GDP per Capita)': 'GDP_Per_Capita', 'Happiness Score' : 'Happiness_Score',
                       'Happiness Rank' : 'Happiness_Rank', 'Health (Life Expectancy)' : 'Healthy_Life_Expectancy',
                          'Trust (Government Corruption)' : 'Government_Corruption_Perception', 'Family' : 'Social_Support'}, inplace=True)
    dt['Year'] = year
    return dt[['Country', 'Happiness_Score', 'GDP_Per_Capita', 'Social_Support', 'Healthy_Life_Expectancy', 'Freedom','Government_Corruption_Perception', 'Generosity','Year']]

def rename_17_columns (dt, year):
    dt.rename(columns={'Happiness.Rank' : 'Happiness_Rank', 'Happiness.Score' : 'Happiness_Score',
                            'Economy..GDP.per.Capita.' : 'GDP_Per_Capita', 'Health..Life.Expectancy.' : 'Healthy_Life_Expectancy',
                            'Trust..Government.Corruption.' : 'Government_Corruption_Perception', 'Family' : 'Social_Support'}, inplace=True)
    dt['Year'] = year
    return dt[['Country', 'Happiness_Score', 'GDP_Per_Capita', 'Social_Support','Healthy_Life_Expectancy', 'Freedom','Government_Corruption_Perception', 'Generosity','Year']]


def rename_18_19_columns (dt, year):
    dt.rename(columns={'Country or region' : 'Country', 'Overall rank' : 'Happiness_Rank', 'Score' : 'Happiness_Score',
                       'GDP per capita' : 'GDP_Per_Capita', 'Healthy life expectancy' : 'Healthy_Life_Expectancy',
                       'Freedom to make life choices' : 'Freedom', 'Perceptions of corruption' : 'Government_Corruption_Perception', 'Social support' : 'Social_Support'}, inplace=True)
    dt['Year'] = year
    return dt[['Country', 'Happiness_Score', 'GDP_Per_Capita', 'Social_Support', 'Healthy_Life_Expectancy', 'Freedom','Government_Corruption_Perception', 'Generosity','Year']]

def get_continent (country):
    cc = coco.CountryConverter()
    try:
        return cc.convert(names=country, to='continent_7')
    except:
        return None

def get_continent_dummies (dt):
    return pd.get_dummies(dt, columns=['Continent'], prefix='Continent')

def rename_america (dt):
    dt.rename(columns={'Continent_North America' : 'Continent_North_America', 'Continent_South America' : 'Continent_South_America'}, inplace=True)
    return dt

def delete_columns (dt):
    return dt.drop(columns=['Country'], axis=1)






