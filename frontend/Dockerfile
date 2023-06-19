# Use the official Node.js 16 image as the base image
FROM node:16

COPY package*.json ./
RUN npm install
COPY public public
COPY src src
COPY vite.config.js ./

# Expose port 3000 to the host machine
EXPOSE 3000

# Set the command to run when the container starts
CMD [ "npm", "run", "dev" ]
