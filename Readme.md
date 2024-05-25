# Project Blackcoffer Intern Task

## Overview

This project is part of the internship task at Blackcoffer. The project is divided into backend and frontend components.
## Installations

### Backend

1. Navigate to the backend directory:
    ```sh
    cd backend
    ```

2. If you want to create a virtual environment for the setup, do the following:

    - Install the `virtualenv` package(if necessary)
        ```sh
        pip install virtualenv
        ```

    - Create a virtual environment:
        ```sh
        python -m venv myenv
        ```

    - Activate the virtual environment:
        ```sh
        .\myenv\Scripts\activate.ps1
        ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the backend server:
    ```sh
    python run.py
    ```

### Frontend
1. Navigate to fronend2 directory:
    ```sh
    cd frontend2
    ```

2. Install the required packages:
    ```sh
    npm install
    ```

3. Run the frontend development server:
    ```sh
    npm run dev
    ```

## Database Setup

### Initial Database Activation

1. Navigate to the `run.py` file.
2. Uncomment these two lines of code:
    ```python
    from core.models.reportmodel import EnergyReport  
    loadintodb.load_into_db()
    ```
3. Ensure that you add your credentials in the `.env` file to function the database properly. The database used here is PostgreSQL.
 ```sh
DATABASE_URL="postgresql://<username>:<password>@localhost:5432/<database>"
FLASK_ENV="development"
 ```

4. After the database has been set up, comment those lines again to avoid duplicate data entries:
    ```python
    # from core.models.reportmodel import EnergyReport  # Import your models here
    # loadintodb.load_into_db()
    ```

## Project Components

### Backend

- **Testing**: Implemented and conducted tests through postman to ensure the APIs function correctly.
- **APIs**: Created APIs for the dashboard and filter properties 


### Frontend

- **Development**: Set up the frontend environment and developed the necessary components for interaction with the backend.

## Usage

1. Ensure that both the backend and frontend servers are running.
2. Access the application via the frontend development server URL (usually `http://localhost:5173`).

## Notes

- Make sure to have Python and Node.js installed on your system.
- For any issues, ensure all dependencies are correctly installed and the virtual environment is activated for the backend.
