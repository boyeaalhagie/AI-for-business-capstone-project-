# 🚀 Deployment Guide for Gambian Rights AI Assistant

## Option 1: Streamlit Cloud (Recommended - FREE)

### Steps:
1. **Push to GitHub**:
   - Create a new repository on GitHub
   - Upload all your files (except .env)
   - Make sure your OpenAI API key is set as a secret

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file: `gambian_rights_chatbot.py`
   - Add secrets for API key

### Secrets Configuration:
```toml
# In Streamlit Cloud secrets
OPENAI_API_KEY = "your_api_key_here"
```

---

## Option 2: Heroku (FREE tier available)

### Steps:
1. **Create Procfile**:
```
web: streamlit run gambian_rights_chatbot.py --server.port=$PORT --server.address=0.0.0.0
```

2. **Create runtime.txt**:
```
python-3.11.0
```

3. **Deploy**:
   - Install Heroku CLI
   - `heroku create your-app-name`
   - `git push heroku main`

---

## Option 3: Railway (Modern alternative)

### Steps:
1. **Connect GitHub repository**
2. **Set environment variables**
3. **Deploy automatically**

---

## Option 4: Local Network Access

### For testing on your network:
```bash
streamlit run gambian_rights_chatbot.py --server.address 0.0.0.0
```

Then access via: `http://YOUR_IP:8501`

---

## Quick Start - Streamlit Cloud (Easiest)

1. **Create GitHub repo** with your files
2. **Go to share.streamlit.io**
3. **Connect your repo**
4. **Add your OpenAI API key as a secret**
5. **Deploy!**

Your app will be live at: `https://your-app-name.streamlit.app`

## Security Notes:
- Never commit your .env file to GitHub
- Use platform secrets for API keys
- Consider rate limiting for production use

## Cost:
- **Streamlit Cloud**: FREE
- **Heroku**: FREE tier (with limitations)
- **Railway**: $5/month after free credits
