# Troubleshooting Guide

## Common Issues

**Q: The app won't start / crashes at launch**
- Check your Python and Node versions.
- Run `pip install -r requirements.txt` and `npm install` again.

**Q: API keys not working / can't connect to exchange**
- Double-check your `.env` file—are keys correct? Permissions enabled?

**Q: No signals / bots not running**
- Is your exchange account funded?
- Backend logs show errors? See `/logs/app.log`.

**Q: Alerts not coming through**
- Telegram/Discord tokens correct?
- Push notifications allowed on your device?
- Try toggling off and on in **Settings → Notifications**.

**Q: Premium/paid features not working**
- Is the toggle enabled in **Settings → Paid Features**?
- If you upgraded, try restarting backend and frontend.

## Need More Help?
- Review [User Modes](user_modes.md) for correct feature setup.
- See [Integrations](integrations.md) for third-party connection help.
- Check the [logs directory](/logs/) for error files.
