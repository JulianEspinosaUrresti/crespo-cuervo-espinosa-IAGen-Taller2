# Fase 3. Integración, ejecución y evaluación del sistema RAG

## 1. Objetivo

Implementar un sistema de generación aumentada por recuperación (RAG) para mejorar el asistente de atención al cliente de EcoMarket desarrollado en el Taller Práctico #1.

La solución integra LangChain, ChromaDB, embeddings multilingües y Llama 3.2 mediante Ollama, permitiendo consultar información documental antes de generar respuestas.

## 2. Preparación y arquitectura

La arquitectura implementada sigue el siguiente flujo:

1. **Carga de documentos:** políticas de devoluciones, preguntas frecuentes e inventario.
2. **Segmentación:** división del contenido en fragmentos con metadatos.
3. **Embeddings:** transformación de los fragmentos en representaciones vectoriales.
4. **Indexación:** almacenamiento de los vectores en ChromaDB.
5. **Recuperación:** selección de hasta cuatro fragmentos relevantes para la consulta.
6. **Generación:** construcción del prompt contextual mediante LangChain y generación con Llama 3.2.
7. **Respuesta:** presentación de información al cliente o reconocimiento de información insuficiente.

Para las consultas transaccionales, los pedidos se verifican mediante identificadores exactos en un archivo JSON ficticio. Esta decisión evita depender exclusivamente de la similitud vectorial para identificar pedidos.

## 3. Componentes del código

El archivo `src/rag_ejemplo.py` contiene los componentes principales:

| Componente | Función |
|---|---|
| `crear_documentos()` | Carga y segmenta documentos de EcoMarket |
| `embeddings()` | Inicializa el modelo multilingüe de embeddings |
| `indexar()` | Construye y persiste la base vectorial |
| `buscar_pedido()` | Recupera pedidos por identificador exacto |
| `consultar()` | Integra recuperación documental y generación |
| `ChatPromptTemplate` | Estructura las instrucciones, el contexto y la consulta |
| `ChatOllama` | Ejecuta el modelo Llama 3.2 localmente |
| `main()` | Permite ejecutar el prototipo desde la terminal |

LangChain facilita la integración de los componentes sin necesidad de desarrollar manualmente toda la lógica de comunicación entre el recuperador y el modelo generativo.

## 4. Integración con el Taller 1

El Taller 1 abordó el asistente de atención al cliente de EcoMarket mediante ingeniería de prompts y consultas sobre pedidos y devoluciones.

En el Taller 2 se amplía esa propuesta incorporando una base de conocimiento recuperable.

Esta integración permite separar dos responsabilidades:

- **Recuperación de información:** identificar datos documentales pertinentes para la consulta.
- **Generación de lenguaje:** elaborar respuestas comprensibles utilizando el contexto recuperado.

Se mantiene el rol de asistente de atención al cliente y se incorporan restricciones para evitar inventar información comercial o confirmar operaciones no autorizadas.

## 5. Ejecución del sistema

El prototipo fue ejecutado localmente en Windows con Python y Ollama.

### 5.1 Pruebas unitarias

Comando utilizado:

`python -m unittest discover -s tests -v`

Resultado obtenido:

**8 pruebas ejecutadas y 8 aprobadas (OK).**

Las pruebas verificaron funcionalidades relacionadas con documentos, pedidos y construcción del contexto.

### 5.2 Indexación

Comando utilizado:

`python -m src.rag_ejemplo --indexar`

Resultado obtenido:

**10 fragmentos indexados correctamente en ChromaDB.**

### 5.3 Generación de respuestas

Se realizaron consultas relacionadas con:

- Estados de pedidos.
- Devoluciones de productos.
- Productos dañados.
- Inventario disponible.
- Cancelaciones.
- Tarifas de envío desconocidas.

El sistema generó respuestas mediante el modelo Llama 3.2, utilizando el contexto recuperado y las instrucciones del prompt.

## 6. Evaluación experimental de prompts

Se compararon dos variantes del prompt sobre un conjunto de 12 casos de prueba.

La evaluación consideró tres categorías:

- **Correcto:** respuesta alineada con el comportamiento esperado.
- **Parcial:** respuesta que omite información relevante.
- **Incorrecto:** respuesta que incorpora información no sustentada o potencialmente engañosa.

### Resultados de V3

| Indicador | Prompt mejorado | Prompt corregido |
|---|---:|---:|
| Respuestas correctas | 8 | 10 |
| Respuestas parciales | 4 | 1 |
| Respuestas incorrectas | 0 | 1 |
| Porcentaje de respuestas correctas | 66,7 % | 83,3 % |

Se observó un incremento de **16,7 puntos porcentuales** en las respuestas correctas dentro del conjunto de evaluación.

Sin embargo, la variante corregida también produjo una URL de GitHub inventada en una respuesta relacionada con devoluciones. Este resultado demuestra que las instrucciones adicionales pueden mejorar determinados comportamientos sin eliminar completamente las alucinaciones.

Los archivos originales y evaluados se conservan en la carpeta `resultados/`.

## 7. Limitaciones técnicas y de recursos

### 7.1 Recursos computacionales

La ejecución local de Llama 3.2 y del modelo de embeddings requiere memoria RAM, almacenamiento y capacidad de procesamiento.

La inferencia en CPU puede incrementar los tiempos de respuesta frente a una implementación con GPU.

No se realizó una medición sistemática de latencia, consumo energético ni capacidad de atención simultánea.

### 7.2 Recuperación documental

La estrategia de recuperación utiliza similitud semántica y un número limitado de fragmentos.

No se implementaron mecanismos de reranking ni umbrales de relevancia calibrados. Por tanto, recuperar documentos no garantiza que sean suficientes o correctos para responder.

### 7.3 Confiabilidad

El modelo puede generar respuestas incompletas, referencias inexistentes o afirmaciones no respaldadas.

Las pruebas identificaron dificultades para comunicar el escalamiento humano ante productos defectuosos.

### 7.4 Seguridad y privacidad

El prototipo no implementa autenticación ni autorización por cliente.

Por esta razón, los pedidos utilizados son ficticios y el sistema no debe conectarse directamente a información personal real sin controles adicionales.

### 7.5 Escalabilidad

ChromaDB se utiliza mediante persistencia local. El prototipo no dispone de alta disponibilidad, procesamiento concurrente controlado ni actualización incremental de documentos.

Una implementación empresarial requeriría mecanismos adicionales de despliegue, monitoreo, control de acceso y mantenimiento de la base de conocimiento.

## 8. Suposiciones de la solución

Para delimitar el alcance académico se establecieron las siguientes suposiciones:

1. Todos los pedidos, productos, existencias y políticas utilizados son ficticios.
2. Los documentos de prueba se consideran la fuente de conocimiento del prototipo.
3. Las políticas comerciales no cambian durante cada ejecución experimental.
4. Los pedidos se consultan mediante identificadores exactos.
5. Las solicitudes de devolución requieren validación humana.
6. El asistente no realiza cancelaciones, reembolsos ni modificaciones transaccionales.
7. El sistema está diseñado para demostrar la arquitectura RAG, no para operar directamente en producción.

## 9. Conclusiones

La implementación permitió integrar exitosamente recuperación documental
