from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return 'Hello World!'

# 通过访问路径, 获取用户的整形参数 (还有float等)
@app.route('/user/<int:id>')
def welcome(id):
    return f'hello, {id}'

# 向页面传递一个变量
@app.route('/')
def page():
    time = datetime.date.today()    # 普通变量
    name = ['Jill', 'Eric', 'Paul'] # 列表类型
    task = {'任务': '打扫卫生', '时间': '三小时'}
    return render_template('index.html', var=time, list=name, task=task)

# 表单提交
@app.route('/register')
def register():
    return render_template('register.html')
# 获取表单元素
@app.route('/result', methods=['POST', 'GET'])  # 默认为单独GET
def result():
    if request.method == 'POST':
        result = request.form
    return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
