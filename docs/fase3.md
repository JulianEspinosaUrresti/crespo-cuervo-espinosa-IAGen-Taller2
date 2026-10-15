# Fase 3. Integración, ejecución y evaluación
## Componentes del script
- `crear_documentos()`: carga la política, FAQ e inventario; divide textos y añade metadatos.
- `embeddings()`: instancia el codificador semántico multilingüe.
- `indexar()`: crea Chroma persistente con embeddings de documentos.
- `buscar_pedido()`: consulta JSON por identificador exacto, evitando errores de similitud entre pedidos.
- `consultar()`: recupera cuatro fragmentos, compone el prompt y lo envía al LLM de Ollama.
- `ChatPromptTemplate | ChatOllama`: cadena de generación. Las fuentes recuperadas se pasan como contexto, no como instrucciones.
- `main()`: interfaz CLI para indexación y preguntas.

## Prompt: estructura y modificación
**Rol:** agente de EcoMarket. **Contexto:** fragmentos con fuentes y pedido verificado. **Restricciones:** no inventar, escalar si falta información, no aprobar devoluciones. **Salida:** respuesta breve en español con referencias. Es un prompt zero-shot; puede evaluarse una variante few-shot agregando ejemplos sin alterar las fuentes.

**Experimento sugerido (no ejecutado):** comparar prompt A sin la restricción «no inventes fechas» con prompt B que sí la incluye. Registrar las respuestas ante un pedido retrasado sin fecha confirmada y contabilizar afirmaciones no respaldadas. No afirmar mejoras sin medición.

## Casos manuales propuestos (resultados esperados, NO medidos)
| Pregunta | Comportamiento esperado |
|---|---|
| Estado ECO-1001 | Informar Preparando |
| Estado ECO-1003 | Informar Entregado |
| Estado ECO-1004 | Informar Retrasado y fecha por confirmar |
| Estado ECO-9999 | Abstenerse: no existe en datos de prueba |
| ¿Puedo devolver un jabón abierto? | Explicar exclusión ordinaria y excepción por defecto |
| ¿Puedo devolver frutas? | Explicar exclusión ordinaria de perecederos |
| Llegó dañado mi producto | Escalar a agente humano |
| ¿Hay botellas disponibles? | Informar stock ficticio de 18, sin garantizar reserva |
| ¿Puedo cancelar mi compra? | Solicitar validación por soporte |
| ¿Cuánto cuesta el envío? | Abstenerse: no existe tarifa en fuentes |
| ¿Cómo devuelvo una bolsa sin uso? | Explicar plazo y validación |
| ¿Cuál es el estado de ECO-1002 y ECO-1003? | Abstenerse ante múltiples identificadores en esta versión |

## Limitaciones y supuestos
- Datos, plazos, existencias y pedidos ficticios; no se conecta a sistemas reales.
- No se han medido precisión, latencia ni costo energético; ejecutar y documentar pruebas antes de entregar.
- La similitud top-k no garantiza relevancia: falta umbral calibrado, reranking y evaluación cuantitativa de recuperación.
- El prototipo no autentica clientes: **no exponer públicamente** el acceso a pedidos; en producción exigir identidad y autorización por pedido.
- El LLM puede ignorar restricciones o generar afirmaciones erróneas; la revisión humana sigue siendo necesaria.
- El indexador reconstruye la base completa; en producción usar indexación incremental, versionado y control de vigencia.
- La selección del LLM local depende de RAM/CPU/GPU disponibles; si no es posible ejecutar, documentar el impedimento y no inventar resultados.
- La integración con Taller 1 se realiza conservando el rol de atención, casos de pedidos y devoluciones, y añadiendo recuperación documental antes de generar.
