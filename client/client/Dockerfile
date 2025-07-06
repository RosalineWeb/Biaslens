# Stage 1: Build React app using Node
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy project files and build the app
COPY . .
RUN npm run build

# Stage 2: Use Nginx to serve the built app
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
