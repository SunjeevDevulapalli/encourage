from flask import Flask, render_template, request, url_for
from open_ai_service import get_response

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def encourage():
    if request.method == "POST":
        response = get_response(request.form["user_text"])
        return render_template('encourage.html', content=response)
    else:
        return render_template('encourage.html')

if __name__ == '__main__':
    app.run(debug=True)