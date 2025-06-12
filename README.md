# ING – Cookie Consent Automation Test

## 📋 Task Overview

This project automates the process of accepting analytical cookies on the [ING Poland website](https://www.ing.pl), following this scenario:

1. Navigate to the ING homepage
2. Open the cookie consent modal by clicking **"Dostosuj"** (Customize)
3. Enable analytical cookies
4. Confirm the selection by clicking **"Zaakceptuj zaznaczone"** (Accept selected)
5. Verify that the appropriate cookies are stored in the browser

### Non-functional requirements:
- Ensure test results are repeatable
- Implement tests in Python using the Playwright framework
- Publish your results on GitHub and share the solution with us
- Provide a README explaining how to run the solution
- Bonus: Run tests on multiple browsers simultaneously and present a pipeline automating this

---

## 🧪 Tech Stack

- **Python 3.8+**
- **Behave** – BDD test framework
- **Playwright (synchronous API)** – browser automation
- **Allure** – test reporting (optional)
- **Page Object Model (POM)** – for clean and maintainable test design

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed and available in your system PATH
- Internet connection to download dependencies and browser binaries

### 1. Clone the repository

```bash
git clone https://github.com/Nosfer-Projects/TASK.git
cd TASK
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate# On Windows use: .venv\Scripts\activate
```

> **ℹ️ Windows PowerShell Note:**
> If you see an error about script execution being disabled, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run the tests

```bash
behave
```

---

## 🔄 Running Tests on Multiple Browsers Locally

> **Note:**
> Behave is not natively designed to run tests concurrently.
> However, this project includes a custom script (`run_all_browsers.py`) to launch tests simultaneously on Chromium, Firefox, and WebKit.
>  This approach achieves parallel test execution locally, but Allure does not natively support aggregating results from simultaneous test runs, which can lead to errors or conflicts during report generation.

To run tests simultaneously on Chromium, Firefox, and WebKit locally, use the provided script:

```bash
python run_all_browsers.py
```

---

## 📈 Reporting with Allure (optional)

### 1. Install Allure CLI

Follow instructions at [Allure Documentation](https://docs.qameta.io/allure/#_get_started)

### 2. Generate and view the report

```bash
behave
allure serve allure_results/
```

> **Note:** Output directories are configured in the separate `behave_chromium.ini`, `behave_firefox.ini`, and `behave_webkit.ini` files to avoid mixing results.

---

## 🏗 Project Structure

- `class_objects/` – Contains Page Object Model classes (e.g., `CookieManager.py`)
- `config_files/` – Contains configuration variables (`config.py`) and cookie text constants (`cookie_constants.py`)
- `features/` – Contains feature files, step definitions, hooks (`environment.py`)
- `type_class_files/` – Contains custom typed classes for better type hinting (e.g., `CustomContext`)
- `behave_chromium.ini`, `behave_firefox.ini`, `behave_webkit.ini` – Separate Behave config files for each browser, each with distinct Allure results folder
- `requirements.txt` – Project dependencies
- `run_all_browsers.py` – Script to run tests on all browsers sequentially with proper results separation

---

## ⚙️ GitHub Actions Pipeline

The pipeline is located at `.github/workflows/test_pipeline.yml`. It runs tests on Chromium, Firefox, and WebKit simultaneously. After the tests finish (regardless of pass or fail), it generates the Allure report and deploys it to a GitHub Pages site (`pages-build-deployment`).


### Important Note on Pipeline Failures

During pipeline runs on GitHub Actions, all tests failed due to the bank’s security systems triggering CAPTCHA challenges. This happened because the website detected access from a foreign IP/location and blocked automated access.

![VIDEO](https://github.com/user-attachments/assets/14838d86-23d5-42ba-ab70-8ab689d36ba8)



---

## 🛠 Troubleshooting

- If the cookie modal does not appear, try clearing browser cookies or run tests in a fresh browser context
- To run tests headlessly, set `headless=True` in `environment.py` when launching the browser
- By default, tests run on the **Chromium** browser.
- To run tests on a different browser, set the `BROWSER` environment variable to `"firefox"` or `"webkit"` before running the tests.
- The `config_files/config.py` file reads this variable with a fallback to `"chromium"` if not set.

---

Thank you for reviewing this task!
