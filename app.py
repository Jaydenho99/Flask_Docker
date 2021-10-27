from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "hello 2"
if __name__=='__main__':
    app.run(debug=True)
