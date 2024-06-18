import numpy as np

def print_array(name, array):
    print(f"{name}:\n {np.array2string(array, formatter={'float_kind':lambda x: '%.2f' % x})}\n")

vector = np.array([1, 2, 3])
print_array("Vector", vector)

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print_array("Matriz", matriz)

array_3d = np.random.rand(2, 3, 4)
print_array("Array 3D", array_3d)

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
suma_vectores = vector_a + vector_b
resta_vectores = vector_a - vector_b
producto_punto = np.dot(vector_a, vector_b)

print_array("Suma de vectores", suma_vectores)
print_array("Resta de vectores", resta_vectores)
print("Producto punto de vectores:", f"{producto_punto:.2f}")

matriz_a = np.random.rand(3, 3)
matriz_b = np.random.rand(3, 3)
suma_matrices = matriz_a + matriz_b
resta_matrices = matriz_a - matriz_b
producto_matrices = np.dot(matriz_a, matriz_b)
producto_elemento_a_elemento = matriz_a * matriz_b
transpuesta_a = matriz_a.T
inversa_a = np.linalg.inv(matriz_a)

print_array("Matriz A", matriz_a)
print_array("Matriz B", matriz_b)
print_array("Suma de matrices", suma_matrices)
print_array("Resta de matrices", resta_matrices)
print_array("Producto de matrices", producto_matrices)
print_array("Producto elemento a elemento de matrices", producto_elemento_a_elemento)
print_array("Transpuesta de la matriz A", transpuesta_a)
print_array("Inversa de la matriz A", inversa_a)

array_3d_a = np.random.rand(2, 3, 4)
array_3d_b = np.random.rand(2, 3, 4)
suma_arrays_3d = array_3d_a + array_3d_b
resta_arrays_3d = array_3d_a - array_3d_b
producto_arrays_3d = array_3d_a * array_3d_b

print_array("Array 3D A", array_3d_a)
print_array("Array 3D B", array_3d_b)
print_array("Suma de arrays 3D", suma_arrays_3d)
print_array("Resta de arrays 3D", resta_arrays_3d)
print_array("Producto de arrays 3D (elemento a elemento)", producto_arrays_3d)

