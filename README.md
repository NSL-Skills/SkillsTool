# Skills-Outcome Extraction and Comparison Tool

## Description

The Skills-Outcome Extraction and Comparison Tool is designed to connect industry employers with students graduating from academic programs. This tool analyzes employers' career pages and job postings to understand the skills and knowledge required for various roles in the job market.

By scraping website data, identifying relevant keywords, and clustering and classifying these skills, the tool aims to bridge the gap between potential employees and employers. It empowers students to gain insights into the skills they need to succeed in their desired careers, while helping employers articulate their expectations clearly.


## Key Features
- **Data Scraping**: Automatically collects job postings and career information from employer websites.
- **Keyword Identification**: Extracts essential skills and qualifications from job descriptions.
- **Clustering and Classification**: Groups similar skills to provide a clearer understanding of industry requirements.

## Installation Instructions

### For Users

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/NSL-Skills/SkillsTool.git
   ```

2. **Navigate to the Project Directory**:
   Change to the directory of the cloned repository:
   ```bash
   cd SkillsTool
   ```

3. **Open the Project in Your Browser**:
   Open the `index.html` file in your web browser. You can do this by either:
   - Double-clicking on the `index.html` file in your file explorer.
   - Running a local server (optional) for a better experience. You can use Python's built-in server:
   ```bash
   python -m http.server
   ```
   Then navigate to `http://localhost:8000` in your web browser.

4. **Start Using the Tool**:
   Follow the on-screen instructions in the web application to start using the Skills-Outcome Extraction and Comparison tool.


### For Developers

1. **Clone the Repository**:
   Clone the repository to your local machine using the same command as above.

2. **Set Up a Virtual Environment**: 
   Create a virtual environment to isolate the project dependencies. Run the following command:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. **Install Requirements**:
   Install the necessary packages listed in `requirements.txt`: 
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Tests**:
   To run the tests located in the `tests/` folder, use: 
   ```bash
   python -m unittest discover -s tests
   ```


## Contributing
We welcome contributions! If you'd like to help out, please follow these steps:

1. **Fork the repository** to create your own copy.
2. **Clone your fork** to your local machine.
3. **Create a new branch** for your changes.
4. **Make your edits** and commit them with a descriptive message.
5. **Push your changes** to your fork.
6. **Open a Pull Request** against the main repository.

Thank you for your interest in contributing!


### License
This project is licensed under the [GPL v3.0 License](https://www.gnu.org/licenses/gpl-3.0.html). See the LICENSE file for details.


### Contact
For inquiries, please contact me at [thomastrebat@my.unt.edu](mailto:thomastrebat@my.unt.edu).


### Acknowledgments
I would like to thank my professors and mentors at the University of North Texas for their invaluable support and guidance throughout this project. Special thanks to my fellow students who collaborated with me and shared their insights. 

I also acknowledge the open-source libraries and tools that made this project possible, including NumPy, Pandas, scikit-learn, Pyodide, YAKE, and FuzzyWuzzy.

Lastly, I appreciate the support from the Department of Defense (DoD) for their grant funding this project.








