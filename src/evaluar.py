"""Ejecuta ambas variantes y guarda evidencia sin afirmar exactitud automática."""
import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from src.rag_ejemplo import BASE, consultar

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limite", type=int, default=12)
    parser.add_argument("--variantes", nargs="+", choices=["base","mejorado","corregido"],
                        default=["mejorado","corregido"])
    parser.add_argument("--salida", default="comparacion_v3.csv")
    args = parser.parse_args()
    casos = json.loads((BASE/"data"/"casos_evaluacion.json").read_text(encoding="utf-8"))
    salida = BASE/"resultados"
    salida.mkdir(exist_ok=True)
    archivo = salida/args.salida
    with archivo.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["id","pregunta","variante","esperado","respuesta","revision_humana","fecha_utc"])
        writer.writeheader()
        for caso in casos[:args.limite]:
            for variante in args.variantes:
                try:
                    respuesta = consultar(caso["pregunta"], variante)
                except Exception as exc:
                    respuesta = f"ERROR: {type(exc).__name__}: {exc}"
                writer.writerow({"id":caso["id"],"pregunta":caso["pregunta"],
                    "variante":variante,"esperado":caso["esperado"],
                    "respuesta":respuesta,"revision_humana":"",
                    "fecha_utc":datetime.now(timezone.utc).isoformat()})
                print(f"{caso['id']} {variante}: {respuesta[:110]}")
    print(f"Resultados guardados en {archivo}")
    print("Completar columna revision_humana: correcto/parcial/incorrecto.")

if __name__ == "__main__":
    main()
