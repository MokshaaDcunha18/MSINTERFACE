from PIL import Image
import random

# Function to encrypt the image
def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = list(image.getdata())  # Get the pixel data

    # Perform pixel manipulation (e.g., swap pixel values based on a key)
    random.seed(key)  # Seed the random number generator with the key
    random.shuffle(pixels)  # Shuffle the pixel values

    # Create a new encrypted image
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image
def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    pixels = list(image.getdata())  # Get the pixel data

    # Reverse the pixel manipulation (e.g., unshuffle using the same key)
    random.seed(key)  # Seed the random number generator with the key
    indices = list(range(len(pixels)))
    shuffled_indices = indices[:]
    random.shuffle(shuffled_indices)

    # Unshuffle the pixels to get the original order
    unshuffled_pixels = [None] * len(pixels)
    for i, shuffled_index in enumerate(shuffled_indices):
        unshuffled_pixels[shuffled_index] = pixels[i]

    # Create a new decrypted image
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(unshuffled_pixels)
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to run the tool
def main():
    # Ask the user for operation type (encrypt/decrypt)
    operation = input("Do you want to (E)ncrypt or (D)ecrypt the image? ").upper()
    
    # Ask the user for the image file path and output file path
    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the path to save the output image: ")
    key = input("Enter a numeric key (same key must be used for encryption and decryption): ")
    
    if not key.isdigit():
        print("Invalid key! Please enter a numeric value.")
        return

    key = int(key)

    if operation == 'E':
        encrypt_image(image_path, output_path, key)
    elif operation == 'D':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid operation! Please enter 'E' to encrypt or 'D' to decrypt.")

# Run the program
if __name__ == "__main__":
    main()
