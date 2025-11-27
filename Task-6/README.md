AI-Driven Development - 30-Day Challenge-Task-
6

Task 6 - GitHub × MCP Integration (Hosted Method)
https://drive.google.com/file/d/1ucqxD-adXqB0MQZwGg2yAsqiNPBpzRs7/view
⏳ Deadline: 48 Hours
Slot:(Friday 6–9 PM)

🎯 Task Objective
Students will connect GitHub MCP Server with the Google Gemini CLI using the Hosted
(Remote) MCP Server.
This method does not require Docker or MCP installation - it's the simplest method.
After completing this task, AI will be able to read repositories and interact with GitHub.
📌 Steps to Complete Task 6 (Easy Method)
🔹 Step 1 - Create Your GitHub Personal Access Token (PAT)
Open this link:
https://github.com/settings/personal-access-tokens/new
Generate a token with:
✔ repo (Read & Write)
Copy the token and save it safely.
🔹 Step 2 - Store Your Token Securely
Do NOT put the token directly into JSON.
Create this file:

Add:

🔹 Step 3 - Configure Gemini to Use GitHub MCP Server
Open or create:

Paste this:

✔ No installation required
✔ Token auto-loads from .env
✔ Fast & easiest MCP setup
🔹 Step 4 - Restart Gemini CLI

🔹 Step 5 - Verify Connection
Run:

Expected:
🟢 github — Ready (90+ tools)
If you see this → SUCCESS
🔹 Step 6 - Test the Server
Ask:
“List my GitHub repositories”
If Gemini shows your repos → MCP is fully connected ✔
⚠ Troubleshooting
❌ Invalid Token
→ Create a new PAT
→ Must include: repo scope
❌ settings.json Error
Run:

❌ MCP not connecting
Run:

📤 Submission Requirements
Students must submit:
✔ Screenshot of:
.env file (token blurred)
settings.json
/mcp list result
GitHub repo list output
📚 Prepared by:Asma Yaseen - Class Coordinator
🧑‍🏫 Supervised by: Sir Hamzah Syed