# SR2021 League 2 Retrospective 2021-02-06

## Attendees

- Andy Barrett-Sprot
- Alistair Lynn
- Jake Howard
- James Seden Smith
- Jenny Fletcher
- Peter Law

## Topics

- Today went well

- Running the scheduler
  - We can run the scheduler in OBS if we use webm
  - WebM takes too long to transcode
  - Maybe interface directly with OBS to play the .mp4s

- Overlay had issues during the first match
  - This was due to the compbox not being updated.
  - We should have done a test-run beforehand.

- Music
  - There was too little variety of music
    - Jenny has made a list
  - Music stopped
    - Was played manually through VLC, missed hitting the loop button as it was set up rather quickly
  - Music volume varied between tracks
    - Volume needs to be normalized

- There was no scheduled start time for volunteers
  - There should be an announcement the day before
  - Shouldn’t be before 9am

- SRComp
  - Was a very manual faff to get the compstate set up for this league.
  - No tooling to handle adding part of a league (lots had to be done manually)
  - Some parts are hard-coded to be 4 teams.
  - League schedule import resulted in very similar matches this time around as league 1 (initially, we fixed it before running matches).
  - James hit a unicode issue on Windows.

- LSS & WGS ‘dropped out’, realized it quite late.
  - We should not keep code between modules, they should need to submit each time.

- Not much commentary prep time.
  - Should run through the intro, outro, & presentation. (30 mins?)
  - Final League positions weren’t announced.
  - Jake’s door was left open.

- Logs sent out fast.

- Rules were ready while they were talked through.

- Module 3 code will likely be shipped this evening.

- HRS2 left their robot in a blocking position.
  - They were doing it accidentally.
  - We don’t think we need to do anything more about this.

- A commentator was doing production
  - Allowing to naturally change between slides was a benefit
  - This means prep time was taken from commentary.
  - (Also volume levels take longer to be fixed)
  - Bus factor in the form of concentrating these roles in the same person
    - Doesn’t allow others to learn
    - Not conducive to creating documentation (which then makes it hard for others to contribute at all)

- We can improve on the production quality
  - End title ‘GAME OVER’
  - Sound effects?
  - Longer time between matches was a bit short?
  - Webcam screen didn’t feel like a good use of space
    - Vertical rather than horizontal didn’t help here
    - ‘You’ instead of ‘Jake Howard’.
  - Flashing colons in the countdown screen
    - Colon should either not flash, or flash at 2Hz.
  - Orange on Blue titles don’t look good.
  - Jake needs to clean his room.
  - Hand off between Alistair and Jake needs improvement.

- Answering questions in the livestream:
  - The team had some different opinions to the answers of the commentators.
    - Team should filter (& discuss) questions before they’re put to the commentators

- Struggling teams
  - One team has not scored any game points
    - We should see if they need any help
  - We should see if we can help LSS and WGS.

- Announcing to teams when the cutoff for code submissions is
  - Generally wasn’t clear and not really early enough
  - Lead to confusion about how to cope with LSS/WGS not submitting code
  - So we didn’t gain much from the earlier deadline

## Tasks

- Have a checklist of tasks which need doing ([#262](https://github.com/srobo/competition-team-minutes/issues/262))
  - Pre-event
  - Match running
  - Go-live
  - Have a doing to make this.

- Construct schedule and run matches on Friday evening ([#263](https://github.com/srobo/competition-team-minutes/issues/263))

- Prepare music more in advance, and have more of it ([#264](https://github.com/srobo/competition-team-minutes/issues/264))

- Set & publicise a regular scheduled start time for volunteers ([#265](https://github.com/srobo/competition-team-minutes/issues/265))

- Solve the OBS video scheduling issues ([#266](https://github.com/srobo/competition-team-minutes/issues/266))

- Simplify adding league matches to the compstate ([#267](https://github.com/srobo/competition-team-minutes/issues/267))

- Allocate prep time for commentators ([#268](https://github.com/srobo/competition-team-minutes/issues/268))

- Allocate a Q&A moderator, post questions (with answers) in Slack for the commentators to talk about ([#269](https://github.com/srobo/competition-team-minutes/issues/269))

- Have larger match spacing ([#270](https://github.com/srobo/competition-team-minutes/issues/270))

- Try and make webcam feeds be horizontal (and hide names) ([#271](https://github.com/srobo/competition-team-minutes/issues/271))

- Remove flashing colons on countdown screen ([#272](https://github.com/srobo/competition-team-minutes/issues/272))

- Change contrast of title on rules screen ([#273](https://github.com/srobo/competition-team-minutes/issues/273))

- Send email to all teams about whether they’d like mentoring ([#274](https://github.com/srobo/competition-team-minutes/issues/274))
  - Also send to discord

- Send email to league 2 no-shows about whether they’re interested in competing ([#275](https://github.com/srobo/competition-team-minutes/issues/275))
