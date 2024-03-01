# landing

# Cloning and Running a Django Project from GitHub

This guide will walk you through the steps to clone and run a Django project from GitHub.

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Python
- pip (Python package installer)
- Git

## Steps
1. **Clone the Repository:** Open your terminal and run the following command to clone the repository:

```git clone https://github.com/JoseArQ/landing.git```

2. **Navigate to the Project Directory:** Change your current directory to the cloned project directory:

```cd landing```

3. **Set up a Virtual Environment (Optional but Recommended):** Create and activate a virtual environment for the project to isolate its dependencies:

```
python -m venv <venv-name>
source <venv-name>/bin/activate # For Linux/Mac
<venv-name>\Scripts\activate.bat # For Windows
```

4. **Install Dependencies:** Use pip to install the project dependencies specified in the `requirements.txt` file:

```
pip install -r requirements.txt
```

5. **Run the Development Server:** Start the Django development server:

```
python manage.py runserver
```

6. **Access the Project:** Open your web browser and go to `http://localhost:8000` to access the running Django project.