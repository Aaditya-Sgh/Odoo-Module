{
    "name": "My Odoo Chatbot Module",
    "version": "1.0.0",
    "summary": "Chatbot button and response interface for Odoo backend",
    "author": "Your Name",
    "category": "Tools",
    "depends": ["web"],  # Required for UI (WebClient, assets, systray)
    "data": [
        "views/my_odoo_module_views.xml",
    ],
    "qweb": [
        "views/my_odoo_module_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
