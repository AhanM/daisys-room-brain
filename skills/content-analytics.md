# Skill: weekly content analytics

Trigger: "run content analytics" or the Sunday scheduled task.

## Goal
Find which content attributes earn **shares/sends**, the signal that breaks reels out of the ~9K plateau. Feed the winners into next week's ideas. Views alone are not a win.

## Inputs
1. **Instagram:** latest Muse AI trial reels report (Ahan pastes it or drops it in `logs/raw/`).
2. **TikTok:** TikTok Studio, read through the built-in browser on Ahan's computer (must be on and logged in). Per video from the last 7 days: views, likes, comments, shares, saves, avg watch time, % watched full, traffic sources, new followers.
3. **Tags:** `logs/content-tags.md`. Infer missing tags from caption and on-screen hook text, mark them `(inferred)`, and ask Ahan to confirm.

## Tag scheme (one per variable)
- **hook:** on-screen hook text (short label, e.g. `psych-3sec`)
- **footage:** `photobooth`, `backcam`, `live`, `mv`, `visualizer`, `assets`, `talking`
- **song:** song + section, e.g. `addicted-intro`, `limerence-chorus`, or `none`
- **format:** `song`, `event-invite`, `story`, `lore`, `behind-scenes`
- **platform:** `ig-trial`, `ig-feed`, `tiktok`

## Metrics (in priority order)
1. **Shares per 1K views** (primary)
2. Saves per 1K views
3. Avg watch time / % watched full
4. Follows per 1K views
5. Views (context only)

## Analysis
- Compare by one variable at a time (hook, footage, song, format). Flag when a comparison mixes variables and can't be read.
- Treat n < 3 posts per variant as a hint, not a finding.
- Compare against the baseline: song reels ~80 sends at ~9K views; viral event reel ~3,300 sends at ~145K.
- Call out anything with shares per 1K well above baseline, even if views are low.

## Output (short)
1. **Top 3 and bottom 3** posts by shares per 1K, each with its tags.
2. **What worked / what didn't:** at most 3 bullets each, tied to a variable.
3. **Kill / keep / test:** one variant to drop, one to double down on, one new test with a single variable changed.
4. **3 content ideas for next week** built from the winners. Shareable formats get priority.

## Logging
Append one row per post to `logs/experiments.md`. Never rewrite past rows.
