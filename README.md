# Prácticas de Python para análisis de datos

Este repositorio reúne ejercicios prácticos de Python relacionados con el análisis y la manipulación de datos. Incluye una práctica de operaciones numéricas con arreglos y matrices, y otra de exploración estadística y visualización de datos tabulares.

El contenido documentado aquí se basa en los ejercicios presentes en el repositorio; no se especifican el nombre ni el programa completo del curso.

## Contenido del repositorio

| Archivo | Descripción |
| --- | --- |
| [`practica_numpy.py`](practica_numpy.py) | Creación y visualización de vectores, matrices y arreglos tridimensionales con NumPy; operaciones aritméticas y de álgebra lineal. |
| [`practica_pandas.py`](practica_pandas.py) | Obtención de datos desde Random User Generator, normalización a un DataFrame, análisis descriptivo de edades y visualizaciones. |

## Stack y tecnologías

- **Python**: lenguaje de programación de los ejercicios.
- **NumPy**: arreglos multidimensionales, operaciones vectorizadas, generación de datos aleatorios y álgebra lineal.
- **Pandas**: carga y exploración de datos tabulares, normalización de JSON, selección de columnas y estadísticas descriptivas.
- **Requests**: consumo de una API HTTP para obtener registros de usuarios de ejemplo.
- **Matplotlib** y **Seaborn**: creación de histogramas, diagramas de caja, mapas de calor y gráficos de dispersión.
- **SciPy**: aparece importada en la práctica de Pandas (`scipy.stats`), aunque actualmente no se utiliza en los cálculos del ejercicio.

## Temas y funcionalidades practicadas

### NumPy: arreglos y operaciones numéricas

`practica_numpy.py` trabaja con estructuras de distintas dimensiones:

- Construcción de un vector y una matriz a partir de listas.
- Generación de arreglos tridimensionales con valores aleatorios.
- Formateo de arreglos para imprimir sus valores con dos decimales.
- Suma y resta de vectores y matrices.
- Producto punto entre vectores.
- Producto matricial y producto elemento a elemento.
- Transposición e inversión de una matriz mediante `numpy.linalg`.
- Operaciones elemento a elemento con arreglos tridimensionales.

Las matrices y los arreglos tridimensionales aleatorios se generan nuevamente en cada ejecución, por lo que sus resultados cambian.

### Pandas: datos y estadística descriptiva

`practica_pandas.py` solicita 100 registros a la API de [Random User Generator](https://randomuser.me/), convierte la respuesta JSON en un DataFrame y explora los datos. El análisis se centra en la edad (`dob.age`) e incluye:

- Inspección de nombres de columnas e información general del DataFrame.
- Resumen descriptivo, mínimo, máximo, media, mediana y moda.
- Varianza y desviación estándar.
- Cuartiles, rango intercuartílico (IQR) y límites para identificar posibles valores atípicos.
- Rango y coeficiente de variación de las edades.
- Creación de un DataFrame reducido con edad y género.
- Conversión de las categorías de género a valores numéricos para calcular y visualizar una matriz de correlación.

### Visualización

La práctica de Pandas muestra cuatro gráficos con Matplotlib y Seaborn:

1. Histograma de edades.
2. Diagrama de caja de edades.
3. Mapa de calor de la matriz de correlación de edad y género codificado.
4. Gráfico de dispersión de edad frente a género codificado.

Los gráficos se abren en ventanas interactivas mediante `plt.show()`.

## Requisitos

- Python 3.
- Conexión a Internet para ejecutar `practica_pandas.py` y consultar la API.
- Los paquetes de Python importados por las prácticas: `numpy`, `pandas`, `requests`, `matplotlib`, `seaborn` y `scipy`.

Instala las dependencias con pip:

```bash
python -m pip install numpy pandas requests matplotlib seaborn scipy
```

## Cómo ejecutar

Desde la carpeta del repositorio:

```bash
python practica_numpy.py
```

```bash
python practica_pandas.py
```

La primera práctica imprime resultados en la terminal. La segunda imprime estadísticas y abre las ventanas de gráficos; necesita acceso a Internet para recuperar los datos de la API. Si se ejecuta en un entorno sin interfaz gráfica, puede ser necesario configurar Matplotlib para guardar las figuras en archivos en lugar de mostrarlas.

## Consideraciones

- Los datos de Random User Generator son de ejemplo y pueden variar entre ejecuciones.
- La práctica realiza la solicitud HTTP sin manejo explícito de errores de conexión o de respuesta de la API.
- En `practica_pandas.py`, `requests.get` usa `verify=False`, lo que desactiva la verificación del certificado TLS. Es una configuración insegura para uso real; para aplicaciones habituales se debe mantener habilitada la verificación (`verify=True`, valor predeterminado de Requests).
- El género es una variable categórica codificada como `0` y `1` únicamente para el ejercicio de correlación y visualización. Esa codificación no convierte la categoría en una medida continua ni implica por sí sola una relación estadística significativa.
- La inversión de una matriz solo está definida si la matriz es invertible. En esta práctica, la matriz se genera aleatoriamente y el código no contempla el caso excepcional de una matriz singular.
