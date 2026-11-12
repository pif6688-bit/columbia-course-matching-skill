# Where to find each piece of course information

Verified against Vergil in November 2026. Sites change; if a page looks different,
adapt rather than give up, and tell the student what you could not find.

## Vergil (vergil.columbia.edu) — needs the student's login

Everything in Vergil sits behind Columbia sign-in (UNI + password + Duo). See
"Signing in" in SKILL.md.

Course search: Dashboard → Course Search, or `/vergil?term=<code>`. Term codes are
year + 1 (spring), 2 (summer), 3 (fall): Fall 2026 = `20263`, Spring 2027 = `20271`.
Vergil opens on its own default term, which may not be the one the student is
planning, so always set the term explicitly.

Search filters worth using: keyword, school, department, subject, instructor,
days, time range, credits, course level, method of instruction, course type,
"only show classes with open seats". Results show 10 courses per page.

Searching and expanding courses happens inside one page without reloading, so one
site approval covers a whole search session.

Expanding a course lists its sections with: section number, call number, class
type (LECTURE, SEMINAR, ...), days and times, room and campus, instructor, date
range (reveals half-term courses, e.g. 10/25-12/12 is a CBS B-term), in-person or
online, grading mode, credits, and enrollment as enrolled / capacity.

Clicking a section opens tabs:
- Details: school, department, session (e.g. "CBS B-Term"), instructor.
- Pre-Requisites: required prior courses and whether set by instructor or department.
- Faculty Evaluations: official evaluation PDFs per instructor and term. Present
  for many Engineering courses; often disabled for Business School courses.
- Syllabus: frequently disabled. Do not count on it.
- View in CourseWorks: link to the Canvas site, often disabled before the term.
- A banner such as "This class is not open for online registration" with notes.
  Common on CBS courses, which use Course Match / CBS add-drop instead.

Vergil writes codes as subject + number + school letter (`IEOR4650E`,
`DROM8131B`). Department lists write `IEORE4650`, `DROMB8131`. Same course.

Student record pages (also in Vergil): the dashboard's Program Summary shows
program and completed credits; Student Records → Academic Records lists courses
taken; "View My Degree Audit Report" shows requirement progress. Columbia also
runs Stellic (columbia.stellic.com) for degree audits.

The Details tab also has an "Open To" line. Read it with care: every Business
School section shows "Open To: SCHOOL OF BUSINESS", including the sections that
MSBA and MSE students are in fact enrolled in, because those students get into
CBS courses through Course Match and CBS add/drop rather than Vergil. So on a
CBS course this line does not rule a section out. Which CBS section a master's
student should aim for is shown on the CBS course catalogue page instead (see
below). For non-CBS courses, an "Open To" line that excludes the student's
school, or a "not open to your program or school" notice, does disqualify that
section.

Degree audit: "View My Degree Audit Report" opens Stellic
(columbia.stellic.com/app/audit). It lists every requirement group with status
(taken / in progress / remaining), the courses applied, exceptions, GPA checks
and the catalog version applied to the student. This is the best single source
for graduation questions. Enrollment history with grades is under
Student Records -> Academic Records -> Show All.

Practical notes for driving the search page:
- The "Course Identifier" filter accepts a prefix (`IEOR4`, `MRKT`, `DROM8`),
  which is the quickest way to list one department or level for a term.
- "Expand courses" opens all sections on the page and then turns into "Collapse
  courses"; results are paged 10 at a time.
- Section details open by clicking the section's title cell. The panel does not
  always open on the first try; if the tabs (Details, Pre-Requisites, ...) are
  not there, click again or take a screenshot and click the row, rather than
  recording "no prerequisites". "No Pre-Requisites tab" on an opened panel means
  none are listed; a panel that never opened means unknown.
- Seat counts show 0 / capacity until registration opens for the term.
- Keep scripted page interactions short; long multi-course loops time out. Do a
  few courses per step.

Read only. Never press Add to Plan, registration, waitlist, drop, or degree
application controls. The student acts themselves.

## Business School course catalogue (courses.business.columbia.edu) — public

One page per course at `https://courses.business.columbia.edu/B<number>`, e.g.
`/B8609`, `/B8148`. No login. Check it for every CBS course you recommend. It gives,
per term and per section:

- Section label: sections are marked "MBA" or "MS" (and A-term / B-term). The MS
  sections are usually numbered 050 or 060 and are the ones meant for MSBA / MSE
  and other MS students; 001, 002... are usually MBA sections. Prefer the MS
  section when one exists, and when a course has only MBA sections say that
  getting a seat is less certain. Courses numbered B9651-B9657 with "MS" in the
  title are MS-designated throughout.
- Days, times, dates, room and faculty for upcoming and past terms.
- Section notes, e.g. mandatory first-class attendance, or no credit if a
  related course was taken.
- Syllabi: a "Download Syllabus" link per section where the instructor uploaded
  one, at `https://courses.business.columbia.edu/get-syllabus/<id>`. These open
  without login and state grading weights, exams, attendance and prerequisites.
  The upcoming term usually shows "No Syllabus", so use the most recent past
  term that has one and report which term and instructor it belongs to.
  Example: the B8148 syllabus lists 70% assignments (best 4 of 6), 30%
  attendance and participation, and no final exam.

## Exams, papers, attendance, workload

No single source has this, and before a term starts the Vergil Syllabus tab is
usually disabled. Try in order and stop when you have a trustworthy answer:

1. Vergil Syllabus tab for the section.
2. A syllabus the student already has (ask them).
   For Business School courses, the CBS course catalogue page's "Download
   Syllabus" links (see above) are the most productive source; try them early.
3. CourseWorks (courseworks2.columbia.edu) course site, if the student can open it.
4. Instructor and department websites, found by web search. Many Columbia
   instructors keep a public course page on their department's site, outside
   Vergil, with the full syllabus: grading weights, exam dates, prerequisites,
   homework policy. Example: searching `analysis of algorithms columbia` finds
   `www.cs.columbia.edu/~xichen/algorithm/`, Xi Chen's page for the current
   term, listing five graded components at 20% each including a midterm and a
   final evaluation with dates, plus prerequisites.
   - Search the plain course title plus "columbia" first, the way a student
     would; then try the course code, the instructor's name, and "syllabus".
   - Good hits live at `<dept>.columbia.edu/~<uni>/...` or `www1.columbia.edu/~<uni>/...`.
     Computer Science, Statistics, Mathematics and some IEOR faculty do this
     often; many departments and most adjunct-taught courses do not, so a miss
     here is normal.
   - If a page will not load through a web-fetch tool (some of these servers
     redirect in a loop), open it in the browser instead.
   - Department "Courses" pages (e.g. `ieor.columbia.edu/content/<course>`,
     `www.ee.columbia.edu/content/<course>`) are a different thing: catalogue
     descriptions for a past term. They rarely give grading, but they do state
     enrollment restrictions such as "MSBA students only" or "IEOR students
     only; priority to MSBA students", which are worth reporting.
5. Official evaluation PDFs from the Faculty Evaluations tab: student comments
   describe workload, exams and projects.

Other universities reuse the same course numbers and similar titles, so a
search hit is only usable if all of these hold:

- It is clearly Columbia's (or the school the student named): hosted on a
  columbia.edu domain, or the document itself names the university. A matching
  course number alone proves nothing.
- The course code and title match the course being considered.
- You have noted the instructor and term on the document and compared them with
  the section being considered. Same instructor, recent term: good evidence.
  Different instructor or no date: weak evidence, since exam structure follows
  the instructor. Report it only with that label.

Example of correct reporting: "Final exam: likely. An undated syllabus by Jay
Sethuraman (columbia.edu) lists midterm 30%, final 40%, homework 30%; the Spring
2027 sections are taught by Eric Stratman, so treat as indicative only."

When nothing passes these checks, write "not found". A guessed exam format that
turns out wrong costs the student far more than an honest blank.

## Instructor ratings

1. Official Faculty Evaluations in Vergil: best evidence. Give the terms covered.
   Often disabled for Business School courses.
2. CULPA (culpa.info), Columbia's own anonymous professor and course review
   site. This is the review site to use for Columbia; it only contains Columbia
   instructors, so there is no risk of picking up someone from another school.
   General web search does not surface its pages and direct search URLs render
   blank, so open https://culpa.info/ in the browser, type the instructor's last
   name (or the course name) into the search box, and pick from the suggestions,
   which link to `/professor/<id>` pages. Two Columbia instructors can share a
   surname (searching "Johar" returns both Gita Johar and Hardeep Johar), so
   match the first name. Report the rating or nugget (gold 4.0+, silver 3.5+,
   bronze 3.0+, awarded only above 5 approved reviews), the number of reviews,
   and how recent they are. A professor page showing a rating of 0.00 with no
   reviews listed means "no reviews yet", not a score of zero; report it as
   unrated. Coverage is thin for graduate-only and Business School instructors,
   and a search that shows no suggestion means the instructor is not listed.
   CULPA's job here is to rate the instructor, so
   reviews of the same person teaching a different course (including
   undergraduate courses) are perfectly good evidence of teaching quality; what
   matters is that it is the same instructor. Only comments about workload and
   exams are course-specific: quote those when the review is for the course
   being considered, and otherwise leave exam format to the syllabus sources.
3. Rate My Professors: only if the student asks for it or names another school.
   Search inside the school, never site-wide:
   `https://www.ratemyprofessors.com/search/professors/278?q=<last name>` (278 is
   Columbia). Its results page mixes in same-named people "at other schools";
   ignore those.

Report the source next to every rating. If an instructor is unannounced, new, or
has no reviews, say so rather than leaving the reader to guess.

## Public pages (no login)

- Directory of Classes: doc.sis.columbia.edu — sections, times, instructors.
- Engineering bulletin: bulletin.engineering.columbia.edu — descriptions, prerequisites.
- CBS course catalogue: courses.business.columbia.edu (section types and syllabi; see above)
- Program requirement pages, e.g. ieor.columbia.edu/msba-curriculum

These are the fallback when no browser sign-in is possible. They lack enrollment
counts, official evaluations and the student's own record.
