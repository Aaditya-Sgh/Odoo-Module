{
    "name": "Odoo Chatbot Module",
    "version": "1.0",
    "summary": "A simple context-aware chatbot for Odoo",
    "category": "Tools",
    "author": "Aaditya Singh",
    "website": "http://www.example.com",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/my_odoo_module_views.xml"
    ],
    "qweb": [
        "views/my_odoo_module_views.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}