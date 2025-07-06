FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy all source files
COPY . .

EXPOSE 3000

# Run the server
CMD ["npm", "start"]
