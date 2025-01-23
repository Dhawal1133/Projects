#Exploratory Data Analysis (EDA) 
#Titanic Dataset
#Problem statement - Predict Whether a passagner will survive or not

import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv(r'C:\Users\Dell\Documents\data science\train.csv')
test = pd.read_csv(r'C:\Users\Dell\Documents\data science\test.csv')
Gender = pd.read_csv(r'C:\Users\Dell\Documents\data science\gender_submission.csv')
print(train.head())
#print(train.shape)
#print(train.describe(include='all'))       #by incl all it shows both quantative as well as qualitative data
#print(train.info())
#print(train.isnull().sum())

##extracting menaingful info 

#survived people or dead people
""" def bar_plot(Feature):
    survived = train[train['Survived']==1][Feature].value_counts()
    print(survived)
    dead = train[train['Survived']==0][Feature].value_counts()
    print(dead)
    df = pd.DataFrame([survived, dead])
    df.index = ['Survived' , 'Dead']
    df.plot( kind='bar' , stacked='True' , figsize=(5,2))
    plt.show()
    print(df) """

""" bar_plot('Pclass')
bar_plot('Sex') """

## ML has two sets. Namely, train set(train our model) and test set(evaluate our model).

""" train_test= [train , test]              #combined to perform operations at same time on both sets
for data in train_test:
    data['Title'] = data['Name'].str.extract('([A-Za-z]+)\.') """
#print(train)
#print(test)
#print(train['Title'].unique())
#print(train['Title'].value_counts())

""" 
title_mapping = {'Mr' : 0 , 'Miss' : 1 , 'Mrs' : 2 , 'Master' : 3 , 'Dr' : 3}  #etc...     #ML cannot proceses str values therefore we replace it with numerical values
for data in train_test:
    data['Title'] = data['Title'].map(title_mapping)            ##Engineered new feature(Encoding)

print(train.head()) """

"""#Encode male and female as numbers
sex_mapping = {'male' : 0 ,'female' : 1}
for data in train_test:
    data['Sex'] = data['Sex'].map(sex_mapping)
print(train.head()) """

""" 
#print(train['Age'].isnull().sum())
#177 Nans. We need to fill it
a1 = train['Age'].fillna(train['Age'].mean())

#method 2
a1 = train.groupby('Title')['Age'].mean()


train['Age'] = train['Age'].fillna(train.groupby('Title')['Age'].transform('mean'))      #If Nan values are present. Tranform function will fill those accordance with the title
test['Age']= test['Age'].fillna(test.groupby('Title')['Age'].transform('mean'))      #If Nan values are present. Tranform function will fill those accordance with the title

print(train['Age'].isnull().sum()) """


""" print(train['Embarked'].isnull().sum())
print(train['Embarked'].value_counts())

train['Embarked'] = train['Embarked'].fillna('S')
test['Embarked'] = test['Embarked'].fillna('S')

print(train['Embarked'])
print(train['Embarked'].isnull().sum())

embarked_mapping = {'S': 0 , 'C': 1, 'Q': 2}
for data in train_test:
    data['Embarked']  = data['Embarked'].map(embarked_mapping)
print(train['Embarked'].head()) """



#FARE

#print(test['Fare'].isnull().sum())
""" a1 = train.groupby('Pclass')['Fare'].mean()
train['Fare'] = train['Fare'].fillna(train.groupby('Pclass')['Fare'].transform('mean'))
test['Fare'] = test['Fare'].fillna(test.groupby('Pclass')['Fare'].transform('mean'))
#print(train['Fare'])
print(test['Fare'].isnull().sum()) """

""" import seaborn as sns
facet = sns.FacetGrid(train, hue='Survived', aspect=4)
facet.map(sns.kdeplot , 'Fare')                            #probability density graph
facet.set(xlim=(0,train['Fare'].max()))
facet.add_legend()
plt.show() """

#SIbSp and Parch - siblings and parents columns
# we are combining both columns into  one family column

""" train['Family'] = train['SibSp'] +train['Parch']+1    #+1 to add yourself with family
test['Family'] = test['SibSp'] +test['Parch']+1    #+1 to add yourself with family
print(train['Family']) """


#print(train['Cabin'].isnull().sum())
#print(train['Cabin'].value_counts())

""" for data in train_test:
    data['Cabin'] = data['Cabin'].str[:1]
print(train['Cabin'].value_counts())
print(train['Cabin'].unique())

C1=train[train['Pclass']==1]['Cabin'].value_counts()
C2=train[train['Pclass']==2]['Cabin'].value_counts()         #nans filledaccordance with Pclass
C3=train[train['Pclass']==3]['Cabin'].value_counts()
print(C1, C2, C3) """






