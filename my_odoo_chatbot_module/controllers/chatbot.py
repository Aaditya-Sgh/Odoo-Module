from odoo import http
from odoo.http import request

class ChatbotController(http.Controller):

    @http.route('/chatbot/query', type='json', auth='user')
    def chatbot_query(self, **kwargs):
        """
        Endpoint to handle chatbot messages from frontend.
        Accepts a 'message' key via JSON and returns a response.
        """
        user_query = kwargs.get('message', '').strip().lower()

        # Simple hardcoded intent recognition (placeholder)
        if not user_query:
            return {"response": "Please enter a message."}

        if "create field" in user_query or "add field" in user_query:
            return {"response": "To add a field, go to Studio > Edit View and use the 'Add' button."}

        elif "conditional logic" in user_query:
            return {"response": "You can add conditional visibility using 'Set Conditions' under the field settings."}

        elif "approval" in user_query:
            return {"response": "To configure an approval workflow, use the 'Approvals' module or set server actions with conditions."}

        elif "hello" in user_query or "hi" in user_query:
            return {"response": "Hello! How can I assist you in Odoo today?"}

        # Default fallback response
        return {"response": f"I'm not sure how to help with: '{user_query}'. Try rephrasing or using keywords like 'field', 'logic', or 'approval'."}
