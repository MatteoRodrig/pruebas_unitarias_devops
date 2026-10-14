"""
Pruebas unitarias para el módulo descuentos.
Estructura AAA: Arrange, Act, Assert.
"""
import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado
)

# ==================== APLICAR DESCUENTO ====================
def test_aplicar_descuento_normal():
    # Arrange
    precio, porcentaje = 100, 10
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 90

def test_aplicar_descuento_cero():
    # Arrange
    precio, porcentaje = 100, 0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 100

def test_aplicar_descuento_100():
    # Arrange
    precio, porcentaje = 100, 100
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0

def test_aplicar_descuento_precio_negativo_lanza_error():
    with pytest.raises(ValueError):
        aplicar_descuento(-10, 10)

def test_aplicar_descuento_porcentaje_invalido_lanza_error():
    with pytest.raises(ValueError):
        aplicar_descuento(100, 150)

# ==================== CALCULAR DESCUENTO ====================
def test_calcular_descuento_normal():
    # Arrange
    precio, porcentaje = 200, 25
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 50

def test_calcular_descuento_cero():
    # Arrange
    precio, porcentaje = 100, 0
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0

# ==================== CALCULAR PRECIO FINAL ====================
def test_calcular_precio_final_sin_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 19, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 119

def test_calcular_precio_final_con_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 19, 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 107.1

def test_calcular_precio_final_precio_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_precio_final(-100, 19, 10)

def test_calcular_precio_final_impuesto_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_precio_final(100, -19, 10)

def test_calcular_precio_final_descuento_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_precio_final(100, 19, 150)

# ==================== DESCUENTO POR VOLUMEN ====================
def test_descuento_por_volumen_sin_descuento():
    # Arrange
    cantidad, precio_unitario = 5, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 50

def test_descuento_por_volumen_10_unidades():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 95

def test_descuento_por_volumen_20_unidades():
    # Arrange
    cantidad, precio_unitario = 20, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 180

def test_descuento_por_volumen_50_unidades():
    # Arrange
    cantidad, precio_unitario = 50, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 425

def test_descuento_por_volumen_100_unidades():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 800

def test_descuento_por_volumen_cantidad_negativa_lanza_error():
    with pytest.raises(ValueError):
        descuento_por_volumen(-5, 10)

# ==================== DESCUENTO CUMULATIVO ====================
def test_descuento_cumulativo_lista_vacia():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100

def test_descuento_cumulativo_un_descuento():
    # Arrange
    precio, descuentos = 100, [10]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 90

def test_descuento_cumulativo_multiples():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 72

def test_descuento_cumulativo_descuento_invalido_lanza_error():
    with pytest.raises(ValueError):
        descuento_cumulativo(100, [10, 150])

# ==================== DESCUENTO APILADO ====================
def test_descuento_apilado_lista_vacia():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100

def test_descuento_apilado_un_descuento():
    # Arrange
    precio, descuentos = 100, [10]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 90

def test_descuento_apilado_multiples():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 70

def test_descuento_apilado_excede_100_devuelve_cero():
    # Arrange
    precio, descuentos = 100, [60, 50]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0
