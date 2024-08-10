from setuptools import setup, find_packages

setup(
    name='keylogger_monitor',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'streamlit',
        'psutil',
        'Pillow',
        'boto3',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'run_all = run_all:main',
        ],
    },
)
