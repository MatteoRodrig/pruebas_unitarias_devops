"""
Pruebas unitarias para el módulo csv_parser.
Estructura AAA: Arrange, Act, Assert.
Usa StringIO para simular archivos CSV sin leer del disco (mocking).
"""
import pytest
from io import StringIO
from src.csv_parser import (
    parse_csv_line, leer_csv_como_lista, csv_a_diccionarios,
    validar_csv, extraer_columna, filtrar_por_columna,
    contar_filas, contar_columnas
)

# ==================== PARSE_CSV_LINE ====================
def test_parse_csv_line_simple():
    # Arrange
    linea = "a,b,c"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "b", "c"]

def test_parse_csv_line_vacia():
    # Arrange
    linea = ""
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == []

def test_parse_csv_line_con_comillas():
    # Arrange
    linea = '"Hola, mundo",otro,valor'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["Hola, mundo", "otro", "valor"]

# ==================== LEER_CSV_COMO_LISTA ====================
def test_leer_csv_como_lista_normal():
    # Arrange
    contenido = "a,b,c\n1,2,3\n4,5,6"
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == [["a", "b", "c"], ["1", "2", "3"], ["4", "5", "6"]]

def test_leer_csv_como_lista_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == []

# ==================== CSV_A_DICCIONARIOS ====================
def test_csv_a_diccionarios_con_cabecera():
    # Arrange
    contenido = "nombre,edad\nAna,30\nLuis,25"
    # Act
    resultado = csv_a_diccionarios(contenido, tiene_cabecera=True)
    # Assert
    assert resultado == [
        {"nombre": "Ana", "edad": "30"},
        {"nombre": "Luis", "edad": "25"}
    ]

def test_csv_a_diccionarios_sin_cabecera():
    # Arrange
    contenido = "Ana,30\nLuis,25"
    # Act
    resultado = csv_a_diccionarios(contenido, tiene_cabecera=False)
    # Assert
    assert resultado == []

def test_csv_a_diccionarios_fila_incompleta():
    # Arrange
    contenido = "nombre,edad,ciudad\nAna,30\nLuis,25,Bogota"
    # Act
    resultado = csv_a_diccionarios(contenido, tiene_cabecera=True)
    # Assert
    assert resultado[0] == {"nombre": "Ana", "edad": "30", "ciudad": None}
    assert resultado[1] == {"nombre": "Luis", "edad": "25", "ciudad": "Bogota"}

# ==================== VALIDAR_CSV ====================
def test_validar_csv_valido():
    # Arrange
    contenido = "a,b,c\n1,2,3\n4,5,6"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is True

def test_validar_csv_invalido():
    # Arrange
    contenido = "a,b,c\n1,2\n4,5,6"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False

def test_validar_csv_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False

# ==================== EXTRAER_COLUMNA ====================
def test_extraer_columna_normal():
    # Arrange
    contenido = "a,b,c\n1,2,3\n4,5,6"
    # Act
    resultado = extraer_columna(contenido, 1)
    # Assert
    assert resultado == ["b", "2", "5"]

def test_extraer_columna_fuera_de_rango():
    # Arrange
    contenido = "a,b\n1,2"
    # Act
    resultado = extraer_columna(contenido, 5)
    # Assert
    assert resultado == ["", ""]

# ==================== FILTRAR_POR_COLUMNA ====================
def test_filtrar_por_columna_normal():
    # Arrange
    contenido = "nombre,edad\nAna,30\nLuis,25\nAna,40"
    # Act
    resultado = filtrar_por_columna(contenido, 0, "Ana")
    # Assert
    assert resultado == [["Ana", "30"], ["Ana", "40"]]

def test_filtrar_por_columna_sin_resultados():
    # Arrange
    contenido = "nombre,edad\nAna,30\nLuis,25"
    # Act
    resultado = filtrar_por_columna(contenido, 0, "Pedro")
    # Assert
    assert resultado == []

# ==================== CONTAR_FILAS ====================
def test_contar_filas_normal():
    # Arrange
    contenido = "a,b\n1,2\n3,4"
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 3

def test_contar_filas_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 0

# ==================== CONTAR_COLUMNAS ====================
def test_contar_columnas_normal():
    # Arrange
    contenido = "a,b,c\n1,2,3"
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 3

def test_contar_columnas_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 0
