# AI Project Management Assistant

An agentic AI system that automates project management tasks 
using Claude's API, n8n, and Google Sheets.

## What It Does

- **Feature 1 — RAID Log Generator:** Saves meeting notes to 
Google Drive. System automatically extracts every Risk, Action, 
Issue and Decision and writes them to Google Sheets. High priority 
items trigger automatic email alerts.

- **Feature 2 — Status Update Generator:** Fill in a form. 
Claude writes a polished 150-word executive update in seconds.

- **Feature 3 — Risk Flagging:** Describe a project. Claude 
identifies top 5 risks with severity, likelihood and mitigation.

- **Feature 4 — Project Health Q&A:** Upload project documents 
to Claude Projects. Ask plain English questions. Claude answers 
from your actual data.

## Tools Used

- Claude API by Anthropic
- n8n (workflow automation)
- Google Drive, Google Docs, Google Sheets, Gmail

## How To Use

1. Import the JSON workflow file into your n8n instance
2. Replace YOUR_API_KEY_HERE with your Claude API key
3. Connect your Google account credentials
4. Create a Google Drive folder called: Meeting Notes — AI PM Tool
5. Save meeting notes as Google Docs to that folder
6. Watch the RAID log appear automatically in Google Sheets

## Built By

Shivoy Malhotra  
LinkedIn: linkedin.com/in/shivoymalhotra
