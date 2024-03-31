# Use a base image with Python 3 installed
FROM python:3.8

# Set the working directory in the container
WORKDIR /assignment3

# Copy the contents of your project into the container
COPY . /assignment3

# Install the required Python packages using pip
RUN pip install --no-cache-dir fastapi uvicorn jupyter spacy flask flask-restful flask-sqlalchemy streamlit graphviz mypy

# Download the Spacy English model
RUN python -m spacy download en_core_web_sm

# Expose the ports for FastAPI, Flask, and Streamlit
EXPOSE 8000 5000 8501

# start for sh file
COPY start_web.sh /assignment3/start_web.sh
RUN chmod +x /assignment3/start_web.sh


CMD ["/assignment3/start_web.sh"]
