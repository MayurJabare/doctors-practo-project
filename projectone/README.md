# Doctor Listings Django Project

This project is a Django web application that lists doctors with their details and provides filtering options based on specialization and locality. The data is scraped from a specified URL and stored in a database.

## Features

- List of doctors with details including name, specialty, experience, locality, city, clinic name, consultation fee, recommendation percentage, and patient stories.
- Filtering options for specialization and locality.
- Styled form and table for a user-friendly interface.



## Database Schema

To create the database schema, run the following SQL script (assume we are using POSTGRESQL database):

```sql
-- doctors.sql
CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    doctor_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255),
    experience INT,
    locality VARCHAR(255),
    city VARCHAR(255),
    clinic_name VARCHAR(255),
    consultation_fee VARCHAR(255),
    recommendation VARCHAR(255),
    patient_stories VARCHAR(255)
);
```
## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MayurJabare/doctors-practo-project.git
    cd projectone
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Load initial data:**
    ```bash
    python manage.py loaddata doctors.json
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Open the application:**
    Go to `http://127.0.0.1:8000/` in your web browser.
    Go to `http://127.0.0.1:8000/refresh_table` in browser to update database table created.

