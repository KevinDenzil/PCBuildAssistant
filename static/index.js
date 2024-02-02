
class chatBox {
    constructor() {
        this.args = {
            chatBox: document.querySelector(".chatbox__support"),
            sendButton: document.querySelector(".send__button"),
            func: "get_response",
            arg: -1
        }
        this.messages = [];
    }
    display() {
        const { chatBox, sendButton } = this.args;
        // const input_Field = chatBox.addEventListener('input');
        chatBox.addEventListener('keydown', function (event) {
            // Check if the pressed key is Enter (key code 13)
            if (event.key === 'Enter') {
                // Trigger the click event on the button
                sendButton.click();
            }
        });
        sendButton.addEventListener('click', () => this.onsendButton(chatBox));

    }


    onsendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1.trim() === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);
        const { func, arg } = this.args

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1, func: func, arg: arg }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => response.json())
            .then(response => {
                this.args.func = response.func
                this.args.arg = response.arg
                let msg2 = { name: "JENSON", message: response.answer };
                this.messages.push(msg2);
                this.updateChatText(chatbox);
                textField.value = '';

            })
            .catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox);
                textField.value = '';
            });
    }
    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().forEach(function (item, index) {
            const avatarImage = item.name === "JENSON" ? "static/icons/icon.jpg" : "static/icons/icon2.jpg";
            if (item.name === "JENSON") {
                html += `<span class="avatar"><img src="${avatarImage}" alt="${item.name} Avatar"></span>` + '    <div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new chatBox();
chatbox.display();

