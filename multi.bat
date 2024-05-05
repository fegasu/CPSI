@echo off
cd apirest
start python main.py
start python routes.py
cd ..
timeout 5
cls
start chrome http://127.0.0.1:8000
