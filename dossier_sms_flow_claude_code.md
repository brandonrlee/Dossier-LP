# Claude Code Build Spec: Dossier SMS-First Web App Flow

## Goal
Build the core web app flow for **Dossier**, inspired by folk's SMS-first onboarding and dashboard aesthetic.

Dossier is a pre-event intelligence agent that lives in your texts. Users verify their phone number, text a Twilio number with an event link, and receive a pre-event room brief.

Core product sentence:

> Dossier tells you who matters, what to say, and who to remember before you walk into the room.

## Stack
Use the existing project stack if present. If starting from scratch, use:

- Next.js App Router
- TypeScript
- Tailwind CSS
- `lucide-react`
- optional: `motion` for subtle transitions

Install if missing:

```bash
npm install lucide-react motion
```

## App routes to create

Create or update these routes:

```txt
app/page.tsx                    Landing page
app/login/page.tsx              Phone number login
app/verify/page.tsx             6-digit OTP code page
app/start/page.tsx              Text Dossier / Twilio number page
app/dashboard/page.tsx          Dashboard overview
app/brief/page.tsx              Sample event brief
```

Use static fake data. Do not build real auth or Twilio unless already configured.

## Design system

Match folk-style minimalism:

- warm off-white / pale lavender background
- centered layout
- clean black text
- elegant serif headings where possible
- rounded pill buttons
- thin gray borders
- soft shadows
- generous whitespace
- no dashboard clutter
- SMS-first, not CRM-first

Colors:

```txt
background: #fbfaf7
soft lavender: #faf7ff
text: #111111
muted text: #737373
border: #d8d4ce
primary button: #2c292c
greenlight: #34c759
risk orange: #f97316
```

## Screen 1: Landing page `/`

Purpose: Explain Dossier and push user to text-first onboarding.

Top nav:

```txt
Dossier | by Nozomio Labs
Features
Pricing
FAQ
Log in
Get Dossier
```

Hero:

```txt
small pill: ● 12,482 rooms briefed
headline: meet dossier. it lives in your texts and reads the room before you do.
subheadline: connect luma, partiful, and your calendar. dossier quietly finds who matters, what to say, and who you forgot to follow up with.
primary button: text dossier now →
secondary button: see what it does ↓
```

Right side: iPhone/message preview with Dossier conversation.

Below hero: three cards:

```txt
1. Text an event link
Luma, Partiful, Calendar, or pasted attendee list.

2. Get the room brief
Who matters, what to say, who to avoid.

3. Follow up after
Dossier drafts the messages you should send tomorrow.
```

Dark CTA band:

```txt
one hour before the event, dossier texts you the brief.
button: Get Dossier
```

## Screen 2: Login page `/login`

Purpose: User enters phone number.

Layout should match screenshot style.

Top-left:

```txt
Dossier | by Nozomio Labs
```

Centered content:

```txt
headline: welcome.
subtitle: what’s your phone number? we’ll text you a code.
```

Phone input:

```txt
🇺🇸 +1 | (201) 555-0123
```

Buttons:

```txt
continue with phone
OR
continue with telegram
```

Footer:

```txt
by continuing you agree to our terms and privacy policy.
```

Clicking “continue with phone” should navigate to `/verify`.

## Screen 3: OTP verification `/verify`

Purpose: User enters 6-digit code.

Top-left:

```txt
Dossier | by Nozomio Labs
```

Centered content:

```txt
headline: enter your code.
subtitle: sent a 6-digit code to 🇺🇸 +1 480 246 5857
```

Show six rounded OTP boxes.

Below:

```txt
didn’t get it? try again
```

Clicking or submitting should navigate to `/start`.

## Screen 4: Text Dossier page `/start`

Purpose: Tell user to text the Twilio number.

This is the page immediately after verification.

Top-left:

```txt
Dossier | by Nozomio Labs
```

Centered content:

```txt
headline: text dossier.
subtitle: send your first event link to start your room brief.
```

Large center card:

```txt
label: your dossier number
big number: +1 (480) 246-5857
helper: text this number a Luma, Partiful, or Calendar link.
```

Buttons:

```txt
copy number
open messages
```

Below card: iMessage-style preview:

```txt
Dossier: send me an event link and i’ll brief the room before you arrive.
User: https://lu.ma/ai-founder-party
Dossier: got it. scanning attendees now.
Dossier: brief will be ready before the event.
```

Small status pill:

```txt
● agent waiting for first event
```

Three steps:

```txt
1. Text the number
2. Send an event link
3. Get your brief before you arrive
```

Footer:

```txt
Dossier texts you only when there’s something useful. No spam.
```

Primary button can route to `/dashboard` for demo purposes.

## Screen 5: Dashboard overview `/dashboard`

Purpose: Show the whole system overview after onboarding.

Style should match folk dashboard cards.

Top left:

```txt
Dossier
```

Top right:

```txt
text dossier →
settings icon
```

Main heading:

```txt
good to see you.
```

Card grid:

### Card 1: Rooms

```txt
label: ROOMS
main: 2 briefs ready
sub: AI Founder Party · Miami Tech Dinner
```

### Card 2: On a schedule

```txt
label: ON A SCHEDULE
main: 3 running
sub: next in 19h · founder_party_scan
```

### Card 3: Upcoming

```txt
label: UPCOMING
main: AI Founder Party
sub: Tonight 8 PM · 47 attendees scanned
button: view brief
```

### Card 4: Recently

```txt
label: RECENTLY
items:
- scanned 47 attendees
- found 5 high-signal people
- drafted 3 openers
- flagged 2 clout risks
```

### Card 5: Memory Graph

```txt
label: MEMORY GRAPH
main: 12 people remembered
sub: 3 warm intros · 2 missed follow-ups · 4 investors
```

### Card 6: Plan

```txt
label: PLAN
main: trial · 3d
bullets:
✓ texts before events
✓ remembers who you met
✓ drafts follow-ups
button: subscribe →
```

## Screen 6: Brief page `/brief`

Purpose: Show the sample event brief.

Header:

```txt
AI Founder Party
Tonight · 8:00 PM · 47 attendees scanned
Brief ready
```

Sections:

```txt
Talk to first
Warm intros
Clout risks
Forgot to follow up
```

Person cards:

### Maya Chen

```txt
badge: 94 GREENLIGHT
role: Healthcare AI investor
why: mutual friend Alex · interested in workflow AI
opener: “Are you seeing more healthcare AI founders start with workflow wedges or diagnostics?”
```

### Jake

```txt
badge: 31 CLOUT RISK
role: Stealth founder
why: no product link · 14 podcast clips · buzzword-heavy bio
directive: Talk if bored. Do not pitch.
```

### Sarah Lee

```txt
badge: 88 FOLLOW-UP
role: Founder
why: you met last month and forgot to follow up
draft: great seeing you again — I still owe you that healthcare AI note.
```

Bottom CTA:

```txt
Dossier already scanned your next room.
button: send me the brief
```

## Components to create

```txt
components/AppShell.tsx
components/AuthCard.tsx
components/PhoneInput.tsx
components/OtpInput.tsx
components/MessagePreview.tsx
components/DashboardCard.tsx
components/PersonCard.tsx
components/StatusPill.tsx
components/StepList.tsx
```

## Interactions

Keep simple:

- `/login` button routes to `/verify`
- `/verify` routes to `/start`
- `/start` “open dashboard” or primary CTA routes to `/dashboard`
- dashboard “view brief” routes to `/brief`
- copy number button copies `+14802465857` if easy; otherwise show static button

## Acceptance criteria

The app must:

- feel SMS-first
- feel like a premium personal agent, not B2B CRM
- have consistent folk-like visual language
- include login → code → text number → dashboard → brief flow
- use realistic fake data
- be responsive
- avoid real integrations
- not require env vars

## Do not build

Do not build:

- real Twilio logic
- real OTP auth
- real Luma or Partiful integrations
- real scraping
- payment logic
- complex settings

This is a polished hackathon demo flow.
