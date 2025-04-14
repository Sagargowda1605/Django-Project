**Django Study Chatroom App**

A Django-based web application that enables users to register, log in, and participate in topic-specific chatrooms for collaborative study and discussion.

**Features**
User Authentication: Secure registration and login functionality.

Chatrooms: Users can join existing chatrooms or create new ones based on study topics.

Messaging: Real-time messaging within chatrooms to facilitate discussions.

User Profiles: Basic user profile management (planned feature).

Responsive Design: Accessible on various devices (planned feature).

**Technologies Used**
Backend: Django (Python)

Database: SQLite (default; can be switched to PostgreSQL)

Frontend: HTML, CSS, JavaScript

Version Control: Git

**Installation**

Clone the repository:
git clone https://github.com/Sagargowda1605/Django-Project.git
cd Django-Project

Create a virtual environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:
pip install django 

Apply migrations:
python manage.py migrate

Run the server :
python manage.py runserver
