## 🧠 Backend Dependencies – What Each One Does (Simple Explanation)

### FastAPI
- Modern Python framework to build APIs
- Very fast, easy to write, and auto-generates API docs

### Uvicorn
- Lightweight ASGI server
- Used to run your FastAPI application

### SQLAlchemy
- Python ORM (Object-Relational Mapper)
- Lets you work with databases using Python instead of raw SQL

### passlib[bcrypt]
- Secure password hashing
- Never store plain text passwords in a database

### python-jose
- Used for JWT authentication
- Creates and verifies access tokens for secured APIs

### python-dotenv
- Loads environment variables from a .env file
- Keeps secrets (keys, passwords) out of your code

### python-multipart
- Enables handling forms and file uploads
- Required for login forms and file submissions
