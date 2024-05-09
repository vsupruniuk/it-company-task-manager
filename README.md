## Task Manager

Task Manager is a web application built with Python and Django framework. It allows users to efficiently manage teams, projects, and tasks in an organized manner.

### Features

- **User Authentication:** Secure user authentication system to ensure only authorized users can access the application.
- **Team Management:** Create, edit, and delete teams. Assign team members and manage team-specific tasks.
- **Project Management:** Organize projects within teams. Add, update, or remove projects easily.
- **Task Tracking:** Efficiently track tasks within projects. Assign tasks to team members and set deadlines.
- **Search Functionality:** Search for teams, projects, or tasks using keywords for quick access.
- **Responsive Design:** Mobile-friendly interface for seamless user experience across devices.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/task-manager.git
   ```

2. Navigate to the project directory:
   ```
   cd task-manager
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application in your web browser at [localhot](http://localhost:8000). Or use deployed [production](https://it-company-task-manager-44bm.onrender.com)

### Usage

1. Create a superuser to access the Django admin panel:
   ```
   python manage.py createsuperuser
   ```
   Or use existing user credentials:
   ```
   username: admin.user
   password: Qwerty12345!
   ```

2. Log in to the app at `/accounts/login/` to manage users, teams, projects, and tasks.
