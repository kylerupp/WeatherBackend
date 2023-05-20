@echo off
title BACKEND
cd app
cmd /k python -m flask run --host=0.0.0.0
@echo on
