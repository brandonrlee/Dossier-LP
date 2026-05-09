# Claude Code Build Spec: Dossier Phone Hero Animation

## Goal
Build a premium folk-style animated phone hero for **Dossier**.

Dossier is a pre-event intelligence agent that lives in texts. Users send an event link from Luma, Partiful, or Calendar, and Dossier replies with who matters, what to say, who to avoid, and who they forgot to follow up with.

The hero should feel like:

> **meet dossier. it lives in your texts and reads the room before you do.**

## Stack
Use the existing project stack if present. If starting from scratch, use:

- Next.js App Router
- TypeScript
- Tailwind CSS
- `motion` / Framer Motion
- `lucide-react`

Install if missing:

```bash
npm install motion lucide-react
```

## Files to create or update

Create:

```txt
components/DossierPhoneHero.tsx
components/MessageBubble.tsx
components/FloatingIcon.tsx
```

Update:

```txt
app/page.tsx
app/globals.css
```

## Visual direction

Match this vibe:

- warm off-white background
- premium minimal layout
- large iPhone mockup
- iMessage-style chat bubbles
- floating app icons around phone
- soft shadows
- subtle bottom fade
- slow float animations
- no loud gradients
- no generic AI robot visuals

Colors:

```txt
background: #fbfaf7
text: #111111
phone: #ffffff
blue bubble: #0a84ff
gray bubble: #e9e9eb
accent green: #34c759
accent orange: #f97316
```

## Component requirements

### `DossierPhoneHero.tsx`

Build a centered iPhone mockup with:

- black rounded phone frame
- dynamic island
- Dossier conversation header
- message bubbles
- bottom fade
- floating icons

Phone dimensions should be approximately:

```txt
width: 360px
height: 720px
border radius: 56px
black frame: 8-10px
```

### Message content

Use these exact messages:

User blue bubble:

```txt
i’m going to this ai founder party tonight
```

User blue bubble:

```txt
https://lu.ma/ai-founder-party
```

Dossier gray bubble:

```txt
got it. scanning 47 attendees.
```

Dossier gray bubble:

```txt
brief ready. found 5 high-signal people, 2 clout risks, and 1 missed follow-up.
```

Dossier gray bubble:

```txt
maya chen — healthcare ai investor. ask her: “are you seeing founders start with workflow wedges or diagnostics?”
```

Dossier gray bubble:

```txt
jake — stealth founder. no product link. 14 podcast clips. clout risk: high. talk if bored. do not pitch.
```

## Animation requirements

Use Motion for React.

Animate:

1. Phone enters with fade + slight upward movement.
2. Floating icons gently bob forever.
3. Message bubbles appear with slight delay.
4. Floating icons rotate very subtly.

Example animation behavior:

```tsx
animate={{ y: [0, -12, 0], rotate: [-6, 4, -6] }}
transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
```

## Floating icons

Use floating app-style icons around phone:

- Messages icon, green
- Calendar icon, purple
- Link/event icon, indigo
- Send/Telegram-style icon, blue

Use `lucide-react` icons if no assets exist.

## Landing page hero integration

In `app/page.tsx`, create a two-column hero:

Left:

```txt
small pill: ● 12,482 rooms briefed
headline: meet dossier. it lives in your texts and reads the room before you do.
subheadline: send a luma, partiful, or calendar link. dossier texts back who matters, what to say, and who you forgot to follow up with.
primary button: text dossier now →
secondary button: see sample brief ↓
```

Right:

```txt
<DossierPhoneHero />
```

## Copy for hero

Use this exact copy:

```txt
meet dossier. it lives in your texts and reads the room before you do.
```

```txt
send a luma, partiful, or calendar link. dossier texts back who matters, what to say, and who you forgot to follow up with.
```

CTA:

```txt
text dossier now →
```

Secondary CTA:

```txt
see sample brief ↓
```

## Tailwind styling guidance

Use classes like:

```txt
min-h-screen
bg-[#fbfaf7]
text-[#111111]
tracking-tight
rounded-full
rounded-[56px]
shadow-2xl
border-black
```

Add global background texture if easy:

```css
body {
  background: #fbfaf7;
}

.noise-bg {
  background-image: radial-gradient(rgba(0,0,0,0.035) 1px, transparent 1px);
  background-size: 18px 18px;
}
```

## Acceptance criteria

The finished hero must:

- Look premium and SMS-first
- Show Dossier inside an iPhone mockup
- Have animated floating icons
- Have sequential or polished message bubble animations
- Feel similar in spirit to folk/getfolk.app
- Clearly explain Dossier in under 5 seconds
- Be responsive enough for desktop and mobile

## Do not build

Do not build:

- real SMS/Twilio logic
- real Luma scraping
- real dashboard
- 3D scene
- generic AI assistant UI
- neon/purple SaaS gradients

Keep it focused on the hero animation.
