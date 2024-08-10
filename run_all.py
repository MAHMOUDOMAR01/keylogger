import subprocess

def run_script(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, text=True, capture_output=True)
        print(f"{script_name} output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr}")

if __name__ == "__main__":
    scripts = [
        'keylogger.py',
        'advanced_keylogger.py',
        'generate_pdf_report.py',
        'ai_analysis.py',
        'performance_monitor.py'
        'dashboard.py',
    ]
    
    for script in scripts:
        run_script(script)
