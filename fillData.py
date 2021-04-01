from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.100.16'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'esp8266'
app.config['MYSQL_PASSWORD'] = 'Ajedrez,9191'
app.config['MYSQL_DB'] = 'datos_temp'

mysql = MySQL(app)

@app.route('/datos')
def datos():
    cur = mysql.connection.cursor()
    #para obtener los 100 ultimos datos utlizar order by idDatos_Sensores desc limit 100
    cur.execute('SELECT Datos_Sensores_temp, fecha FROM Datos_Sensores')
    data = cur.fetchall()
    legend = 'Temperatura Heladera 1'
    return render_template('datos.html', values=data, labels=data, legend=legend)  

if __name__=='__main__':
    app.run(debug=True)
