# README File Generator

This project is a README file generator. It prompts users for essential project information and creates a README.md file.

## Installation

Clone the repository and install dependencies:

```bash
# Navigate to the project directory
cd readme-file-generator

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the generator script:

```bash
python main.py
```

The script will prompt you for the following information:

1. **Title**: Your project title
2. **Description**: A brief description of your project
3. **Installation**: Installation instructions
4. **Usage**: Usage examples or code snippets
5. **Author**: Author name
6. **Contact**: Contact information (email, etc.)
7. **License**: Select from a list of licenses

After providing all the information, the README.md file will be generated in the `output/README.md`.

## Project Structure

```
readme-file-generator/
├── main.py
├── prompt.py
├── requirements.txt
├── utils/
│   └── functions.py
└── output/
│   └── README.md
├──README.md
└──
```
