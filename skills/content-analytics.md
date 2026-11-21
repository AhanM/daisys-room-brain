# Skill: weekly content analytics (Flagship Evolution System)

Trigger: "run content analytics" or the Sunday scheduled task.
Method: see `context/content-playbook.md` for structure and metrics. Troy AI connector has the verbatim teaching.

## Goal
Find the **flagship**: the one or two song sections that convert best, then post them ~80% of the time and "throw the kitchen sink" of formats at them. Primary metric is **views** (distribution). Retention metrics explain them; shares decide whether a flagship can break the plateau.

## Phases (track which one we're in at the top of each report)
1. **Collect evidence.** Score candidate sections: top 3 performing section = 3 pts, high share rate = 2, strong comments = 1, +1 per flagship type it fits (melody, loop, kick in the face). Pick the top 5.
2. **Structured testing.** 5 sections x 4 proven formats = 20 posts over ~7 days. Constants: same hashtags (new music, wider genre, smaller genre, sound-alike artist), same description, default fonts, no fade-ins. Only variables: song section and format.
3. **Weekly culling.** Cut losing sections and formats, replace with new ideas, repeat. Once a flagship is clear, hold it constant and test formats against it.

## Inputs
1. **Instagram:** the Trial Reels Shared Tracker Google Sheet via the Google Drive connector (see `context/content-playbook.md`). Follow its README tab (drop rules, maturity flags, 0-view reels = distribution failures).
2. **TikTok:** TikTok Studio via the built-in browser on Ahan's computer (on, logged in). Views, comments, saves, shares, avg watch time, % watched full.
3. **Tags:** `logs/content-tags.md` (song section, format, hook, footage). Infer missing tags, mark `(inferred)`, ask Ahan to confirm.

## Rules
- Only enter data for posts at least **48 hours** old.
- Ignore likes.
- **Primary: views.**
- **Diagnostics (why views moved):** skip rate / % past first 3s, avg watch time as % of length, % watched full. Pull these directly; don't infer them from views.
- **Secondary: engagement rate** = (shares + comments + saves) / views x 100. Also report shares/1K on its own, since the sum hides it.
- **Flagship:** a reel clearing 3,264 views at 48h+. A section is the flagship when it clears that repeatedly across formats.
- n < 3 posts per variant is a hint, not a finding.
- If nothing clears ~200-300 views, it's the content, not the music. Say so.
- Flag any post that broke a constant (different hashtags, description, font) as unreadable.

## Output (short)
1. **Phase + flagship status:** current leader, confidence, what would confirm it.
2. **Section x format grid:** views, skip rate, completion, engagement rate per cell.
3. **Cull list:** sections and formats to cut, with replacements.
4. **Next week's plan:** the posts, in order, with constants listed.
5. **Trend check:** weekly median views vs prior weeks (from the tracker's Weeks tab).

## Logging
Append one row per post to `logs/experiments.md`. Never rewrite past rows.
