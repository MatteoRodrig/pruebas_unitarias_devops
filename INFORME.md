# Informe — Taller de Pruebas Unitarias

## Datos
- **Nombre:** Julián Mateo Rodríguez Díaz
- **Fecha de entrega:** 17 de octubre de 2026
- **Curso:** Introducción a DevOps — Universidad Nacional de Colombia, Sede Manizales

---

## Análisis por módulo

### Módulo: calculadora

**¿Qué hace?**
Contiene funciones matemáticas básicas: suma, resta, multiplicación, división, potencia, raíz cuadrada, promedio, máximo, mínimo, área y perímetro de rectángulo.

**Casos probados y por qué:**
Se diseñaron 23 pruebas siguiendo la estructura AAA. Se eligieron tres tipos de casos:
1. **Casos normales:** números positivos, listas con múltiples elementos. Verifican el funcionamiento esperado en condiciones típicas.
2. **Casos límite:** cero, listas vacías, exponente cero, valores negativos. Buscan revelar comportamientos incorrectos en los extremos del dominio.
3. **Casos de error:** división por cero, raíz de negativo, listas vacías en promedio/máximo/mínimo. Verifican que el código lance excepciones controladas en lugar de fallar silenciosamente.

Este enfoque permitió cubrir el "camino feliz" y también los errores que el código debe manejar explícitamente.

**Bugs encontrados:**

1. **`raiz_cuadrada` con números negativos**
   - La función no validaba la entrada. Al recibir un número negativo, Python devolvía un número complejo en lugar de lanzar una excepción, lo cual es inconsistente con el contrato de la función.
   - **Corrección:** Se agregó una verificación `if numero < 0: raise ValueError(...)`.

2. **`minimo` con listas de positivos**
   - La variable `min_val` se inicializaba en `0`. Si la lista contenía solo números positivos, el mínimo devuelto era `0`, aunque no perteneciera a la lista.
   - **Corrección:** Se inicializó con el primer elemento de la lista: `min_val = lista[0]`.

**Evidencia:**
- ![Captura 1 — pytest inicial sin pruebas](capturas/Cap1.png)
- ![Captura 2 — prueba en rojo revelando el bug de raiz_cuadrada](capturas/Cap2error_1.png)
- ![Captura 3 — pytest en verde con las 23 pruebas pasando](capturas/Cap3.png)

---

## Tabla de bugs encontrados

| Función | Entrada | Resultado erróneo | Resultado esperado | Corrección aplicada |
|---------|---------|-------------------|--------------------|---------------------|
| `raiz_cuadrada` | `-4` | Devolvía un número complejo | Lanzar `ValueError` | Agregar verificación `if numero < 0` |
| `minimo` | `[5, 3, 8, 1, 9]` | Devolvía `0` | Devolver `1` | Inicializar con `lista[0]` |

---

## Cobertura

*Pendiente: se agregará al final del taller.*

---

## Reflexión final

*Pendiente: se agregará al final del taller.*
