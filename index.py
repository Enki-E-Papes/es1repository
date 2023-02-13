'''
Per realizzare un sito web con flask che abbia le seguenti funzionalità :
1)Home page deve descrivere una breve descrizione delle caratteristeche della città di milano 
2)Al link /<nomesito>/immagini.devono essere visualizate le immagini di 4 monumenti di milano(controllare sul sito del
 prof come mettere le immagini)
3)fare in modo che cliccando sul immagine si venga mandati ad un breve testo descrittivo del documento(controllare sempre 
sul sito del docente)
4)La repository che conterra il sito si chiamerà FlaskMilano
'''

from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index1.html')
#---------------------------------------------
@app.route('/img1', methods=['GET'])
def img1def():
    return render_template('perImg1.html')
#---------------------------------------------
@app.route('/img2', methods=['GET'])
def img2def():
    return render_template('perImg2.html')
#---------------------------------------------  
@app.route('/img3', methods=['GET'])
def img3def():
    return render_template('perImg3.html')
#---------------------------------------------
@app.route('/img4', methods=['GET'])
def img4def():
    return render_template('perImg4.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma