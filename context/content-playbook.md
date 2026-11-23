# Content playbook

How we structure content and what we optimize. Findings and flagship status live in the **Trial Reels Shared Tracker** (Google Sheet `1f_UKsG_DMIRhr9PZt_qHxjwHodMik82YEEqDESqTB8A`, written by Muse). Read its All reels, Rotation and README tabs first. Don't edit Muse's tabs; Claude's notes go in a 'Claude notes' tab (needs edit access) or in this repo.
- Flagship threshold: **3,264 views** (from the tracker).
- Instagram data comes from the tracker. TikTok data comes from TikTok Studio and is logged in `logs/experiments.md`.

## Structure: Flagship Evolution System
1. **Collect evidence:** score candidate song sections, pick the top 5.
2. **Structured testing:** 4 sections x 5 formats (format = visual + on-screen text) = 20 posts over ~7 days. No repeats.
3. **Weekly culling:** cut losing sections and formats, replace, repeat.
4. **Once the flagship is confirmed:** post it ~80% of the time and test new formats against it.

**Constants during tests:** on-screen hook text, hashtags, description, default fonts, no fade-ins.
**Variables:** song section and format only. One at a time.
**Data:** enter only after a post is 48+ hours old.

## Metrics
1. **Primary: views.** The ranker allocates distribution on predicted time spent (avg watch time, completion %, comment surface time), so views is the best single summary of those signals.
2. **Diagnostics (when available):** avg watch time %, completion %, skip rate. Faster read than views on small samples.
3. **Secondary: engagement rate** = (shares + comments + saves) / views x 100. Doesn't capture time spent, so it never outranks views.
4. **Check: shares per 1K.** Song reels run ~2-4 per 1K. Flag anything well above that.

## Cadence
- Weekly analytics run on Sunday (`skills/weekly-content-review.md`).
- Batch approval once a week; the scheduler posts daily.
