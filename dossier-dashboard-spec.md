# Dossier — Dashboard Build Spec

You are building the logged-in dashboard for **Dossier**, an AI event-networking intelligence app. This file is the source of truth — follow it precisely. When the spec and your instinct disagree, ask before deviating.

---

## 1. Product context

Dossier helps founders/operators decide which events are worth attending and who to meet once they're there. It is **not a CRM**. It feels like a calm, premium intelligence tool — closer to ChatGPT/Claude UI than Salesforce.

The core insight: **Dossier remembers people across events.** Every person discovered at an event is stored once and updated as they reappear. Over time this becomes a living AI rolodex of every high-signal person in the user's orbit.

The dashboard answers four questions in three seconds:
1. Which events ahead are worth my time?
2. Who are the top 10 people to meet at each one?
3. Who keeps showing up across high-signal rooms?
4. Who have I saved, met, or want to follow up with?

Tone: clean, calm, smart, organized, high-signal, premium. No fluff, no fake complexity, no CRM patterns.

---

## 2. Stack

- **Framework:** Vite + React 18 + TypeScript
- **Styling:** Tailwind CSS 3.4 + shadcn/ui components
- **Icons:** lucide-react
- **State:** local React state only — no Supabase yet. Data lives in `src/data.ts` as static fixtures. Wire Supabase later behind the same shapes.
- **Fonts:** Geist (body), Geist Mono (numerals), Instrument Serif (display) — all loaded via Google Fonts in `index.css`.

This is a **single-page app with tab routing via local state**, not Next.js. Five tabs: Dashboard, Events, People, Saved, Settings.

---

## 3. Setup

```bash
pnpm create vite@latest dossier -- --template react-ts
cd dossier
pnpm add lucide-react clsx tailwind-merge class-variance-authority
pnpm add -D tailwindcss@3.4.1 postcss autoprefixer
pnpm dlx tailwindcss init -p
# shadcn init
pnpm dlx shadcn@latest init -y
# Install only the components actually used:
pnpm dlx shadcn@latest add button input sheet tooltip scroll-area textarea
```

Add path alias `@/*` → `./src/*` in `tsconfig.json` and `vite.config.ts`.

Run with `pnpm dev`. Production-ready single HTML bundle is **not required** — `pnpm build` is enough.

---

## 4. Project structure

```
src/
├── App.tsx                    # main shell + routing + state
├── main.tsx                   # entry
├── index.css                  # tokens + base + component utilities
├── data.ts                    # types + sample data
├── lib/
│   └── utils.ts               # cn() helper
└── components/
    ├── ui/                    # shadcn primitives only
    └── dossier/               # all custom components below
        ├── Sidebar.tsx
        ├── DossierLogo.tsx
        ├── PersonAvatar.tsx
        ├── FilterChip.tsx
        ├── CategoryTag.tsx
        ├── EventCard.tsx
        ├── EventDetailPanel.tsx
        ├── PersonRow.tsx
        ├── PersonCard.tsx
        ├── PersonProfileDrawer.tsx
        ├── DashboardView.tsx
        ├── PeopleView.tsx
        ├── SavedView.tsx
        └── SettingsView.tsx
```

Keep `App.tsx` to ~80 lines: layout shell, top-level state, view switching. Everything else lives in its own file.

---

## 5. Design system

### Color tokens

Define in `index.css` as HSL CSS variables (shadcn convention) and use via Tailwind's `bg-background`, `text-foreground`, etc.

| Token | HSL | Hex | Use |
|---|---|---|---|
| `--background` | `285 100% 99%` | `#FEFCFF` | Page background |
| `--card` | `0 0% 100%` | `#FFFFFF` | Card surface |
| `--secondary` / `--muted` | `258 100% 97%` | `#F5F0FF` | Soft lavender wash |
| `--border` | `266 65% 91%` | `#E9DDF7` | Borders, dividers |
| `--primary` | `258 100% 68%` | `#8B5CFF` | Primary CTAs, accents |
| `--accent` | `327 100% 68%` | `#FF5DB1` | Signal pinks, dots |
| `--foreground` | `258 14% 9%` | `#16141C` | Body text |
| `--muted-foreground` | `258 8% 44%` | `#6F687A` | Secondary text |

Add a fixed background gradient on `body`:
```css
background:
  radial-gradient(1200px 600px at 85% -10%, hsl(258 100% 95% / 0.55), transparent 60%),
  radial-gradient(900px 500px at -10% 110%, hsl(327 100% 95% / 0.35), transparent 55%),
  hsl(var(--background));
background-attachment: fixed;
```

### Typography

- Body: `Geist`, weights 300–700
- Display (headings, large numerals in stat cards): `Instrument Serif`
- Numerals (scores, counts, dates): `Geist Mono` with `font-variant-numeric: tabular-nums`

Helper classes in `@layer base`:
```css
.font-mono { font-family: 'Geist Mono', ui-monospace, monospace; font-feature-settings: "tnum", "ss01"; }
.font-serif { font-family: 'Instrument Serif', ui-serif, Georgia, serif; }
.tabular { font-variant-numeric: tabular-nums; }
```

### Component utilities (in `@layer components`)

```css
.surface {
  @apply bg-card border border-border rounded-xl;
  box-shadow: 0 1px 0 0 hsl(258 30% 95% / 0.6), 0 1px 3px 0 hsl(258 30% 60% / 0.04);
}
.surface-soft {
  @apply rounded-xl;
  background: hsl(258 100% 98%);
  border: 1px solid hsl(266 65% 93%);
}
.score-pill {
  @apply font-mono tabular text-[11px] font-medium px-1.5 py-0.5 rounded-md;
  background: hsl(258 100% 96%);
  color: hsl(258 60% 40%);
  border: 1px solid hsl(266 65% 92%);
}
.signal-dot {
  @apply inline-block w-1.5 h-1.5 rounded-full;
  background: hsl(327 100% 68%);
  box-shadow: 0 0 0 3px hsl(327 100% 92% / 0.7);
}
.pip {
  @apply inline-flex items-center gap-1.5 text-[11px] font-medium px-2 py-0.5 rounded-full border;
}
```

Subtle entrance animation only:
```css
@keyframes rise {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
.rise   { animation: rise 0.4s ease-out both; }
.rise-1 { animation-delay: 0.05s; }
.rise-2 { animation-delay: 0.10s; }
.rise-3 { animation-delay: 0.15s; }
```

No other animations. No hover lift. No gradient buttons. No emoji.

### Scrollbar

Slim, lavender, transparent track. Apply globally.

---

## 6. Data model

```ts
// src/data.ts

export type EventCategory =
  | 'startup-vc' | 'ai-tech' | 'creator-social'
  | 'healthcare' | 'university' | 'private';

export type PersonStatus =
  | 'not-met' | 'want-to-meet' | 'saved'
  | 'met' | 'followed-up' | 'ignored';

export interface Person {
  id: string;
  name: string;
  title: string;
  company: string;
  tags: string[];
  score: number;              // 0–100 relevance
  whyMeet: string;            // one-liner
  status: PersonStatus;
  eventIds: string[];         // every event this person has appeared at
  initials: string;
  hue: number;                // 0–360, drives avatar gradient
  talkingPoint?: string;
  introMessage?: string;
  summary?: string;
}

export interface DEvent {
  id: string;
  name: string;
  category: EventCategory;
  date: string;               // "Fri, Nov 14"
  dayLabel: string;           // "In 5 days"
  time: string;               // "7:00 PM"
  location: string;           // venue
  city: string;
  summary: string;            // one-line
  topSignal: string;          // "Active seed investors writing first checks"
  attendingPersonIds: string[];
}

export const ME = { firstName: 'Brandon', goal: '...' };
```

### Category metadata

Map of `EventCategory` → `{ label, description, tagBg, tagText }`. Each category has its own pastel background tint:

| Category | Label | Tint |
|---|---|---|
| `private` | Private / Invite-only | dark `#16141C/4%` |
| `ai-tech` | AI / Tech | blue `#EFF7FF` / `#1E5BBF` |
| `startup-vc` | Startup / VC | lavender `#F1ECFF` / `#5B3DCC` |
| `healthcare` | Healthcare | green `#EAF8F1` / `#1F7A4F` |
| `university` | University / Student | amber `#FFF7E6` / `#9A6B0A` |
| `creator-social` | Creator / Social | pink `#FFF0F8` / `#B83085` |

### Status metadata

Map of `PersonStatus` → `{ label, dot, text, bg, border }`. "Met" and "Followed up" are green. "Want to meet" / "Saved" are lavender. "Not met" / "Ignored" are neutral.

### Sample data (use exactly these IDs and shapes)

**6 events, 15 people**, with overlapping `attendingPersonIds` and `eventIds` so the repeat-detection UI has signal to display.

Events:
1. `e_ai_founder_dinner` — Private, AI Founder Dinner – Mission, in 5 days, 9 attendees
2. `e_cerebral_valley` — AI/Tech, Cerebral Valley Demo Night, in 9 days, 11 attendees
3. `e_yc_demo` — Startup/VC, Y Combinator Fall Demo Day, in 10 days, 3 attendees
4. `e_healthcare_roundtable` — Healthcare, Healthcare AI Roundtable at UCSF, in 11 days, 5 attendees
5. `e_stanford_mixer` — University, Stanford GSB Founder Mixer, in 13 days, 2 attendees
6. `e_creator_brunch` — Creator/Social, Creator Economy Brunch, in 14 days, 1 attendee

People (each must have a realistic `whyMeet`, 2–3 tags, a score 79–94, and `eventIds` that match their `attendingPersonIds` membership):

`p_sarah_chen` Partner @ SeedFund (94, AI/Healthcare/Seed, saved, 3 events) · `p_marcus_webb` Founder @ Cortex (91, AI/Agents/Infra, met, 2 events) · `p_priya_raman` Partner @ First Round (89, Vertical AI/Enterprise, want-to-meet, 4 events) · `p_daniel_park` VP Product @ Vercel (86, Devtools/DX, followed-up, 2 events) · `p_elena_rodriguez` Founder @ Remedy (92, Healthcare/Clinical AI, saved, 3 events) · `p_tomas_acuna` GP @ Spark Capital (88, Seed/Frontier, want-to-meet, 3 events) · `p_aisha_kapoor` Founder @ Lumen (84, Creator/Growth, want-to-meet, 2 events) · `p_jordan_reeves` Research Engineer @ Anthropic (90, AI/Agents/Research, not-met, 1 event) · `p_kenji_tanaka` Founder @ Rookie Health (87, Healthcare/Operator, saved, 2 events) · `p_lila_brown` Investor @ Founders Fund (93, Frontier/Seed, saved, 4 events) · `p_felix_ng` GP @ HF0 Fellowship (89, Accelerator/Founders, want-to-meet, 2 events) · `p_marina_solo` Founder @ Stitch (85, Devtools/OSS, not-met, 1 event) · `p_aaron_vasquez` Surgeon & Founder @ UCSF/Stealth (86, Healthcare/Operator, not-met, 1 event) · `p_mira_patel` Stanford GSB '26 (79, Student/Founders, not-met, 1 event)

`whyMeet` should be specific and actionable. Examples:
- "Leads SeedFund's healthcare AI thesis. Six checks in clinical workflow startups in 2025."
- "Pre-seed checks into Cursor and Cognition. Decisive — no second meeting."
- "Practicing cardiothoracic surgeon spinning out a clinical decision support tool."

For 3–4 of the highest-score people, also fill in `talkingPoint`, `introMessage`, and `summary`.

---

## 7. Layout

```
┌──────────┬─────────────────────────────────────┬──────────────────┐
│          │                                     │                  │
│ Sidebar  │  Main view                          │ Event detail     │
│ 240px    │  (Dashboard / Events / People /     │ panel            │
│          │   Saved / Settings)                 │ 440px            │
│          │  max-width 1100px, generous         │ (only on         │
│          │  horizontal padding                 │  Dashboard /     │
│          │                                     │  Events when     │
│          │                                     │  event selected) │
└──────────┴─────────────────────────────────────┴──────────────────┘
```

### Responsive

- **`lg` and up (≥1024px):** three-column layout above
- **`md` (768–1023px):** sidebar visible, event detail opens in a right `Sheet` instead of inline column
- **`sm` (<768px):** sidebar hidden behind a hamburger top bar (height 56px, sticky, white/85 backdrop-blur). Sidebar opens as a slide-in panel with backdrop. Event detail and person profile both open as full-width sheets.

---

## 8. UI spec — component by component

### `<Sidebar />`
- Width 240px, white/60 backdrop-blur, right border in `--border`
- Logo at top: small SVG of a folder/dossier shape + "Dossier" wordmark in Instrument Serif 20px
- Nav items: Dashboard, Events, People, Saved, Settings — each is a button with a 16px lucide icon and 13.5px label
  - Active state: lavender bg `#F5F0FF`, dark text, primary purple icon
  - Inactive: muted text, hover bg `#F8F4FF`
- Saved item shows a small mono-tabular count badge if > 0
- Bottom: a `surface-soft` card showing "This week — 3 high-signal events, 42 people worth meeting" with a Sparkles icon
- Below that: user chip (gradient avatar circle + first name + "Tract · SF" caption)

### Top of main view (Dashboard / Events / People / Saved)
Every view starts the same:
- Tiny uppercase eyebrow with optional dot indicator
- Display heading in Instrument Serif, 40–48px, tracking-tight: `Good evening, Brandon.` / `People` / `Your shortlist` / `Tune your signal`
- 15px muted subhead with inline mono-tabular numbers ("3 events ahead. 42 people worth meeting.")

### Search bar
- Full-width, height 44px, white card border
- 15px lucide `Search` icon left, ⌘K kbd hint right (hidden on mobile)
- Placeholder: "Search events, people, companies…"
- Focus ring: primary purple at 20% opacity

### Filter chips
- Pill buttons, 12.5px text
- Active: `bg-[#16141C] text-white border-[#16141C]` (dark, not purple — keeps the lavender calm)
- Inactive: white, muted text, lavender border on hover
- Optional count in mono after the label
- "Filter" label with a small `Filter` icon prefix

### `<EventCard />`
A button (the whole card is clickable). Padding 20px. Layout:

1. **Top row:** category tag + day-label ("In 5 days") in mono-tabular muted
2. **Title:** 16px medium, tracking-snug, truncated
3. **Meta row:** 12.5px muted, with `Clock` icon + date·time, then `MapPin` icon + location, separated by spacing
4. **`ChevronRight`** in the top-right corner, lavender, slides 2px right on hover
5. **Summary:** 13px muted, 2-line clamp
6. **Bottom row, left:** stacked overlapping avatars (first 4 attendees, 22px, -space-x-2, white border) + `+N` count in mono if more
7. **Bottom row, right:** mono-tabular signals separated by `·` —
   - `{n} high-signal` (count of attendees with score ≥ 85)
   - `<Eye/> {n} seen before` (count seen at ≥ 2 events)
   - `<Bookmark filled/> {n}` in primary purple if any saved are attending
8. **Footer:** dashed top border, then `<Sparkles/>` (accent pink) + "Top signal: " (muted) + topSignal text (foreground, medium, truncated)

Hover: border darkens to `#C9B4ED`, soft purple shadow appears.
Selected (when this event is the one shown in the detail panel): 2px purple ring at 30%.

### `<EventDetailPanel />`
Sticky right column on `lg+`, `Sheet` on smaller. Padding 24px.

**Header block** (border-bottom):
- Row: category tag (left) + close X (right)
- Display title in Instrument Serif 24px
- Meta: `Clock` + date · time, `MapPin` + location, city (12.5px muted)
- Description: 13px, 80% foreground
- **Stat strip:** 3-column grid of small `surface`-style boxes — each box has a 22px Instrument Serif tabular number and a 10.5px uppercase label. Labels: "To meet" / "Seen before" / "Saved" (saved box uses lavender accent variant)
- **CTAs:** primary `Build my plan` button with `ArrowUpRight` icon (purple, white text) + outline `Save event` with bookmark icon

**Scrollable body** with 4 sections, each separated by `space-y-7`:

1. **Top 10 people to meet** — `<TrendingUp/>` icon (purple)
   - Caption: "Ranked by relevance to your goals"
   - List of `<PersonRow>`, ranked 01..10
2. **People you've seen before** — `<Repeat/>` icon (purple)
   - Caption: "{n} repeat across your events"
   - Up to 4 rows, hide whyMeet, show "Seen at N events" tag
3. **New high-signal people** — `<Sparkles/>` icon (pink)
   - Caption: "First time appearing in a Dossier event"
   - Up to 4 rows, hide whyMeet
4. **Saved people attending** — `<Bookmark filled/>` icon (purple)
   - Caption: "{n} from your network"
   - All matching rows, hide whyMeet

Section headers are 12.5px medium, with right-aligned 11px muted caption.

### `<PersonRow />` (used inside event detail)
Single row, 38px avatar on left, name + score-pill + optional signal-dot inline, title·company below in muted, then optional whyMeet (12.5px), then tag chips. Save icon-button on the right that fades in on row hover. If `rank` prop given, mono-tabular `01..10` on the far left, muted lavender.

A `signal-dot` appears next to the name when `eventIds.length ≥ 4`. Wrap it in a Tooltip showing "High repeat signal · seen at N events".

### `<PersonAvatar />`
- Deterministic 135° gradient from `hsl(person.hue 80% 88%)` to `hsl((hue+30) 80% 78%)`
- Foreground color: `hsl(person.hue 60% 28%)`
- Initials inside, font weight 500, 1px white/60 border
- Sizes: 22 (stack), 38 (row), 42 (card), 64 (drawer)

### `<PersonCard />` (used in People + Saved views)
- `surface`, 16px padding
- Top: avatar (42px) + name (14px medium) + signal-dot if high-repeat + score pill (right)
- whyMeet (12.5px, 2-line clamp)
- Tag chips
- Footer (dashed top border):
  - Left: `<Repeat/>` + "Seen at N events" (Repeat icon turns pink for high-repeat)
  - Right: status pip + save icon-button

### `<PersonProfileDrawer />` — `<Sheet side="right">`, max-width 480px
1. **Identity row:** 64px avatar + name (Instrument Serif 24px) + title·company (13px muted) + tag chips
2. **Score band** (`surface-soft`): "RELEVANCE" eyebrow + score in Instrument Serif 26px purple + tier label ("Exceptional" ≥92, "High" ≥85, "Strong" ≥78, "Notable" else). On the right, "High repeat signal" with signal-dot if ≥4 events.
3. **Why meet** field: whyMeet + summary (smaller, muted)
4. **Your status** field: row of all 6 status pips, plus a separate Save toggle pip on the end. Click to switch.
5. **Seen at N events** field: vertical timeline list. Each item is a 6px purple filled circle, event name, category tag (xs size), and date in mono. Caption "Appears often in AI / healthcare rooms" if high-repeat.
6. **Suggested talking point** field (if present): `surface-soft` card, 13px text, `<MessageSquareQuote/>` icon in title
7. **Suggested intro** field (if present): `surface` card, 13px text wrapped in italic Instrument Serif quotes. Below: primary "Copy & open LinkedIn" button + outline "Edit"
8. **Your notes** field: 88px-min textarea, white, lavender focus ring

Each field has a 10.5px uppercase muted title with optional caption right-aligned in accent pink.

### `<PeopleView />` (Rolodex)
- Heading: "People". Subhead: "A living rolodex. Every person Dossier finds at an event is here — with their full event history. {repeatCount} people show up across multiple high-signal rooms."
- Search bar: "Search people, companies, roles…"
- Filter chips: Everyone (default active), Founders, VCs, Engineers, Healthcare, AI, Students, Operators, Investors. Each chip shows a count; hide chips with count 0.
- Grid: 2-column on `md+`, single column on mobile, `<PersonCard>` items sorted by score descending.

### `<SavedView />`
Two sections:
1. **Saved people** — grid of saved-status `<PersonCard>` items
2. **Events where saved people are attending** — grid of `<EventCard>` items where any attendee has status `saved`. Clicking one switches to Dashboard tab and selects that event.

### `<SettingsView />`
Minimal placeholder:
- "Tune your signal" heading
- "Goals" surface card showing the user's goal text + Edit button
- "Categories I care about" surface card with a row of selected category tags

---

## 9. Repeat-person detection — UI affordances only

The dedup/merge logic is **out of scope** for this build. The data is already deduplicated. But the UI must clearly communicate when someone is a repeat:

- **Pink signal-dot** next to name anywhere they appear, when `eventIds.length ≥ 4`
- **"Seen at N events"** chip on PersonRow (when `showSeenBefore` is true) and PersonCard footer
- **"People you've seen before"** section in event detail (anyone with `eventIds.length ≥ 2`)
- **"High repeat signal"** label with dot in profile drawer score band
- **"Appears often in AI / healthcare rooms"** caption on the "Seen at N events" timeline section in the drawer (when high-repeat)
- **Repeat icon turns pink** in PersonCard footer when high-repeat

The matching/merging logic itself will be a backend concern (Supabase + a job that matches by name+company+linkedin+email). Don't build it. Don't reference it in the UI as "scraped" or "merged" — use **People / Network / Rolodex / Seen Before / Signal Map** language only.

---

## 10. State & interactivity

All state is local React state in `App.tsx`:

```ts
const [tab, setTab] = useState<Tab>('dashboard');
const [search, setSearch] = useState('');
const [activeCategories, setActiveCategories] = useState<Set<EventCategory>>(new Set());
const [selectedEventId, setSelectedEventId] = useState<string | null>('e_ai_founder_dinner');
const [selectedPerson, setSelectedPerson] = useState<Person | null>(null);
const [profileOpen, setProfileOpen] = useState(false);
const [sidebarOpen, setSidebarOpen] = useState(false);
const [people, setPeople] = useState<Person[]>(PEOPLE);
```

Interactions that must work:
- Switching tabs
- Toggling category filter chips (multi-select)
- Searching events by event name, summary, attendee name, attendee company
- Searching people by name, company, title, tags
- Switching the People filter chip (single-select)
- Selecting an event → opens detail panel/sheet
- Closing the detail panel
- Selecting a person → opens profile drawer
- Save / unsave a person from any surface (PersonRow, PersonCard, drawer) — updates everywhere immediately
- Changing a person's status from the drawer — updates the pip color in card footers
- Opening sidebar on mobile

Things that don't need real behavior (UI present, no-op or `console.log`):
- "Build my plan" button
- "Save event" button (vs save person — different)
- "Copy & open LinkedIn" button
- Notes textarea (uncontrolled or controlled with no persistence)
- ⌘K keyboard shortcut (don't implement)

---

## 11. Acceptance criteria

A reviewer should be able to confirm each of these without asking:

- [ ] Five-tab layout (Dashboard, Events, People, Saved, Settings) with Dashboard and Events sharing the same view
- [ ] Events on Dashboard are grouped under category section headers in a stable order: Private → AI/Tech → Startup/VC → Healthcare → University → Creator
- [ ] Each event card shows category tag, day-label, title, meta row, summary, attendee avatar stack, three signal counts, and a "Top signal" footer
- [ ] Selecting an event opens a right-side panel (or sheet on small screens) with header, stat strip, two CTAs, and four ranked people sections
- [ ] Top 10 people section is ranked 01..10 and visually distinct
- [ ] People tab shows a filterable, searchable rolodex sorted by score
- [ ] Person profile drawer shows score band, why meet, status row, event timeline, talking point, intro message, and notes
- [ ] Status changes and save toggles propagate everywhere immediately
- [ ] Repeat-person UI cues are present in 4+ surfaces (signal-dot, seen-at chip, "people you've seen before" section, "high repeat signal" label)
- [ ] No "Recently" section anywhere
- [ ] No emoji, no purple gradient buttons, no heavy animations
- [ ] Lavender/white/purple palette holds across every surface
- [ ] Three-column layout on desktop; collapses cleanly to single column with sheets on mobile
- [ ] No TypeScript errors. No console errors at runtime.

---

## 12. Out of scope

Do **not** build:
- Auth / login screen (assume already logged in)
- Real Supabase/database integration
- Person dedup/merge logic
- Event scraping/ingestion
- AI-generated intro messages (use the static `introMessage` field)
- Email/LinkedIn integrations
- Analytics
- Settings beyond the two placeholder cards
- ⌘K command palette
- Dark mode
- Mobile-native (Expo) version — that's a separate project

If something feels missing, prefer to leave the affordance visible (button present, no-op) rather than build a half-working version.

---

## 13. Style guardrails

Things that will get rejected on review:
- Inter as the body font (use Geist)
- Purple gradient buttons or backgrounds (purple is for solid CTA only)
- Centered hero layouts with big call-to-actions (this is a tool, not a marketing page)
- Card hover lift / scale transforms
- Emoji in any UI text
- Drop shadows heavier than `0 1px 3px` at very low opacity
- Icons larger than 18px outside of the avatar/header context
- Bold body text used decoratively (bold is reserved for active nav items, names, and stat numbers)
- Anything that reads as "CRM" — pipeline stages, deal values, contact lists with phone columns
- Calling people "leads", "contacts", "prospects", or "scraped"

When in doubt: less is more, calm beats loud, and the user should be able to read the dashboard like a one-page intelligence brief.
