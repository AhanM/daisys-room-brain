# Skill: weekly content review

**Trigger:** "run weekly content review" (or the Sunday scheduled task).
**Read first:** `context/content-playbook.md` (structure, metrics, flagship threshold).

## Steps

### (a) Pull data
1. **Instagram:** export the Trial Reels Shared Tracker with the Google Drive connector's download tool (`exportMimeType` = xlsx). The plain read tool only returns one sample row per tab, so don't use it. Then run `python3 -I scripts/ig_summary.py <file>` and work from its output. Follow the sheet's README rules.
2. **TikTok:** open TikTok Studio in the built-in browser. For every post from the last 14 days: views, avg watch time, % watched full, likes, comments, saves, shares, new followers. Append rows to `logs/experiments.md`.
3. **Non-music posts:** the tracker drops show promos, so for the week-in-review count, also list this week's Instagram posts from the profile in the built-in browser (trial and regular).
4. If a source fails, say so in one line and continue with the rest. Never estimate missing numbers.

### (b) Run the strategy
- Judge only 48h+ posts. Exclude 0-view distribution failures and show promos (per README).
- Views first. Engagement rate and TikTok watch time/completion as context.
- Compare one variable at a time: section (format fixed) and format (section fixed).
- n < 3 = hint, not finding.
- Check each Rotation cell: Keep / Test / Cut, using the flagship threshold.

### (c) Summarize learnings
Top 2 formats and top 2 song sections by median views (n >= 3 to qualify). Name one under-tested contender if it beats them on fewer posts.

### (d) Recommend next week
Pick 2 sections + 1 test section, 2 formats + 1 test format. Build 3 videos per day, Mon to Sun. Mark each video as existing footage (combo already posted, per the script's footage list) or NEW footage. Group all new footage into one shoot early in the week.

## Output format (one phone screen per section)

**0. Week in review**: table, rows Mon to Sun, columns: IG trial reels | TikToks | total (music posts only). One line: total, zero-post days, days below 3.
**1. Data status**: one line. Sources pulled, anything missing.
**2. Learnings**: top 2 formats and top 2 sections, each with median views and n. Plus the contender, if any.
**3. Next week's mix**: small table: sections (2 + test) and formats (2 + test).
**4. Daily plan**: table: day | video 1 | video 2 | video 3 | new footage? Then one line: what to film and when.
**5. Questions for Ahan**: max 3.

No preamble, no recap of method, no em dashes.
