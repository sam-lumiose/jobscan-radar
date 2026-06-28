# Risk, Finance & Board Radar — Cowork daily-job spec

A **twice-daily** Cowork job (08:00 and 14:00 Australia/Sydney) that scans job boards,
public-sector sites, board-vacancy services, and senior recruiters for roles matching a
senior risk / finance / governance professional, and writes a styled digest that a
separate helper publishes to GitHub Pages. The agent writes structured JSON, never HTML;
a native macOS helper does the git push.

> Current context (2026): the senior contract/interim market in Sydney moves fast —
> specialist finance and risk recruiters often fill day-rate and interim roles from the
> first handful of strong applicants and never advertise them on the big boards. Treat
> recruiter listings as the time-critical surface. Board/NED supply is steady; the AICD
> Directorship Opportunities platform adds roughly 15 new positions a week but is
> member-gated, so only its public teasers are visible here.

---

## 0. Candidate profile — the filter target

- **Credentials:** FCPA, FAICD. Degrees in Software Engineering, Accounting, Business
  Administration, Environmental Law.
- **Level:** senior-manager to one tier above; limited direct people-management. Existing
  board experience: Ku-ring-gai Council; Non-Executive Director, StateCover Mutual.
- **Sectors of strength:** energy/utilities, local government, insurance/mutual — open to
  others (financial services, superannuation, government, NFP).
- **Wants:** permanent, fixed-term, temporary **and** short-term / interim contracting;
  employment **or** directorships.
- **Target titles:** Non-Executive Director, Chair, board/committee/advisory member; CRO,
  COO, CFO, CEO, GM; group manager, senior manager, "Head of" in risk, compliance,
  assurance, finance, operations, business, IT.
- **Location rule:** Sydney metro + hybrid + Australia-remote. **Board/NED only:**
  interstate acceptable (willing to travel for monthly board/committee meetings) — tag
  `Interstate`.

---

## 1. Source register

> On the **first run**, verify each URL resolves and note any that have moved or gone
> login-only; thereafter scan the working set. Never log in, never bypass a paywall or
> ToS gate, never scrape behind authentication. Where a source is gated, use only the
> public listing/teaser.

### 1a. Senior recruiters — PRIMARY (speed-critical, esp. interim/contract)
These are the firms most likely to hold short-term/interim and unadvertised contract
roles. Scan each firm's public "browse jobs / live roles" page **and** web-search
`<firm> Sydney contract OR interim <function> <this week>`. Flag interim/contract finds
as `act` by default (see §5).

| # | Firm | Why it's on the list | URL (verify) |
|---|---|---|---|
| 1 | Robert Half | Finance & accounting contract/interim + exec search; large temp desk | roberthalf.com/au/en |
| 2 | Robert Walters | Banking & FS interim/contract; payroll-backed temp | robertwalters.com.au |
| 3 | Michael Page | Finance, public sector, perm + temp | michaelpage.com.au |
| 4 | Page Executive | Exec/leadership end of PageGroup | pageexecutive.com |
| 5 | Hays | Accountancy & finance contract; deep volume | hays.com.au |
| 6 | Hudson | Exec, board & **interim/fractional** leaders | au.hudson.com |
| 7 | Morgan McKinley | Risk & compliance, finance, FS | morganmckinley.com/au |
| 8 | Sharp & Carter | Finance & accounting, Sydney, strong contract desk | sharpandcarter.com.au |
| 9 | Bluefin Resources | Risk & compliance specialist; fast contract turnaround | bluefinresources.com.au |
| 10 | Kaizen Recruitment | Risk & compliance, FS/super/funds | kaizenrecruitment.com.au |
| 11 | JS Careers | Compliance, risk, audit, legal | jscareers.com.au |
| 12 | KPP Search | Audit, risk, compliance (Sydney + global) | kppsearch.com |
| 13 | Lanson Partners | Finance/treasury + risk/compliance/legal | lansonpartners.com |
| 14 | TOM Recruitment / Executive | Audit, risk, compliance, finance, exec search | tomexecutive.com |
| 15 | Morgan Consulting | Accounting & exec search | morganconsulting.com.au |
| 16 | Derwent | Board, CEO, leadership + **Interim Solutions** | derwentsearch.com.au |
| 17 | Watermark Search Intl | Board & executive search | watermarksearch.com.au |
| 18 | NGS Global | Board & C-suite search | ngs-global.com |
| 19 | Blenheim Partners | Board & senior executive search | blenheimpartners.com |
| 20 | Stanton Chase / Boyden | Board, C-suite, FS; Boyden also interim management | stantonchase.com · boyden.com/australia |

> Standing note for the daily market-read (not a per-item action): several of these firms
> rarely advertise interim roles publicly. The reader gets the most value by being
> **registered and CV-current** with the risk/finance specialists (Bluefin, Kaizen, JS
> Careers, KPP, Robert Half, Sharp & Carter). Surface this reminder only when an interim
> role appears, or when a scan returns no public interim listings.

### 1b. General job boards — FREE, broad net
Seek (au.seek.com) · LinkedIn Jobs public pages (au.linkedin.com/jobs) · Indeed
(au.indeed.com) · Jora (au.jora.com) · Adzuna (adzuna.com.au) · CareerOne (careerone.com.au).
Use public search-result pages and web search only; do not log in.

### 1c. Government & public sector — FREE
I Work for NSW (iworkfor.nsw.gov.au) — primary for NSW gov + many councils ·
APS Jobs (apsjobs.gov.au) — federal · relevant council career pages (local-government
sector affinity) · state-owned energy/utility career pages where applicable.

### 1d. Board / NED / advisory — listing services
Board Direction (boarddirection.com.au) — NED vacancies & directory · Nurole (nurole.com)
— board roles, partly gated · EthicalJobs (ethicaljobs.com.au) — NFP board & exec ·
Institute of Community Directors (communitydirectors.com.au) — NFP board matching ·
Hutton Education (hutton.education) — education-sector leadership search; **include its
school Board Director appointments AND any school CFO / COO / Business Manager / Director
of Business / Director of Finance & Operations roles** (independent schools list these
through Hutton periodically). Its principal / deputy-principal / academic / teaching roles
are off-target — filter them out per §3 ·
Seek "Board Appointments" subclassification.

### 1e. Gated / paid — headline + teaser ONLY, flagged
AICD **Directorship Opportunities** (do.aicd.com.au) — member subscription (~$85–88/yr);
visible teasers only, set `"paywall": true`, recommend manual login if a teaser looks
strong · any LinkedIn/recruiter listing that is login-gated — public teaser only.

### 1f. Scan routine — coverage discipline (MANDATORY)

Most boards below are **JavaScript-rendered**: a plain web fetch or web search sees almost
none of the live listings, so they MUST be read in **Chrome** (the rendered job cards), not
via search alone. Use search only for *discovery* of URLs; do verification and capture in the
browser. Confirm a browser is connected (`list_connected_browsers`); if none, note the
search-only fallback in the digest `summary` and treat results as leads, not verified roles.

**For every source: render the listing page, scrape the job cards, dedupe by job ID (or
org + title + location).** Do not stop at the top few results.

- **Seek** — run the **fixed query battery** below, each sorted most-recent first
  (append `?sortmode=ListedDate`), and read **all of page 1 (~22 cards) and keep going while
  listings are ≤14 days old**, then dedupe. Queries (Sydney NSW unless noted):
  `chief risk officer` · `chief financial officer` · `chief operating officer` ·
  `head of risk` · `head of compliance` · `head of audit` · `head of finance` ·
  `head of governance` · `governance` · `risk manager` · `senior risk manager` ·
  `senior manager risk` · `senior manager governance` · `compliance manager` ·
  `internal audit` · `company secretary` · `financial controller` ·
  `interim` and `contract` (finance & risk) · plus the **Board Appointments**
  subclassification. Re-run the core terms with **Remote-AU** for remote roles.
- **LinkedIn Jobs** (public pages) and **Indeed** — render the public search results in
  Chrome for the same core terms (risk, compliance, audit, governance, CFO/CRO/COO, head of
  finance, company secretary, interim). Public teasers only; never log in.
- **I Work for NSW** — render the keyword searches (risk, audit, governance, compliance,
  director, CFO, head of) and read the rendered listings; don't rely on web search alone.
- **§1a recruiter boards** (Applyflow-based) — render each firm's live-roles page and read
  the cards; capture deep-link job URLs.

**Triage discipline:** every role that is browser-verified live, passes the §3 filter, and
is **senior-manager-and-above** MUST be logged in the digest — do **not** silently drop
verified, on-target matches just to keep the list short. Trim only genuine duplicates and
clearly off-target/below-level roles. Include strong roles that are older but still live
(note the listing date). Coverage is still a *sample*, so close the `summary` by noting that
a manual look remains worthwhile and stating which boards were browser-verified this run vs.
search-only.

---

## 2. Access & copyright policy

- **Free/public listings:** fetch the public page (RSS-first where available, respect
  robots.txt), summarise the role in your own words, link out to the original.
- **Gated sources (AICD DO, login-walled boards/recruiters):** use only the public
  headline + teaser, set `"paywall": true`, link out, and (for AICD) add a one-line
  "worth a manual look in DO" note. Never log in, never bypass a gate.
- **Always paraphrase.** Never reproduce a job ad's text verbatim; rewrite duties and
  requirements in your own words. No reproduction of more than a short factual phrase.

---

## 3. Relevance filter + weighting rule

**Include if** the title/level is **manager-and-above** in one of the candidate's
functions, **and** the location rule is met. (Plain *Manager* roles are in-scope but
**lower priority** — see the seniority weighting below.)

- **Title triggers:** non-executive director, NED, chair, board member, committee member,
  advisory board; chief risk officer / CRO, chief operating officer / COO, chief financial
  officer / CFO, chief executive / CEO, managing director; general manager, group manager,
  senior manager; "head of" + (risk | compliance | assurance | audit | finance |
  operations | strategy | transformation | technology | IT); company secretary; financial
  controller; head of internal audit; plus function **Manager** roles (risk manager,
  compliance manager, audit manager, finance manager, operations manager, IT manager,
  business manager) — in-scope but lower priority.
- **Function affinity:** risk, compliance, assurance, internal audit, governance, finance/
  accounting, operations, business/strategy, transformation, IT/technology leadership.
- **Sector boost (not a filter):** energy/utilities/renewables, local government/council,
  insurance/mutual, financial services, superannuation, government, NFP.
- **Location rule:**
  - Permanent / fixed-term / contract / interim → include only if **Sydney metro,
    Sydney-hybrid, or Australia-remote**.
  - **Board / NED / committee / advisory → also include Interstate** (tag `Interstate`);
    assume monthly-travel cadence is acceptable.
- **Seniority weighting:**
  - **Senior Manager is a core target, not a stretch.** The candidate's own level is
    senior-manager (§0), so any **Senior Manager** / **"Senior &lt;function&gt; Manager"**
    role (e.g. Senior Risk Manager, Senior Manager — Risk & Resilience, Senior Manager
    Governance, Senior Finance Manager) counts as senior-manager-and-above and is a
    **highly valued, direct match** — eligible for `act` on good function/location fit.
    Do **not** reflexively downgrade Senior Manager roles to `watch`; weight them like
    "Head of"/director roles.
  - Senior-manager-and-above, "Head of", group manager, director, C-suite, board → eligible
    for **any** match tier (`act`/`watch`/`inform`) on fit.
  - **Plain** function **Manager**-level roles — titled just *Manager* with no
    "Senior"/"Head of"/"Group"/"Senior Manager" qualifier (e.g. Risk Manager, Finance
    Manager, Audit Manager, Compliance Manager) → **in-scope but lower priority**: cap at
    `watch` (never `act`); use `inform` if the sector/function fit is loose.
  - Clearly **below** manager (analyst, officer, coordinator, associate, junior, graduate)
    → `inform` only, *unless* board/advisory. Off-target functions (quota sales, clinical,
    trades) → exclude.
- **Tagging rule:** every item's tags are ordered **engagement-type first**, then region,
  then sector — e.g. `["Interim", "Sydney", "Insurance"]`, `["Board", "Interstate",
  "Energy"]`, `["Permanent", "Remote-AU", "FS"]`. Engagement-type ∈ {Board, Interim,
  Contract, Fixed-term, Permanent}.

---

## 4. Role taxonomy — assign each item exactly one category

1. **Board & NED** — Chair, NED, committee, advisory, company secretary at board level.
2. **C-Suite & Executive** — CEO, COO, CFO, CRO, MD, EGM.
3. **Risk, Compliance & Assurance** — enterprise/operational risk, compliance, internal
   audit, governance, AML, ESG/regulatory.
4. **Finance & Accounting** — financial control, head of finance, finance manager, FP&A
   leadership, CPA-track senior roles.
5. **Operations, Strategy & Transformation** — COO-track GM/ops, strategy, PMO,
   transformation/change leadership.
6. **Technology & Digital** — CIO, head of IT/technology, digital/data leadership.
7. **Interim, Contract & Advisory** — short-term / day-rate / fractional roles whose
   defining feature is the engagement (use this when the function is mixed or generic; a
   clearly-functional interim role, e.g. *interim CFO*, goes under its function category
   with an `Interim` tag instead).

---

## 5. Match strength — assign exactly one (`severity` field, renderer-compatible)

The renderer's three severity tiers are repurposed as **match strength**:

- **`act`**  — strong match and/or time-critical. Apply or contact the recruiter **today**.
  Default for any interim/contract role from a §1a recruiter (speed matters).
- **`watch`** — relevant but needs a judgement call (slight level/sector/location stretch).
- **`inform`** — peripheral: adjacent function, below-level (per §3), or aspirational —
  situational awareness only.

Reserve `act` for genuinely strong, actionable matches so the count stays meaningful.
**Senior Manager** and above (incl. "Senior &lt;function&gt; Manager", e.g. Senior Risk
Manager) is core-target and may be `act` on good fit — do not default it to `watch` (see §3).
Only **plain** *Manager*-level roles (no Senior/Head of/Group qualifier) are capped at
`watch` — never `act`.

---

## 6. Writing rules

- Paraphrase every listing; never reproduce ad text. `headline`: a rewritten one-line role
  title incl. org + location. `summary`: 1–2 sentences on the role. `so_what`: 1–2
  sentences on fit and the action (e.g. "Direct match to your risk/insurance background;
  recruiter-held interim — apply fast").
- **Deduplicate** across sources and against the previous 3 days (same org + title + level
  = one item; keep the most direct source). The 14:00 run refreshes the same day's file in
  place — carry forward still-live morning items, add anything new, drop expired ones.
- Never fabricate. Every item needs a real source + working URL. Empty category → omit or
  show empty; an empty day → publish empty sections and say so in `summary`.

---

## 7. Output schema (same renderer as all digests)

Write `data/digests/<TODAY>.json` (`YYYY-MM-DD`, Australia/Sydney). Overwrite if present.

```json
{
  "date": "YYYY-MM-DD",
  "generated_at": "ISO-8601",
  "posture": "one-line market read incl. interim count, e.g. '14 roles · 3 strong · 2 interim worth fast action'",
  "summary": "2–3 sentence plain-English read of today's matches",
  "counts": { "act": 0, "watch": 0, "inform": 0 },
  "sections": [
    {
      "category": "one of the 7 in §4",
      "items": [
        {
          "severity": "act | watch | inform",
          "headline": "rewritten role + org + location",
          "summary": "1–2 sentences",
          "so_what": "1–2 sentences: fit + action",
          "tags": ["<engagement-type>", "<region>", "<sector>"],
          "source": "board/recruiter/site name",
          "url": "https://…",
          "published": "YYYY-MM-DD or best-known",
          "paywall": false
        }
      ]
    }
  ]
}
```

Then update `data/manifest.json`: refresh today's top entry in place if present, else
**prepend** `{ date, file, posture, counts }` (newest first); leave older entries alone.
Validate both files parse. **Do NOT run git** — the helper publishes.
