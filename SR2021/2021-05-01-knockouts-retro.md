# SR2021 Knockouts Retrospective

## Present

- Alistair Lynn
- Andy Barrett-Sprot
- Antoine Petty
- Dan Trickey
- Jake Howard
- James Seden Smith
- Jenny Fletcher
- Karina Kwiatek
- Peter Law
- Will Barber

We used easyretro.io to run this retro. We took 10 minutes to write up our own
notes before sharing them (see "Raw comments" below), then had discussion on
retrospective topics we felt warranted it. We tried to avoid forwards facing
discussions in this session, though we should definitely review these topics
when planning our future tasks.

## Topics

### Timings mishaps during the livestream

_This section was noted when the issues happened and is kept for context_.

There were a number of contributing factors to this:

- No single producer / having one of the commentators as presenter is very hard

- High latency on the livestream, making it hard to judge timings from the outside

  - This also meant that the knockouts chart didn’t have the latest scores available when it was shown, as the scores weren’t published yet, since the scores were published based on the livestream

- Static knockout scheduler not working with our normal delays mechanism

- Livestream overlay not handling changes meaningfully

### Producer

It feels fairly obvious now that we need this. A lot of the things which were complex today were a result of this not being a separate role. The lack of this also created complexities around not spoilering the commentators.

This would also enable the commentators to fill for time when needed, while the producer is fixing stuff.

This being a separate role would enable easier comms between support volunteers and commentators if needed.

How widely did we ask about this? We did have Alana looking at this, but hit technical issues.

Sounds like others would have been interested in doing this, but we weren’t able to find them.

What do we need to change to ensure that we publicise this directly.

We had previously publicised the Doings including around livestream, which we thought was publicised but not very clearly.

During the leagues we managed to automate much of the role, which (combined with the leagues being relatively simpler) led us to believe it may not have been needed.

We have earlier in the year invited volunteers for other roles and not had anyone express an interest, which discourages pushing for people in other roles.

Need to clarify the runbook that the producer should be not one of the commentators.

However we also need to source and train the roles well in advance of the event, which likely means earlier than the way we’ve been using the checklist.

We need confirmation that a producer is going to be present for the livestream sessions, though this shouldn’t be a reason not to get more people involved.

### Wider volunteer engagement

We’ve been pretty good at reducing the amount of work needed to run a competition, meaning that there is less to do.

However we do always benefit from more mentors.

Would we benefit from running more explicit training sessions as a way to maintain engagement?

Would assigning an internal mentor help? This could be their point of contact and could guide them through being a volunteer, building a personal relationship with them.

We need to get better at advertising to our wider volunteer base. That is -- not just posting in Slack. But also ensuring that messaging to the email list have a clear path for getting involved.

Would a formal onboarding process help here? Some of this has been happening recently, driven by Rob & Tom.

This still feels like it has quite a lot of friction. We’ve found that joining e.g: a Discord, lurking for a while then joining more formally tends to be a more common route.

We should asses the reach that our emails have.

Feels like we’d benefit from a volunteer coordinator for all of SR, someone who can specialise on this.

### Teams don’t know about `R.zone`

The kits are very much framed around a physical kit, which is confusing in a simulator based competition. Even otherwise the organisation of this part of the docs isn’t clear.

We’ve previously discussed having a how-to section which is distinct from a reference section.

Not sure how much the teams are using the docs? We feel like we’re pushing them quite a bit, we mention them in lots of presentations and in the microgames.

Short of mentoring them it’s hard to ensure that they’re actually using them?

Could we make use of the microgames to encourage different behaviour by zone?

The docs are also currently laid out around the physical components, which makes a lot less intuitive sense during the SR2021 virtual competition.

The current docs didn’t really get any updates for this year, and what was done was done on the Saturday morning of Kickstart.

When have we last reviewed the UX of the docs? Never.

Action: Dan to own reviewing the UX of the docs.

### Press coverage & sponsor outreach

Would have been much better if we’d done this much sooner. The outreach we did (for the press) was on Friday evening before the knockouts livesteram.

It’s very different sharing a livestream link with someone than inviting them to a physical competition.

We can still reach out to press after the event (and this was something we planned to do).

Would be really useful to have some pre-made graphics or templates for social media, along with a list of hashtags and where to post etc.

There were lots of teams this year on Instagram. We do have a small presence there, but the platform itself isn’t actually very usable.

### Collaboration between the comp & kit teams

There hasn’t been very much.

The kit team has not been involved in developing the simulator. When asked about this, the kit team committee were not interested in being involved even though members of the competition team offered considerable support. There wasn’t anyone with the knowledge or time to take on supporting the simulator.

Feels like there’s a lack of trust between the two teams.

If we had been able to involve the kit team in the simulator development, there would have needed to be good communication between the teams during the development of the modules.

Are there any regular meetings between the two teams in order enable cross-team communications?

The regular competition meeting are open to all, however this doesn’t necessarily create a clear communication channel as it would rely on the kit team coming to all those meetings.

Would it make sense to think a bit more about the SR teams as like company departments? While this does create some delineation, it also provides an alternative for how we handle cross-team projects -- that they’re organised as projects rather than remaining purely within a single team.

The earlier game design meetings felt like they achieved input from a wider collection of people, though the later module design meetings haven’t.

A lot of the simulator development this year has been done by a very small number of people. How do we get better at onboarding people and finding out who’s interested in picking things up? Part of the simulator work challenge is that it’s not something which can be picked up without prior introduction.

Let’s take this to the next members’ meeting.

### Livestream chat moderation

It would have been better to have had some more upfront guidance on what our limits are, what’s acceptable, what is the escalation policy, etc. so that moderators know what rules they’re holding people to. This makes it easier for our actions to be defensible.

The SR (volunteer) code of conduct could help here, however at the moment it’s framed around volunteers at the moment. It does state that it covers competitors, though we’re not sure that we publicise it to them?

There are other organizations which have similar challenges, we can probably reference their guidelines/rules to build ours.

Action Karina: pull together some guidelines for the runbook. James can help.

YouTube’s moderation tooling is limited. Let’s explore what we can do with them.

Should we consider other platforms if there are ones which are better supported? (Twitch maybe?)

### Multi camera / vision mixing

It might be nice to have more camera viewpoints in the simulator. One approach could be to use a secondary application to render the videos (e.g: Blender). This could push up the production value of the matches. However this might also take a lot more time to render, both in terms of compute and volunteer time to organise.

Webots does have a WebGL export which would easily allow more camera angles etc., however the quality of these visuals are pretty bad compared to the current renders.

Due to the nature of this, it would be very time constrained -- needing to happen between the submission deadline and the start of the livestream.

There may be approach here which enable this to be handled without too much effort being needed.

Parked this discussion for now.

### Live scoring changes the dynamic

It made the prize awards a bit less climactic.

Not sure this is a bad thing though -- ideally the game would be easy enough to work out anyway.

This did seem to increase engagement and made commentary easier too.

### SRComp

There are some technical issues here we’ve found.

Did we do enough to test it? Feels like we caught a lot of the functionality side, but less so checking that operationally it would work.

### Use of volunteer time

Are we too perfectionist? Feel like we could be better at stepping back and considering simpler solutions.

We often end up spending late nights on things. Is this partly a function of evenings being the times that we as volunteers have free and that it’s easier to spend time then? Is there a scheduling thing here?

Would a hard cutoff on weekdays be useful?

We’ve run 4 league sessions, the knockouts and five friendlies session; even before Doings we’ve had events on a majority of the weekends this year.

### Analysis

It was really good!

We ended up actually starting this later than ideal. We definitely could have started this sooner.

Feel like we’ll have a better idea of how to do this next time.

This could be a way to get people involved in commentary -- as an easy way in to doing a small bit.

Can it work at a physical event? Probably, but might need some tweaks.

There’s lots of things we can do here in the future.

## Raw comments

These notes are extracted from the retro tool used to facilitate the discussions above.

Where several people had made similar notes these are merged, into a single bullet point, with `|` separating the entries.

### Liked

* Analysis segments |
  Analyst Role |
  Analysts added some extra information! |
  Today: Having in-stream analysis is really good.
* New international teams
* Preparation doings before events
* Year: more people learning about and contributing to SRComp.
* Felt like we worked well as a team. Not that it's been easy, but we've worked together well and tackled challenges as a group.
* Split league |
  Modules
* Year: Discord was really good. Much more reactive, better community. |
  Discord |
  Interaction between teams in Discord and chat celebrating each others success |
  Good team engagement in chat and discord |
  Funposting
* Commentators recovering from technical difficulties |
  Recovered from technical difficulties well
* Today: livestream interactions were good.
* Really great matches throughout the knockouts. |
  Games felt exciting - few matches where there were immobile robots |
  Quality of matches
* Today: Having time to pause and reflect right after the knockouts is so different to the usual competition.Feels good to have a break :)
* Year: Will taking a lead on the simulator. Also that his coding has improved a lot over time as a result.
* Video and commentary on livestream |
  Commentary was great |
  Some nice graphics/visualizations
* Today: well done livestream moderators
* Friendlies
* we shipped a competition
* Lots of like cards
* Game design choices meant knockout results didn't feel too unfair
* Replay videos were useful.
* Today: ramped up our social media recently
* Teams' enthusiasm
* Full rehearsal of intro and outro

### Learned

* Competition - Teams don't know about R.Zone
* Live scoring makes things way easier to munge
* SRComp Delays don't affect the static scheduler |
  SRComp still has a long way to go.
* Avoiding spoilers is a messy business
* Major time crunch with preparing analysis
* Surprising upsets happen disconcertingly often
* Experimented with game mechanics
* Just because there's no venue doesn't mean the competition is easy
* Hand signals and explicit colour/play-by-play roles for each match makes joint commentary much easier
* 🇦🇺 is OP
* always need more rehearsal time than is planed for
* How to do livestreams
* Increased youtube chat moderation
* Today: Google slides as livestream content is under-rated. |
  How to present with a remote clicker |
  Remote slide clicker + meet call is an effective way of doing multi-person broadcasts remotely

### Lacked

* Producer |
  Producer |
  Today: realtime livestream producer (felt like this created a bunch of knock-on challenges) |
  Would have been smoother with separate producer role |
  Stream got a bit chaotic |
  Need a producer
* Wider volunteer engagement
* Press coverage |
  would have been better to reach out to potential sponsors and press earlier if we wanted more responses/ better reach
* explicit communication to team leaders about scope of their role
* Rehearsals/content for analysis bit last minute |
  Today: Overall stream rehearsals.
* Spontaneous Friendlies
* Communication with teams which communicated outside of Discord
* Gaps in social media
* Testing the simulator beforehand to get an idea of the usages
* Competition - Tutorials on how to code a robot
* Functional finals delay mechanism
* Hairbrush
* Mentors
* Jenny Crab vtuber
* Today: SRComp/website displays in the knockouts aren't great during the knockouts.This has always felt a small issue, but really felt out of place today.
* Scheduling issues especially around third place match should ideally have been tested/better communicated
* Spicier stream visuals

### Longed For

* better collaboration between comp and kit team
* More well defined livestream chat moderation rules
* Multi-camera setup / vision mixing
* Fewer late nights
* More simulator developers
* Would have been nice for a greater no. of teams to make it into knockouts
* beehives |
  bees
* Today: earlier preparation of livestream analysis content.
* Year/Today: A clearer picture of which things would turn out to be important.Or: more forward thinking and planning.We've achieved a lot of great stuff, but much of it (again) happened as a result of a last minute push.
* Better match timing display for commentary than staging screen
* Better livestream account verification (alternatives to youtube?)
* A better livestream overlay. |
  A rewrite of the livestream overlay
* More teams?
* Live production studio
* Competition - more mentoring
* easier way to find previous match info for commentating/analysis
* Year: a bit more flexibility in SRComp.
* Better rendering
* should reconsider colour choices with accessibility in mind
* Full-stack finals rehearsal
* Producer to handle stream problems
* Professional commentators?
