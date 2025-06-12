import subprocess
import os

# This script is used to run tests locally in parallel on three different browsers: Chromium, Firefox, and WebKit.
# For each browser, the BROWSER environment variable is set, and tests are executed using 'behave'.
# Each test run is started as a separate process, and the script waits for all of them to complete.

browsers = ['chromium', 'firefox', 'webkit']
processes = []

for browser in browsers:
    env = os.environ.copy()
    env['BROWSER'] = browser
    results_dir = f"allure_results_{browser}"
    cmd = [
        'behave'
    ]
    process = subprocess.Popen(cmd, env=env)
    processes.append(process)

for process in processes:
    process.wait()