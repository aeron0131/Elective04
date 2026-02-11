# Elective04

# Introduction
Elective04 is a Python-based project that performs automated image analysis using multiple detection multiple computer vision techniques. The project integrates automated testing and a Continuous Integration (CI) pipeline using GitHub Actions.

The project processes images placed inside the input directory and automatically generates transformed results inside the output directory. It demonstrates modular architecture, automated workflows, unit testing, CI/CD automation, and structured team collaboration using Git.

# Functionality
1.	Acne Detection – Detects and enhances acne-like features in facial images.
2.	Crack Detection – Identifies and highlights crack patterns in structural images.
3.	Dawn Enhancement – Applies edge detection and enhancement techniques.
4.	Jigsaw Processing – Performs creative image manipulation effects.

Each module automatically reads from the input folder and saves processed outputs into the output folder without manual configuration.

# Architecture Overview

Main Components
•	image_processing – processing modules
•	input – raw images
•	output – processed results
•	tests – automated unit tests
•	.github/workflows – CI pipeline configuration 

Workflow:
•	Input Images
•	Processing Modules
•	Output Images
•	Automated Tests
•	CI Validation 

The repository is integrated with a GitHub CI pipeline that automatically runs tests, validates code execution, and ensures consistent builds to maintain project reliability.

# Testing
Each module has a corresponding pytest test file
•	Run tests locally:
    pytest

Tests verify successful execution and output generation to ensure system reliability

# Continuous Integration (CI Pipeline)

This project uses GitHub Actions.

The CI workflow is defined in:
•	.github/workflows/ci.yml

The workflow automatically triggers on:
•	Every push
•	Every pull request

Pipeline Steps:
1.	Set up Python
2.	Install dependencies from requirements.txt
3.	Install pytest
4.	Run automated tests
5.	Fail the build if tests fail

This ensures automated validation and collaboration safety.

# Installation & Setup

Requirements:
•	Python 3.9 or latest version
•	Pip package Manager
•	Git

Installation:
1.	Clone the repository: 
      •	git clone https://github.com/<your-username>/Elective04.git
      •	cd Elective04-main

2.	Create a virtual environment
      •	python -m venv venv

3.	Activate the environment.
      •	Windows: venv\Scripts\activate
      •	Mac/Linux: source venv/bin/activate

4.	Install dependencies
      •	pip install -r requirements.txt

5.	Running the Modules
      •	python image_processing/acne_detector.py
      •	python image_processing/crack_detector.py
      •	python image_processing/dawn.py
      •	python image_processing/jigsaw.py
    
    Processed images will automatically appear in the output/ directory.

# Running Tests
To execute automated tests locally:
•	pytest

# Installation (For Contributors)

Development Setup
1.	Fork the repository and clone your fork.
2.	Clone your fork:
      •	git clone https://github.com/<your-username>/Elective04.git
      •	cd Elective04-main
3.	Create a virtual environment
      •	python -m venv venv
      •	source venv/bin/activate   # Windows: venv\Scripts\activate
4.	Install dependencies
      •	pip install -r requirements.txt
      •	pip install pytest
5.	Commit and push changes.
      •	git add .
      •	git commit -m "feat: add new feature"
      •	git push origin feature/your-feature-name

# Collaboration & Git Workflow
1.	Feature branches were used
2.	Pull Requests before merging
3.	Structured commit messages 
4.	All members contributed to development, testing, CI, and documentation.  


# Authors

Mangahas, Romualdo Jr. N.  — **Programmer**
****

Lorenzo, Aeron Abigail R.  — **DevOps**
**  **

Verueco, Joemar A.  — **QA**
** **

Correa, Reingel F.  — **Presenter**
** **








  



