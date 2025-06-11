# ING – Cookie Consent Automation Test

## 📋 Task Overview

This project automates the process of accepting analytical cookies on the [ING Poland website](https://www.ing.pl), following this scenario:

1. Navigate to the ING homepage
2. Open the cookie consent modal by clicking **"Dostosuj"** (Customize)
3. Enable analytical cookies
4. Confirm the selection by clicking **"Zaakceptuj zaznaczone"** (Accept selected)
5. Verify that the appropriate cookies are stored in the browser

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
source .venv/bin/activate# On Windows: .venv\Scripts\activate
```

> **ℹ️ Windows PowerShell Note:**
> If you see this error:
> ```
> .\.venv\Scripts\activate : File ... cannot be loaded because running scripts is disabled on this system.
> ```
> Run the following command in PowerShell to temporarily allow script execution:
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

## 📈 Reporting with Allure (optional)

### 1. Install Allure CLI

Follow the instructions at [Allure Documentation](https://docs.qameta.io/allure/#_get_started)

### 2. Generate and view the report

```bash
behave
allure serve allure_results/
```

> **Note:** Output directory and formatter are configured in `behave.ini`:
> ```ini
> [behave]
> format = allure_behave.formatter:AllureFormatter
> outfiles = allure_results
> ```

---

## ⚙️ Notes

- Tests use **Playwright’s synchronous API** for compatibility with Behave.
- By default, tests run on **Chromium** browser; support for **Firefox** and **WebKit** can be easily added.
- The project follows the **Page Object Model (POM)** pattern to keep tests clean, modular, and maintainable.

---

## 🛠 Troubleshooting

- If cookies modal does not appear, try clearing browser cookies or running tests in a fresh browser context.
- To run tests in headless mode, modify `headless=True` in `environment.py` in the browser launch options.
- To run tests on other browsers, change the `BROWSER` variable in `config.py` to `"firefox"` or `"webkit"`.

---