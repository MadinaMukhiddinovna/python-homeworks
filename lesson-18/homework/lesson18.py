import pandas as pd

df = pd.read_csv('C:\Users\user\Downloads\tackoverflow_qa.csv')

# 1. Questions created before 2014
q1 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']

# 2. Questions with a score more than 50
q2 = df[df['score'] > 50]

# 3. Questions with a score between 50 and 100
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Questions answered by Scott Boston
q4 = df[df['ans_name'] == 'Scott Boston']

# 5. Questions answered by 5 users 
users = ['Unutbu', 'Scott Boston', 'Mike Pennington', 'unutbu', 'jezrael']
q5 = df[df['ans_name'].isin(users)]

# 6. Questions from Mar to Oct 2014 answered by Unutbu and score < 5
df['creationdate'] = pd.to_datetime(df['creationdate'])
q6 = df[(df['creationdate'] >= '2014-03-01') & 
        (df['creationdate'] <= '2014-10-31') &
        (df['ans_name'] == 'Unutbu') &
        (df['score'] < 5)]

# 7. Score between 5–10 OR viewcount > 10000
q7 = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]

# 8. Questions NOT answered by Scott Boston
q8 = df[df['ans_name'] != 'Scott Boston']


#Titanic Dataset

titanic_df = pd.read_csv("C:\Users\user\Downloads\titanic.csv")

# 1. Female passengers in Class 1, aged 20–30
t1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                (titanic_df['Pclass'] == 1) & 
                (titanic_df['Age'] >= 20) & 
                (titanic_df['Age'] <= 30)]

# 2. Passengers who paid more than $100
t2 = titanic_df[titanic_df['Fare'] > 100]

# 3. Passengers who survived and were alone
t3 = titanic_df[(titanic_df['Survived'] == 1) & 
                (titanic_df['SibSp'] == 0) & 
                (titanic_df['Parch'] == 0)]

# 4. Embarked from 'C' and paid > $50
t4 = titanic_df[(titanic_df['Embarked'] == 'C') & 
                (titanic_df['Fare'] > 50)]

# 5. Passengers with both SibSp and Parch > 0
t5 = titanic_df[(titanic_df['SibSp'] > 0) & 
                (titanic_df['Parch'] > 0)]

# 6. Aged 15 or younger who didn't survive
t6 = titanic_df[(titanic_df['Age'] <= 15) & 
                (titanic_df['Survived'] == 0)]

# 7. With cabin info and fare > $200
t7 = titanic_df[titanic_df['Cabin'].notna() & 
                (titanic_df['Fare'] > 200)]

# 8. Odd-numbered Passenger IDs
t8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# 9. Passengers with unique ticket numbers
t9 = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]

# 10. Female passengers with 'Miss' in name and in Class 1
t10 = titanic_df[(titanic_df['Name'].str.contains('Miss')) & 
                 (titanic_df['Pclass'] == 1) & 
                 (titanic_df['Sex'] == 'female')]


