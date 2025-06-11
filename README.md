# ING – Cookie Consent Automation Test

## 📋 Task Overview

This project automates the process of accepting analytical cookies on the [ING Poland website](https://www.ing.pl), according to the following scenario:

1. Navigate to the ING homepage
2. Open the cookie consent modal by clicking **"Customize"**
3. Enable analytical cookies
4. Confirm the selection by clicking **"Accept selected"**
5. Verify that the appropriate cookies are stored in the browser

---

## 🧪 Tech Stack

- **Python 3.8+**
- **Behave** – BDD test framework
- **Playwright (sync API)** – browser automation
- **Allure** – test reporting (optional)
- **Page Object Model (POM)** – clean and maintainable test design

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nosfer-Projects/TASK.git
cd TASK
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate          # On Windows: .venv\Scripts\activate
```

> **ℹ️ Windows PowerShell Note:**\
> If you encounter the following error:
>
> ```
> .\.venv\Scripts\activate : File ... cannot be loaded because running scripts is disabled on this system.
> ```
>
> It means PowerShell"s execution policy is too strict.\
> You can temporarily allow script execution for the current session with:
>
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run the test

```bash
behave
```

---

## 📈 Reporting with Allure (optional)

### 1. Install Allure CLI

Follow instructions from: [Allure Documentation](https://docs.qameta.io/allure/#_get_started)

### 2. Generate and view report

```bash
behave
allure serve allure_results/
```

> **Note:** Output directory and formatter are configured in `behave.ini`:
>
> ```ini
> [behave]
> format = allure_behave.formatter:AllureFormatter
> outfiles = allure_results
> ```

---

## ⚙️ Notes

- The test uses **Playwright’s synchronous API** for full compatibility with Behave.
- By default, it runs on **Chromium**, but you can easily add support for **Firefox** and **WebKit**.
- The project is structured using the **Page Object Model**, making it scalable and maintainable.

---