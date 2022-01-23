from flask import Flask,render_template

app=Flask(__name__)

@app.route('/play')

def MuestreTresCajas():
    return render_template("index.html",num1=3)

@app.route('/play/<int:num1>')
def cajasMultiples(num1):
    return render_template("index.html",num1=num1)

@app.route('/play/<int:num1>/<string:color>')
def cajasDeColores(num1,color):
    return render_template("index.html",num1=num1,color=color)

if __name__ == "__main__":
    app.run(debug=True)
