import random
import time
from flask import Flask, render_template, jsonify, request, redirect, url_for


app = Flask(__name__)

# Simulated sensor data (you can replace this with actual data)
sensor_data = {
    'temperature': 0,
    'humidity': 0,
    'soil_moisture': 0,
    'light_level': 0
}

# Optimal ranges for parameters
optimal_ranges = {
    'temperature': (70, 85),
    'humidity': (40, 60),
    'soil_moisture': (30, 70),
    'light_level': (200, 800)
}
global temp_min
global temp_max
temp_min = 65
temp_max = 80

def generate_random_data():
    while True:
        print(temp_max, temp_min)
        sensor_data['temperature'] = round(random.uniform(temp_min, temp_max), 2)
        sensor_data['humidity'] = round(random.uniform(40, 60), 2)
        sensor_data['soil_moisture'] = random.randint(0, 100)
        sensor_data['light_level'] = random.randint(0, 1000)
        time.sleep(5)  # Update data every 5 seconds
    

@app.route('/')
def dashboard():
    return render_template('controls.html', optimal_ranges=optimal_ranges)

@app.route('/update_range', methods=['POST'])
def update_range():
    # Retrieve the updated range values from the form
    temperature_min = float(request.form.get('temperature_min'))
    temperature_max = float(request.form.get('temperature_max'))
    sensor_data['temperature'] = round(random.uniform(temperature_min, temperature_max), 2)
    sensor_data['humidity'] = round(random.uniform(temperature_min, temperature_max), 2)
    sensor_data['soil_moisture'] = round(random.uniform(temperature_min, temperature_max), 2)
    sensor_data['light_level'] = round(random.uniform(temperature_min, temperature_max), 2)
    temp_min=temperature_min
    temp_max=temperature_max
    print(temp_min, temp_max)
    # Retrieve other parameter range values similarly

    # Update the optimal_ranges dictionary with the new values
    optimal_ranges['temperature'] = (temperature_min, temperature_max)
    print(sensor_data)
    # Update other parameter ranges similarly

    # Redirect to the dashboard or provide a success message
    return render_template('controls.html', optimal_ranges=optimal_ranges)


@app.route('/data')
def get_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    import threading
    data_thread = threading.Thread(target=generate_random_data)
    data_thread.start()
    app.run(debug=True)