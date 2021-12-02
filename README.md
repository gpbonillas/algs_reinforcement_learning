# Algoritmos de aprendizaje por refuerzo

Jupyter notebook con la solución a la aplicación de los siguientes algoritmos al problema [Cliff Walking](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py):

- [Programación dinámica - Itración por valor](https://www.deeplearningwizard.com/deep_learning/deep_reinforcement_learning_pytorch/dynamic_programming_frozenlake/#value-iteration)
- [Monte Carlo - On-policy every-visit MC](https://medium.com/aprendizaje-por-refuerzo/5-evaluaci%C3%B3n-de-pol%C3%ADticas-con-monte-carlo-a6d70d1db7d4)
- [Aprendizaje por Diferencia Temporal - SARSA](https://towardsdatascience.com/reinforcement-learning-temporal-difference-sarsa-q-learning-expected-sarsa-on-python-9fecfda7467e)

![Cliff Walking](CliffWalking.png)

## Descripción del problema

El entorno CliffWalking consiste en un agente que se mueve en una cuadrícula de dimensiones 12x4 (ancho x alto). 
En cada paso, el agente tiene 4 opciones de acción o movimiento: ARRIBA, DERECHA, ABAJO, IZQUIERDA. 
La posición de cada casilla viene dada por una pareja de números naturales [x, y], donde la posición de la esquina de arriba a la izquierda sería el origen de coordenadas [0, 0]. 
El agente siempre sale de la misma casilla [0, 3] (esquina abajo izquierda) y el juego termina cuando el agente llega a la casilla de llegada [11, 3] (esquina abajo derecha).

El entorno se corresponde con el ejemplo 'Cuadrícula con precipicio' explicado en la sección 3.2.1. del módulo "Métodos de Diferencia Temporal". 
El problema radica en que en todas las casillas la recompensa inmediata es R=-1 excepto en las casillas que unen en línea recta la casilla de salida con la de llegada, 
casillas [1, 3] a [10, 3]. En estas casillas, que simulan un precipicio, la recompensa es R=-100 y se vuelve a la casilla inicial.
