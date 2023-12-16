# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# informs Docker that the container listens on the specified network ports at runtime.
EXPOSE 8501

WORKDIR /app
COPY . /app

# Used to set executables that will always run when the container is initiated
ENTRYPOINT ["streamlit", "run"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["app.py"]