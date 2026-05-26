# AI Project Management Assistant → Zero‑Touch RAID Governance Engine

An evolution from a smart assistant to a fully autonomous, database‑backed governance system for program managers. Built with **Claude API**, **n8n (self‑hosted)**, **Supabase**, **ntfy**, and **Streamlit**.

---

## 📌 What’s New (Version 2 – Zero‑Touch RAID Engine)

After the original AI PM Assistant proved the concept, the engine was completely rebuilt to run **indefinitely for free** and **actively manage the RAID lifecycle**, not just log items.

| Feature | Original (v1) | New Engine (v2) |
|--------|---------------|-----------------|
| **Storage** | Google Sheets | Supabase (PostgreSQL) |
| **Alerts** | Gmail (OAuth) | ntfy (zero‑auth, instant) |
| **Hosting** | n8n Cloud (paid limits) | Self‑hosted Docker (free forever) |
| **Drive Access** | OAuth (frequent re‑auth) | Google Service Account (permanent) |
| **Data Quality** | `"Unknown"` dates stored as text | Dates cleaned to `null` automatically |
| **Overdue Escalation** | ❌ Not present | ✅ Runs every weekday at 9 AM, sends reminders |
| **Live Dashboard** | ❌ Only static Google Sheets tabs | ✅ Streamlit web dashboard with AI Q&A |
| **Parser Robustness** | Basic | Handles single objects, missing fields, date cleaning |

---

## 🧠 Original AI PM Assistant (v1)

**Feature 1 – RAID Log Generator:**  
Save meeting notes to Google Drive → the system extracts every Risk, Action, Issue, and Decision and writes them to Google Sheets. High‑priority items trigger automatic email alerts.

**Feature 2 – Status Update Generator:**  
Fill in a form → Claude writes a polished 150‑word executive update in seconds.

**Feature 3 – Risk Flagging:**  
Describe a project → Claude identifies the top 5 risks with severity, likelihood, and mitigation.

**Feature 4 – Project Health Q&A:**  
Upload project documents to Claude Projects → ask questions in plain English → answers based on your actual data.

---

## 🚀 Zero‑Touch RAID Governance Engine (v2)

**What it does end‑to‑end:**

1. **🗂️ Automatic RAID Extraction**  
   Drop a meeting transcript (Google Doc) into a Drive folder.  
   → n8n reads it, sends it to Claude, stores structured RAID items in **Supabase**.  
   → High/Critical items instantly trigger **ntfy** notifications.

2. **⏰ Daily Overdue Escalation**  
   Every weekday at 9 AM, a separate n8n workflow queries Supabase for open items past their due date and sends a reminder.

3. **📊 Live Dashboard (Streamlit)**  
   Web dashboard shows real‑time counts of Open, High/Critical, and Overdue items.  
   Filterable RAID table.  
   **AI Q&A** – ask questions like *“Which risks are overdue and critical?”* and Claude answers using only your live database.

4. **🔐 Self‑Hosted & Free Forever**  
   n8n runs in a Docker container on your own machine. No usage limits, no paywalls.

---

## 🛠 Tools Used

- **Claude API** (Anthropic) – RAID extraction, status updates, risk analysis  
- **n8n** (self‑hosted via Docker) – all workflow automation  
- **Supabase** – PostgreSQL database for RAID items and escalation logs  
- **ntfy** – instant, zero‑OAuth notifications  
- **Streamlit** – live web dashboard with Claude‑powered Q&A  
- **Google Drive / Google Docs** – input via a watched folder  
- **Google Sheets** – original output (v1 only)

---

## ⚙️ How to Use (v2)

1. Clone this repository or download the workflow JSON files.
2. Start n8n locally with Docker:
   ```bash
   docker run -d --name n8n --restart unless-stopped -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
