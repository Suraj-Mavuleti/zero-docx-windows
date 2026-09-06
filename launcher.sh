#!/bin/bash
# AUTO-UPDATER
cd /home/suraj/.gemini/antigravity/scratch/zero_suite/zero-docx-windows
git pull origin main --quiet
python3 zero_docx_gui.py
