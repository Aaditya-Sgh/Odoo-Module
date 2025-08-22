odoo.define('my_odoo_chatbot_module.chatbot', function (require) {
    "use strict";
    var rpc = require('web.rpc');

    document.addEventListener('DOMContentLoaded', function () {
        const input = document.getElementById('chat-input');
        const sendBtn = document.getElementById('chat-send');
        const responseBox = document.getElementById('chat-response');

        if (sendBtn && input && responseBox) {
            sendBtn.onclick = function () {
                var userMessage = input.value;
                rpc.query({
                    route: '/chatbot/query',
                    params: { message: userMessage },
                }).then(function (result) {
                    responseBox.innerText = result.response;
                });
            };
        }
    });
});