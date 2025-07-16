@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/dashboard', '/dareyio')
    markup.row('/discord', '/assessments')
    markup.row('/showcase', '/peerlearning')
    markup.row('/support', '/faq', '/help')
    bot.send_message(message.chat.id, """👋 Welcome to *Yobe Community Assistant* – your personal guide for all things 3MTT in Yobe State.

Here to help you with:
📚 Weekly Assessments  
📥 Darey.io access  
🎓 Peer Learning  
🤝 Discord Support  
🎥 Knowledge Showcase  
📲 And everything in between

Tap a button or type /help to get started.
""", parse_mode="Markdown", reply_markup=markup)
# HELP
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """
🛠️ *Available Commands*

/dashboard – Login, course access, and fixes  
/dareyio – What Darey.io is and how it works  
/discord – How to join and use Discord for support  
/assessments – Weekly assessment process  
/showcase – How to submit your project showcase  
/peerlearning – Purpose and setup of peer groups  
/support – Who to contact and how  
/faq – Common questions about devices, browsers, etc.
""", parse_mode="Markdown")

# DASHBOARD
@bot.message_handler(commands=['dashboard'])
def dashboard(message):
    bot.send_message(message.chat.id, """
📥 *3MTT Dashboard Help*

- Visit [https://app.3mtt.training](https://app.3mtt.training)
- Use your registered email to login.
- If you forgot your password, click “Reset Password”.
- If your dashboard shows no course, it may not be assigned yet. Be patient or contact your Coach.

🛑 Use a modern browser (Chrome or Firefox).
""", parse_mode="Markdown")

# DAREY.IO
@bot.message_handler(commands=['dareyio'])
def dareyio(message):
    bot.send_message(message.chat.id, """
📘 *What is Darey.io?*

Darey.io is your core learning platform for 3MTT. You’ll:
- Complete your milestones  
- Learn technical content  
- Submit mini projects  
- Track your progress

🔗 [https://darey.io](https://darey.io)
""", parse_mode="Markdown")

# DISCORD
@bot.message_handler(commands=['discord'])
def discord(message):
    bot.send_message(message.chat.id, """
💬 *Discord Support Community*

All 3MTT learners must join the 3MTT Discord for:
- Asking questions
- Announcements
- Discussions

To join:
1. Visit the link shared via email or dashboard  
2. Use the same email you used for 3MTT  
3. Accept the rules and select your cohort/state  
4. Join the right channels (e.g., #yobe-fellows)

Use @ everyone responsibly.
""", parse_mode="Markdown")

# ASSESSMENTS
@bot.message_handler(commands=['assessments'])
def assessments(message):
    bot.send_message(message.chat.id, """
📋 *Weekly Assessment Guide*

✅ Each week, check Darey.io for your milestone  
✅ Complete the mini-project or quiz  
✅ Submit directly on Darey.io before the deadline  
✅ Ensure your work is original – plagiarism is penalized

Use the *Weekly Assessment Guide* shared in your Starter Pack for format and expectations.
""", parse_mode="Markdown")

# SHOWCASE
@bot.message_handler(commands=['showcase'])
def showcase(message):
    bot.send_message(message.chat.id, """
🎥 *Knowledge Showcase Guide*

- Create a short video (max 3 minutes)
- Show the problem you're solving  
- Demonstrate what you built using your 3MTT skills  
- Mention your name and Fellow ID  
- Post on social media with:
  `#My3MTT` and `#3MTTLearningCommunity`  
  Tag @3MTTNigeria

📨 Submit the form shared on your dashboard or email.
""", parse_mode="Markdown")

# PEER LEARNING
@bot.message_handler(commands=['peerlearning'])
def peerlearning(message):
    bot.send_message(message.chat.id, """
🤝 *Peer Learning Groups*

These are local groups for:
- Collaboration
- Accountability
- Hands-on sessions

Each group has:
- A Coordinator
- Group Size (10–30 fellows)
- Weekly physical meetings (if possible)

Ask your State Manager for your assigned group.
""", parse_mode="Markdown")

# SUPPORT
@bot.message_handler(commands=['support'])
def support(message):
    bot.send_message(message.chat.id, """
📞 *Need Help?*

Here’s who to reach out to:

- **State Manager:** Yobe's official coordinator  
- **Coach:** Assigned learning guide in Discord or ALC  
- **Training Provider:** The organization responsible for your training delivery

Contact them via Discord, ALC or Email if unsure.
""", parse_mode="Markdown")

# FAQ
@bot.message_handler(commands=['faq'])
def faq(message):
    bot.send_message(message.chat.id, """
❓ *General FAQs*

- *No Course Assigned Yet?* Wait 1–2 weeks or contact Coach.  
- *Browser Issues?* Use Chrome or Firefox on laptop.  
- *Can't Join Discord?* Use correct email & check your spam folder for invite.  
- *Stuck on Dashboard?* Clear cache or switch browser.  
- *Missed ALC Session?* Request recording link or summary from peer group.

Stay engaged, be consistent, and ask for help when needed!
""", parse_mode="Markdown")

# Start the bot
bot.polling()
