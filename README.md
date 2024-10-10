## Flask Application Design for Telegram Bot Interaction using Google AppEngine

### HTML Files

- `index.html`:
  - Home page with a form for sending messages to the bot
  - Includes input fields for the message text and a submit button

### Routes

- `/`: Renders the `index.html` home page
- `/send_message`:
  - Accepts a POST request with the message text
  - Interacts with the Telegram bot using Google AppEngine
  - Sends the message and displays a success/error message on the page