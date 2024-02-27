# TOPRESUMEUAM

Brief description of the project.

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/harshit151001/topresumeuam
   ```
2. Navigate to the project directory:
   ```
   cd topresumeuam
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```
5. Apply the migrations:
   ```
   python manage.py migrate
   ```

## Running the Project

1. Start the Django development server:
   ```
   python manage.py runserver
   ```
2. Open your web browser and visit `http://127.0.0.1:8000/`.

## API Endpoints

- `POST /files/`: To upload resume and get text data as response.
- `POST /match-candidates/`: Matches candidates based on job description and resumes.
