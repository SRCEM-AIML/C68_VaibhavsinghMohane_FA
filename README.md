# Final Assignment: Flask and Django Web Applications

This repository contains a full-stack project that demonstrates the development of web applications using both **Flask** and **Django** frameworks. It also includes **Docker** support for containerization and a **Jenkins pipeline** for CI/CD automation. This project is structured to show how lightweight and heavyweight Python web frameworks can coexist in a real-world deployment scenario.

---

## ✅ Features

### Django Application
- Custom homepage displaying 12 recipe cards (image, name, view button).
- Custom admin panel (not using Django’s default admin site).
- "Add a Recipe" form to submit new recipe name and image.
- Recipes stored in a database (`db.sqlite3`), images saved in `media/recipe_images/`.
- Placeholder pages for recipe details.
- Clean and user-friendly template designs.

### Flask Application
- Lightweight web app using Flask.
- Static and dynamic routing.
- Template rendering with HTML and CSS.
- Organized folder structure for `static/` and `templates/`.

### Docker Integration
- Separate `Dockerfile` for both Flask and Django apps.
- `docker-compose.yml` to run both applications together.
- Simplified containerized development environment.

### Jenkins CI/CD
- Automated build, test, and deployment pipeline using `Jenkinsfile`.

---

## 🧰 Prerequisites

Before running the project, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)
- [Jenkins](https://www.jenkins.io/) (optional, for CI/CD)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/SRCEM-AIML/C68_VaibhavsinghMohane_A2.git
   cd C68_VaibhavsinghMohane_A2
   ```


2. **Set Up Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```


3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Running the Application

Follow the steps below to run both the Flask and Django applications using **Jenkins** and **Docker Compose**.

---

### 1. **Open Jenkins and Create a New Pipeline**

- Launch Jenkins in your browser (usually at `http://localhost:8080`).
- Click on **"New Item"**.
- Enter a name for your project (e.g., `Final_Assignment_Pipeline`).
- Select **"Pipeline"** and click **OK**.

---

### 2. **Configure the Pipeline**

- Scroll down to the **Pipeline** section.
- Under **Definition**, select `Pipeline script from SCM`.
- Choose **Git** as the SCM.
- Enter your repository URL:  
  `https://github.com/SRCEM-AIML/C68_VaibhavsinghMohane_A2.git`
- Set the branch to `main` (or `mohanews` if using that branch).
- Jenkins will automatically use the `Jenkinsfile` from your repo.

---

### 3. **Build the Pipeline**

- Click **Save**, then click **Build Now**.
- Wait for the pipeline to complete all stages:
  - Cloning the repo
  - Building Docker images
  - Running containers via Docker Compose

---

### 4. **Access the Applications**

Once the build succeeds, open your browser and access:

- **Flask App** → [http://localhost:5000](http://localhost:5000)
- **Django App** → [http://localhost:8000](http://localhost:8000)

You should see the respective homepages for both apps.

---

### 📝 Note

If ports 5000 or 8000 are already in use on your machine, you may need to stop other services or update the port mappings in `docker-compose.yml`.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

---

*Crafted with ❤️ by Vaibhavsingh Mohane*
```