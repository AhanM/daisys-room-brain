"""Summarize the Trial Reels Shared Tracker export.

Usage: python3 -I scripts/ig_summary.py path/to/tracker.xlsx
Prints scoreboard, section/format medians, and rotation cell stats for judged reels.
"""
import sys
import pandas as pd

THRESHOLD = 3264
DROP_WORDS = ("halloween", "21+", "party")


FORMAT_RULES = [  # first match wins; keep in sync with Rotation tab
    ("photo booth", "Photo booth"), ("live", "Live"), ("music vid", "Music video"),
    ("subway", "Subway selfie"), ("transit", "Music video"), ("night walk", "Night walk"),
    ("floor", "Floor / bed recreate"), ("acoustic", "Acoustic to camera"),
    ("rooftop", "Rooftop selfie"), ("balcony", "Rooftop selfie"),
    ("guitar", "Bedroom guitar"), ("band room", "Bedroom guitar"), ("selfie", "Bedroom selfie"),
]


def norm_format(f):
    f = str(f).lower()
    for key, name in FORMAT_RULES:
        if key in f:
            return name
    return "Other"


def load(path):
    sheets = pd.read_excel(path, sheet_name=None)
    df = sheets["All reels"].copy()
    df["posted"] = pd.to_datetime(df["posted"])
    for c in ["views", "likes", "comments", "saves", "shares"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    text = df.fillna("").astype(str).apply(lambda r: " ".join(r), axis=1).str.lower()
    df["kind"] = text.apply(lambda t: "other" if any(w in t for w in DROP_WORDS) else "music")
    df["judged"] = df["maturity_flag"].astype(str).str.startswith("48h+")
    df["counted"] = df["judged"] & (df["views"] > 0)
    df["eng"] = (df.comments + df.saves + df.shares) / df.views.where(df.views > 0)
    df["format"] = df["content_format"].apply(norm_format)
    df["text"] = df["on_screen_text"].apply(norm_text)
    df["song"] = df["song_section"].apply(song_of)
    df["week"] = df["posted"].dt.to_period("W-SUN").dt.start_time.dt.date
    return df, sheets


TEXT_RULES = [  # short codes for on-screen text hooks; specific keys first
    ("marketable", "CITY"), ("what city", "CITY"), ("where you're watching", "NYC"),
    ("i hate ai", "HATEAI"), ("human to human", "HUMAN"), ("hypothetically", "HYPO"), ("great taste", "TASTE"), ("concert ticket", "TICKET"),
    ("copy the link", "COPYLINK"), ("copy link", "COPYLINK"), ("target audience", "TARGET"),
    ("finding my listeners", "FINDING"), ("finding our listeners", "FINDING"),
    ("strokes", "STROKES"), ("doomscrolled", "DOOMSCROLL"), ("backstage", "BACKSTAGE"),
]


def norm_text(t):
    t = str(t).lower()
    if t in ("nan", "", "none noted") or t.startswith("no distinct"):
        return "none"
    for key, code in TEXT_RULES:
        if key in t:
            return code
    return "lyrics/other"


def song_of(sec):
    sec = str(sec).lower()
    for name in ["addicted", "limerence", "no:reunion", "c&k", "validation"]:
        if name in sec:
            return name
    return "other"


def week_in_review(df):
    wk = df["week"].max()
    w = df[df.week == wk]
    days = pd.date_range(wk, periods=7)
    out = pd.DataFrame({"day": [d.strftime("%a %b %d") for d in days]})
    counts = w[w.kind == "music"].groupby(w.posted.dt.date).size()
    out["ig_reels"] = [int(counts.get(d.date(), 0)) for d in days]
    print(f"WEEK IN REVIEW ({wk}), Instagram music trial reels:")
    print(out.to_string(index=False))
    print(f"Total: {out.ig_reels.sum()}, days with 0 posts: {(out.ig_reels == 0).sum()}")


def main(path):
    df, sheets = load(path)
    week_in_review(df)
    df = df[df.kind == "music"]
    c = df[df.counted]
    print()
    print(f"POSTS: {len(df)} total, {int(df.judged.sum())} judged 48h+, {len(c)} counted (>0 views)")
    print(f"UNDER 48h (not judged): {int((~df.judged).sum())}")

    print("\nWEEKLY (counted):")
    w = c.groupby("week").agg(n=("views", "size"), median=("views", "median"),
                              max=("views", "max"),
                              flagships=("views", lambda v: int((v >= THRESHOLD).sum())))
    print(w.tail(5).to_string())

    def table(col):
        t = c.groupby(col).agg(n=("views", "size"), median=("views", "median"),
                               max=("views", "max"), eng=("eng", "median"),
                               shares=("shares", "sum"), views=("views", "sum"))
        t["shares_1k"] = (t.shares / t.views * 1000).round(1)
        t["eng"] = (t.eng * 100).round(2)
        return t.drop(columns=["shares", "views"]).sort_values("median", ascending=False)

    def table(col):
        t = c.groupby(col).agg(n=("views", "size"), median=("views", "median"),
                               max=("views", "max"), eng=("eng", "median"),
                               shares=("shares", "sum"), views=("views", "sum"))
        t["shares_1k"] = (t.shares / t.views * 1000).round(1)
        t["eng"] = (t.eng * 100).round(2)
        return t.drop(columns=["shares", "views"]).sort_values("median", ascending=False)

    lw = c[c.week == c.week.max()]
    print(f"\nLAST WEEK ONLY ({c.week.max()}), judged reels:")
    for col in ["format", "song_section", "song", "text"]:
        t = lw.groupby(col)["views"].agg(n="size", median="median", max="max").sort_values("median", ascending=False)
        print(f"\n  by {col}:")
        print(t.to_string())

    print("\nALL TIME BY ON-SCREEN TEXT:")
    print(table("text").to_string())

    print("\nBY SECTION (all time):")
    print(table("song_section").to_string())
    print("\nBY FORMAT:")
    print(table("format").to_string())
    print("\nFOOTAGE ON HAND (section x format combos already posted = reusable):")
    have = sorted(set(zip(c.song_section, c.format)))
    for sec, fmt in have:
        print(f" - {sec} | {fmt}")
    print("\nSECTION x FORMAT (median views, n):")
    grid = c.groupby(["song_section", "format"])["views"].agg(["median", "size"])
    grid = grid.apply(lambda r: f"{int(r['median'])} ({int(r['size'])})", axis=1).unstack(fill_value="")
    print(grid.to_string())

    last = c[c.week == c.week.max()]
    print(f"\nLATEST WEEK ({c.week.max()}) REELS:")
    print(last[["posted", "song_section", "format", "views", "eng"]]
          .sort_values("views", ascending=False).to_string(index=False))

    print("\nROTATION TAB:")
    rot = sheets["Rotation"]
    print(rot.iloc[:6].to_string(index=False))
    print("Notes:")
    for n in rot.iloc[7:, 0].dropna():
        print(" -", n)


if __name__ == "__main__":
    main(sys.argv[1])
