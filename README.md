# FastAPI HTMX Fullstack Development Template

A comprehensive template for building fullstack web applications using FastAPI and HTMX. This project is designed to provide a robust starting point for developing modern, dynamic, and scalable web applications.

## Features

- **FastAPI**: A high-performance web framework for building APIs with Python 3.7+.
- **HTMX**: Simplifies building dynamic web applications without the need for a frontend framework.
- **SQLModel & SQLAdmin**: Seamless database integration and ORM with SQLModel and Admin interface with SQLAdmin.
- **Jinja2**: Server-side templating for rendering dynamic HTML.
- **User Authentication**: Secure user authentication with `bcrypt`, `passlib`, and `fastapi-sessions`.
- **Environment Configuration**: Easy-to-manage environment variables using `python-dotenv`.
- **Production-Ready**: Includes tools like `uvicorn` and `uvloop` for deploying high-performance applications.



## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RexsyBima/fastapi-htmx-fullstack-template.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add required variables, e.g.,
     ```
     DATABASE_URL=sqlite:///./test.db
     SECRET_KEY=your-secret-key
     ```

5. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- Build dynamic pages with HTMX by integrating HTML snippets in `templates/`.
- Leverage FastAPI's dependency injection for robust API design.
- Manage SQL databases with SQLModel's ORM capabilities.
- Use the integrated session management for user authentication.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HTMX Documentation](https://htmx.org/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
