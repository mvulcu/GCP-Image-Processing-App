# Import necessary libraries
from google.cloud import vision_v1
import io


# Define a function to detect text in an image and save it to an output file
def detect_text(image_path, output_file_path):
    # Create a client for the Google Cloud Vision API
    client = vision_v1.ImageAnnotatorClient()

    # Open the image file in binary read mode
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an Image object from the image content
    image = vision_v1.Image(content=content)

    # Perform text detection on the image
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Check if text was detected in the image
    if texts:
        # Get the first (most prominent) detected text and remove leading/trailing whitespace
        detected_text = texts[0].description.strip()

        # Write the detected text to the output file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(detected_text)

        # Print the detected text to the console
        print(f'Detected text: {detected_text}')
    else:
        # If no text was detected, print a message
        print('No text detected on the image.')


if __name__ == '__main__':
    # Define the paths to the input image and the output text file
    image_path = 'path_to_your_image.png'
    output_file_path = 'output.txt'

    # Call the detect_text function with the specified image and output file paths
    detect_text(image_path, output_file_path)
