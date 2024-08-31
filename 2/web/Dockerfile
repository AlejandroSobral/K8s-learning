# This line specifies the base image for our container.
# We're using the official Python image, which provides a minimal Python environment.
FROM python

# This line sets the working directory inside the container.
# All subsequent commands will be executed in this directory.
WORKDIR /app

# This line installs the Flask framework using pip, the Python package manager.
# Flask is a web framework for building web applications in Python.
RUN pip install flask
RUN pip install pymongo
RUN pip install docker
RUN pip install pyyaml

# This line exposes port 5000 of the container.
# This allows external applications to access the web application running inside the container
# on port 5000.
EXPOSE 5000

# This line **copies the contents of the directory /api from the build context**
# (the directory where the Dockerfile is located) to the working directory (/app)
# inside the container. 
COPY /api .

# This line defines the default command that will be executed when the container starts.
# In this case, it runs the Python interpreter ("python") with the argument "app.py".
# This assumes your web application is defined in a file named "app.py". 
CMD  ["python", "app.py"]
