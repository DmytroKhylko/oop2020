from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    return render_template("greeting.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')