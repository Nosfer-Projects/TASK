import subprocess
import os

browsers = ['chromium', 'firefox', 'webkit']

processes = []

for browser in browsers:
    env = os.environ.copy()
    env['BROWSER'] = browser
    results_dir = f"allure_results_{browser}"
    cmd = [
        'behave'
    ]
    p = subprocess.Popen(cmd, env=env)
    processes.append(p)

for p in processes:
    p.wait()