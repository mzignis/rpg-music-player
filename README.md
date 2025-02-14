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
YOUTUBE_API_KEY=<paste_your_youtube_api_key_here>
```
   
### 3. Configurate OLLAMA model

Download and install OLLAMA server:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Run OLLAMA server:

```bash
ollama serve
````

Download and install OLLAMA model:

```bash
ollama pull llama3.2
```

Before use make sure you have installed OLLAMA python package:

```bash
pip install ollama
```

### 4. **Running the Application**

Once your virtual environment is activated and the `.env` file is configured, you can run the different components of the application using the `make` command.

#### To run the RPG Music Player:

Use the following `make` command to start the music player:

```bash
make run
```

If you want to kill all ffplay processes, you can use the following command:

```bash
make kill-ffplay
```

If you want close port from app, you can use the following command:

```bash
make kill-port
```

### 5. **Additional Configuration (Optional)**

You may modify other configuration files to suit your preferences for player settings or chatbot behavior. Refer to the documentation within the project or code for additional customization options.

## Troubleshooting

- **Missing dependencies**: If you encounter missing packages, ensure you've installed everything with `pip install -r requirements.txt`.
- **API key issues**: Make sure your `.env` file is correctly configured and contains valid API keys for OpenAI and YouTube.
- **Virtual environment issues**: Double-check that your virtual environment is activated when running the commands.


## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

This guide should help you get up and running with the RPG Music Player app. If you have any issues, feel free to open an issue in the project repository!

