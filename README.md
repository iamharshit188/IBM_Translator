# Flask Language Translator

Flask Language Translator is a simple web application built with Flask that utilizes the IBM Watson Language Translator service to translate text from one language to another.

## Features

- Translate text from one language to another using the IBM Watson Language Translator service.
- Simple and intuitive user interface.
- Responsive design for desktop and mobile devices.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages by running the following command in your terminal or command prompt:

    ```
    pip install -r requirements.txt
    ```

3. Set up an IBM Cloud account and create a Language Translator service instance to obtain the API key and service URL.

## Usage

1. Replace `"your_api_key"` and `"your_service_url"` in `app.py` with your actual IBM Cloud Language Translator credentials.

2. Run the Flask application by executing the following command in the terminal or command prompt:

    ```
    python app.py
    ```

3. Open a web browser and go to `http://127.0.0.1:5000/` to access the Flask application.

4. Enter some text to translate and select the target language from the dropdown menu.

5. Click the "Translate" button to see the translated text.

## File Structure

The project directory structure is as follows:
`
project/
│
├── app.py
│
└── templates/
    └── index.html
`
- `app.py`: Python script containing the Flask application code.
- `templates/`: Directory containing HTML templates for the frontend.

## Dependencies

- Flask: Micro web framework for Python.
- IBM Watson Language Translator SDK: Python SDK for the IBM Watson Language Translator service.

