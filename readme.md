# Aarya – AI-Powered Nurse Interviewer & Hospital Outreach System

## Overview

Aarya is an AI-powered voice interviewer designed to automate nurse outreach, screening, and initial interviews for hospitals and healthcare organizations.

It fully replaces manual first-round recruitment calls using AI voice conversations powered by Vapi and Twilio.

---

## Key Features

- Automated outbound and inbound calls
- AI-driven nurse screening & qualification
- IVR handling and transfer waiting
- Call recording and transcripts
- Terminal & API-based call triggering
- Scalable campaign system

---

## Architecture

Backend / Terminal
   ↓
Vapi API
   ↓
Twilio (Telephony)
   ↓
Hospitals & Nurses
   ↓
AI Conversations + Logs

---

## Core Components

### Twilio

- Provides phone numbers
- Handles PSTN calling

### Vapi

- AI voice orchestration
- Call routing
- Recording & transcripts

### Aarya Assistant

- Conversation logic in System Prompt
- Opening line in First Message
- IVR & transfer handling

---

## Example Outbound Call (cURL)

```bash
curl https://api.vapi.ai/call \
  -H "Authorization: Bearer YOUR_PRIVATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistantId": "YOUR_ASSISTANT_ID",
    "phoneNumberId": "YOUR_PHONE_NUMBER_ID",
    "customer": {
      "number": "+DESTINATION_PHONE_NUMBER"
    }
  }'
```

---

## Monitoring

- Live listening via Vapi dashboard
- Call logs and recordings
- Full transcripts

Path: Observe → Call Logs

---

## Compliance

- Recording disclosure in opening message
- No confidential data collection
- Polite opt-out handling

---

## Status

✅ AI assistant live
✅ Twilio integrated
✅ Outbound calls working
✅ Recording enabled

---

## Contact

[Your Name]
[Company]
[Email]
[Phone]

