# Image Processing Application using Google Cloud Vision API

This repository contains instructions and code for creating an image processing application using the Cloud Vision API in Google Cloud. This application allows you to extract text from images and save it to a text file.

## Getting Started

Follow these steps to set up and run the application:

### Step 1: Creating a Project in Google Cloud

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one. Click on the "Select a project" button and choose "New Project." Provide a project name and select an organization (if necessary), then click "Create."

### Step 2: Enabling the Cloud Vision API

1. Enable the Cloud Vision API for your project. To do this, go to the Google Cloud Console, select your project, then navigate to the "APIs & Services" > "Library" menu. In the search bar, enter "Cloud Vision API," then click "Enable."
<img src="/screenshots/1.png" width="50%" alt="Screenshot 1">
<img src="/screenshots/2.png" width="50%" alt="Screenshot 2">
<img src="/screenshots/3.png" width="50%" alt="Screenshot 3">


### Step 3: Creating a Service Account and Key

1. In the left sidebar, select "APIs & Services" > "Credentials."
<img src="/screenshots/4.png" width="50%" alt="Screenshot 4">

2. Click "Create credentials" and select "Service Account Key."
<img src="/screenshots/5.png" width="50%" alt="Screenshot 5">
<img src="/screenshots/6.png" width="50%" alt="Screenshot 6">

3. Fill in the necessary information to create the service account and assign the "VisionAI Admin" role to this account.
<img src="/screenshots/7.png" width="50%" alt="Screenshot 7">

4. Choose "JSON" as the key format and click "Create." The JSON key file will be automatically downloaded to your computer
<img src="/screenshots/8.png" width="50%" alt="Screenshot 8">
<img src="/screenshots/9.png" width="50%" alt="Screenshot 9">
<img src="/screenshots/10.png" width="50%" alt="Screenshot 10">


### Step 4: Setting an Environment Variable

1. Open the command prompt (Command Prompt) or PowerShell.
2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable by specifying the path to the JSON key file you downloaded:

In the command prompt:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-key.json
```

In PowerShell:

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="path\to\your\service-account-key.json"
```

### Step 5: Creating a Python Application

1. Open a text editor on your computer, such as Notepad, Visual Studio Code, or another.
2. Create a new file with a `.py` extension. For example, you can name it `image_processing.py`.
3. You can view the code with comments in the provided Python files.

### Step 6: Running the Application

1. Navigate to the Command Prompt/PowerShell in the directory where your `.py` file is located.
2. Execute the following command to run your application:

```bash
python image_processing.py
```

After running this command, your application will process the image and write the recognized text to the `output.txt` file.

## Result

This is what the result files look like:
<img src="/screenshots/11.png" width="30%" alt="Screenshot 11">

- Take a screenshot and save it with the name "imageGCP.png."
<img src="/screenshots/12.png" width="50%" alt="Screenshot 12">

- After running `image_processing.py`, a text file named `output.txt` will appear in the folder.
<img src="/screenshots/13.png" width="50%" alt="Screenshot 13">

For example, I have my lab report with code presented as an image in a PDF file. I can take a screenshot of the PDF file, specifically of that image, and extract text from it:

<img src="/screenshots/14.png" width="100%" alt="Screenshot 14">

### Note

While this feature is useful, it's important to double-check the extracted text. In some cases, a few characters may be missed, and special characters like underscores might not be recognized. However, it can still save a significant amount of time when dealing with image-based text extraction tasks.

Feel free to contribute to this repository or provide feedback on its functionality. 

Enjoy using the Google Cloud Vision API for image processing!
