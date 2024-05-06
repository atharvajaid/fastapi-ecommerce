# Ecommerce API with Fast API Framework

Successfully built a RESTful API using FastAPI to handle product management within an e-commerce platform. Leveraging FastAPI documentation resources, I've incorporated all necessary functionalities, including JWT-based authentication and authorization. Additionally, I've implemented pagination using query parameters for limit and skip. While some tasks were straightforward, others required deeper understanding, leading to occasional challenges and less precise outcomes.

## Table of Contents

- [Ecommerce API with Fast API Framework](#ecommerce-api-with-fast-api-framework)
  - [Table of Contents](#table-of-contents)
  - [DIR Structure](#dir-structure)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [API Endpoints](#api-endpoints)
  - [Screenshots](#screenshots)
  - [Installation](#installation)
  - [Usage](#usage)


## DIR Structure
<pre>
- fastapi-ecommerce [Folder]
- sql_app [Folder]
    - auth.py
    - main.py
    - crud.py
    - database.py
    - models.py
    - schemas.py
    - sqlconnect.py
    - run.py
- sql_app.db
</pre>

## Features
- **Managing Product Endpoints:**
	- Offering comprehensive CRUD operations for handling product details, encompassing creation, retrieval, updating, and deletion.
- **Ensuring User Authentication:**
	- Implementing secure user authentication via JWT (JSON Web Token) to ensure robust access control and identity verification.
- **Seamless Integration with Swagger / FastAPI:**
	- Integrating Swagger UI or ReDoc seamlessly for extensive API documentation, providing developers with clear and accessible guidance to effectively understand and utilize the API.


## Technologies Used

- **FastAPI:** 
	- A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
 - **SQLite::** 
	- A widely-used, lightweight, open-source, and self-contained relational database management system (RDBMS) that can be embedded within applications.
- **JWT Authentication:** 
	- Implementing JSON Web Token authentication for secure user authentication.
- **Pydantic:** 
	- A data validation and settings management library for Python, often used with FastAPI.
- **Uvicorn:** 
	- A lightweight ASGI server that serves FastAPI applications. It is used for running FastAPI applications in production.
- **SQLAlchemy:** 
	- An SQL toolkit and Object-Relational Mapping (ORM) library for Python, useful for database interactions.



## API Endpoints



| Endpoint                          | HTTP Method | Path                                      | Description                                              |
|-----------------------------------|-------------|-------------------------------------------|----------------------------------------------------------|
| Product List                      | GET         | `/products/`                              | Get a list of all products                               |
| Create Product                    | POST        | `/products/`                              | Create a new product                                     |
| Retrieve Product by ID            | GET         | `/products/{id}/`                         | Get details of a specific product by ID                  |
| Update Product by ID              | PUT         | `/products/{id}/`                         | Update details of a specific product by ID               |
| Delete Product by ID              | DELETE      | `/products/{id}/`                         | Delete a specific product by ID                          |
| User List                         | GET         | `/users/`                                 | Get a list of all users                                  | 
| User Signup                       | POST        | `/auth/`                                  | Register a new user                                      |
| User Login                        | POST        | `/auth/token/`                            | Authenticate and generate access tokens for a user       |
| Swagger UI                        | -           | `/docs/`                                  | Swagger UI for API documentation                         |



## Screenshots 

![image]()


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/atharvajaid/FastAPI-Ecommerce
   ```

2. **Navigate to the project directory:**

   ```bash
   FastAPI-Ecommerce
   ```


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI development server:**

   ```bash
   python run.py
   ```

   The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

3. **Access the Swagger UI:**

   - Swagger UI: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)



