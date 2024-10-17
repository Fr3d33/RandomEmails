from flask import Flask, jsonify
import MinuteMail  # Importing a module for handling temporary email addresses
import time
import threading
import requests

# Initialize a Flask web application
app = flask = Flask(__name__)

# A global list to store fetched email addresses
email_adresses = []

# Function to fetch new emails periodically
def fetch_new_emails():
    global email_adresses  # Reference the global list
    while True:
        box = MinuteMail.mailbox()  # Access the mailbox from MinuteMail
        print(box.get_emails()[0])  # Print the first email for debugging
        email_adresses.append(box.get_emails()[0])  # Add the first new email to the list
        time.sleep(6)  # Pause for 6 seconds before checking for new emails again

# Run the email fetching function in a separate thread, so it doesn’t block the web server
threading.Thread(target=fetch_new_emails, daemon=True).start()

# Define a route for the base URL, which returns "Hello World!"
@app.route("/")
def hello_world():
    return "Hello World!"

# Define a route to return the list of new emails in JSON format
@app.route("/new_emails", methods=["GET"])
def get_new_emails():
    return jsonify(email_adresses)  # Convert the email addresses list to JSON and return it

# Start the Flask app on port 8495, accessible on any network interface, with debug mode enabled
if __name__ == "__main__":
    app.run('host=0.0.0.0', port=8495, debug=True)