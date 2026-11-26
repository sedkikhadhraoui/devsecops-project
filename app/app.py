from flask import Flask,request
SECRET_KEY = "password123456"
app = Flask(__name__)

@app.route("/")
def home():
    return "Webmail Demo"

@app.route("/search")
def search():
    q = request.args.get("q","")
    return f"Result: {q}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
