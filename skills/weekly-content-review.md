# Skill: weekly content review

**Trigger:** "run weekly content review" (or the Sunday scheduled task).
**Read first:** `context/content-playbook.md` (structure, metrics, flagship threshold).

## Steps

### (a) Pull data
1. **Instagram:** export the Trial Reels Shared Tracker with the Google Drive connector's download tool (`exportMimeType` = xlsx). The plain read tool only returns one sample row per tab, so don't use it. Then run `python3 -I scripts/ig_summary.py <file>` and work from its output. Follow the sheet's README rules.
2. **TikTok:** open TikTok Studio in the built-in browser. For every post from the last 14 days: views, avg watch time, % watched full, likes, comments, saves, shares, new followers. Append rows to `logs/experiments.md`.
3. If a source fails, say so in one line and continue with the rest. Never estimate missing numbers.

### (b) Run the strategy
- Judge only 48h+ posts. Exclude 0-view distribution failures and show promos (per README).
- Views first. Engagement rate and TikTok watch time/completion as context.
- Compare one variable at a time: section (format fixed) and format (section fixed).
- n < 3 = hint, not finding.
- Check each Rotation cell: Keep / Test / Cut, using the flagship threshold.

### (c) Summarize learnings
At most 3. Each must cite numbers and n. Flag confidence (high / medium / low). Note anything that contradicts last week's learnings.

### (d) Recommend next week
A concrete posting plan that fills the most valuable untested cells and doubles down on Keeps. Hold on-screen text constant unless the test is the text.

## Output format (keep it to one phone screen per section)

**1. Data status**: posts pulled per platform, how many judged (48h+), anything missing.
**2. Scoreboard**: this week's median and max views vs the last 4 weeks; flagships (>= threshold) this week.
**3. Learnings**: max 3 bullets, each with numbers, n, confidence.
**4. Rotation changes**: only cells that changed (section x format: old -> new status, why).
**5. Next week's plan**: table: day | platform | section | format | on-screen text. Then one line on what this week's test is.
**6. Questions for Ahan**: unconfirmed sections or tags, max 3.

No preamble, no recap of method, no em dashes.
