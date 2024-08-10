# Keylogger and Monitoring Tool

## Overview

This project includes various scripts for keylogging, monitoring system performance, generating reports, and more. The components of this project are designed to work together to provide a comprehensive monitoring solution.

## Components

1. **`advanced_keylogger.py`**: Keylogger script for capturing keystrokes.
2. **`ai_analysis.py`**: Analyzes captured data using AI techniques.
3. **`dashboard.py`**: Streamlit app for visualizing keylogging data.
4. **`encryption.py`**: Handles encryption and decryption of data.
5. **`generate_pdf_report.py`**: Generates a PDF report of the logged data.
6. **`performance_monitor.py`**: Monitors system performance.
7. **`run_all.py`**: Main script to run all components sequentially.
8. **`run_application.py`**: Runs a specified application.
9. **`track_user_activity.py`**: Tracks user activity.
10. **`upload_to_s3.py`**: Uploads files to AWS S3 (note: requires AWS credentials).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MAHMOUDOMAR01/keylogger.git


# Keylogger Project

هذا المشروع هو برنامج لتسجيل ضغطات المفاتيح والتقاط لقطات الشاشة. يتضمن المشروع كود Python يستخدم مكتبات مختلفة مثل `pynput` و`PIL` لتتبع النشاط على جهاز الكمبيوتر.

## الوصف

البرنامج يتضمن:
- **تسجيل ضغطات المفاتيح**: يقوم بتسجيل كل مفتاح يتم الضغط عليه في ملف نصي.
- **التقاط لقطات الشاشة**: يقوم بالتقاط لقطات شاشة بشكل دوري.
- **توليد تقارير PDF**: يقوم بإنشاء تقارير PDF بناءً على النشاط المسجل.

## المتطلبات

تأكد من تثبيت المكتبات التالية:

- `pynput`
- `PIL` (أو `Pillow`)
- `fpdf`
- `pywin32` (للويندوز فقط، استخدم `pywin32` للتعامل مع واجهة Windows API)

يمكنك تثبيت المكتبات المطلوبة باستخدام `pip`:

```bash
pip install pynput pillow fpdf pywin32
