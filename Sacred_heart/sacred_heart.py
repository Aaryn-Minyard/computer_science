from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, secret value

# Configure the SQLite database (persistent storage)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------------
# Database Models
# ------------------------

class User(db.Model):
    """
    A general user model to cover doctors, admins, and patients.
    The 'role' field determines which type of user it is.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # e.g., 'doctor', 'admin', 'patient'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialty = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Link to the login user account
    # Relationship to patients (one-to-many)
    patients = db.relationship('Patient', backref='doctor', lazy=True)
    
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(200))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))  # Assigned doctor

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    appointment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='scheduled')  # e.g., scheduled, completed, cancelled

# ------------------------
# Routes for Authentication
# ------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Find the user in the database
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['role'] = user.role
            flash("Logged in successfully.", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# ------------------------
# Core Dashboard (Example for Doctors)
# ------------------------

@app.route('/dashboard')
def dashboard():
    # Only allow logged-in users to view the dashboard
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # For this example, show the doctor dashboard if the user is a doctor.
    if session.get('role') == 'doctor':
        # Get the doctor profile using the linked user account
        doctor = Doctor.query.filter_by(user_id=session['user_id']).first()
        if doctor:
            patients = Patient.query.filter_by(doctor_id=doctor.id).all()
            return render_template('doctor_dashboard.html', doctor=doctor, patients=patients)
        else:
            flash("Doctor profile not found.", "warning")
            return redirect(url_for('login'))
    else:
        flash("Dashboard access for your role is not implemented yet.", "info")
        return "Dashboard for role: " + session.get('role')

# ------------------------
# Patient Management (Admin Example)
# ------------------------

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    # For now, assume that only an admin can add patients.
    if 'user_id' not in session or session.get('role') != 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        doctor_id = request.form['doctor_id']  # Ensure this ID corresponds to an existing doctor
        new_patient = Patient(name=name, age=int(age), address=address, doctor_id=int(doctor_id))
        db.session.add(new_patient)
        db.session.commit()
        flash("Patient added successfully.", "success")
        return redirect(url_for('list_patients'))
    # For GET, display a simple form (in a real app, include proper error handling and form validation)
    doctors = Doctor.query.all()
    return render_template('add_patient.html', doctors=doctors)

@app.route('/list_patients')
def list_patients():
    if 'user_id' not in session or session.get('role') != 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('login'))
    patients = Patient.query.all()
    return render_template('list_patients.html', patients=patients)

# ------------------------
# Appointment Booking (Simplified)
# ------------------------

@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if 'user_id' not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        # For simplicity, we use the current time; a real app would allow choosing a date/time
        appointment_date = datetime.utcnow()
        appointment = Appointment(doctor_id=int(doctor_id), patient_id=int(patient_id), appointment_date=appointment_date)
        db.session.add(appointment)
        db.session.commit()
        flash("Appointment booked.", "success")
        return redirect(url_for('dashboard'))
    doctors = Doctor.query.all()
    patients = Patient.query.all()
    return render_template('book_appointment.html', doctors=doctors, patients=patients)

# ------------------------
# Main Entry Point
# ------------------------

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
