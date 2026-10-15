# Mejoras V3 y protocolo de validación

## Evidencia previa
Los archivos `resultados/comparacion_v2_original.csv` y `resultados/comparacion_v2_evaluada.csv` conservan las respuestas anteriores. No se modificaron ni se presentan como resultados de V3.

## Cambios de implementación
- Nuevo prompt `corregido`: reglas explícitas sobre pedidos retrasados, excepción por defectos, escalamiento humano, abstención ante tarifas desconocidas y referencias documentales verificables.
- Para consultas de devoluciones, se añade al contexto la **política completa**, además de los cuatro fragmentos recuperados, evitando que una excepción quede fuera de `top-k`.
- La búsqueda de pedidos sigue siendo por ID exacto en el JSON ficticio.
- Evaluador configurable para contrastar `mejorado` y `corregido` sin sobrescribir el CSV original.

## Limitaciones
- Añadir la política íntegra es apropiado solo por ser un documento académico corto; para documentos extensos se necesita segmentación por secciones y recuperación selectiva.
- Los tests unitarios comprueban contexto y datos, **no** la exactitud generativa.
- Las instrucciones reducen riesgos, pero no garantizan que el LLM obedezca. La revisión manual de las 24 respuestas nuevas sigue siendo obligatoria.
- Sin autenticación ni autorización por pedido: no usar con datos reales.

## Ejecución
```bat
python -m unittest discover -s tests -v
python -m src.rag_ejemplo --indexar
python -m src.rag_ejemplo --pregunta "Cual es el estado del pedido ECO-1004?" --variante corregido
python -m src.rag_ejemplo --pregunta "Puedo devolver un jabon abierto?" --variante corregido
python -m src.rag_ejemplo --pregunta "Cuanto cuesta el envio a Bogota?" --variante corregido
python -m src.evaluar --limite 12 --variantes mejorado corregido --salida comparacion_v3.csv
```
Registrar corrección/parcialidad/error por cada respuesta, citar fragmentos utilizados y calcular proporción de casos correctos solo después de la revisión.
