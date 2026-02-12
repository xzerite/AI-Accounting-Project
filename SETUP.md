# Setup Instructions for AI Accounting Fraud Dashboard

## Prerequisites
Before you begin, ensure you have met the following requirements:

- **Node.js**: Install Node.js from [Node.js official website](https://nodejs.org/).
- **npm**: Node Package Manager should come installed with Node.js.
- **Git**: Make sure Git is installed on your machine. You can download it from [Git official website](https://git-scm.com/).

## Installation Steps
1. **Clone the Repository**  
   Open your terminal and run the following command to clone the repository:
   
   ```bash
   git clone https://github.com/xzerite/AI-Accounting-Project.git
   cd AI-Accounting-Project
   ```

2. **Install Dependencies**  
   Navigate to the project directory and install the required packages by running:
   
   ```bash
   npm install
   ```

3. **Configuration**  
   - Create a `.env` file in the root of the project directory.  
   - Copy the contents from `.env.example` provided in the repository and customize them according to your environment settings.
   
   ```bash
   cp .env.example .env
   ```

4. **Start the Server**  
   You can now start the development server by running:
   
   ```bash
   npm start
   ```

5. **Access the Dashboard**  
   Open your web browser and go to `http://localhost:3000` to access the AI Accounting Fraud Dashboard.

## Troubleshooting
- If you encounter any issues, please check the following:
  - Ensure all dependencies are installed properly.
  - Double-check your configuration values in the `.env` file.
  - Consult the project's issue tracker for known bugs and fixes.

## Contribution
Feel free to contribute to the project by opening issues or submitting pull requests. 
