import sys
import re

def extract_app_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    app_name = re.search(r'### Application Name\n\n(.*?)\n', content, re.DOTALL)
    repo_name = re.search(r'### Repository Name\n\n(.*?)\n', content, re.DOTALL)
    helm_chart_name = re.search(r'### Helm Chart Name\n\n(.*?)\n', content, re.DOTALL)
    helm_path = re.search(r'### Helm Path\n\n(.*?)\n', content, re.DOTALL)
    app_version = re.search(r'### Application Version\n\n(.*?)\n', content, re.DOTALL)
    environment = re.search(r'### Environment\n\n(.*?)\n', content, re.DOTALL)
    
    extracted_info = {
        "Application Name": app_name.group(1).strip() if app_name else "Not found",
        "Repository Name": repo_name.group(1).strip() if repo_name else "Not found",
        "Helm Chart Name": helm_chart_name.group(1).strip() if helm_chart_name else "Not found",
        "Helm Path": helm_path.group(1).strip() if helm_path else "Not found",
        "Application Version": app_version.group(1).strip() if app_version else "Not found",
        "Environment": environment.group(1).strip() if environment else "Not found",
    }

    # Save extracted info to a file
    with open("extracted_info.txt", "w", encoding="utf-8") as output_file:
        for key, value in extracted_info.items():
            output_file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_app_info.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    extract_app_info(file_path)
