# product_context_from_whiteboards.md

Revision source: 

# Product Context From Whiteboards

## 1. Raw Extracted Notes

### Photo 1

#### Left side: Sponsors

* Sponsors:

  * Nia

    * people context and memory layer
  * Tensorlake

    * always active agent and workflow runtime
  * InsForge

    * backend layer
  * Hyperspell

    * data and RAG layer
  * Twilio

    * messaging transport layer

#### Top center: Pain point

* PainPoint

  * talking to NPCs

#### Center right: Event flow

* Event Sign Up

  * agent wakes up
  * asks goals for events
  * pulls context/data
  * Nia infers context

    * memory
  * rank people
  * generate briefs
  * event follow up

    * better context/NPCs for events

#### Diagram structure

* A vertical flow starts at “Event Sign Up.”
* The flow moves down into the agent waking up, asking the user for event goals, pulling context/data, and then using Nia to infer context and memory.
* The system then ranks people and generates briefs.
* A large bracket or loop connects this process to event follow up and better context for future events.

---

### Photo 2

#### Left side: Sponsors

* Sponsors:

  * Nia

    * people context and memory layer
  * Tensorlake

    * always active agent and workflow runtime
  * InsForge

    * backend layer
  * Hyperspell

    * data and RAG layer
  * Twilio

    * messaging transport layer

#### Top left: Pain point

* PainPoint

  * talking to NPCs/bots
  * wasting time

#### Middle left: User need or query examples

* finding signal people
* any baddies
* 1. Any VC’s
* 3. high signal
* 4. [unclear]

#### Center: Event flow

* Event Sign Up

  * agent wakes up
  * asks goals for events
  * pulls context/data
  * Nia infers context

    * memory
  * rank people
  * generate briefs
  * event follow up

    * better context/NPCs for events

#### Right side: Problem

* Problem

  * approved event?
  * handle hidden or unavailable attendee lists

#### Lower right

* to signal messages
* ask questions
* messages
* connections
* LinkedIn?
* X?
* for invite?

#### Diagram structure

* The pain point on the left connects toward finding “signal people.”
* “Finding signal people” connects into example queries.
* Example queries point into the event sign up and agent flow.
* The event flow ends near messages, questions, and follow up.
* The right side problem notes suggest a blocker: if the user is not approved for an event, the attendee list may not be visible.

---

### Photo 3

#### Left side: Sponsors

* Sponsors:

  * Nia

    * people context and memory layer
  * Tensorlake

    * always active agent and workflow runtime
  * InsForge

    * backend layer
  * Hyperspell

    * data and RAG layer
  * Twilio

    * messaging transport layer

#### Top center

* Joins event →

#### Center: Problem

* Problem

  * people active/active?
  * from when user signs up

#### Top right: Event timing example

* Event 2 to 8pm
* sign up 5pm
* pulls 15 min
* stops 30 min after start

#### Center left

* retrieve system prompts
* efficient
* AI
* vs. Auto

#### Center

* who to scrape

  * too many

#### Right center

* filter top 10 based on goals

#### Bottom center

* who actually goes vs. non attend

#### Diagram structure

* “Joins event” points toward the problem of determining which people are active or available from the moment the user signs up.
* The timing example shows an event that runs from 2 to 8pm, with the user signing up at 5pm.
* The scraper or agent appears to pull data for 15 minutes and stop 30 minutes after the event starts.
* A central problem is deciding “who to scrape” because there may be too many people.
* The solution direction is to filter the top 10 people based on the user’s goals.
* There is a note about determining who actually attends versus who does not attend.

---

## 2. Cleaned and Organized Notes

### Working product label

* PainPoint is currently being used as a product label.
* The actual final product name is not decided yet.

### Core idea

* The product helps users get more value out of networking events.
* After a user joins an event on Luma or Partiful, the system scrapes the visible attendee list.
* The system gathers context about attendees from public or available sources, especially LinkedIn and X.
* The user interacts with the product through SMS messages instead of a traditional front end interface.
* The user can ask natural language questions such as:

  * “Find me people who are VCs investing in med tech.”
  * “Any VC’s?”
  * “Any high signal people?”
* The system returns relevant people, short profiles, and conversation starters.
* The goal is to help users avoid low value conversations and quickly find people aligned with their goals.

### Pain point

* Users waste time at events talking to people who are not aligned with their goals.
* The whiteboards call these low alignment conversations “talking to NPCs.”
* “NPCs” means people who are unlikely to provide value for the user’s current goal, not literally artificial characters.
* In a polished product spec, this should be written as:

  * low value conversations
  * low alignment attendees
  * people not relevant to the user’s goals
* Users need help identifying which attendees are worth talking to before or during the event.

### User goal matching

* The product should understand what the user wants from an event.
* The user’s goals determine which attendees are useful.
* Example:

  * If the user is raising funding, VCs may be useful.
  * If the user already has funding and needs technical engineers, VCs may be less useful.
* People should be ranked from most useful conversation to least useful conversation based on the user’s current goals.

### Attendee context and mini profiles

* The system generates mini profiles for relevant people.
* A mini profile may include:

  * career background
  * current role
  * investment focus
  * interests
  * social signals
  * relevance to the user’s goal
  * conversation starters
* Example mini profile:

  * “This person worked as a surgeon for 20 years before pivoting to AI. They may be useful for your med tech project.”
* Example social context:

  * “This person likes boba and Laufey. Start a conversation about that.”

### Signal people

* “Signal people” means people who align with the user’s goals or seem generally valuable to know.
* Signal people can include:

  * investors
  * founders
  * engineers
  * med tech people
  * high achieving people
  * socially relevant people
  * people matching a user query

### Main interface

* The main interface is messaging based.
* The app operates through an LLM.
* The user asks questions through messages.
* There is no major front end UI planned on the whiteboard besides the messaging interface.

The product will be accessed through a messaging first interface. For the MVP, users will text a Twilio powered phone number from the iPhone Messages app or any standard SMS app. The assistant will receive inbound messages through Twilio webhooks, process the user’s event question or goal, and reply with ranked attendees, mini profiles, and conversation starters. This keeps the interface lightweight for live events because users do not need to open a full dashboard.

### Event approval blocker

* The system can only scrape attendee data if the attendee list is visible.
* If the user is on a waitlist or has not been approved, the app may not be able to access the event attendee list.
* The board raises the need to handle hidden or unavailable attendee lists.
* Confirmed blocker:

  * If the attendee list is not visible, scraping may not work.

### Scraping scope problem

* There may be too many attendees to scrape deeply.
* The system needs a way to decide who to scrape or process first.
* The board suggests filtering the top 10 people based on the user’s goals.
* This implies a two stage process:

  * first identify possible relevant attendees
  * then gather deeper context for the best matches

### Event timing behavior

* The board includes an example event:

  * Event runs from 2 to 8pm.
  * User signs up at 5pm.
  * System pulls data for 15 minutes.
  * System stops 30 minutes after the event starts.
* This likely relates to when the agent begins and ends scraping or monitoring.
* The exact intended timing behavior needs confirmation.

---

## 3. Product Idea Summary

PainPoint is a messaging based AI networking copilot for events. Once a user joins an event on Luma or Partiful, the assistant scrapes the visible attendee list and gathers context from sources like LinkedIn, X, and Instagram. The user can text the assistant with a goal, such as finding VCs who invest in med tech, finding high signal people, or identifying attendees with shared interests. The assistant ranks attendees by usefulness, generates mini profiles, and gives conversation starters so the user can spend less time in low value conversations and more time talking to people aligned with their goals.

The product appears to be built around an always active event agent that wakes up when the user signs up for an event, asks or infers the user’s goals, pulls attendee context, ranks people, generates briefs, and supports follow up through SMS messages.

---

## 4. Key Problems

### User problems

* Users waste time at events talking to people who are not aligned with their goals.
* Users often do not know who in the room is worth approaching.
* Users may not have enough context to start strong conversations.
* Users may want to find specific categories of people quickly.
* Users may need help turning attendee lists into useful action.
* Users may attend events where the best people are not obvious from name or profile alone.
* Users may not know who actually attends versus who only RSVP’d.

### Business or product problems

* The product needs access to event attendee lists.
* The product may fail if the user is waitlisted or not approved for the event.
* The product must handle hidden or unavailable attendee lists.
* The product must avoid scraping too many people deeply because that may be inefficient.
* The product needs to prioritize which people to research first.
* The product needs to produce useful results through a message interface, not a complex UI.
* The product needs to decide when to start and stop scraping or monitoring.
* The product needs to integrate sponsor technologies in a way that clearly supports the build.

### Technical problems

* Scraping attendee lists from Luma and Partiful.
* Gathering data from LinkedIn, X, and Instagram.
* Matching people to the user’s event goals.
* Ranking attendees by usefulness.
* Generating accurate mini profiles.
* Generating conversation starters.
* Maintaining memory and context across events.
* Supporting event follow up.
* Handling cases where attendee lists are hidden or inaccessible.
* Distinguishing actual attendees from people who RSVP but do not attend.
* Avoiding unnecessary scraping of low relevance attendees.
* Mapping each SMS sender to the correct user and active event session.

### Important implied privacy and compliance questions

* Whether scraping LinkedIn, X, Instagram, Luma, and Partiful is allowed under each platform’s rules.
* Whether users and attendees need consent.
* Whether sensitive personal traits should be inferred or avoided.
* How long attendee data should be stored.
* Whether the product should avoid ranking people based on attractiveness or other sensitive personal judgments.
* The “Any baddies?” phrase should stay only as a raw whiteboard example, not as a serious MVP feature, because it creates privacy and reputation risk.

These concerns are not fully written on the whiteboards, but they are directly implied by the data sources and product behavior.

---

## 5. Target Users

### Primary users

* People attending networking events.
* Founders attending startup events.
* Builders looking for investors, engineers, advisors, or collaborators.
* People trying to find high value conversations at Luma or Partiful events.
* Users who prefer messaging an assistant instead of using a full dashboard.

### Possible user goals

* Find VCs.
* Find VCs investing in med tech.
* Find technical engineers.
* Find high signal people.
* Find people with shared interests.
* Find people useful for a project, company, or career goal.
* Get conversation starters before approaching someone.
* Follow up with useful contacts after an event.

### Stakeholders

* Event attendees.
* Event organizers.
* Users looking for networking value.
* Sponsor technology providers.
* Possible backend or infrastructure providers.
* Possible data or context providers.

---

## 6. Core Features

### Event signup trigger

* User joins an event on Luma or Partiful.
* The event signup triggers the agent.
* Tensorlake wakes the agent workflow after the event join action.

### Attendee scraping

* The system scrapes visible attendees from the event page.
* Supported event platforms:

  * Luma
  * Partiful
* Limitation:

  * If the user is waitlisted or the attendee list is not visible, the app may not be able to scrape users.

### Social and professional context scraping

* The system gathers context from:

  * LinkedIn
  * X
  * Instagram
* Priority:

  * LinkedIn and X are top priority.
  * Instagram is also useful for interests and social context.

### Goal collection

* The agent asks the user what their goals are for the event.
* The user can also directly ask a goal oriented query through SMS.
* Example goals:

  * find VCs
  * find med tech investors
  * find technical engineers
  * find high signal people
  * find people with shared interests

### Ranking people

* The system ranks attendees from most useful to least useful.
* Ranking depends on the user’s current event goals.
* Ranking is contextual, not universal.
* Example:

  * A VC is highly relevant if the user is raising money.
  * A VC is less relevant if the user already has funding and wants technical engineers.

### Mini profile generation

* The system generates a brief for each relevant person.
* Each brief may include:

  * who they are
  * what they do
  * why they matter
  * why they are relevant to the user
  * useful background
  * interests
  * conversation starters

### Conversation starters

* The assistant suggests how to start conversations.
* Conversation starters can be based on:

  * work background
  * company
  * investment focus
  * project relevance
  * social media interests
  * shared interests

### Messaging interface

* The product is accessed through SMS messages.
* Users text a Twilio powered phone number.
* Users can access the assistant from the iPhone Messages app or any standard SMS app.
* Twilio handles inbound and outbound SMS.
* The assistant replies with ranked people, mini profiles, and suggestions.
* The whiteboards do not show a full front end UI.

### Event follow up

* The board includes “event follow up.”
* The product may support post event follow up.
* Possible follow up outputs:

  * who to message
  * what to say
  * reminders
  * better context for future events
* Exact follow up behavior is not fully specified.

### Memory and context

* Nia is planned for agent context of people.
* The system uses memory and context.
* The memory may help the assistant understand:

  * user goals
  * past events
  * past conversations
  * preferred types of contacts
  * attendee profiles
* Exact memory scope needs clarification.

### Data and RAG

* Hyperspell is planned as the data and RAG layer.
* Hyperspell handles attendee context retrieval.
* Hyperspell organizes profile data.
* Hyperspell supports grounding and search across collected event and people data.

### Top 10 filtering

* The system may filter down to the top 10 attendees based on the user’s goals.
* This helps avoid scraping or analyzing too many attendees deeply.
* This is likely a practical ranking and efficiency layer.

### Actual attendance detection

* The board includes “who actually goes vs. non attend.”
* The product may need to distinguish actual attendees from people who RSVP but do not show up.
* The method is not specified.

---

## 7. User Flows

### Flow 1: User joins an event

* User joins a Luma or Partiful event.
* Tensorlake wakes the agent workflow.
* The agent checks whether the attendee list is visible.
* If the attendee list is visible, the system scrapes attendees.
* If the attendee list is not visible because the user is waitlisted or not approved, scraping may fail.

### Flow 2: Agent asks for goals

* After the user joins an event, the agent asks what the user wants from the event.
* The user gives a goal.
* Example:

  * “I want to meet VCs who invest in med tech.”
* The system uses that goal to decide who is relevant.

### Flow 3: User directly messages the assistant

* User opens the iPhone Messages app or another SMS app.
* User texts the Twilio powered phone number.
* User asks a question.
* Example:

  * “Find me people who are VCs investing in med tech.”
* Twilio receives the inbound SMS and sends it to the backend through webhooks.
* InsForge maps the sender’s phone number to the correct user and active event session.
* The assistant searches attendee context.
* The assistant returns ranked people and conversation starters through SMS.

### Flow 4: Scraping and context generation

* System starts from the event attendee list.
* System pulls profile data from LinkedIn, X, and Instagram.
* Hyperspell organizes and retrieves relevant attendee context.
* Nia adds memory and people context.
* InsForge stores event sessions, user goals, attendees, and message history.
* System generates mini profiles for people.
* System ranks the people according to user goals.

### Flow 5: Top 10 attendee filtering

* Event has many attendees.
* System cannot or should not deeply research everyone.
* System filters to the top 10 based on goals.
* System generates deeper briefs for those people.

### Flow 6: In event assistance

* User is at the event.
* User texts the assistant.
* Assistant tells the user who to talk to.
* Assistant gives pointers and conversation starters.
* User uses that information to avoid low value conversations.

### Flow 7: Event follow up

* Event ends or user finishes conversations.
* Assistant uses event context and memory.
* Assistant may suggest follow up messages.
* Assistant may store useful context for future events.
* Exact follow up flow is not fully defined.

### Flow 8: Event timing behavior

* Event runs from 2 to 8pm.
* User signs up at 5pm.
* Agent begins pulling data after signup.
* Board says “pulls 15 min.”
* Board says “stops 30 min after start.”
* This may describe a scraping window or monitoring window.
* Exact intended behavior needs clarification.

---

## 8. Data and Inputs

### Event platforms

* Luma
* Partiful

### Social and professional sources

* LinkedIn
* X
* Instagram

### Messaging source

* Twilio SMS
* iPhone Messages app
* Standard SMS apps

### User inputs

* Event signup
* User SMS messages
* User event goals
* Possible examples:

  * “Any VC’s?”
  * “Any high signal people?”
  * “Find me people who are VCs investing in med tech.”
* Raw whiteboard example only:

  * “Any baddies?”

### Event data

* Event attendee list
* Event timing
* Event approval status
* Whether the user is waitlisted or approved
* Whether attendee list is visible
* RSVP list
* Possible actual attendance signal

### Attendee data

* Names
* Jobs
* Companies
* LinkedIn profiles
* X profiles
* Instagram profiles
* Interests
* Background
* Social signals
* Relevance to user goals

### Memory and context

* Nia is planned for context about people.
* Memory may include user preferences and past event context.
* Memory may include previous useful contacts.
* Memory may improve future event recommendations.

### Sponsor product usage

* Nia:

  * People context and memory layer.
  * Nia helps the agent understand people, user preferences, past event context, and relevance between attendees and the user’s goals.

* Tensorlake:

  * Always active agent and workflow runtime.
  * Tensorlake handles the agent that wakes up, runs event workflows, pulls data, and manages longer running background processes.

* InsForge:

  * Backend layer.
  * InsForge handles auth, database, storage, APIs, user event sessions, message routing, and coordination between the messaging layer, scraping layer, ranking layer, and LLM response layer.

* Hyperspell:

  * Data and RAG layer.
  * Hyperspell handles attendee context retrieval, profile data organization, grounding, and search across collected event and people data.

* Twilio:

  * Messaging transport layer.
  * Twilio provides the phone number and SMS infrastructure so users can text the assistant from the iPhone Messages app or any standard SMS app.

---

## 9. Outputs and Results

### Main outputs

* Ranked list of relevant attendees.
* Mini profiles for people.
* Conversation starters.
* Pointers for how to approach a person.
* Answers to natural language event queries.
* Top 10 people based on the user’s goals.
* Follow up suggestions after the event.
* SMS replies from the assistant through Twilio.

### Example output style

* Person A:

  * Worked as a surgeon for 20 years before pivoting into AI.
  * Relevant because they may understand clinical workflows and med tech adoption.
  * Good opener: ask about the transition from surgery to AI.

* Person B:

  * Likes boba and Laufey based on social profile signals.
  * Relevant for a more casual conversation based on shared interests.
  * Good opener: mention boba spots or music.

### Expected user benefit

* Less wasted time.
* Better networking outcomes.
* More targeted conversations.
* Faster identification of useful people.
* Stronger conversation openings.
* Better post event follow up.
* No need to open a full dashboard during a live event.

---

## 10. System Architecture Clues

### Confirmed or strongly supported by the whiteboards and clarifications

* Messaging based LLM interface.
* SMS through Twilio, accessed from the iPhone Messages app or any standard SMS app.
* Agent wakes up after event signup.
* Event attendee scraping from Luma and Partiful.
* Context scraping from LinkedIn, X, and Instagram.
* Ranking layer based on user goals.
* Brief generation layer.
* Memory/context layer using Nia.
* Always active agent and workflow runtime using Tensorlake.
* Backend layer using InsForge.
* Data and RAG layer using Hyperspell.
* Messaging transport layer using Twilio.
* Possible prompt system or retrieval of system prompts.
* Filtering system to avoid processing too many people.
* Top 10 relevant people output.

### Final architecture wording

The product is a messaging based AI networking copilot for events. Users interact with the assistant through SMS using a Twilio powered number. InsForge provides the backend for users, events, sessions, storage, and API coordination. Tensorlake runs the always active event agent workflows. Hyperspell powers the data and RAG layer for retrieving and organizing attendee context. Nia provides people context and memory so the assistant can personalize recommendations across events. The system uses this stack to rank attendees, generate mini profiles, and give conversation starters based on the user’s goals.

### Twilio Messaging Layer

Twilio will handle inbound and outbound SMS for the MVP. Each user’s phone number will be mapped to an active event session, allowing the backend to connect incoming texts with the correct event, attendee list, user goals, previous recommendations, and conversation history. Twilio only handles the messaging transport. InsForge handles backend state, Nia handles memory and people context, Tensorlake handles agent workflows, and Hyperspell handles data retrieval and grounding.

### Updated pipeline

* User joins a Luma or Partiful event.
* Tensorlake wakes the agent workflow.
* The agent checks whether the attendee list is visible.
* The system pulls attendee data.
* Hyperspell organizes and retrieves relevant attendee context.
* Nia adds memory and people context.
* InsForge stores event sessions, user goals, attendees, and message history.
* User texts the assistant through Twilio.
* The assistant ranks attendees based on the user’s goal.
* The assistant replies with top people, mini profiles, and conversation starters.

### Possible pipeline details

* User joins event.
* Tensorlake wakes the agent workflow.
* System checks attendee visibility.
* System scrapes attendee list.
* System asks user for goals or receives goals through SMS.
* System pulls external profile context.
* Hyperspell organizes and retrieves relevant attendee context.
* Nia uses memory and people context to understand relevance.
* InsForge stores event sessions, user goals, attendees, and message history.
* System ranks people.
* System generates mini profiles.
* System answers user questions through Twilio SMS.
* System supports follow up after the event.

### Not confirmed

* Whether there will be a separate dashboard.
* Whether the product will send follow up messages automatically.
* Whether follow up messages are generated only or sent automatically.
* Whether the system will store all attendee data long term.
* Whether the system can legally or technically scrape all intended platforms.
* Whether the system can access attendee lists before event approval.
* Whether actual attendance can be detected reliably.
* Whether “stop 30 min after start” is the final timing rule.

---

## 11. Open Questions

### Product scope

* Is the first version only for Luma and Partiful?
* Should the product work before the event, during the event, after the event, or all three?
* Should event follow up be part of the first version?
* Should the assistant only suggest messages, or should it send them too?
* Should there be any UI besides the SMS message interface?

### Data access

* How will the system access Luma and Partiful attendee lists?
* What happens if the attendee list is hidden?
* What happens if the user is waitlisted?
* How should the system handle hidden or unavailable attendee lists?
* How will LinkedIn, X, and Instagram data be retrieved?
* Will the system use public profile pages, APIs, browser automation, user provided links, or another method?

### Ranking

* What exact signals determine “most useful”?
* How should the system weigh professional relevance versus social relevance?
* Should the user choose categories like investors, engineers, founders, collaborators, or general high signal?
* Should the system rank based only on the current event goal or also long term user goals?
* Should the system avoid attraction based ranking entirely outside of raw brainstorm notes?

### Memory

* What user information should be remembered?
* What attendee information should be remembered?
* Should memory persist across events?
* Can users delete memory?
* Should the product remember people the user already met?

### Brief generation

* What should every mini profile include?
* How short should briefs be?
* Should the assistant cite where profile information came from?
* Should the assistant show confidence levels?
* How should uncertain or inferred details be labeled?

### Messaging

* Will one Twilio number serve all users, or will users get separate numbers?
* How will phone numbers map to user accounts?
* How will users connect their Luma or Partiful event to their SMS session?
* How should the assistant handle multiple active events for the same user?
* What should happen if a user texts without an active event session?

### Timing behavior

* When should scraping begin?
* How long should scraping continue?
* What does “pulls 15 min” mean?
* What does “stops 30 min after start” mean?
* If a user signs up after the event already started, should the agent still scrape?
* Should the system refresh the attendee list during the event?

### Attendance accuracy

* How can the system know who actually attends?
* Is RSVP enough?
* Should it mark people as “listed attendee” rather than “confirmed present”?
* Should the user manually mark who they met?

### Safety, privacy, and compliance

* What platforms allow scraping under their terms?
* Should the product require user consent before scraping?
* Should attendee information be cached?
* How long should data be stored?
* Should the product avoid attraction based ranking?
* Should the product avoid sensitive inferences?
* Should the product avoid making claims that are not directly supported by public data?

### Sponsor usage

* Confirm exact role boundaries between InsForge, Tensorlake, Nia, Hyperspell, and Twilio.
* Confirm whether Nia is the memory layer, people context layer, or both.
* Confirm whether Tensorlake is the always active agent layer.
* Confirm whether Hyperspell stores data, indexes data, retrieves data, or only powers RAG over data stored elsewhere.
* Confirm whether InsForge will be the source of truth for user sessions, message history, and event state.

---

## 12. Assumptions

### High confidence assumptions

* PainPoint is a temporary product label, not necessarily the final name.
* The core product is an AI assistant for event networking.
* Luma and Partiful are the main event sources.
* LinkedIn and X are top priority data sources.
* Instagram is also used for interests and social context.
* The main interface is SMS through Twilio.
* Users can access the assistant from the iPhone Messages app or any standard SMS app.
* The assistant ranks people based on the user’s goals.
* The assistant generates mini profiles and conversation starters.
* The system cannot scrape attendee lists that are not visible to the user.
* The product is meant to reduce wasted time in low value conversations.
* Hyperspell is the data and RAG layer.
* InsForge is the backend layer.
* Tensorlake is the always active agent and workflow runtime.
* Nia is the people context and memory layer.
* Twilio is the messaging transport layer.

### Medium confidence assumptions

* The system will use a two stage process where it first gathers event attendees, then filters to the top 10 before deeper research.
* The agent will wake up automatically after signup.
* The product will support both pre event preparation and during event question answering.
* Event follow up will be supported in some form.
* Memory will persist across multiple events.
* InsForge will store user event sessions, user goals, attendees, and message history.
* Twilio webhooks will route inbound messages to the backend.
* Hyperspell will support retrieval across collected attendee and profile context.

### Low confidence assumptions

* The timing rule is that the scraper pulls for 15 minutes and stops 30 minutes after event start.
* The product will detect who actually attended rather than who only RSVP’d.
* The product will retrieve or manage system prompts dynamically.
* The product will send messages or invites, rather than only drafting them.
* The product will support attraction based queries beyond raw whiteboard brainstorming.

---

## 13. MVP Assumptions

### Small demo cost note

For a small hackathon or demo version, Twilio can be used with a small number of test messages. The initial demo only needs enough SMS usage to show the core experience of texting the assistant, receiving ranked event attendees, and getting conversation starters. The main product risk is not SMS cost. The harder parts are attendee access, enrichment quality, ranking accuracy, and privacy compliance.

---

## 14. Potential Product Spec Sections

### Overview

* Product summary
* Problem statement
* Target users
* Event networking use case

### User goals

* Founder goals
* Investor discovery
* Engineer discovery
* Collaborator discovery
* High signal contact discovery
* Interest based discovery
* Follow up goals

### Supported platforms

* Luma
* Partiful
* LinkedIn
* X
* Instagram
* Twilio SMS

### Core user flows

* Join event flow
* Goal collection flow
* Attendee scraping flow
* Ranking flow
* Mini profile flow
* In event messaging flow
* Follow up flow

### Data model context

* User
* Phone number
* Event
* Event session
* Attendee
* User goal
* Profile source
* Signal score
* Mini profile
* Conversation starter
* Follow up item
* Message history
* Memory item

### Ranking logic context

* Goal matching
* Relevance signals
* Top 10 filter
* Confidence
* Personalization
* Exclusions

### Agent behavior context

* Wake up trigger
* Scraping window
* User messaging
* Memory usage
* Follow up behavior
* Failure states

### Technical architecture context

* Twilio messaging layer
* InsForge backend
* Tensorlake agent workflow runtime
* Hyperspell data and RAG layer
* Nia people context and memory layer
* Event scraper
* Social profile collector
* LLM response layer
* Ranking layer
* Brief generation layer
* Data storage
* Sponsor product mapping

### Privacy and compliance context

* Platform rules
* User consent
* Attendee data handling
* Data retention
* Sensitive inference policy
* User control and deletion

### MVP scope

* Messaging interface through Twilio SMS
* Access from the iPhone Messages app or any SMS app
* InsForge backend
* Luma and Partiful attendee list support
* LinkedIn and X priority for context
* Instagram optional
* Hyperspell for data retrieval and RAG
* Nia for people context and memory
* Tensorlake for always active agent workflows
* Top 10 people ranked by user goal
* Mini profiles
* Conversation starters
* Manual follow up suggestions

### Future scope

* Better actual attendance detection
* Automated follow up drafting
* Event history memory
* More platforms
* Better profile enrichment
* Stronger personalization
* Better ranking controls
* Optional dashboard
* Multi event support
* Stronger source grounding
* Better privacy controls
