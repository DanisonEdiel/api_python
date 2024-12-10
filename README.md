
# Python GraphQL API with FastAPI and Ariadne

This repository contains a simple GraphQL API built with **FastAPI** and **Ariadne**. It demonstrates how to set up a Python backend to serve GraphQL queries, including support for CORS and integration with a Vue.js frontend.

---

## **Requirements**

- Python `3.12.4`
- Pip (Python package manager)
- A modern web browser to test the GraphQL interface

---

## **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install fastapi ariadne uvicorn
   ```

5. **Run the Application**
   ```bash
   uvicorn server:app --reload
   ```

6. **Access the API**
   Open your browser and navigate to:
   ```
   http://localhost:8000/graphql
   ```

## **Notes**

- Ensure your Python version is `3.12.4` or higher.
- Use a `.env` file for production secrets if needed.

---

## **License**

This project is licensed under the MIT License.
