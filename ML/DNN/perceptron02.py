from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
x=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1] #and
#y=[0,1,1,1] #or
#y=[0,1,1,0] #xor

model = Perceptron(tol=1e-3,random_state=1)
model.fit(x,y)
print(model.predict(x))

m_model =MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=100,random_state=1)
m_model.fit(x,y)
m_model.predict(x)
