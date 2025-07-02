# Vynix: Your AI Dude

Vynix is a sleek, modern chatbot application built with Python, Tkinter, and the Google Gemini API. It features a dark-themed interface, a typing animation for bot responses, a customizable user message color, and intuitive controls including "Send" and "Stop" buttons. The chatbot, named Vynix, allows users to interact with the Gemini AI model to receive intelligent responses, making it ideal for conversational tasks, quick queries, or AI-driven assistance.

## Features

- **Dark Theme Interface**: A visually appealing dark black (#121212) background with a clean, professional design.
- **Typing Animation**: Bot responses are displayed with a smooth typing effect for an engaging user experience.
- **Customizable Colors**: User messages are styled in a sophisticated Soft Gold (#E6B800) for a refined look.
- **Interactive Controls**: Includes a "Send" button to submit messages and a "Stop" button (■) to halt the bot's typing animation.
- **Responsive Layout**: Centered input box, buttons, and footer with a header displaying "Vynix."
- **Footer Credit**: Displays "Developed by Dee" at the bottom.
- **Key Bindings**: Press "Enter" to send messages for faster interaction.

## Prerequisites

To run Vynix, ensure you have the following installed:

- **Python 3.8+**: The project is built with Python and requires a compatible version.
- **Tkinter**: Included with standard Python installations for the GUI.
- **Google Generative AI SDK**: Required to interact with the Google Gemini API.
- **Google AI Studio API Key**: Obtain an API key from [Google AI Studio](https://aistudio.google.com/) to enable the chatbot's AI capabilities.

## Installation

Follow these steps to set up and run Vynix on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Vynix-AI-Dude.git
   cd Vynix-AI-Dude
   ```

2. **Install Dependencies:Install the required Python package for the Google Gemini API**:
```bash
pip install google-generativeai
```


3. **Set Up the API Key**:

Obtain your API key from Google AI Studio.
Open the vynix.py file and replace "YOUR_API_KEY" with your actual API key in the line:
```bash
genai.configure(api_key="YOUR_API_KEY")
```


4. **Verify Python Installation:Ensure Python 3.8 or higher is installed**:
```bash
python --version
```
If Tkinter is not included, install it (e.g., on Ubuntu):
```bash
sudo apt-get install python3-tk
```


## Usage

1. **Run the Application:Execute the main script to launch the chatbot**:
```bash
python vynix.py
```

2. **Interact with Vynix**:

- On startup, Vynix displays a welcome message: "Welcome to Vynix! How can I assist you today?"
- Type your message in the input box at the center of the window.
- Press the "Send" button or hit "Enter" to submit your message.
- Vynix will respond with a typing animation, displaying answers from the Google Gemini API.
- Use the "Stop" button (■) to interrupt the typing animation if needed.
- User messages appear in Soft Gold (#E6B800), bot messages in light green (#a5d6a7), and errors in red (#ef5350).

3. **Close the Application**:

- Close the window to exit the chatbot.



## Project Structure

- <mark>vynix.py</mark>: The main Python script containing the chatbot's code, including the GUI and API integration.
- <mark>README.md</mark>: This file, providing project documentation.

## Customization
You can customize the chatbot by modifying the vynix.py file:

- Change User Message Color:Update the foreground value in the "user" tag configuration:
```
chat_log.tag_configure("user", foreground="#E6B800", font=("Times New Roman", 14, "bold"))
```
- Replace #90caf9 with your preferred hex color code.

- Adjust Typing Animation Speed:Modify the time.sleep(0.02) value in the send_message() function or time.sleep(0.05) in the welcome_animation() function to speed up or slow down the typing effect.

- Change Theme Colors:Update colors like the background (#121212), input box (#333333), or button hover effects (#4CAF50 for Send, #e53935 for Stop).


## Troubleshooting

API Key Error: Ensure the API key from Google AI Studio is correctly inserted in vynix.py. Verify your internet connection and API quota.
Tkinter Not Found: Install Tkinter if missing (see Installation step 4).
No Response from Bot: Check if the Gemini model name (gemini-1.5-flash) is valid and supported by your API key. You can try other models like gemini-1.5-pro if available.
UI Issues: Ensure your Python version is compatible (3.8+), and test on a display with at least 600x700 resolution.

## Contributing
Contributions are welcome! To contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature-name).
- Make your changes and commit (git commit -m "Add feature").
- Push to the branch (git push origin feature-name).
- Create a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
- Developed by Dipman (Dee).
- Powered by Google Gemini API.
- Built with Tkinter for the GUI.


