from flask import Flask, jsonify
import MinuteMail
import time
import threading
import requests

app = flask = Flask(__name__)

email_adresses = []

def fetch_new_emails():
    global email_adresses
    while True:
        box = MinuteMail.mailbox()
        print(box.get_emails()[0])
        email_adresses.append(box.get_emails()[0])
        time.sleep(6)  # Check for new emails every 2 minutes

threading.Thread(target=fetch_new_emails, daemon=True).start()

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/new_emails", methods=["GET"])
def get_new_emails():
    return jsonify(email_adresses)

if __name__ == "__main__":
    app.run('host=0.0.0.0', port=8495, debug=True)