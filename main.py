from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "1234"  # Replace this with your own secret

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403

# Optional: add POST handler for webhook events if you want here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
