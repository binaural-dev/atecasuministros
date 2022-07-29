{
    "name": "Ateca Facturación",
    "summary": "Modificaciones sobre el módulo de contabilidad",
    "category": "Accounting/Invoicing",
    "sequence": 255,
    "version": "1.0",
    "depends": [
        "base",
        "account",
    ],
    "data": [
        "data/report_paperformat.xml",
        "views/report_templates.xml",
        "views/account_report_inherit.xml",
        "views/report_invoice_templates_inherit.xml",
    ],
    "installable": True,
    "application": False,
}
