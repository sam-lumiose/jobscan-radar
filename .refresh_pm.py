import json, os, collections

BASE = os.path.dirname(os.path.abspath(__file__))
DIGEST = os.path.join(BASE, "data", "digests", "2026-08-19.json")
MANIFEST = os.path.join(BASE, "data", "manifest.json")
GEN = "2026-08-19T13:28:45+10:00"

d = json.load(open(DIGEST))

# --- 1. Drop items no longer live (re-checked in Chrome this run) ---
DROP = {"https://www.seek.com.au/job/93900082"}
dropped = []
for s in d["sections"]:
    keep = []
    for it in s["items"]:
        if it["url"] in DROP:
            dropped.append(it["headline"])
        else:
            keep.append(it)
    s["items"] = keep

# --- 2. New items found this afternoon (all opened + verified live in Chrome) ---
NEW = {
 "Risk, Compliance & Assurance": [
  {
   "severity": "act",
   "headline": "Head of Enterprise Risk — Resimac, Sydney (hybrid)",
   "summary": "ASX-listed non-bank lender is hiring a Head of Enterprise Risk to build out and mature its enterprise risk framework across the Australian and New Zealand lending business.",
   "so_what": "A 'Head of' enterprise risk role at a listed financial services group is squarely at your level and function. Listed within the hour this afternoon — get in early.",
   "tags": ["Permanent", "Sydney", "FS"],
   "source": "Seek / Resimac",
   "url": "https://www.seek.com.au/job/94068269",
   "published": "2026-08-19",
   "paywall": False
  },
  {
   "severity": "act",
   "headline": "Group Manager, Business Improvement & Assurance — City of Parramatta, Sydney (hybrid)",
   "summary": "Local government group-manager post leading business improvement and assurance, offered as a full-time term contract running through to August 2029 at roughly $228k–$253k plus 12% super.",
   "so_what": "Local government plus an assurance mandate is about as close to your background as this market gets, and the group-manager grade with a long fixed term is a strong fit. Applications close 2 September — worth starting today.",
   "tags": ["Fixed-term", "Sydney", "Local Government"],
   "source": "Seek / City of Parramatta",
   "url": "https://www.seek.com.au/job/94066969",
   "published": "2026-08-19",
   "paywall": False
  },
  {
   "severity": "inform",
   "headline": "Assistant Manager, Audit, Risk & Integrity (integrity lead) — Commonwealth DPP, Sydney",
   "summary": "Federal prosecution agency is recruiting an EL1 assistant manager to lead its integrity work within the audit and risk team, with the role open in Sydney, Melbourne or Canberra.",
   "so_what": "The function is right but the EL1 grade sits below your level. Useful as a read on where Commonwealth agencies are investing in integrity and assurance capability.",
   "tags": ["Permanent", "Sydney", "Government"],
   "source": "Seek / Office of the Director of Public Prosecutions",
   "url": "https://www.seek.com.au/job/94059166",
   "published": "2026-08-19",
   "paywall": False
  },
  {
   "severity": "inform",
   "headline": "Assistant Manager, Governance & Secretariat — Commonwealth DPP, Sydney",
   "summary": "EL1 governance and secretariat role supporting committee decision-making and corporate governance processes across the agency, also open in Melbourne and Canberra.",
   "so_what": "Board-secretariat work that maps to your company-secretary interests, but pitched a grade or two below where you would come in.",
   "tags": ["Permanent", "Sydney", "Government"],
   "source": "Seek / Office of the Director of Public Prosecutions",
   "url": "https://www.seek.com.au/job/94059164",
   "published": "2026-08-19",
   "paywall": False
  },
  {
   "severity": "inform",
   "headline": "Senior Internal Auditor — international insurer via Profusion PAC, Sydney (hybrid, $170k–$180k)",
   "summary": "Established international insurance group is adding a senior internal auditor to a function focused on independent assurance across a heavily regulated environment.",
   "so_what": "Insurance and internal audit are both core to your background, but the role sits below manager level. Worth a call to the recruiter if you want a route into that audit function at a higher grade.",
   "tags": ["Permanent", "Sydney", "Insurance"],
   "source": "Seek / Profusion PAC",
   "url": "https://www.seek.com.au/job/94007340",
   "published": "2026-08-17",
   "paywall": False
  },
  {
   "severity": "inform",
   "headline": "Head of WHSEQ — JCDecaux, Sydney (hybrid)",
   "summary": "Out-of-home media group is hiring a head of work health, safety, environment and quality to lead its assurance and compliance agenda across Australian operations.",
   "so_what": "The 'Head of' grade and the quality/assurance half of the brief are in range, but the centre of gravity is WHS rather than enterprise risk or finance. Situational awareness only.",
   "tags": ["Permanent", "Sydney", "Media"],
   "source": "Seek / JCDecaux",
   "url": "https://www.seek.com.au/job/94060671",
   "published": "2026-08-19",
   "paywall": False
  }
 ],
 "Finance & Accounting": [
  {
   "severity": "watch",
   "headline": "Business Services Manager / Senior Manager — mid-tier chartered firm via Lawson Elliott, Sydney CBD (hybrid, $150k–$180k package)",
   "summary": "Mid-tier accounting practice is hiring at manager or senior-manager level into business services and corporate advisory, with an ongoing client fee base attached.",
   "so_what": "Your CPA credentials and finance depth fit, and the senior-manager band is at your level — the judgement call is whether a practice-side advisory role is the direction you want.",
   "tags": ["Permanent", "Sydney", "Professional Services"],
   "source": "Seek / Lawson Elliott Recruitment",
   "url": "https://www.seek.com.au/job/94060287",
   "published": "2026-08-19",
   "paywall": False
  }
 ],
 "Operations, Strategy & Transformation": [
  {
   "severity": "watch",
   "headline": "Senior Project Manager, Business Special Projects — City of Parramatta, Sydney (hybrid, $160k–$177k)",
   "summary": "Council is recruiting a senior project manager for a business special-projects portfolio on a full-time term contract, sitting alongside its business improvement and assurance group.",
   "so_what": "Local government affinity and a transformation brief make this a reasonable fit, though it is a delivery role rather than a governance one. Consider it alongside the Parramatta group-manager post above.",
   "tags": ["Fixed-term", "Sydney", "Local Government"],
   "source": "Seek / City of Parramatta",
   "url": "https://www.seek.com.au/job/94066978",
   "published": "2026-08-19",
   "paywall": False
  }
 ],
 "Technology & Digital": [
  {
   "severity": "watch",
   "headline": "Senior Manager, Data & Analytics — market-leading lender via Reo Group, Sydney (hybrid, $165k–$185k plus super and bonus)",
   "summary": "Financial services lender is hiring a senior manager to lead an established data and analytics team and drive commercially oriented decision-making.",
   "so_what": "Senior-manager grade in financial services with a technology-leadership brief plays to your software engineering background, though it is more analytics-led than risk-led.",
   "tags": ["Permanent", "Sydney", "FS"],
   "source": "Seek / Reo Group",
   "url": "https://www.seek.com.au/job/94066775",
   "published": "2026-08-19",
   "paywall": False
  }
 ],
 "Interim, Contract & Advisory": [
  {
   "severity": "watch",
   "headline": "Manager, Application Services (Finance) — major Sydney university via Bluefin Resources (3-month contract, $900–$1,000 per day plus super)",
   "summary": "Urgent three-month parental-leave cover leading a seven-person team that supports the university's finance applications and platforms, including its TechnologyOne financials stack.",
   "so_what": "A day-rate brief sitting exactly at the intersection of your finance and software engineering backgrounds, and Bluefin move fast on these. Capped at watch only because it is a plain manager grade — call them today if the rate suits.",
   "tags": ["Interim", "Sydney", "Education"],
   "source": "Bluefin Resources",
   "url": "https://www.bluefinresources.com.au/jobview/manager-apps-services-finance-3-month-contract-start-asap/0cfce56a-6102-4d1f-8cfa-e2fd90b48d93/",
   "published": "2026-08",
   "paywall": False
  }
 ]
}

by_cat = {s["category"]: s for s in d["sections"]}
ORDER = ["Board & NED", "C-Suite & Executive", "Risk, Compliance & Assurance",
         "Finance & Accounting", "Operations, Strategy & Transformation",
         "Technology & Digital", "Interim, Contract & Advisory"]

for cat, items in NEW.items():
    if cat not in by_cat:
        sec = {"category": cat, "items": []}
        by_cat[cat] = sec
        d["sections"].append(sec)
    existing = {i["url"] for i in by_cat[cat]["items"]}
    for it in items:
        if it["url"] not in existing:
            by_cat[cat]["items"].append(it)

# order sections, and within each section order act > watch > inform
rank = {"act": 0, "watch": 1, "inform": 2}
d["sections"].sort(key=lambda s: ORDER.index(s["category"]) if s["category"] in ORDER else 99)
for s in d["sections"]:
    s["items"].sort(key=lambda i: rank.get(i["severity"], 9))

# --- 3. Recount ---
c = collections.Counter()
for s in d["sections"]:
    for it in s["items"]:
        c[it["severity"]] += 1
counts = {"act": c["act"], "watch": c["watch"], "inform": c["inform"]}
total = sum(counts.values())

d["generated_at"] = GEN
d["counts"] = counts
d["posture"] = (
    f"{total} roles · {counts['act']} strong-act · 2 day-rate/interim briefs worth moving on today "
    f"— afternoon refresh, every item re-opened in Chrome; 89 of 90 morning items re-confirmed live, "
    f"1 dropped, 10 new roles added"
)
d["summary"] = (
    "The afternoon sweep added ten roles, and the two worth acting on both landed today: a Head of Enterprise Risk "
    "at Resimac, listed within the hour, and a Group Manager, Business Improvement & Assurance at City of Parramatta "
    "on a term contract to 2029 at $228k–$253k plus super — local government and an assurance mandate together, "
    "which is the closest match this radar has surfaced in weeks. One morning item dropped out: the Ethos BeathChapman "
    "day-rate Director, Risk, Compliance & Safety brief expired during the day, which is the usual pattern for "
    "recruiter-held contract work and the reason speed matters on the interim surface. The only fresh day-rate brief is "
    "Bluefin's three-month finance applications manager role at $900–$1,000 a day; if interim work is the priority, "
    "being registered and CV-current with Bluefin, Kaizen, JS Careers, KPP, Robert Half and Sharp & Carter still matters "
    "more than watching the boards. Browser-verified this run: Seek (query battery plus Board Appointments), EthicalJobs, "
    "Robert Half, Kaizen, Bluefin, and every carried-forward I Work for NSW listing individually. I Work for NSW's search "
    "index could not be swept this afternoon — the site returned gateway timeouts and its keyword filter stopped "
    "returning results — so new NSW government postings since this morning may be missing and a manual look there is "
    "worthwhile. AICD Directorship Opportunities remains member-gated and was not scanned beyond public teasers."
)

json.dump(d, open(DIGEST, "w"), indent=2, ensure_ascii=False)

# --- 4. Manifest ---
m = json.load(open(MANIFEST))
entry = {"date": "2026-08-19", "file": "data/digests/2026-08-19.json",
         "posture": d["posture"], "counts": counts}
digests = m["digests"]
if digests and digests[0]["date"] == "2026-08-19":
    digests[0] = entry
else:
    digests.insert(0, entry)
json.dump(m, open(MANIFEST, "w"), indent=2, ensure_ascii=False)

print("dropped:", dropped)
print("counts:", counts, "total:", total)
for s in d["sections"]:
    print(f"  {s['category']}: {len(s['items'])}")
