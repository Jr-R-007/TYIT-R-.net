Third-Year Engineering Lab Projects 
This repository contains a collection of lab projects developed during my third year of engineering. The projects cover a diverse technical landscape, including Artificial Intelligence, full-stack web development (.NET and
MERN architectures), and Biomedical Research/Machine Learning (BMRL) concepts.

🚀 Project Overview
 Artificial Intelligence
2. (AI)Focus: Algorithm implementation, data analysis, and predictive modeling.
3. Key Features: Implementation of search algorithms, neural networks, and automated problem-solving agents.
4. Tech Stack: Python, NumPy, Pandas, Scikit-Learn, TensorFlow/PyTorch.
  

  NET Enterprise Application
  Focus: Scalable backend architectures and robust desktop/web service development.
  Key Features: Secure user authentication, RESTful API design, and structured database migrations.
  Tech Stack: C#, .NET Core / ASP.NET, Entity Framework, SQL Server.
  
   Biomedical Research Lab (BMRL) Integration
   Focus: Signal processing and machine learning applied to healthcare and biological data.
   Key Features: Feature extraction from physiological signals (e.g., ECG/EEG) and health-status classification.
   Tech Stack: MATLAB / Python, SciPy, Biosignals Notebooks, Seaborn.
   
   4. MERN Full-Stack Application
    Focus: Modern, dynamic web application development with a JavaScript-only ecosystem.
    Key Features: Single Page Application (SPA) design, state management, and real-time database updates.
    Tech Stack: MongoDB, Express.js, React.js, Node.js, Tailwind CSS.

🛠️ Getting Started
Prerequisites
Ensure you have the following runtime environments installed:
Python 3.x
.NET SDK (6.0 or later)
Node.js (v18 or later)
MongoDB Compass or a local instance

Installation & Execution
Running the MERN Stack Project
Navigate to the directory: cd mern-project
Install backend dependencies: cd backend && npm install
Configure environment variables in a .env file.
Start backend server: npm start
Install frontend dependencies: cd ../frontend && npm install
Start frontend client: npm start

Running the .NET Project
Navigate to the directory: cd dotnet-project
Restore dependencies: dotnet restore
Update the connection string in appsettings.json.
Run database updates: dotnet ef database update 
Launch application: dotnet run

Running the AI & BMRL Scripts
Navigate to the respective folder: cd ai-project or cd bmrl-project
Install required packages: pip install -r requirements.txt
Execute the core notebooks or scripts: python main.py

📁 Repository Structure
├── AI-Projects/          # Python scripts, datasets, and Jupyter notebooks
├── DotNet-Projects/      # C# source code, controllers, and database configurations
├── BMRL-Projects/        # Biomedical signal analysis and processing scripts
├── MERN-Projects/        # Full-stack JavaScript application split into client/server
└── README.md             # Project documentation
