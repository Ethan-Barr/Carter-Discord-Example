import schedule
import subprocess
import time

REQUIRED_MODULES = [
    'nextcord',
    'schedule',
    'requests'
]

def check_requirements():
    for module in REQUIRED_MODULES:
        try:
            __import__(module)
        except ImportError:
            print(f"Error: {module} is not installed. Please install it using pip.")
            return False
    return True



def update_repo():
    repo_path = r'C:\Users\ethan\OneDrive\Documents\GitHub\HuwBot'
    repo_url = 'https://github.com/Ethan-Barr/HuwBot.git'
    branch_name = 'main'
    remote_name = 'origin'
    subprocess.call(['cd', repo_path])
    subprocess.call(['git', 'fetch', remote_name, branch_name])
    current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
    
    if current_branch != branch_name:
        subprocess.call(['git', 'checkout', branch_name])

    subprocess.call(['git', 'pull', remote_name, branch_name])

    if not check_requirements():
        return

    subprocess.call(['python', 'main.py'])

check_requirements()
schedule.every(1).hour.do(update_repo)
update_repo()


while True:
    schedule.run_pending()
    time.sleep(1)
