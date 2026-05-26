import streamlit as st
import os
from supabase import create_client, Client
from datetime import date
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="RAID Command Center", layout="wide")
st.title("🤖 Zero-Touch RAID Command Center")
st.caption("Live view of all Risks, Actions, Issues, Decisions across your programs.")

# Summary cards
open_items = supabase.table("raid_items").select("*", count="exact").eq("status", "Open").execute().count
high_critical = supabase.table("raid_items").select("*", count="exact").in_("severity", ["High", "Critical"]).neq("status", "Closed").execute().count
overdue = supabase.table("raid_items").select("*", count="exact").lt("due_date", str(date.today())).in_("status", ["Open", "In Progress"]).execute().count

col1, col2, col3 = st.columns(3)
col1.metric("Open Items", open_items)
col2.metric("High / Critical", high_critical)
col3.metric("Overdue", overdue)

st.divider()

# Filterable table
st.subheader("📋 All RAID Items")
type_filter = st.selectbox("Filter by Type", ["All", "Risk", "Issue", "Assumption", "Decision", "Action"])

query = supabase.table("raid_items").select("*").order("created_at", desc=True)
if type_filter != "All":
    query = query.eq("type", type_filter)

items = query.execute().data
st.dataframe(items, use_container_width=True)

st.divider()

# AI Q&A
st.subheader("🧠 Ask the Robot About Your RAID Log")
question = st.text_input("e.g., Which risks are overdue and critical?")

if question:
    context_data = supabase.table("raid_items").select("type,description,severity,owner,due_date,status,program_id").in_("status", ["Open", "In Progress"]).execute().data
    context_str = "\n".join([str(item) for item in context_data])

    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": "claude-haiku-4-5",
        "max_tokens": 500,
        "system": "You are a program management assistant. Answer the question using ONLY the provided RAID log data. If the answer is not there, say so.",
        "messages": [{"role": "user", "content": f"RAID log data:\n{context_str}\n\nQuestion: {question}"}]
    }

    with st.spinner("Claude is thinking..."):
        resp = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
    if resp.status_code == 200:
        answer = resp.json()['content'][0]['text']
        st.success(answer)
    else:
        st.error(f"Claude API error: {resp.status_code}")