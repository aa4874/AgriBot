from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

AUTH_TOKEN = 'jwLmGGC7dKKgft'

def send_to_blynk(pin, value):
    url = f"https://blynk.cloud/external/api/update?token={AUTH_TOKEN}&{pin}={value}"
    response = requests.get(url)
    return response.text

# Global dictionary to hold sensor values
sensor_data = {
    "moisture": 0,
    "temperature": 0,
    "pump_status": 0,
    "pump_control": 0
}

@app.route('/')
def dashboard():
    return render_template('index.html', data=sensor_data)

@app.route('/update_sensor', methods=['POST'])
def update_sensor():
    data = request.get_json()
    sensor_data.update({
        "moisture": data.get("moisture", 0),
        "temperature": data.get("temperature", 0),
        "pump_status": data.get("pump_status", 0),
        "pump_control": data.get("pump_control", 0)
    })
    return jsonify({"status": "success", "data": sensor_data})

if __name__ == '__main__':
    app.run(debug=True)
