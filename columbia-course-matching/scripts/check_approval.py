#!/usr/bin/env python3
"""Check whether courses count toward an IEOR MS degree (MSOR, MSIE, MSBA, MSE, MSFE).

Usage:
  python check_approval.py --program MSBA DROM8131B "IEOR E4650" COMSW4995
  python check_approval.py --program MSBA --cbs my_cbs.csv --non-ieor my_other.csv FINCB8306

Accepts any spelling of a course code: Vergil style (DROM8131B), list style
(DROMB8131), or spaced (DROM B8131). Prints one JSON object per course.

Verdicts:
  approved            on the pre-approved list for this program (status shows Elective/Core/...)
  not_counted         listed as "No", or falls under a never-approved rule
  ieor_department     IEOR-department course (IEOR/IEME/ORCS/CSOR), 4000+; counts as IEOR credit,
                      no pre-approval list applies
  needs_approval      not on any list: student must request approval BEFORE taking it
  ambiguous           several list rows share this code (e.g. topics courses); match by title
  list_not_loaded     the pre-approved list CSVs are not present, so approval is unknown

The pre-approved lists are not distributed with the public copy of this skill.
See references/programs/ieor-ms/README.md for how to obtain them.
"""
import argparse, csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "references", "programs", "ieor-ms")
PROGRAMS = ["MSOR", "MSIE", "MSBA", "MSE", "MSFE"]
IEOR_DEPTS = {"IEOR", "IEME", "ORCS", "CSOR"}
# From the "Notes" tab of the 2026-2027 sheet.
NEVER_IEOR = {"IEOR4212", "IEOR4307", "IEOR4003", "ORCA2500"}
SPS_DEPTS = {"ACTU", "APAN", "ERMC", "SUMA", "TMGT", "BUSI", "COPR", "IKNS", "FUND"}
QMSS_DEPTS = {"QMSS"}


def keys(code):
    """Return normalized keys like ['DROM8131'] for any spelling of a course code."""
    c = re.sub(r"[^A-Z0-9/]", "", code.upper())
    m = re.match(r"^([A-Z]{4})([A-Z]?)(\d{4})([A-Z]{0,2})((?:/\d{4})*)$", c)
    if not m:
        return []
    dept, nums = m.group(1), [m.group(3)] + [n for n in m.group(5).split("/") if n]
    return [dept + n for n in nums]


MISSING = []


def load(path, source):
    rows = []
    if not os.path.exists(path):
        MISSING.append(source)
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["_keys"], r["_source"] = keys(r["course_code"]), source
            rows.append(r)
    return rows


def check(code, program, rows):
    ks = keys(code)
    if not ks:
        return {"input": code, "verdict": "unrecognized_code",
                "note": "Could not parse; expected e.g. DROM8131B, DROMB8131 or IEOR E4650."}
    key = ks[0]
    dept, num = key[:4], int(key[4:])
    hits = [r for r in rows if key in r["_keys"]]
    out = {"input": code, "normalized": key, "program": program}
    if hits:
        out["matches"] = [{"list": r["_source"], "course_code": r["course_code"],
                           "title": r["course_title"], "status": r[program],
                           "comments": r["comments"]} for r in hits]
        statuses = {r[program].strip().lower() for r in hits}
        if len(hits) > 1 and len(statuses) > 1:
            out["verdict"] = "ambiguous"
            out["note"] = "Several rows share this code with different statuses; match the section title."
        elif statuses == {"no"}:
            out["verdict"] = "not_counted"
        else:
            out["verdict"] = "approved"
            if len(hits) > 1:
                out["note"] = "Several rows share this code; confirm the section title is one of them."
        return out
    if key in NEVER_IEOR:
        out.update(verdict="not_counted", note="Listed as never approved (undergraduate-level IEOR course).")
    elif dept in SPS_DEPTS:
        out.update(verdict="not_counted", note="School of Professional Studies courses are never approved.")
    elif dept in QMSS_DEPTS:
        out.update(verdict="not_counted", note="QMSS courses are never approved.")
    elif num < 4000:
        out.update(verdict="not_counted", note="Undergraduate (1000-3000 level) courses are never approved.")
    elif dept in IEOR_DEPTS:
        out.update(verdict="ieor_department",
                   note="IEOR-department course; counts toward IEOR credits. Check program notes for priority/exclusions.")
    elif MISSING and not (dept in IEOR_DEPTS):
        out.update(verdict="list_not_loaded",
                   note="Pre-approved list(s) not found: " + ", ".join(MISSING) + ". Cannot tell whether this course is "
                        "pre-approved. Get the department's current list (see references/programs/ieor-ms/README.md) "
                        "and pass it with --cbs / --non-ieor.")
    else:
        out.update(verdict="needs_approval",
                   note="Not on the pre-approved lists. Approval must be requested from the academic team BEFORE taking it. "
                        "CBS programming courses are never approved.")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--program", required=True, choices=PROGRAMS)
    ap.add_argument("--cbs", default=os.path.join(DATA, "preapproved_cbs.csv"))
    ap.add_argument("--non-ieor", default=os.path.join(DATA, "preapproved_non_ieor.csv"))
    ap.add_argument("codes", nargs="+")
    a = ap.parse_args()
    rows = load(a.cbs, "CBS") + load(a.non_ieor, "NON-IEOR")
    for c in a.codes:
        print(json.dumps(check(c, a.program, rows), ensure_ascii=False))


if __name__ == "__main__":
    main()
