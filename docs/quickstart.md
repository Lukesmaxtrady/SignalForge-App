# Quickstart Guide

Welcome to **SignalForge**!  
Follow these steps to get up and running in minutes.

## 1. Clone and Install  
```bash
git clone https://github.com/YOUR_USER/signalforge.git
cd signalforge
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd frontend
npm install
cp .env.example .env
2. Configure Environment
Copy .env.example to .env and fill in your keys:

bash
Copy
cp .env.example .env
Binance/Bitget/Blofin keys for live signals/trading

Telegram, Discord bot tokens (optional)

OpenAI, TradingView, etc.

3. Launch Backend
bash
Copy
cd ..
uvicorn src.main:app --reload
App runs at: http://localhost:8000

4. Launch Frontend
bash
Copy
cd frontend
npm run dev
Visit: http://localhost:3000

5. Sign Up & Onboard
Create your user, pick mode, and start exploring bots, signals, and settings!

Need more help?

Onboarding Guide

Troubleshooting

Integrations

yaml
Copy

---

### **11. `signalforge/docs/onboarding.md`**
```markdown
# SignalForge Onboarding

Welcome!  
SignalForge was built for both beginners and power users. This guide will walk you through:

## 1. Account Creation
- Register an account in the app.
- Set your notification preferences (email, Telegram, Discord).

## 2. Connect Exchange(s)
- Go to **Settings → Exchange Integration**.
- Enter API keys for Binance, Bitget, Blofin, or your preferred exchange.
- Toggle “Paper Trading” to practice safely.

## 3. Choose Bot & Performance Mode
- Explore available bots (TA/ML/LLM-based, see bot descriptions).
- Select your preferred mode: Beginner, Pro, Quant, High Security, Ultra Performance, etc.
- All modes can be toggled later in **Modes**.

## 4. Enable Features
- Toggle paid or premium features (optional).
- Try different UI themes (Space, Gold, Cyberpunk, etc.).

## 5. Notifications & Alerts
- Set up Telegram, Discord, mobile push, and voice alerts in **Settings → Notifications**.
- You can get overlay signals no matter where you are in the app.

## 6. Explore
- The Home and Dashboard show your signals, portfolio, security, and more.
- Check **SuperTuner** for advanced bot control.
- Access help any time from the sidebar or Help Hub.

**Questions?**  
- [Troubleshooting](troubleshooting.md)  
- [User Modes](user_modes.md)
