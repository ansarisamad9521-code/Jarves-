import subprocess
import webbrowser

def run_system_command(cmd: str):
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return out
    except Exception as e:
        return str(e)

def open_url(url: str):
    webbrowser.open(url)
    return f"Opened {url}"
