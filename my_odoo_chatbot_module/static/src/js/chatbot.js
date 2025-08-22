odoo.define('my_odoo_chatbot_module.chatbot', function (require) {
    "use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');

    function ensureChatboxInDOM() {
        if (!document.getElementById('chatbot-box')) {
            var chatboxTemplate = document.querySelector('template#chatbot_box_template');
            if (chatboxTemplate) {
                var tempDiv = document.createElement('div');
                tempDiv.innerHTML = chatboxTemplate.innerHTML;
                document.body.appendChild(tempDiv.firstElementChild);
            } else {
                // fallback: try to find by xml id
                var xml = document.querySelector('[id^="chatbot-box"]');
                if (xml) document.body.appendChild(xml);
            }
        }
    }

    function showChatbox() {
        ensureChatboxInDOM();
        var box = document.getElementById('chatbot-box');
        if (box) box.style.display = 'block';
    }
    function hideChatbox() {
        var box = document.getElementById('chatbot-box');
        if (box) box.style.display = 'none';
    }

    document.addEventListener('DOMContentLoaded', function () {
        // Insert chatbox template if not present
        ensureChatboxInDOM();

        // Add click event to systray button
        var observer = new MutationObserver(function() {
            var btn = document.querySelector('.o_chatbot_systray_btn');
            if (btn && !btn.dataset.chatbotBound) {
                btn.addEventListener('click', showChatbox);
                btn.dataset.chatbotBound = '1';
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });

        // Chatbox close button
        document.body.addEventListener('click', function(e) {
            if (e.target && e.target.id === 'chatbot-close') {
                hideChatbox();
            }
        });
    });

});