# Voice-Activated Assistant

A Python-based voice-activated personal assistant that leverages speech recognition, natural language processing, and text-to-speech technologies to create an interactive and intuitive user experience.

## Features
- **Voice Command Recognition**: Accurately captures and interprets voice commands using the SpeechRecognition library.
- **Natural Language Processing**: Utilizes the `neuralintents` library to understand user intents and execute appropriate actions.
- **Text-to-Speech**: Implements `pyttsx3` to convert text responses into natural-sounding speech.
- **Task Management**: Create notes, add items to a to-do list, and display the current to-do list using voice commands.
- **Personalized Interaction**: Custom greetings and the ability to exit the application gracefully via voice commands.

## Getting Started
### Prerequisites
- Python 3.7 or higher
- Required Python libraries: `speech_recognition`, `pyttsx3`, `neuralintents`, `pyaudio`

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/voice-activated-assistant.git
   cd voice-activated-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and install PyAudio**:
   Follow the instructions for your operating system from the [PyAudio GitHub page](https://github.com/jleb/pyaudio).

### Usage
1. **Run the application**:
   ```bash
   python test.py
   ```

2. **Interact with the assistant**:
   - Use voice commands to create notes, manage your to-do list, and more.
   - Example commands: 
     - "Create a note"
     - "Add to my to-do list"
     - "Show my to-do list"
     - "Hello"
     - "Exit"

### Intent Mapping
The assistant uses a JSON file (`VoiceRec.json`) to map user intents to functions. Here is an example of the intent mapping:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello! How can I assist you today?"]
    },
    {
      "tag": "create_note",
      "patterns": ["Make a note", "Create a note", "Write this down"],
      "responses": ["What would you like to write in your note?"]
    },
    {
      "tag": "add_todo",
      "patterns": ["Add to my to-do list", "I need to do something", "Remember to"],
      "responses": ["What would you like to add to your to-do list?"]
    },
    {
      "tag": "show_todo",
      "patterns": ["Show my to-do list", "What do I need to do?", "List my tasks"],
      "responses": ["Here are the items on your to-do list:"]
    },
    {
      "tag": "exit",
      "patterns": ["Exit", "Quit", "Goodbye"],
      "responses": ["Goodbye!"]
    }
  ]
}
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements
- **Expanded Intent Library**: Add more intents and functionalities, such as setting reminders, checking the weather, and controlling smart home devices.
- **Machine Learning Integration**: Incorporate machine learning models to improve speech recognition accuracy and user intent prediction.
- **Multilingual Support**: Add support for multiple languages to cater to a broader audience.

## License
This project is licensed under the MIT License.
