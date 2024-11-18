# RPG Music Player README

## Overview
RPG Music Player is a Python-based application that allows users to play music while engaging with an RPG-themed interface. It integrates with external APIs such as OpenAI and YouTube to enhance the user experience with AI-driven features and music streaming capabilities.

## Requirements

Before running the application, ensure you have the following:

- Python 3.7+ installed
- `make` command available (for running scripts)
- API keys for OpenAI and YouTube

## Setup Instructions

### 1. **Setting Up a Virtual Environment**

It is recommended to use a virtual environment to manage the dependencies for this project. To set it up:

1. Install `virtualenv` (if not already installed):
   ```bash
   pip install virtualenv
   ```

2. Create a virtual environment in the project directory:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. **Configuring the `.env` File**

The `.env` file contains sensitive information, such as your API keys. To configure it:

1. Create a `.env` file in the root directory of the project.

2. Add the following content to the `.env` file, replacing the placeholders with your actual API keys:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   YOUTUBE_API_KEY=your_youtube_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

### 3. **Running the Application**

Once your virtual environment is activated and the `.env` file is configured, you can run the different components of the application using the `make` command.

#### To run the RPG Music Player:

Use the following `make` command to start the music player:

```bash
make run-player
```

#### To run the Chatbot:

To start the chatbot interface, use the following `make` command:

```bash
make run-chatbot
```

### 4. **Additional Configuration (Optional)**

You may modify other configuration files to suit your preferences for player settings or chatbot behavior. Refer to the documentation within the project or code for additional customization options.

## Chatbot Commands
Use the following commands to control the music or environment sounds:

1. **Play Music**:  
   `-play music {description}`  
   Example: `-play music play relaxing jazz`

2. **Play Environment Sound**:  
   `-play environment {description}`  
   Example: `-play environment play forest sounds`

3. **Stop Music or Environment Sound**:  
   `-stop music` or `-stop environment`  
   Example: `-stop music`

4. **Exit**:  
   `-exit`  
   Example: `-exit`

Type `-play`, `-stop`, or `-exit` followed by the type (music/environment) to start, stop, or exit the program.


## Troubleshooting

- **Missing dependencies**: If you encounter missing packages, ensure you've installed everything with `pip install -r requirements.txt`.
- **API key issues**: Make sure your `.env` file is correctly configured and contains valid API keys for OpenAI and YouTube.
- **Virtual environment issues**: Double-check that your virtual environment is activated when running the commands.


## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

This guide should help you get up and running with the RPG Music Player app. If you have any issues, feel free to open an issue in the project repository!

