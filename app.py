from flask import Flask

from flask import jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/get_line_chart_data')
def get_line_chart_data():
    conn = get_db_connection()
    res = conn.execute("""select SUBSTRING(InvoiceDate, 1, 4) as Year, sum(Total) as TotalBilling from Invoice i 
group by SUBSTRING(InvoiceDate, 1, 4);""").fetchall()
    conn.close()

    x = []
    y = []

    for i in res:
        x.append(i[0])
        y.append(i[1])

    return jsonify([x, y])


@app.route('/get_bar_chart_data')
def get_bar_chart_data():
    conn = get_db_connection()
    res = conn.execute("""select a2.Name, count(*) as AlbumCount from Album a 
inner join Artist a2 on a.ArtistId = a2.ArtistId
group by a.ArtistId order by AlbumCount desc limit 10;""").fetchall()
    conn.close()

    x = []
    y = []

    for i in res:
        x.append(i[0])
        y.append(i[1])

    return jsonify([x, y])


@app.route('/get_scatter_chart_data')
def get_scatter_chart_data():
    conn = get_db_connection()
    res = conn.execute("""select Milliseconds/60000 as min, Bytes/1024 as mb from Track;""").fetchall()
    conn.close()

    x = []
    y = []

    for i in res:
        x.append(i[0])
        y.append(i[1])

    return jsonify([x, y])


@app.route('/get_pie_chart_data')
def get_pie_chart_data():
    conn = get_db_connection()
    res = conn.execute("""select mt.Name, sum(Milliseconds)/60000 as min from Track t 
                            inner join MediaType mt on mt.MediaTypeId = t.MediaTypeId 
                            group by t.MediaTypeId;""").fetchall()
    conn.close()

    x = []
    y = []

    for i in res:
        x.append(i[0])
        y.append(i[1])

    return jsonify([x, y])


def get_db_connection():
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    return conn
