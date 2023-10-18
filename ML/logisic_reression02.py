import pandas as pd
df=pd.read_csv("./datasets/Titanic Passengers.csv")
print(df.columns)

#여:1 ,남:0
df['sex']=df['sex'].map({'female':1,'male':0})
print(df.head())

#null값을 평균으로
df['age'].fillna(value=df['age'].mean(),inplace=True)

#등실별 칼럼을 만들어 1 or 0 으로 만들기
df['firstClass']=df['pclass'].apply(lambda x: 1 if x==1 else 0)
df['secondClass']=df['pclass'].apply(lambda x: 1 if x==2 else 0)
df['thirdClass']=df['pclass'].apply(lambda x: 1 if x==3 else 0)
print(df.head())
x=df[['sex','age','firstClass','secondClass','thirdClass']]
y=df[['survived']]

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test =train_test_split(x,y,test_size=0.2)

from sklearn.preprocessing import StandardScaler
scaler =StandardScaler() # 스케일을 평균 0 표준편차가 1되도록 표준화

x_train =scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
model =LogisticRegression()
model.fit(x_train,y_train)
print(model.coef_) # 기울기
print(model.intercept_)# y절편
print('학습데이터 성능=>',model.score(x_train,y_train))
print('테스트데이터 성능=>',model.score(x_test,y_test))

import numpy as np
Jack=np.array([0.0,20.0,0.0,0.0,1.0])
Rose=np.array([1.0,17.0,1.0,0.0,0.0])
Nick=np.array([1.0,30.0,0.0,1.0,0.0])
Baby=np.array([1.0,5.0,0.0,1.0,0.0])
sample= np.array([Jack,Rose,Nick,Baby])
sample=scaler.transform(sample)
print(model.predict(sample))
print(model.predict_proba(sample))