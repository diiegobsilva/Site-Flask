from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def index():  
    return render_template('index.html')

@app.route("/ads") 
def ADS():  
    return render_template('ads.html')

@app.route("/bd") 
def BD():  
    return render_template('bd.html')

@app.route("/ads2020_2") 
def ADS2020_2():  
    return render_template('ads-2020-2.html')

@app.route("/logistica2020_2") 
def Logistica2020_2():  
    return render_template('Logistica2020.2.html')

@app.route("/manufaturaavançada2020_2") 
def manufaturaavançada_2():  
    return render_template('manufaturaavançada20202.html')

@app.route("/manutençaodeaeronaves2020_2") 
def ManutençaodeAeronaves2020_2():  
    return render_template('manutençaodeaeronaves20202.html')
