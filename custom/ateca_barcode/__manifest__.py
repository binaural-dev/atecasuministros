{
    "name": "Ateca Código de Barras",
    "summary": "Modificaciones sobre el módulo stock_barcode",
    "category": "Inventory/Inventory",
    "sequence": 255,
    "version": "1.0",
    "depends": [
        "stock_barcode",
        "web",
    ],
    "data": [
        "views/stock_barcode_extend.xml",
    ],
    "qweb": [
        "static/src/xml/stock_barcode_extend.xml",
    ],
    "installable": True,
    "application": False,
}
