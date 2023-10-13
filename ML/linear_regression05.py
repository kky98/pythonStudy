from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
# 맨해튼 주택 임대료
df = pd.read_csv("./datasets/streeteasy/manhattan.csv")
print(df.describe())
print(df.shape)
print(df.columns)
print(df.info())
x = df[['bedrooms', 'bathrooms', 'size_sqft',
       'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
       'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
       'has_patio', 'has_gym']]
y = df[['rent']]

# 학습데이터와 테스트데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
print(x_train.shape)
model = LinearRegression()
model.fit(x_train, y_train)
print(model.coef_)      # 기울기
print(model.intercept_) # y절편

# 테스트 데이터로 예측
# 예측 rent 값과 실제 rent 값을 그래프로
y_predicted = model.predict(x_test)
import matplotlib.pyplot as plt
plt.scatter(y_test, y_predicted, alpha=0.4)
plt.xlabel("actual rent")
plt.ylabel("predicted rent")
plt.title("linear model")
plt.show()
# 모델 정확도 평가
print("테스트 데이터 정확도 : ",model.score(x_test, y_test))
print("학습 데이터 정확도 : ",model.score(x_train, y_train))