from odoo import http
from odoo.http import request

class ChatbotController(http.Controller):
    @http.route('/chatbot/query', type='json', auth='user')
    def chatbot_query(self, **kwargs):
        user_query = kwargs.get('message')
        # Placeholder for actual chatbot logic
        return {"response": f"You said: {user_query}"}
