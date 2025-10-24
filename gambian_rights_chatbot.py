import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Gambian Rights AI Assistant",
    page_icon="🇬🇲",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

def load_legal_documents():
    """Load legal documents"""
    try:
        with open('gambian_legal_text.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        st.error("Legal text file not found. Please ensure 'gambian_legal_text.txt' exists.")
        return None

def get_openai_api_key():
    """Get OpenAI API key from environment"""
    api_key = os.getenv('OPENAI_API_KEY')
    return api_key

def main():
    # Header
    st.markdown('<h1 class="main-header"> Gambian Rights AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Ask questions about your rights and legal protections in The Gambia</p>', unsafe_allow_html=True)
    
    # Get API key from environment
    api_key = get_openai_api_key()
    
    if not api_key:
        st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY in your .env file")
        return
    
    openai.api_key = api_key
    os.environ['OPENAI_API_KEY'] = api_key
    
    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.legal_text = None
    
    # Load legal documents
    if st.session_state.legal_text is None:
        with st.spinner("Loading legal documents..."):
            legal_text = load_legal_documents()
            if legal_text:
                st.session_state.legal_text = legal_text
    
    # Chat interface
    if st.session_state.legal_text:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Handle sample question responses
        if st.session_state.messages and len(st.session_state.messages) % 2 == 1:
            # Last message was from user, generate response
            last_message = st.session_state.messages[-1]["content"]
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        # Create prompt with legal context
                        system_prompt = f"""You are a helpful AI assistant that provides information about legal rights in The Gambia. 
                        Use the following legal information to answer questions about Gambian rights and laws. 
                        Always be accurate and cite relevant articles or sections when possible.
                        
                        Legal Information:
                        {st.session_state.legal_text}
                        
                        Instructions:
                        - Answer questions about rights and laws in The Gambia
                        - Be clear and easy to understand
                        - Cite relevant constitutional articles or legal provisions
                        - If you don't know something, say so
                        - Focus on helping citizens understand their rights"""
                        
                        # Get response from OpenAI
                        response = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": last_message}
                            ],
                            temperature=0.1,
                            max_tokens=500
                        )
                        
                        response_text = response.choices[0].message.content
                        st.markdown(response_text)
                        
                        # Add assistant response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": response_text})
                        
                    except Exception as e:
                        error_msg = f"Sorry, I encountered an error: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        # Chat input
        if prompt := st.chat_input("Ask about your rights in The Gambia..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        # Create prompt with legal context
                        system_prompt = f"""You are a helpful AI assistant that provides information about legal rights in The Gambia. 
                        Use the following legal information to answer questions about Gambian rights and laws. 
                        Always be accurate and cite relevant articles or sections when possible.
                        
                        Legal Information:
                        {st.session_state.legal_text}
                        
                        Instructions:
                        - Answer questions about rights and laws in The Gambia
                        - Be clear and easy to understand
                        - Cite relevant constitutional articles or legal provisions
                        - If you don't know something, say so
                        - Focus on helping citizens understand their rights"""
                        
                        # Get response from OpenAI
                        response = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": prompt}
                            ],
                            temperature=0.1,
                            max_tokens=500
                        )
                        
                        response_text = response.choices[0].message.content
                        st.markdown(response_text)
                        
                        # Add assistant response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": response_text})
                        
                    except Exception as e:
                        error_msg = f"Sorry, I encountered an error: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Sample questions - only show if no messages yet
    if not st.session_state.messages:
        st.markdown("### 💡 Sample Questions to Try:")
        sample_questions = [
            "What are my fundamental rights in The Gambia?",
            "What are my employment rights?",
            "Can I be forced to work without pay?",
            "What are my property rights?",
            "Do I have the right to freedom of speech?",
            "What are my rights if I'm arrested?",
            "Can I form a trade union?",
            "What are my family law rights?"
        ]
        
        cols = st.columns(2)
        for i, question in enumerate(sample_questions):
            with cols[i % 2]:
                if st.button(question, key=f"sample_{i}"):
                    # Add the question to chat and trigger response
                    st.session_state.messages.append({"role": "user", "content": question})
                    st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🇬🇲 <strong>Gambian Rights AI Assistant</strong> - A prototype to help citizens understand their legal rights</p>
        <p><em>This is a proof-of-concept demonstration. For legal advice, consult a qualified attorney.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
