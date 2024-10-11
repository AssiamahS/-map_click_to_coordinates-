from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinates', methods=['POST'])
def coordinates():
    data = request.get_json()
    lat = data['latitude']
    lon = data['longitude']
    return jsonify({'latitude': lat, 'longitude': lon})

if __name__ == '__main__':
    app.run(debug=True)

