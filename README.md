
# VF_CZ_Task_Python Automation Project

## Project Description
This project automates the testing of the Vodafone Czech Republic website's shopping cart functionality using Selenium and pytest. It includes features like adding an iPhone to the basket and verifying the UI interactions.

---

## Dependencies
The following dependencies are required to run this project:
- selenium
- allure-pytest
- pytest

---

## Setup Instructions

1. **Clone the repository**:
   Clone the project repository to your local machine.

2. **Create a Virtual Environment (optional)**:
   Create and activate a virtual environment to isolate the project's dependencies.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   Install the required Python packages using the provided `requirements.txt` file.
   ```bash
   pip install : 
   allure-pytest         2.13.5
   allure-python-commons 2.13.5
   attrs                 24.2.0
   certifi               2024.8.30
   cffi                  1.17.1
   colorama              0.4.6
   h11                   0.14.0
   idna                  3.10
   iniconfig             2.0.0
   outcome               1.3.0.post0
   packaging             24.2
   pip                   24.3.1
   pluggy                1.5.0
   pycparser             2.22
   PySocks               1.7.1
   pytest                8.3.3
   selenium              4.26.1
   sniffio               1.3.1
   sortedcontainers      2.4.0
   trio                  0.27.0
   trio-websocket        0.11.1
   typing_extensions     4.12.2
   urllib3               2.2.3
   websocket-client      1.8.0
   wsproto               1.2.0
   ```

4. **Install Allure Command-Line Tool**:
   - Download Allure from the [Allure Releases Page](https://github.com/allure-framework/allure2/releases).
   - Extract the downloaded file to a directory (e.g., `C:\allure`).
   - Add the `bin` folder (e.g., `C:\allure\bin`) to your system's `PATH`.

5. **Verify Allure Installation**:
   Run the following command to ensure Allure is installed correctly:
   ```bash
   allure --version
   ```

---
