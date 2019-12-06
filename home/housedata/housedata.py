import pandas as pd
from sklearn.model_selection import train_test_split#将矩阵随机划分为训练子集和测试子集
from sklearn.linear_model import LinearRegression#调用sklearn中的线性回归


data = pd.read_csv('media/csv/house_price.csv')
# print(data)
data1 = data.dropna()#处理缺失值
data2 = pd.get_dummies(data1[['dist','floor']])#返回处理后数据
data3 = data2.drop(['dist_shijingshan','floor_high'],axis=1)
data4 = pd.concat([data3,data1[['roomnum','halls','AREA','subway','school','price']]],axis=1)
X = data4.iloc[:,:-1]
y = data4.iloc[:,-1:]
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.3)
model = LinearRegression().fit(X_train,y_train)
# print(model.score(X_train,y_train))
# print(model.score(X_test,y_test))#打分
# cs = model.predict([[1,0,0,0,0,0,1,1,0,46.09,1,0]])[0][0]#测试数据
# print(cs)
