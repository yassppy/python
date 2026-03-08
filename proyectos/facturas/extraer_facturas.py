import pdfplumber
import re as r
import os
import pandas as pd
# ruta = r"./data/fact_venta_nov_2025/PDF-DOC-E001578120610320351.pdf"
carpeta = ("./data/fact_venta_nov_2025")
archivos = os.listdir(carpeta)

# Lista vacía donde guardarás cada factura
facturas = []

for archivo in archivos:
    ruta = os.path.join(carpeta, archivo)
    
    with pdfplumber.open(ruta) as pdf:
        for pag in pdf.pages:
            text = pag.extract_text()
            factura_ruc = r.findall(r'\d{11}', text)
        serie_numero = r.search(r'([A-Z]\d*)-(\d{4}(?!\d))', text)
        serie = serie_numero.group(1)
        numero = serie_numero.group(2)
        ruc_cliente = factura_ruc[1]
        fecha_emision = r.search(r'(\d{2})/\d{2}/\d{4}', text)
        dia = fecha_emision.group(1)
        precios = r.findall(r'\d+\.\d{2}(?!\d)', text)
        registros = r.findall(r'UNIDAD \d+ ([A-Z]+)', text)
        if(len(registros) == 1):
            descripcion = registros[0][:20]
        else:
            descripcion = "Varios registros"
        
        precios[:5]
        valor_venta = precios[-7]
        igv = precios[-5]
        importe_total = precios[-1]
        
        facturas.append({
                "ruc_cliente": ruc_cliente,
                "serie": serie,
                "numero": numero,
                "fecha": fecha_emision.group(),
                "dia": dia,
                "descripcion": descripcion,
                "valor_venta": valor_venta,
                "igv": igv,
                "importe_total": importe_total
        })

# Convertir la lista en DataFrame y exportar
df = pd.DataFrame(facturas)
df.to_excel("facturas.xlsx", index=False)
print("✅ Exportado correctamente")