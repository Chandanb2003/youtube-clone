# Step 1: Start from a base image with Node.js installed
FROM node:18

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the `package.json` and `package-lock.json` (if exists)
COPY package*.json ./

# Step 4: Install the npm dependencies
RUN npm install

# Step 5: Copy the entire application (including `index.js` and others)
COPY . .

# Step 6: Expose the port your app will run on (this should match your app)
EXPOSE 5000

# Step 7: Define the command to run your app
CMD ["npm", "start"]
