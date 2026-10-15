import json
import unittest
from pathlib import Path
from src.rag_ejemplo import buscar_pedido, crear_documentos

ROOT = Path(__file__).resolve().parents[1]

class PruebasDatos(unittest.TestCase):
    def test_docepedidos(self):
        pedidos = json.loads((ROOT/"data"/"pedidos.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(pedidos), 10)
        self.assertEqual(len({p["id"] for p in pedidos}), len(pedidos))

    def test_pedido_exacto(self):
        pedido, hay_id = buscar_pedido("Estado de ECO-1003")
        self.assertTrue(hay_id)
        self.assertEqual(pedido["id"], "ECO-1003")

    def test_pedido_inexistente(self):
        pedido, hay_id = buscar_pedido("Estado de ECO-9999")
        self.assertTrue(hay_id)
        self.assertIsNone(pedido)

    def test_documentos(self):
        docs = crear_documentos()
        fuentes = {d.metadata["fuente"] for d in docs}
        self.assertEqual(fuentes, {"faq.json", "inventario.json", "politica_devoluciones.md"})

if __name__ == "__main__":
    unittest.main()
