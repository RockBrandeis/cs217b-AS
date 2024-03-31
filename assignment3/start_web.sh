#!/bin/bash

# FastAPI application
uvicorn app_fastapi:app --host 0.0.0.0 --reload --port 8000 &
# Flask application
python myblog.py &
# Streamlit application
streamlit run app_streamlit.py --server.port 8501 &

wait
