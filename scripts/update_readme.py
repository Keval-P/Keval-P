#!/usr/bin/env python3
"""Refresh the generated parts of README.md: Stack Exchange figures and the "updated on" date.

Only text between the <!--NAME:START--> and <!--NAME:END--> markers is replaced.
If the Stack Exchange API cannot be reached, the old figures are kept.
"""
import datetime, gzip, json, re, sys, urllib.request

README = "README.md"
SE_USER = 78733
SE_API = f"https://api.stackexchange.com/2.3/users/{SE_USER}"


def fetch(url):
    req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip", "User-Agent": "profile-readme"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    return json.loads(gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data)


def replace(text, name, value):
    pattern = re.compile(f"(<!--{name}:START-->).*?(<!--{name}:END-->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker {name} not found in {README}")
    return pattern.sub(lambda m: m.group(1) + value + m.group(2), text)


text = open(README, encoding="utf-8").read()
before = text
try:
    reputation = fetch(SE_API + "?site=ai")["items"][0]["reputation"]
    answers = fetch(SE_API + "/answers?site=ai&filter=total")["total"]
    text = replace(text, "SE", f"{answers} answers, {reputation} reputation")
except Exception as e:                      # keep the old figures rather than fail the run
    print(f"Stack Exchange lookup skipped: {e}")

if "--touch" in sys.argv or text != before:
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y")
    text = replace(text, "UPDATED", f"Updated on {today}")
open(README, "w", encoding="utf-8").write(text)
print("README changed" if text != before else "README unchanged")
