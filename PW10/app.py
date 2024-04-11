from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

# Завантаження датасету Iris
iris = load_iris()

# Створення DataFrame з даних та виведення перших рядків
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Розділення даних на навчальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Масштабування ознак
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# print("Test scaled:")
# print(X_test_scaled[:5])
# print("Train scaled:")
# print(X_train_scaled[:5])

# Тренування логістичної регресії
logistic_reg = LogisticRegression(max_iter=1000)
logistic_reg.fit(X_train_scaled, y_train)

# Тренування методу опорних векторів (SVM)
svm = SVC(kernel='linear')
svm.fit(X_train_scaled, y_train)

# Оцінка логістичної регресії
y_pred_logreg = logistic_reg.predict(X_test_scaled)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
print("Accuracy of Logistic Regression:", accuracy_logreg)

# Оцінка методу опорних векторів (SVM)
y_pred_svm = svm.predict(X_test_scaled)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy of SVM:", accuracy_svm)


