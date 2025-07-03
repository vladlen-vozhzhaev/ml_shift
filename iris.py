from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
def get_user_data():
    print("Введите параметры цветка:")
    sepal_length = float(input("Длина чашелистика (см): "))
    sepal_width = float(input("Ширина чашелистика (см): "))
    petal_length = float(input("Длина лепестка (см): "))
    petal_width = float(input("Ширина лепестка (см): "))
    return [[sepal_length, sepal_width, petal_length, petal_width]]

# Загружаем датасет (каталог)
iris = load_iris()

X = iris.data # Массив признаков (150 признаков)
y = iris.target # Массив меток класса (0,1,2)

# Разделяем данные на тренировочные и тестовые
# test_size=0.3 - 30% данных пойдут в тестовую выборку
# random_state=42 - случайность разбиения для воспроизводимости
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Обучение модели
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))

predictions = model.predict(get_user_data())
class_name = iris.target_names[predictions]
print(class_name)

# # Преобразуем в DataFrame для удобного просмотра
# iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
#
# # Добавляем столбец с названиями классов
# iris_df['target'] = iris.target # Название!
# iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
#
# print('Первые 5 строк')
# print(iris_df.head())
#
# print("\nСтатистика по данным:")
# print(iris_df.describe())

