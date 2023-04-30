# Use the official Node.js 16 image as the base image
FROM node:16


# Copy the package.json and package-lock.json files to the container
#COPY package*.json ./
#
## Install the dependencies
#RUN npm install
#
## Copy the rest of the application code to the container
#COPY . .
#
## Build the application for production
#RUN npm run build
COPY package*.json ./
RUN npm install
COPY public public
COPY src src
COPY vite.config.js ./
RUN npm run build


# Expose port 3000 to the host machine
EXPOSE 3000

# Set the command to run when the container starts
CMD [ "npm", "run", "serve" ]
