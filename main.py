
# Flask Application for Telegram Bot Interaction

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Send message to bot
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    # URL for Google AppEngine Cloud Functions
    url = 'https://<app-id>.appspot.com/send-telegram-message'
    
    payload = {'message': message}
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            msg = 'Message sent successfully.'
        else:
            msg = 'Error sending message. Please try again.'
            
    except Exception as e:
        msg = 'Error connecting to server. Please try again.'
    
    return render_template('index.html', message=msg)

if __name__ == '__main__':
    # Run the app locally
    app.run(debug=True)
