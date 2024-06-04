function sendMessage() {
            var userInput = document.getElementById('message-input').value;
            if (userInput.trim() === '') return;

            // Perform an AJAX request to the Flask app
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/process_input", true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var response = JSON.parse(xhr.responseText);
                    appendMessage('chatbot', response.answer);
                }
            };

            var data = JSON.stringify({ input: userInput });
            xhr.send(data);

            appendMessage('user', userInput);

            // Clear the input field
            document.getElementById('message-input').value = '';
        }

        function appendMessage(sender, message)
         {
            var chatContainer = document.getElementById('chat-messages');
            var newMessage = document.createElement('div');
            newMessage.className = sender;
            newMessage.textContent = message;
            chatContainer.appendChild(newMessage);
        
            // Scroll to the bottom of the chat container
            chatContainer.scrollTop = chatContainer.scrollHeight;
                }