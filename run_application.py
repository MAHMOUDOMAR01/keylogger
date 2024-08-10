import os

def run_application(app_path):
    if os.path.isfile(app_path):
        try:
            os.system(app_path)
        except Exception as e:
            print(f"Error running {app_path}: {e}")
    else:
        print(f"File not found: {app_path}")

# مثال على الاستخدام
run_application("notepad.exe")
