FROM node:18

WORKDIR /app

COPY . .

RUN npm install && npm run build

# Use nginx to serve the build folder
FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
