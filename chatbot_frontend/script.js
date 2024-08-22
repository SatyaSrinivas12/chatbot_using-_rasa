// Function to send user message and receive response from backend
function sendMessage() {
    const userInput = document.getElementById('user_input').value;
    if (userInput.trim() === '') return;

    // Display user message in chat
    const chatlogs = document.getElementById('chatlogs');
    chatlogs.innerHTML += `<div class="message user"><div class="bubble">${userInput}</div></div>`;
    console.log(`User message: ${userInput}`);
    // Send message to backend
    fetch(' http://10.84.56.109:5000/ask', { // Replace with your Flask backend URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (Array.isArray(data) && data.length > 0) {
            const botResponses = data.map(response => response.text).join(' ');
            chatlogs.innerHTML += `<div class="message bot"><div class="bubble">${botResponses}</div></div>`;
            console.log(`Bot response: ${botResponses}`);
        } else {
            chatlogs.innerHTML += `<div class="message bot"><div class="bubble">Sorry, I didn’t understand that.</div></div>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Add event listener to the send button
document.getElementById('send_button').addEventListener('click', sendMessage);

// Add event listener for enter key press in the input field
document.getElementById('user_input').addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

