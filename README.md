# Auth Login & Protect API

A secure authentication API built with **FastAPI** and **Supabase Auth**. The project demonstrates user signup, login, JWT-based authentication, protected API routes, logout, and interactive Swagger UI documentation.

## Features

* User registration with Supabase Auth
* User login with email and password
* JWT access token authentication
* Refresh token support
* Protected user profile endpoint
* Protected dashboard endpoint
* Protected logout endpoint
* Public API endpoint
* Reusable FastAPI authentication dependency
* Swagger UI with Bearer Token authorization
* Environment variables for sensitive Supabase credentials

## Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Supabase Auth**
* **Pydantic**
* **python-dotenv**
* **Git & GitHub**
* **Swagger UI** via FastAPI

## Project Structure

```text
auth-login-protect/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> `.env` is used locally but is excluded from GitHub through `.gitignore`.

## Environment Setup

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

Replace the values with your own Supabase Project URL and Anon Key.

**Never commit your `.env` file or Supabase secrets to GitHub.**

## Installation

Clone the repository:

```bash
git clone https://github.com/abdulrehmanatif-alt/auth-login-protect.git
cd auth-login-protect
```

Create and activate a virtual environment:

### Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

Create your `.env` file with your Supabase credentials.

## Running the API

Start the FastAPI development server:

```cmd
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger UI

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

The protected routes use Bearer Token authentication.

Click **Authorize**, enter your Supabase access token, and then use **Try it out** to test protected endpoints.

## API Reference

| Method | Endpoint               | Authentication | Purpose                             |
| ------ | ---------------------- | -------------- | ----------------------------------- |
| GET    | `/`                    | No             | Server status                       |
| POST   | `/auth/signup`         | No             | Create a new user                   |
| POST   | `/auth/login`          | No             | Authenticate and receive JWT tokens |
| POST   | `/auth/logout`         | Yes            | Log out the authenticated user      |
| GET    | `/public/info`         | No             | Access public information           |
| GET    | `/protected/profile`   | Yes            | View authenticated user's profile   |
| GET    | `/protected/dashboard` | Yes            | Access protected dashboard          |

## Authentication Flow

The authentication flow works as follows:

```text
Client
   │
   ├── Sign Up / Login
   │
   ▼
Supabase Auth
   │
   ├── Access Token (JWT)
   └── Refresh Token
   │
   ▼
FastAPI Backend
   │
   ├── Authorization: Bearer <access_token>
   │
   ▼
Supabase Token Verification
   │
   ├── Valid → Protected resource
   │
   └── Invalid/Expired → 401 Unauthorized
```

## Protected Routes

Protected endpoints require an HTTP Authorization header:

```text
Authorization: Bearer <access_token>
```

The FastAPI authentication dependency extracts the token and verifies it with Supabase.

Invalid or expired tokens are rejected with:

```json
{
  "detail": "Invalid or expired token"
}
```

## Status Codes

| Status Code | Meaning                                     |
| ----------- | ------------------------------------------- |
| `200`       | Successful request                          |
| `201`       | User successfully created                   |
| `204`       | Successful logout with no response body     |
| `400`       | Invalid or missing input                    |
| `401`       | Missing, invalid, or expired authentication |

## Security

Sensitive configuration is stored in environment variables rather than hard-coded in the source code.

The `.gitignore` file prevents the `.env` file from being committed:

```text
venv/
.env
__pycache__/
```

Users cloning this repository must provide their own Supabase credentials.

## Testing

The API was tested through FastAPI Swagger UI.

Successful tests included:

* User signup → `201`
* User login → `200`
* Public information → `200`
* Protected profile with valid token → `200`
* Protected dashboard with valid token → `200`
* Invalid token → `401`
* Logout → `204`

## Project Status

The required authentication and API protection stages have been completed.

The project includes:

* Supabase authentication
* JWT token verification
* Protected routes
* Reusable authentication dependency
* Logout
* Swagger Bearer authentication
* GitHub publication
* Environment variable protection

## Author

**Abdulrehman Atif**

Software Engineering Student