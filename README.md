# ChatWithDoc 💬

This was built as a trial of working Codeium Windsurf IDE to judge its potential.  Was able to build this in about an hour with very few hiccups.
- Winsurf (using Sonnet 3.5) wrote all the code, including this readme
- It never got "stuck" there we just some corrections I directed in the implementation

A streamlined chat interface for interacting with documents using Claude, Anthropic's state-of-the-art language model.

## Features

- 📝 Upload and chat with text (.txt) and markdown (.md) files
- 🤖 Powered by Claude-3 Opus for intelligent responses
- 👀 Document preview in a clean popover interface
- 🔒 Secure API key management via environment variables
- 🎨 Modern Streamlit UI with session state management

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ChatWithDoc.git
   cd ChatWithDoc
   ```

2. Set up your environment:
   ```bash
   # Create and activate a virtual environment (optional but recommended)
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
`
   pip install -r requirements.txt
   ```

3. Configure your API key:
   ```bash
   # Copy the environment template
   cp dist.env .env
   
   # Edit .env and add your Anthropic API key
   # ANTHROPIC_API_KEY=your-api-key-here
   ```

4. Run the application:
   ```bash
   streamlit run run_chat.py
   ```

## Usage

1. Start the application using the command above
2. Enter your Anthropic API key in the sidebar (or set it in `.env`)
3. Upload a text or markdown file using the file uploader
4. Preview your document using the "Preview Document" button
5. Start chatting! Ask questions about your document

## Project Structure

The project follows Clean Architecture principles:

```
ChatWithDoc/
├── chat_with_doc/           # Main package directory
│   ├── domain/             # Domain models and interfaces
│   ├── usecases/          # Application business rules
│   ├── interfaces/        # Interface adapters
│   └── infrastructure/    # Frameworks and tools
├── tests/                 # Test directory
├── run_chat.py           # Application entry point
├── pyproject.toml        # Project configuration
└── README.md            # This file
```

## Development

This project uses:
- `uv` for dependency management
- `streamlit` for the web interface
- `anthropic` for LLM integration
- `python-dotenv` for environment management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE.txt)

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Anthropic's Claude](https://www.anthropic.com/)
