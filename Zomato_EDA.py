#zomato dataset analysis
#EDA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv(r'C:\Users\Dell\Documents\data science\zomato.csv')
""" print(df.head)
print(df.shape)
print(df.columns) """
#dropping unwanted columns
df = df.drop(['url','address','phone','menu_item','dish_liked','reviews_list'] , axis= 1)
#print(df.head())
#print(df.info())

#cleaning
#dropping duplicates
df.drop_duplicates(inplace=True)
#print(df.shape)
#Rate column
#print(df['rate'].unique())
#Removing "NEW" , "-" and "/5" from Rate Column
def handlerate(value):
    if(value=='NEW' or value=='-'):
        return np.nan
    else:
        value = str(value).split('/')
        value = value[0]
        return float(value)
    
df['rate'] = df['rate'].apply(handlerate)
#print(df['rate'].head())

#Filling Null Values in Rate Column with Mean

df['rate'].fillna(df['rate'].mean(), inplace = True)
#print(df['rate'].isnull().sum())

#rest_type

df.dropna(inplace = True)
(df.head())
#print(df['rest_type'].isnull().sum())

#rename
df.rename(columns = {'approx_cost(for two people)':'Cost2plates', 'listed_in(type)':'Type'}, inplace = True)

#locations
#print(df['location'].unique())
#print(df['listed_in(city)'].unique())
df = df.drop(['listed_in(city)'], axis = 1)
#print(df.head)

#cost2plates
print(df['Cost2plates'].unique())
def handle_comma(value):
    value = str(value)
    if ',' in value:
        value = value.replace(',' , '')
        return float(value)
    else:
        return float(value)

df['Cost2plates'] = df['Cost2plates'].apply(handle_comma)
#print(df['Cost2plates'].unique())

#print(df.head()) 
#rest_type
rest_types = df['rest_type'].value_counts(ascending=False)
#print(rest_types)
rest_types_lessthan1000 = rest_types[rest_types<1000]

#Making Rest Types less than 1000 in frequency as others
def handle_rest_type(value):
    if(value in rest_types_lessthan1000):
        return 'others'
    else:
        return value
        
df['rest_type'] = df['rest_type'].apply(handle_rest_type)
#print(df['rest_type'].value_counts())

#location
location = df['location'].value_counts(ascending  = False)

location_lessthan300 = location[location<300]



def handle_location(value):
    if(value in location_lessthan300):
        return 'others'
    else:
        return value
        
df['location'] = df['location'].apply(handle_location)
#print(df['location'].value_counts)

#cuisines
cuisines = df['cuisines'].value_counts(ascending  = False)


cuisines_lessthan100 = cuisines[cuisines<100]



def handle_cuisines(value):
    if(value in cuisines_lessthan100):
        return 'others'
    else:
        return value
        
df['cuisines'] = df['cuisines'].apply(handle_cuisines)
#print(df['cuisines'].value_counts())

#visualization
""" plt.figure(figsize=(16,10))
ax = sns.countplot(df['location'])
plt.xticks(rotation=90)
plt.show() """


""" plt.figure(figsize = (6,6))
sns.countplot(df['online_order'], palette = 'inferno')
plt.show() """

""" plt.figure(figsize = (6,6))
sns.countplot(df['book_table'], palette = 'rainbow')
plt.show() """

#visualizing Online Order vs Rate
""" plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)
plt.show() """

#visualizing book table vs Rat

""" plt.figure(figsize = (6,6))
sns.boxplot(x = 'book_table', y = 'rate', data = df)
plt.show() """

#Visualizing Online Order Facility, Location Wise
""" df1 = df.groupby(['location','online_order'])['name'].count()
df1.to_csv('location_online.csv')
df1 = pd.read_csv('location_online.csv')
df1 = pd.pivot_table(df1, values=None, index=['location'], columns=['online_order'], fill_value=0, aggfunc=np.sum)
print(df1)
df1.plot(kind = 'bar', figsize = (15,8))
plt.show() """

#types of restraunts vs rate
""" plt.figure(figsize=(16,6))
sns.boxplot(x='Type' , y='rate', data=df )
plt.show() """

#Grouping Types of Restaurents, location wise
""" df3 = df.groupby(['location','Type'])['name'].count()
df3.to_csv('location_Type.csv')
df3 = pd.read_csv('location_Type.csv')
df3 = pd.pivot_table(df3, values=None, index=['location'], columns=['Type'], fill_value=0, aggfunc=np.sum)
print(df3)
df3.plot(kind = 'bar', figsize = (36,8))
plt.show() """

#Visualizing Top Cuisines
df6 = df[['cuisines', 'votes']]
df6.drop_duplicates()
df7 = df6.groupby(['cuisines'])['votes'].sum()
df7 = df7.to_frame()
df7 = df7.sort_values('votes', ascending=False)
df7 = df7.iloc[1:]
print(df7.head())
df7.plot(kind='bar' , figsize = (16,6))
plt.show()
