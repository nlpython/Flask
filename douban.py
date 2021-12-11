from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('douban.html')

@app.route('/movie')
def movie():
    data_list = []

    conn = sqlite3.connect('movieTop250')
    cur = conn.cursor()
    sql = "select * from moviesTop250"
    data = cur.execute(sql)
    for item in data:
        data_list.append(item)

    cur.close()
    conn.close()

    return render_template('movie.html', movies=data_list)

@app.route('/score')
def score():
    x_list = []
    y_list = []
    conn = sqlite3.connect('movieTop250')
    cur = conn.cursor()
    sql = "select score, count(score) from moviesTop250 group by score"
    data = cur.execute(sql)
    for item in data:
        x_list.append(item[0])   # echarts内容中都是字符串数值
        y_list.append(item[1])

    cur.close()
    conn.close()
    return render_template('score.html', x_list=x_list, y_list=y_list)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)