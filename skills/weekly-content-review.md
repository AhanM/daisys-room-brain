# Skill: weekly content review

**Trigger:** "run weekly content review" (or the Sunday scheduled task).
**Read first:** `context/content-playbook.md` (structure, metrics, flagship threshold).

## Steps

### (a) Pull data
1. **Instagram:** export the Trial Reels Shared Tracker with the Google Drive connector's download tool (`exportMimeType` = xlsx). The plain read tool only returns one sample row per tab, so don't use it. Then run `python3 -I scripts/ig_summary.py <file>` and work from its output. Follow the sheet's README rules.
2. **TikTok** (built-in browser, account @daisysroom.band, already logged in):
   - Open `https://www.tiktok.com/tiktokstudio/content`. In the page, hook XHR/fetch responses whose URL contains `item_list` into `window.__items` (keyed by `item_id`), then click the "Posts (Created on)" header twice and scroll the list to trigger loads. Each item has create_time, duration, play_count, like_count, comment_count, share_count, favorite_count (saves), is_pinned, desc. Keep the last 14 days.
   - For each of this week's posts, open `https://www.tiktok.com/tiktokstudio/analytics/<item_id>` and `get_page_text` for average watch time, watched full video %, new followers, retention drop-off second, For You %.
   - Skip pinned and show-promo posts.
   - Tag section and format in this order: (1) last week's daily plan, matched by day; (2) the same-day Instagram reel with the same length, using Muse's section tag; (3) ask Ahan under Questions. Unanswered posts stay `unconfirmed`: they count for consistency but are left out of section analysis.
   - Append rows to `logs/experiments.md`.
3. If a source fails, say so in one line and continue with the rest. Never estimate missing numbers.

### (b) Run the strategy
- Judge only 48h+ posts. Exclude 0-view distribution failures and show promos (per README).
- Views first. Engagement rate and TikTok watch time/completion as context.
- Compare one variable at a time: section (format fixed) and format (section fixed).
- n < 3 = hint, not finding.
- Check each Rotation cell: Keep / Test / Cut, using the flagship threshold.

### (c) Summarize learnings
Use **last week only** (the Mon to Sun just ended), Instagram views as the ranking, TikTok watch time and completion as context. A format = visual + on-screen text, so rank visuals, sections and text hooks separately (the script prints all three). Top 2 of each. Flag n = 1 results as hints.

### (d) Recommend next week
- A **format = visual + on-screen text**, always as one unit. No separate text variable.
- **4 sections x 5 formats = 20 videos. No repeats.** Plus **1 TikTok carousel format** per week.
- **Sections:** 2 core + **2 challengers** from the queue in `context/song-sections.md`. After each run, update that file's status column with the week's results and move the queue forward.
- **Freshness rule (survival of the fittest):** keep last week's top 2-3 formats; replace the rest with fresh ones from idea generation with **fresh** ones every week.
  - Fresh sections come from `context/song-sections.md` (untested first).
  - Fresh formats come from `skills/idea-generation.md` (Megafolder + saved videos, new since last run).
- 3 videos per day. Existing-footage videos early in the week, new footage later; group new footage into as few shoots as possible.

## Output format (one phone screen per section)

**0. Week in review**: table, rows Mon to Sun, columns: IG trial reels | TikToks (music posts only). One line: total, zero-post days, days below 3.
**1. Data status**: one line. Sources pulled, anything missing.
**2. Learnings (last week only)**: top 2 visuals, top 2 sections, top 2 on-screen texts, each with median views and n. One line of TikTok context.
**3. Next week's mix**: 4 sections, 4 visuals, the constant text, and the text being tested (with full wording).
**4. Daily plan**: table: day | video 1 | video 2 | video 3 | new footage? Each video = section · visual · text code. Then a text-code legend and one line on what to film and when.
**5. Questions for Ahan**: max 3.

No preamble, no recap of method, no em dashes.
