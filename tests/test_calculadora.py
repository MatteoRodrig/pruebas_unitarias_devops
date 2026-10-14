"""
Pruebas unitarias para el módulo calculadora.
Estructura AAA: Arrange, Act, Assert.
"""
import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)

# ==================== SUMAR ====================
def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_sumar_negativos():
    # Arrange
    a, b = -3, -7
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == -10

def test_sumar_cero():
    # Arrange
    a, b = 0, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 5

# ==================== RESTAR ====================
def test_restar_positivos():
    # Arrange
    a, b = 10, 3
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 7

def test_restar_resultado_negativo():
    # Arrange
    a, b = 3, 10
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -7

# ==================== MULTIPLICAR ====================
def test_multiplicar_positivos():
    # Arrange
    a, b = 4, 6
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 24

def test_multiplicar_por_cero():
    # Arrange
    a, b = 5, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0

# ==================== DIVIDIR ====================
def test_dividir_positivos():
    # Arrange
    a, b = 10, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 5

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

# ==================== POTENCIA ====================
def test_potencia_positiva():
    # Arrange
    base, exp = 2, 3
    # Act
    resultado = potencia(base, exp)
    # Assert
    assert resultado == 8

def test_potencia_exponente_cero():
    # Arrange
    base, exp = 5, 0
    # Act
    resultado = potencia(base, exp)
    # Assert
    assert resultado == 1

# ==================== RAIZ CUADRADA ====================
def test_raiz_cuadrada_positiva():
    # Arrange
    numero = 16
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 4.0

def test_raiz_cuadrada_negativa_lanza_error():
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)

# ==================== PROMEDIO ====================
def test_promedio_lista_normal():
    # Arrange
    lista = [10, 20, 30]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 20

def test_promedio_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        promedio([])

# ==================== MAXIMO ====================
def test_maximo_lista_normal():
    # Arrange
    lista = [3, 7, 2, 9, 5]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 9

def test_maximo_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        maximo([])

# ==================== MINIMO ====================
def test_minimo_lista_positivos():
    # Arrange
    lista = [5, 3, 8, 1, 9]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 1

def test_minimo_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        minimo([])

# ==================== AREA RECTANGULO ====================
def test_area_rectangulo():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 15

def test_area_rectangulo_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-5, 3)

# ==================== PERIMETRO RECTANGULO ====================
def test_perimetro_rectangulo():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 16

def test_perimetro_rectangulo_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(5, -3)
