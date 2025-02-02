import streamlit as st
from typing import Optional
import os
from dotenv import load_dotenv
from chat_with_doc.interfaces.llm_api import LlmApi
from chat_with_doc.infrastructure.anthropic_llm import AnthropicLlm, AnthropicConfig
from chat_with_doc.infrastructure.text_processor import TextProcessor
from chat_with_doc.domain.document import Document


# Load environment variables
load_dotenv()


def initialize_state():
    """Initialize session state if it doesn't exist."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "document" not in st.session_state:
        st.session_state.document = None
    if "show_preview" not in st.session_state:
        st.session_state.show_preview = False


def display_chat_history():
    """Display all messages in the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_message(role: str, content: str):
    """Add a message to the chat history."""
    st.session_state.messages.append({"role": role, "content": content})


class ChatInterface:
    """Streamlit interface for chat interactions."""

    def __init__(self, llm: Optional[LlmApi] = None):
        self.llm = llm
        self.text_processor = TextProcessor()

        # Initialize LLM if API key is in environment
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            self.llm = AnthropicLlm(AnthropicConfig(api_key=api_key))

    def setup_sidebar(self):
        """Setup the sidebar with configuration options."""
        st.sidebar.title("Chat Configuration")

        # API Key configuration
        api_key = st.sidebar.text_input(
            "Anthropic API Key",
            value=os.getenv("ANTHROPIC_API_KEY", ""),
            type="password",
            key="api_key",
        )

        if api_key:
            self.llm = AnthropicLlm(AnthropicConfig(api_key=api_key))
            if api_key != os.getenv("ANTHROPIC_API_KEY"):
                st.sidebar.success("API key updated!")

        st.sidebar.markdown("---")

        # File upload
        uploaded_file = st.sidebar.file_uploader(
            "Upload a document",
            type=["txt", "md"],
            help="Supports text (.txt) and markdown (.md) files",
        )

        if uploaded_file:
            try:
                document = self.text_processor.process(uploaded_file, uploaded_file.name)
                st.session_state.document = document
                st.sidebar.success(f"Loaded document: {document.name}")
            except ValueError as e:
                st.sidebar.error(str(e))

        # Document info
        if "document" in st.session_state and st.session_state.document:
            st.sidebar.markdown("---")
            st.sidebar.subheader("Current Document")
            st.sidebar.text(st.session_state.document.name)
            st.session_state.show_preview = True

        st.sidebar.markdown("---")
        if st.sidebar.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

    def show_document_preview(self):
        """Show document preview in a popover."""
        if st.session_state.show_preview and st.session_state.document:
            with st.popover("Document Preview", use_container_width=True):
                st.markdown("### " + st.session_state.document.name)
                st.markdown("---")
                st.markdown(st.session_state.document.content)
                if st.button("Close"):
                    st.session_state.show_preview = False
                    st.rerun()

    def run(self):
        """Run the chat interface."""
        # Initialize state first
        initialize_state()

        st.title("Chat With Doc 💬")

        # Setup sidebar
        self.setup_sidebar()

        # Show document preview modal if triggered
        self.show_document_preview()

        # Display chat history
        display_chat_history()

        # Chat input
        if prompt := st.chat_input(
            "What's on your mind?"
            if st.session_state.document
            else "Please upload a document first"
        ):
            if not st.session_state.document:
                st.error("Please upload a document before chatting!")
                return

            if not prompt.strip():
                return

            # Add user message
            add_message("user", prompt)

            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate and display assistant response
            with st.chat_message("assistant"):
                if self.llm is None:
                    response = "Please configure your API key in the sidebar to start chatting!"
                else:
                    with st.spinner("Thinking..."):
                        try:
                            # Enhance the prompt with document context
                            enhanced_prompt = f"""Context: {st.session_state.document.content}

Question: {prompt}

Please provide a response based on the context above."""

                            response = self.llm.query(enhanced_prompt)
                        except Exception as e:
                            response = f"Error: {str(e)}"

                st.markdown(response)
                add_message("assistant", response)


def main():
    """Main entry point for the Streamlit app."""
    chat = ChatInterface()
    chat.run()


if __name__ == "__main__":
    main()
