import subprocess

# Fetch WLAN profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Iterate through profiles and fetch their key content
for i in profile:
    try:
        # Fetch the detailed profile with key content
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        # Print profile name and key
        print("{:<30}| {:<}".format(i, results[0] if results else None))
    except IndexError:
        # Handle missing key content
        print("{:<30}| {:<}".format(i, None))
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred with profile '{i}': {e}")

input("\n\nPress Enter to continue...")
