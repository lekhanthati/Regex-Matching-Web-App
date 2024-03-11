from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template('home.html')

@app.route('/mail')
def func2():
    return render_template('mail.html')


@app.route('/result')
def func3():
    import re
    string = request.args.get('string')
    pattern = request.args.get('pattern')

    stringList = re.findall(pattern,string)

    return render_template('result.html', stringList = stringList)


@app.route('/mail_result')
def func4():
    import re
    mail = request.args.get('mail') 
    if bool(re.findall('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail)):
        return render_template('mail_result.html', r = 'The mail ID is valid')
    else:
        return render_template('mail_result.html', r = 'The mail ID is not valid')


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000)