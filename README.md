# Columbia-course-matching

An Agent Skill that helps Columbia University students pick courses for a term
and check degree progress. It cross-checks the things students otherwise check
by hand: degree audit and requirements, pre-approved elective lists (including
which Business School courses count), prerequisites and section types, meeting
times and conflicts, exam format, and instructor reviews. It returns a comparison
table and two or three conflict-free weekly timetables with backups.

## What is bundled

- `columbia-course-matching/SKILL.md` — the workflow.
- `scripts/check_approval.py` — looks up whether a course counts toward an IEOR
  MS degree, accepting any spelling of a course code.
- `references/programs/msba/requirements.md` — MSBA requirements (Fall 2026 and
  Fall 2025 cohorts).
- `references/programs/ieor-ms/` — approval rules for MSOR, MSIE, MSBA, MSE and
  MSFE electives. The department's pre-approved course lists are **not**
  included: they are an internal, sign-in-only document. The skill reads the
  current list from the student's own signed-in browser, or from a copy the
  student provides (see the README in that folder).
- `references/data_sources.md` — where each kind of information lives (Vergil,
  Stellic, the CBS course catalogue, instructor pages, CULPA) and how far to
  trust it.

**Data year: 2026-2027.** Requirements and approval lists change every year.
Students in other programs can upload their own requirement documents in chat.

## Before you use it

- **The pre-approved elective lists are not included.** They are an internal
  IEOR department document that requires Columbia sign-in. The first time you
  ask whether a Business School or other non-IEOR course counts, the skill will
  ask you to sign in and will read the current list from the department's
  sheet in your own browser. The google form that IEOR deparment provided. You need to have access to that sheet yourself.
- **The bundled data is for the 2026-2027 academic year.** Requirements and
  approval rules change every year, so check which year you are planning for.
- **Only IEOR department programs are built in.** MSBA requirements are
  included in full, along with elective approval rules for MSOR, MSIE, MSE and
  MSFE. If you are in any other program, upload your program's degree
  requirements and its list of approved courses when you start.

## Install

Zip the `columbia-course-matching` folder (or use the packaged `.skill` file
from a release) and add it as a skill in Claude. The skill follows the open
Agent Skills format, so other assistants that support it can load the same folder.

## How sign-in works

Vergil and Stellic need a Columbia login with Duo. The skill asks the student to
sign in themselves in a browser the assistant can see. It never asks for, types
or stores passwords or Duo codes, and it is read-only: it does not add courses
to a plan, register, or submit anything.

## Disclaimer

Unofficial; not affiliated with or endorsed by Columbia University. A plan
produced with this skill is a starting point. Confirm with your academic advisor
before relying on it for graduation.
