import psutil

# Get all processes
for process in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        # Check if 'ffplay' is in the command line of the process
        if 'ffplay' in process.info['cmdline']:
            print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Command: {process.info['cmdline']}")
            process.terminate()
    except:
        pass  # Ignore processes that are no longer accessible
