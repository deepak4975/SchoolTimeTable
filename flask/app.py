from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkRoom', methods=['GET'])
def check():
    name = request.args.get('name')  # Get name from form
    return render_template('checkRoom.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
