# 🇬🇲 Gambian Rights AI Assistant

A prototype AI-powered chatbot designed to help citizens of The Gambia understand their fundamental rights and legal protections. This project demonstrates how AI can democratize access to legal information and empower citizens with knowledge of their rights.

## 🎯 Project Overview

This is a proof-of-concept prototype that addresses the critical knowledge gap in The Gambia regarding citizens' understanding of their legal rights. The chatbot provides accessible, clear information about constitutional rights, employment law, family law, and other legal protections.

## 🚀 Features

- **Natural Language Queries**: Ask questions about your rights in plain English
- **Constitutional Knowledge**: Access to fundamental rights from The Gambia's Constitution
- **Employment Rights**: Information about workers' rights and protections
- **Family Law**: Rights related to marriage, children, and family matters
- **Property Rights**: Understanding of property ownership and protection
- **Access to Justice**: Information about legal processes and rights
- **Mobile-Friendly**: Accessible via web browser on smartphones

## 🛠️ Technology Stack

- **OpenAI API**: For natural language processing and response generation
- **Streamlit**: For the web interface
- **LangChain**: For document processing and retrieval
- **FAISS**: For vector similarity search
- **Python**: Backend development

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (get from https://platform.openai.com/api-keys)

## 🔧 Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   - Copy `env_example.txt` to `.env`
   - Replace `your_openai_api_key_here` with your actual OpenAI API key

4. **Run the application**:
   ```bash
   streamlit run gambian_rights_chatbot.py
   ```

5. **Open your browser** and go to `http://localhost:8501`

## 💡 How to Use

1. **Enter your OpenAI API key** in the sidebar (if not set in .env file)
2. **Wait for the legal documents to load** (you'll see a success message)
3. **Ask questions** about your rights in The Gambia
4. **Try sample questions** provided in the interface

### Sample Questions:
- "What are my fundamental rights in The Gambia?"
- "What are my employment rights?"
- "Can I be forced to work without pay?"
- "What are my property rights?"
- "Do I have the right to freedom of speech?"
- "What are my rights if I'm arrested?"

## 📚 Legal Information Included

The chatbot is trained on:
- **The Constitution of The Gambia (1997)**
- **Fundamental Rights and Freedoms** (Articles 17-27)
- **Employment Rights**
- **Family Law Rights**
- **Property Rights**
- **Access to Justice**

## 🎯 Success Metrics (Prototype Goals)

- **Accuracy Target**: 80% accuracy in legal information responses
- **User Comprehension**: 3.5/5.0 clarity rating
- **Test Users**: 20-50 users for prototype validation
- **Response Time**: Under 5 seconds for most queries

## ⚠️ Important Disclaimers

- **This is a prototype/proof-of-concept** for demonstration purposes
- **Not a substitute for legal advice** - consult qualified attorneys for legal matters
- **Information accuracy** should be verified with official legal sources
- **For educational and awareness purposes** only

## 🔮 Future Enhancements

- Integration with more comprehensive legal databases
- Multi-language support (Wolof, Mandinka, Fula)
- Voice interface capabilities
- Mobile app development
- Integration with legal aid organizations
- Real-time updates from legal databases

## 📞 Support

For questions about this prototype or technical issues, please refer to the project documentation or contact the development team.

## 📄 License

This project is developed for educational and demonstration purposes as part of the AI for Business Capstone Project at Milwaukee School of Engineering.

---

**🇬🇲 Empowering Gambian citizens with knowledge of their rights through AI technology**
