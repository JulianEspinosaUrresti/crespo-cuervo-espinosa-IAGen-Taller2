# Evaluación comparativa (pendiente de ejecutar)
La versión 1 fue ejecutada en Windows por el estudiante. Evidencias observadas:
- ECO-1004: respondió «Retrasado» (correcto, incompleto: omitió fecha por confirmar).
- Jabón abierto: indicó exclusión ordinaria y pidió datos (correcto; no explicitó excepción por defecto).
- Envío a Bogotá: no inventó tarifa, pero pidió ID de pedido sin necesidad (parcial).

## Diseño de experimento
El script `python -m src.evaluar --limite 12` ejecuta 12 preguntas con dos variantes del prompt (24 respuestas). Registra las respuestas sin asignar notas automáticas. **No se han ejecutado estas 24 pruebas.** Completar `resultados/comparacion_prompts.csv` con juicio humano `correcto/parcial/incorrecto` y calcular la proporción de respuestas correctas por variante.

## Criterios de revisión
1. Exactitud factual respecto de documentos ficticios.
2. Abstención cuando falta información.
3. Mención de excepciones y escalamiento cuando proceda.
4. Ausencia de afirmaciones inventadas.
5. Citas pertinentes cuando se usan fuentes.

## Riesgos
Las dos variantes comparten las restricciones principales; el contraste aísla las reglas adicionales de la versión mejorada, no es un experimento de eliminación completa de guardrails. La búsqueda vectorial puede recuperar fragmentos irrelevantes y el LLM puede no cumplir las reglas. La revisión humana es obligatoria.

## Evidencia de entrega
Adjuntar captura de indexación, capturas de tres consultas iniciales, CSV de comparación y comentario crítico de resultados medidos. Nunca presentar expectativas como métricas observadas.
