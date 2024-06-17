import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

url = 'https://randomuser.me/api/?results=100'
response = requests.get(url, verify=False)
data = response.json()
df = pd.json_normalize(data['results'])

print('DATASET RANDOMUSERS')

print('COLUMNS USER')
print(df.columns)

print('INFO USER:')
print(df.info())

print('DESCRIPCIÓN DE EDAD')
ages = df['dob.age']
print(ages.describe())

print('ANÁLISIS DE DATOS')

minimo = ages.min()
print(f'Mínimo: {minimo}')

maximo = ages.max()
print(f'Máximo: {maximo}')

media = ages.mean()
print(f'Media: {media}')

mediana = ages.median()
print(f'Mediana: {mediana}')

moda = ages.mode()
if len(moda) > 0:
    moda = moda[0]
    print(f'Moda: {moda}')
else:
    print('No se puede calcular la moda porque no hay datos en el DataFrame.')

varianza = ages.var()
print(f'Varianza: {varianza:.2f}')

desviacion_estandar = ages.std()
print(f'Desviación Estándar: {desviacion_estandar:.2f}')

Q1 = ages.quantile(0.25)
Q2 = ages.quantile(0.50)
Q3 = ages.quantile(0.75)

print(f'Primer cuartil (Q1): {Q1}')
print(f'Segundo cuartil (Q2): {Q2}')
print(f'Tercer cuartil (Q3): {Q3}')

IQR = Q3 - Q1
print(f'Rango inter cuartil (IQR): {IQR}')

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f'Límite inferior para valores anómalos: {limite_inferior}')
print(f'Límite superior para valores anómalos: {limite_superior}')

ages.hist(bins=10, edgecolor='black')
plt.title('Histograma de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x=ages)

plt.title('Diagrama de Caja de Edades')
plt.xlabel('Edades')

plt.show()

nuevo_df = pd.DataFrame({'Edad': ages, 'Género': df['gender']})

nuevo_df['Género'] = nuevo_df['Género'].map({'male': 0, 'female': 1})

correlacion = nuevo_df.corr()

print('Matriz de correlación:')
print(correlacion)

plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Correlación')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Edad', y='Género', data=nuevo_df, hue='Género', palette='coolwarm')
plt.title('Gráfico de Dispersión de Edad vs. Género')
plt.xlabel('Edad')
plt.ylabel('Género')
plt.show()

rango_edades = np.max(df['dob.age']) - np.min(df['dob.age'])
print(f'Rango de las edades: {rango_edades}')

coef_variacion_edades = np.std(df['dob.age']) / np.mean(df['dob.age'])
print(f'Coeficiente de variación de las edades: {coef_variacion_edades:.2f}')

