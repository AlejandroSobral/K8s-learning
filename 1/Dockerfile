# Base Image
FROM mongo:latest

# Expose MongoDB Port
# This line exposes port 27017 on the container, making it accessible to other applications or containers.
# MongoDB uses port 27017 by default.
EXPOSE 27017

# Persistent Data Volume
# This line defines a volume named `/data/db` within the container. A volume is a persistent storage location that can be shared between containers or mapped to a directory on the host system.
# By using a volume, any data written to the `/data/db` directory will be preserved even if the container is restarted or removed. This is crucial for MongoDB, as it stores its data in this directory.
VOLUME /data/db

# Run MongoDB Server
# This line specifies the default command that will be executed when the container starts. In this case, it runs the `mongod` process, which is the MongoDB server.
# This ensures that the MongoDB server is running within the container when it starts.
CMD ["mongod"]