@echo off
call conda activate base
call conda create -n llm_code python=3.9 -y
call conda activate llm_code
pip install bpy fake-bpy-module
pip install -r requirements.txt