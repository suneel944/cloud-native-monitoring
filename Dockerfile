# Official python image
FROM python:3.11-slim-buster as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base as python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

#Install python dependencies in /.venv
COPY Pipfile ./
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH:/usr/local/bin"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

# Run the application
# Set the flask run host for flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port for flask backend
EXPOSE  5000

# Run Gunicorn using the entrypoint
# If the environment variables are not explicitly set when running the Docker container, 
# the default values specified in the ENV instruction will be used in the ENTRYPOINT command.
# For example, the WORKERS environment variable has a default value of 4 set using the ENV instruction. 
# If the WORKERS environment variable is not explicitly set when running the Docker container, Gunicorn will use 
# the default value of 4 for the -w option specified in the ENTRYPOINT command.
ENTRYPOINT ["gunicorn", "app:create_app()", "-b", "0.0.0.0:5000", "-w", "4", "--worker-class", "gevent", "--timeout", "15", "--max-requests", "1000"]