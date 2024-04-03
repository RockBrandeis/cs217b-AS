# Assume a base image with Python 3 installed
FROM python:3.8

# Find out the working directory
WORKDIR /assignment3
COPY . /assignment3

# Install the required Python packages using pip, and the Spacy English model as well
RUN pip install --no-cache-dir fastapi uvicorn jupyter spacy flask flask-restful flask-sqlalchemy streamlit graphviz mypy
RUN python -m spacy download en_core_web_sm

# Expose the ports for FastAPI, Flask, and Streamlit, so they can run at the same time
EXPOSE 8000 5000 8501

# start for sh file, it will run three commands for three different server at the same time
COPY start_web.sh /assignment3/start_web.sh
RUN chmod +x /assignment3/start_web.sh


CMD ["/assignment3/start_web.sh"]
