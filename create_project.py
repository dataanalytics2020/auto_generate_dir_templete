import os
import sys

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Created file: {path}")

def create_project_structure(base_path):
    # Create main directory
    create_directory(base_path)

    # Create subdirectories
    create_directory(os.path.join(base_path, "src"))
    create_directory(os.path.join(base_path, "logs"))

    # Create files
    create_file(os.path.join(base_path, "src", "main.py"), "# Main script ")
    create_file(os.path.join(base_path, "src", "config.py"), "# Configuration settings")
    create_file(os.path.join(base_path, "src", "utils.py"), "# Utility functions")
    create_file(os.path.join(base_path, "logs", "log.log"), "")
    create_file(os.path.join(base_path, ".env"), "# Environment variables\n# Add your sensitive data here")
    create_file(os.path.join(base_path, ".gitignore"), "*.log\n.env\n__pycache__/\nlogs/\n.history\n.DS_Store")
    create_file(os.path.join(base_path, "requirements.txt"), "selenium==4.10.0\npython-dotenv==1.0.0")
    create_file(os.path.join(base_path, "README.md"), "#\n\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = input("Enter project name: ")
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    project_path = os.path.join(desktop_path, project_name)
    
    create_project_structure(project_path)
    print(f"Project structure created successfully in {project_path}")