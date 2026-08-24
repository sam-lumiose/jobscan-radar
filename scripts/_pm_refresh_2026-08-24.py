#!/usr/bin/env python3
"""Afternoon (14:00) in-place refresh of the 2026-08-24 digest.

Drops carried-forward items that no longer resolve to a live posting (re-checked
in Chrome this run) and appends the roles newly verified live this afternoon.
Throwaway helper for this run only.
"""
import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIGEST = ROOT / "data" / "digests" / "2026-08-24.json"
MANIFEST = ROOT / "data" / "manifest.json"
TODAY = "2026-08-24"

# Re-checked in Chrome this run and no longer live.
DEAD_SEEK_IDS = {"93628534", "93628402", "93628616", "94007340"}
DEAD_URLS = {
    "https://iworkfor.nsw.gov.au/job/manager-finance-operations-593066",
}

NEW_ITEMS = {
    "C-Suite & Executive": [
        {
            "severity": "act",
            "headline": "Chief Governance and Risk Officer — Commonwealth Director of Public Prosecutions, Sydney",
            "summary": "SES Band 1 executive owning governance, audit and risk, the PMO and parliamentary functions for the CDPP, reporting to the Chief Operating Officer. Advertised at $227k–$293k plus 15.4% super, with Sydney, Melbourne or Canberra as base options.",
            "so_what": "The single best fit on the board today: a whole-of-function governance and risk leadership role in Commonwealth public sector, squarely on your FCPA/FAICD profile. Apply this week — SES advertisements close quickly.",
            "tags": ["Permanent", "Sydney", "Government"],
            "source": "Seek / Office of the Director of Public Prosecutions",
            "url": "https://www.seek.com.au/job/94151901",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
    "Technology & Digital": [
        {
            "severity": "watch",
            "headline": "Chief Information Officer — Westfund Health Insurance, Sydney (Lithgow/Penrith options)",
            "summary": "Member-owned, not-for-profit health insurer seeking a CIO to lead technology, digital, data, cyber and automation, reporting directly to the Chief Executive.",
            "so_what": "Mutual/insurance sector is a strength and your software engineering background plus board exposure fits a member-owned insurer's CIO. It leans more deeply technical than your risk/finance core, so treat as a judgement call rather than an automatic apply.",
            "tags": ["Permanent", "Sydney", "Insurance"],
            "source": "Seek / Westfund Health Insurance",
            "url": "https://www.seek.com.au/job/94155344",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
    "Finance & Accounting": [
        {
            "severity": "act",
            "headline": "Head of Finance — B2B financial technology business via Profusion PAC, Sydney (hybrid)",
            "summary": "Leads the commercial and finance function of a private fintech selling advice technology to large financial institutions, with an established international footprint. Hybrid, three days a week in the office.",
            "so_what": "Head-of-function finance leadership in financial services, one of your listed sectors. Recruiter-held and freshly listed today, so contact Profusion early rather than waiting on the queue.",
            "tags": ["Permanent", "Sydney", "FS"],
            "source": "Seek / Profusion PAC",
            "url": "https://www.seek.com.au/job/94156746",
            "published": "2026-08-24",
            "paywall": False,
        },
        {
            "severity": "act",
            "headline": "Divisional Finance Director — PE-backed consumer products group via The Acquire Group, Sydney (hybrid)",
            "summary": "Commercial finance executive for a roughly $300m business unit inside a private-equity-backed consumer products and distribution group, reporting to the Group CFO and partnering closely with the divisional MD.",
            "so_what": "Director-level finance leadership with genuine P&L breadth and a clear CFO-track line. Sector is outside your core but the level and the CFO reporting line make it worth moving on quickly.",
            "tags": ["Permanent", "Sydney", "Consumer"],
            "source": "Seek / The Acquire Group",
            "url": "https://www.seek.com.au/job/94158465",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
    "Risk, Compliance & Assurance": [
        {
            "severity": "act",
            "headline": "Head of Risk — Coal Services Pty Ltd, Sydney CBD",
            "summary": "Newly created head-of-function role to establish, embed and oversee an enterprise risk management policy and framework for the specialist health, safety and workers-compensation body serving the NSW coal industry.",
            "so_what": "A build-it-from-scratch ERM mandate in a mutual-style insurer with an energy-sector client base — close to the centre of your energy/utilities and insurance/mutual experience. Strong, direct match worth applying to now.",
            "tags": ["Permanent", "Sydney", "Energy"],
            "source": "Seek / Coal Services",
            "url": "https://www.seek.com.au/job/94102449",
            "published": "2026-08-19",
            "paywall": False,
        },
        {
            "severity": "act",
            "headline": "Head of Compliance — Coal Services Pty Ltd, Sydney CBD",
            "summary": "Companion head-of-function role to the Head of Risk, establishing and overseeing the organisation's compliance framework against applicable law, regulation, standards and internal policy.",
            "so_what": "Same organisation and sector fit as the Head of Risk role, on the compliance side. Applying to whichever of the pair better matches your emphasis gives you two shots at the same employer.",
            "tags": ["Permanent", "Sydney", "Energy"],
            "source": "Seek / Coal Services",
            "url": "https://www.seek.com.au/job/94102445",
            "published": "2026-08-19",
            "paywall": False,
        },
        {
            "severity": "watch",
            "headline": "Board & Committee Services Manager — Hort Innovation, North Sydney (hybrid)",
            "summary": "Runs board and committee secretariat services for the grower-owned research and development corporation that invests across Australia's horticulture industry.",
            "so_what": "Board secretariat work sits close to your company-secretary and FAICD interests and would deepen your governance credentials. Plain Manager level, so it is below your current tier — worth a look rather than a priority application.",
            "tags": ["Permanent", "Sydney", "Agribusiness"],
            "source": "Seek / Hort Innovation",
            "url": "https://www.seek.com.au/job/94157708",
            "published": "2026-08-24",
            "paywall": False,
        },
        {
            "severity": "inform",
            "headline": "Enterprise Compliance Lead, Privacy — icare, Barangaroo (hybrid)",
            "summary": "Permanent role supporting the Enterprise Compliance Manager to implement icare's compliance management policy, with a privacy risk specialism. Advertised from $154,231 plus super.",
            "so_what": "icare is a strong sector fit for your insurance and NSW government background, but the role reports into a manager and sits below your level. Useful as a read on where icare is investing rather than a target.",
            "tags": ["Permanent", "Sydney", "Insurance"],
            "source": "Seek / icare",
            "url": "https://www.seek.com.au/job/94153593",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
    "Operations, Strategy & Transformation": [
        {
            "severity": "watch",
            "headline": "Head of Business Operations, Youth Insearch — via Impact Advising, remote across NSW/QLD/VIC",
            "summary": "Newly created, hands-on role driving business operations, projects and continuous improvement for a peer-led youth trauma recovery charity, partnering with the COO and outsourced finance, people and IT providers.",
            "so_what": "Fully remote head-of-function role with real breadth across finance, systems and process — a good NFP entry point. The organisation is small, so weigh scope against the seniority you already hold.",
            "tags": ["Permanent", "Remote-AU", "NFP"],
            "source": "Seek / Impact Advising",
            "url": "https://www.seek.com.au/job/94151922",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
    "Interim, Contract & Advisory": [
        {
            "severity": "watch",
            "headline": "Finance Manager, short-term contract — financial services client via Mars Recruitment, North Sydney",
            "summary": "Hands-on short-term contract finance role with an established financial services organisation, immediate start, office-based in North Sydney.",
            "so_what": "The only genuinely new day-rate finance listing this afternoon and it starts immediately, so recruiter contact today matters. Plain Manager level caps it below your tier, but it is a fast way back into a contracting cadence.",
            "tags": ["Contract", "Sydney", "FS"],
            "source": "Seek / Mars Recruitment",
            "url": "https://www.seek.com.au/job/94159020",
            "published": "2026-08-24",
            "paywall": False,
        },
    ],
}


def is_dead(item):
    if item["url"] in DEAD_URLS:
        return True
    m = re.search(r"seek\.com\.au/job/(\d+)", item["url"])
    return bool(m and m.group(1) in DEAD_SEEK_IDS)


def main():
    digest = json.loads(DIGEST.read_text())

    dropped = 0
    for section in digest["sections"]:
        kept = [i for i in section["items"] if not is_dead(i)]
        dropped += len(section["items"]) - len(kept)
        section["items"] = kept

    existing = {s["category"]: s for s in digest["sections"]}
    added = 0
    for category, items in NEW_ITEMS.items():
        section = existing.get(category)
        if section is None:
            section = {"category": category, "items": []}
            digest["sections"].append(section)
            existing[category] = section
        have = {i["url"] for i in section["items"]}
        for item in items:
            if item["url"] not in have:
                section["items"].append(item)
                added += 1

    counts = {"act": 0, "watch": 0, "inform": 0}
    total = 0
    for section in digest["sections"]:
        for item in section["items"]:
            counts[item["severity"]] = counts.get(item["severity"], 0) + 1
            total += 1

    digest["counts"] = counts
    digest["generated_at"] = datetime.now().astimezone().replace(microsecond=0).isoformat()
    digest["posture"] = (
        f"{total} roles · {counts['act']} strong-act · 1 new interim/contract listing — "
        "Monday afternoon refresh. Every carried-forward role was re-checked in Chrome this run "
        f"({dropped} dropped as expired); {added} new roles added. "
        "Best find: Chief Governance and Risk Officer at the Commonwealth DPP."
    )
    digest["summary"] = (
        "The afternoon refresh is a governance-heavy one. The standout is the Commonwealth DPP's "
        "Chief Governance and Risk Officer role (SES Band 1, $227k–$293k), which bundles governance, "
        "audit, risk and the PMO into a single executive mandate and is the closest thing to a purpose-built "
        "match on the board. Behind it, Coal Services has advertised a matched pair of newly created Head of "
        "Risk and Head of Compliance roles in Sydney — an energy-sector, mutual-style insurer, so two shots "
        "at one employer that sits right on your sector strengths — alongside two fresh finance leadership "
        "roles (Head of Finance via Profusion PAC and a PE-backed Divisional Finance Director via The Acquire "
        "Group). Interim supply stayed thin: only one genuinely new day-rate listing appeared (a short-term "
        "Finance Manager contract via Mars Recruitment, immediate start), which reinforces the standing point "
        "that the specialist risk and finance desks — Bluefin, Kaizen, JS Careers, KPP, Robert Half, Sharp & "
        "Carter — fill interim briefs off their own registers, so being registered and CV-current with them "
        "matters more than watching the boards. Coverage caveats: Seek, I Work for NSW, EthicalJobs, Board "
        "Direction, Sharp & Carter, Robert Half, Bluefin, Kaizen, Watermark and AICD Directorship Opportunities "
        "were all opened in Chrome this run, and every logged role was confirmed live in-browser. Watermark "
        "currently publishes no public vacancies; AICD Directorship Opportunities has moved fully behind a login "
        "with no public teasers, so nothing from it could be logged; Board Direction's listing page renders "
        "publicly but each vacancy detail page is member-gated; and I Work for NSW returned intermittent 502/504 "
        "errors mid-run before recovering. This remains a sample, so a manual look is still worthwhile."
    )

    DIGEST.write_text(json.dumps(digest, indent=2, ensure_ascii=False) + "\n")

    manifest = json.loads(MANIFEST.read_text())
    entry = {
        "date": TODAY,
        "file": f"data/digests/{TODAY}.json",
        "posture": digest["posture"],
        "counts": counts,
    }
    digests = manifest.get("digests", [])
    if digests and digests[0].get("date") == TODAY:
        digests[0] = entry
    else:
        digests.insert(0, entry)
    manifest["digests"] = digests
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    print(f"total={total} dropped={dropped} added={added} counts={counts}")


if __name__ == "__main__":
    main()
