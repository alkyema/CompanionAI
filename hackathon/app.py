from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variables to store data
last_posted_data = {}  # To store the last POSTed user info
medication_reminders = []  # To store medication reminders

# Endpoint to submit user info
@app.route('/submit-info', methods=['GET', 'POST'])
def submit_info():
    global last_posted_data
    
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        mobile = data.get('mobile')
        address = data.get('address')
        blood_group = data.get('blood_group')
        gender = data.get('gender')
        age = data.get('age')


        last_posted_data = {
            "name": name,
            "mobile": mobile,
            "address": address,
            "blood_group": blood_group,
            "gender": gender,
            "age":age
        }
        return jsonify(last_posted_data)
    
    else:
        if last_posted_data:
            return jsonify(last_posted_data)
        else:
            return "No data has been submitted yet.", 200

# Endpoint to add medication reminder
@app.route('/add-reminder', methods=['POST'])
def add_reminder():
    data = request.get_json()
    
    patient_name = data.get('patient_name')
    medicine = data.get('medicine')
    time = data.get('time')
    days = data.get('days')
    
    # Add the reminder to the list
    reminder = {
        "patient_name": patient_name,
        "medicine": medicine,
        "time": time,
        "days": days
    }
    medication_reminders.append(reminder)
    
    return jsonify({"message": "Reminder added successfully", "reminder": reminder})

# Endpoint to view all medication reminders
@app.route('/view-reminders', methods=['GET'])
def view_reminders():
    if medication_reminders:
        return jsonify(medication_reminders)
    else:
        return "No medication reminders have been added yet.", 200

if __name__ == '__main__':
    app.run(debug=True)
