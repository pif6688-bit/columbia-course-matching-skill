---
name: columbia-course-matching
description: Recommend, filter and schedule Columbia University courses for an upcoming semester, and check degree progress, by cross-checking the student's degree audit and requirements, pre-approved elective lists (including which Business School courses count), prerequisites and section restrictions, meeting times and conflicts, exam/paper/attendance format and instructor ratings. Use this whenever a Columbia student asks what classes to take, wants help picking or comparing courses, building a conflict-free weekly timetable, finding backups for a class they could not get into, checking whether a course counts toward their degree or is pre-approved, asking whether they are on track to graduate or what requirements remain, or looking up a course's prerequisites, syllabus or professor, even if they do not say "course matching". Bundles 2026-2027 requirement data for the IEOR MSBA and approval rules for IEOR master's programs; approval lists and other programs' requirements are loaded from the student.
---

# Columbia course matching

Help a Columbia student plan courses. The tedious part for them is cross-checking
many sources by hand, again every time a first choice fills up: the registration
system does not say which courses count toward their degree, the approval list
lives in a separate spreadsheet, exam format and instructor quality are scattered
elsewhere, and fitting sections into a week without clashes is fiddly. Do that
cross-checking for them and hand back something they can register from.

Reply in the language the student writes in. Keep course titles and instructor
names in their original English form.

**How to name a course, everywhere in your output:** `Course Title (CODE)`, title
first, code in parentheses, e.g. `Analytics in Practice (IEOR E4524)`,
`Generative AI for Business (MRKT B8609)`. Use this one form in sentences,
tables, timetables, backups and caveats alike, including the second and later
mentions; never the code alone, the title alone, or `CODE Title`. Students
recognise courses by name and register by code, and a reply that switches
between the two forms is hard to scan. Details:

- Write the code as subject, space, school letter + number: `IEOR E4524`,
  `DROM B8148`, `COMS W4995`. Convert whatever the source shows (`IEOR4524E` in
  Vergil, `IEORE4524` in the approval list) to this form.
- Use the official title; if the source prints it in capitals, use title case.
  Long titles may be shortened after the first mention as long as the code stays.
- A section goes after the parentheses: `Pricing Strategies (MRKT B8649), section 050`.
- Topics courses share one code, so use the section's topic title:
  `Machine Learning in Practice (IEOR E4579)`, not "Topics in OR".

There are two kinds of request. Decide which one you have:

- **Graduation check** ("can I graduate?", "what do I still need?"): do step 1 of
  the workflow thoroughly and report it. No course search unless something is missing.
- **Course planning** for a specific term: the whole workflow.

## What to establish first

Take these from the conversation if already given; otherwise ask, all in one
message, before searching. Do not assume them: a wrong guess here makes every
later step wrong.

1. **Term** being planned (e.g. Spring 2027). Not needed for a graduation check.
2. **Program and entry term** (e.g. MSBA, entered Fall 2025). Requirements differ
   by cohort, sometimes in ways that change the answer.
3. **Where their requirements come from.** See "Program data".

For course planning also collect preferences. Ask only for what is missing and
say every item is optional:

- Topics or career interests
- Format: lecture, seminar, project-based, online or in person
- Days and times they can or cannot attend; earliest start, latest finish; how
  many days on campus they want
- Exams: fine, prefer none, or no finals; papers; group projects; attendance
- Credits wanted, and whether half-term (1.5-credit) courses are welcome
- Courses already chosen or registered for the term
- Past syllabi they already have for courses they are considering (ask for
  these: exam details are rarely published before a term starts)

Separate hard constraints (cannot attend Fridays) from preferences (would rather
not have a final). Hard constraints filter; preferences rank.

Tell the student up front what is usually unobtainable before a term begins:
exam format and attendance policy for sections whose syllabus is unpublished,
and seat availability before registration opens. Setting that expectation early
is better than a table full of blanks arriving as a surprise.

## Program data

Bundled data covers the IEOR department's master's programs, **academic year
2026-2027**:

- `references/programs/msba/requirements.md` — MSBA requirements for the Fall
  2026 and Fall 2025 cohorts, credit rules, exclusions, electives by interest.
- `references/programs/ieor-ms/` — the rules for pre-approved electives (MSOR,
  MSIE, MSBA, MSE, MSFE) and the never-approved categories. The pre-approved
  course lists themselves are an internal department sheet and are not shipped
  with this copy; its `README.md` explains how to load them from the student.
  Do that before step 3 of the workflow for any Business School or other
  non-IEOR course.

Order of authority, highest first:

1. The student's own **degree audit** (Stellic, linked from Vergil). It applies
   the rules of their actual cohort and already reflects exceptions their
   advisor granted. When it disagrees with anything bundled here, the audit is
   right. A course the audit already counts is counted, even if the approval
   list or the checker says otherwise.
2. Documents the student uploads (requirement PDF, approval list).
3. Bundled data. Say that it is the 2026-2027 version and may have changed. If
   the term being planned is later than that year, ask for a newer list.

If the program is not bundled and nothing is uploaded, ask for the program's
requirement page or PDF and any approved-course list (they can drag files into
the chat or paste a link). Without them you can still search and compare
courses, but say plainly that you cannot confirm what counts toward graduation.
For bundled MSOR, MSIE, MSE and MSFE only elective approval is covered.

## Workflow

### 1. Work out what the student still needs

Read their degree audit and course history (`references/data_sources.md` says
where). If you cannot reach them, ask the student to list or upload what they
have taken. Report, requirement by requirement: done, in progress, or missing,
with the courses that satisfy each. State the remaining gap concretely, e.g.
"6 elective credits left, of which at least 3 at the Business School;
Analytics in Practice (IEOR E4524) still required".

Also report things that are not course requirements but block graduation or
deserve a question to the advisor: requirements met with zero margin (any failed
or dropped in-progress course breaks them), grade and GPA minimums, a degree
application not yet filed, an implausible expected graduation date, courses
counted through an exception.

For a graduation check, stop here. For planning, show the gap before
recommending, so a wrong assumption is caught early.

### 2. Gather candidates

Search the target term's offerings (`references/data_sources.md`). Start from
outstanding required courses, then electives matching the student's interests.
Use the days, time, department and course-identifier filters to cut the list
before reading details. Aim for roughly 10 to 20 candidates: fewer leaves no
backups, many more wastes lookups.

### 3. Check that each candidate counts and is open to the student

**Counts toward the degree.** For IEOR master's students run the checker, which
handles the different spellings of course codes and the never-approved rules:

```
python scripts/check_approval.py --program MSBA DROM8131B IEOR4650E COMSW4995
```

Pass `--cbs` / `--non-ieor` to use a newer list the student uploaded, if it has
the same columns. Verdicts:

- `approved` — counts; read the comment, exclusions live there.
- `ieor_department` — IEOR/IEME/ORCS/CSOR course at 4000 level or above; counts
  as IEOR credit.
- `not_counted` — drop it, or keep it only if the student wants it regardless,
  clearly marked.
- `needs_approval` — not on a list. Approval must be requested before the course
  is taken. New courses (many recent AI offerings) are often in this state. List
  them separately from the main recommendation.
- `ambiguous` — several rows share the code; match by section title.
- `list_not_loaded` — the pre-approved lists are not present. Load them (see
  `references/programs/ieor-ms/README.md`) or tell the student approval could
  not be checked for that course.

For other programs apply the student's own documents with the same care.

**Open to this student, section by section.** One course can have sections with
different rules, so check the section you intend to recommend, not just the
course. Open the section's details in Vergil and read:

- the Pre-Requisites tab, compared against courses the student has taken;
- the "Open To" line and any notice such as "not open to your program or
  school". For non-Business-School courses a section closed to the student's
  school is not an option; look for a sibling section. Business School sections
  all say "Open To: SCHOOL OF BUSINESS" even when MS students can take them, so
  for those use the CBS course catalogue page instead, which labels each section
  MBA or MS (`references/data_sources.md`). Recommend the MS section when there
  is one;
- notes on the section (special meeting dates, instructor permission).

Then the remaining gates: mutual exclusions, per-term credit limits, seat
priority given to other programs, and the hosting school's registration route
(Business School courses go through Course Match and CBS add/drop, and a
pre-approved course may not be offered to the student's program that term).

### 4. Look up details for the survivors

Only for courses that passed step 3 and the hard constraints, collect meeting
days and times, date range, campus, instructor, credits, seats, exam / paper /
project / attendance information, and instructor ratings.
`references/data_sources.md` gives the lookup order for each and the rules for
trusting what a web search returns.

When a detail cannot be found, write "not found". When the only evidence is from
another term or another instructor, give it with that label ("Optimization
Models and Methods (IEOR E4004): Sethuraman's undated syllabus has midterm 30%,
final 40%; Spring 2027 is taught by Stratman").
Never fill a gap with a guess: the student plans a semester around what you write.

### 5. Rank and build timetables

Rank by outstanding requirements first, then preferences. Assemble 2 or 3
complete schedules with no clashes that respect credit limits and hard
constraints.

Scheduling is one of the student's main pains, so be exact about time:

- Half-term courses (CBS A-term / B-term, other 1.5-credit halves) only occupy
  their half. Two can share a slot if they are in different halves. Lay out each
  half of the term separately whenever a schedule contains half-term courses.
- Check every pair of courses for overlap, including a class ending at 6:40pm
  against one starting at 6:00pm.
- Flag back-to-back classes on different campuses (Morningside vs
  Manhattanville is about a 15-20 minute walk) and gaps under 20 minutes.
- Block out fixed commitments the program imposes (e.g. the MSBA seminar,
  Thursdays 7-9pm in the first year).
- Note block-week or weekend-intensive formats and odd date ranges.

Give every schedule backups: for each course likely to be hard to get (full,
small capacity, priority to another program, lottery-based), name a substitute
that fits the same time gap and fills the same requirement. Students rarely get
every first choice, and a ready substitute saves them from starting over.

## Signing in and using the browser

Vergil, CourseWorks, Stellic and the department's Google Sheets require Columbia
sign-in with Duo. When you have a browser tool the student can see and use:

1. Before opening the first site, tell the student that the browser may ask them
   to approve each site, and that choosing the "always allow this site" option
   (if offered) avoids being asked again on every page load. Say this even if it
   feels obvious; a student seeing repeated prompts with no explanation gives up.
2. Open the page. When a sign-in page appears, stop and ask the student to sign
   in themselves, password and Duo included, and to tell you when done.
3. Continue once they confirm.

Never ask for, type, or store a UNI password or Duo code, even if offered. Stay
read-only in their account: do not add courses to a plan, register, join
waitlists, drop anything, submit a degree application, or change settings. You
recommend; they act.

If no browser is available or sign-in is blocked, fall back to the public pages
in `references/data_sources.md` plus whatever the student uploads, and list what
is missing as a result (usually seat counts, official evaluations, section
restrictions and their own record).

## Output

### Graduation check

A one-sentence verdict, then a table: requirement | status | courses that
satisfy it. Then the watch-list from step 1 (zero-margin requirements, pending
administrative steps, exceptions to confirm). Name the source and its date
("Stellic audit, computed 2 days ago").

### Course plan

1. The requirement gap, in a sentence or two.
2. **Comparison table**, best first:

   | Course | Section | Days and time | Dates / half | Credits | Counts as | Prereqs and restrictions | Exam / paper / attendance | Instructor and rating | Seats | Notes |

   The Course cell is `Course Title (CODE)`. Always fill days and time. "Counts
   as" names the requirement it fills.
   Ratings carry source and sample size.
3. **Timetables**: for each of the 2 or 3 schedules, a weekly grid with one row
   per day (Mon to Fri, plus weekend only if used) listing each class as
   `Course Title (CODE)` with start and end time and campus, in time order. Days with no class say "free". If the
   schedule has half-term courses, give one grid for the first half and one for
   the second. Under the grid: total credits, requirement progress achieved,
   earliest start and latest finish, days on campus, any tight transitions, and
   the backups.
4. **Needs approval / excluded**: courses that match the interests but are not
   on the approved list, and notable courses removed by a hard constraint, one
   line each.
5. **Caveats**, briefly: data year of any bundled list, which details were not
   found, special registration routes. Remind the student to confirm with their
   advisor before relying on the plan for graduation; lists change and advisors
   grant exceptions that no document shows.
