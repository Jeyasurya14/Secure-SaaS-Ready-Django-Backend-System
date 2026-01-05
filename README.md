# Secure SaaS-Ready Django Backend System

> A production-grade, scalable backend foundation designed for modern SaaS applications. Built with Django Rest Framework, Docker, and PostgreSQL.

## 🚀 Key Features

### 🔐 Authentication & Security
*   **JWT Authentication**: Secure stateless authentication using JSON Web Tokens.
*   **Role-Based Access Control (RBAC)**: Distinct permissions for `Admin`, `Staff`, and `User` roles.
*   **Secure Password Hashing**: Industry-standard encryption for user credentials.
*   **Token Rotation**: Refresh token mechanism for enhanced security.

### 📊 Dashboard & Analytics
*   **API Logger**: Middleware to track and log every API request (User, Endpoint, Status Code, IP).
*   **User Stats**: Admin endpoints to view active users, growth trends, and activity logs.

### ⚙️ Production Ready
*   **Dockerized**: Fully containerized with `Dockerfile` and `docker-compose` for consistent environments.
*   **PostgreSQL**: Configured for high-performance relational database management.
*   **Nginx Strategy**: Ready for reverse-proxy configuration.
*   **Environment Config**: Strict separation of secrets using `.env` files.

---

## 🛠️ Technology Stack
*   **Framework**: Django 4.2+, Django Rest Framework (DRF)
*   **Database**: PostgreSQL (Production), SQLite (Dev)
*   **Auth**: SimpleJWT
*   **Documentation**: Swagger UI & Redoc (`drf-yasg`)
*   **Deployment**: Docker, Gunicorn, WhiteNoise

---

## 💻 Local Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Jeyasurya14/Secure-SaaS-Ready-Django-Backend-System.git
    cd Secure-SaaS-Ready-Django-Backend-System
    ```

2.  **Run with Docker (Recommended)**
    ```bash
    cd backend
    docker-compose up --build
    ```
    The API will be available at `http://localhost:8000`.

3.  **Manual Setup (Optional)**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

---

## 📖 API Documentation
Once the server is running, you can access the interactive API docs:
*   **Swagger UI**: `/swagger/` (e.g., `http://localhost:8000/swagger/`)
*   **Redoc**: `/redoc/`

---

## 🌍 Deployment
This project is configured for seamless deployment on platforms like **Render**, **AWS**, or **DigitalOcean**.

*   **Render**: Push to GitHub, and Render will auto-deploy using the `render.yaml` blueprint.
*   **Docker**: Use `docker-compose.prod.yml` for VPS deployment.

For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md) or [RENDER_DEPLOY.md](RENDER_DEPLOY.md).

---

## 👤 Default Admin
*   **Email**: `admin@example.com`
*   **Password**: `SecurePass123!`
*(Change this immediately after your first login)*
