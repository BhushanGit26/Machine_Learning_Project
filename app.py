from flask import Flask, request
import sys

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
    return "Starting my Flask apllication"


if __name__ == "__main__":
    app.run(debug=True,port=5001)