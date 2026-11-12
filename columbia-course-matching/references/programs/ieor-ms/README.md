# IEOR MS pre-approved electives (MSOR, MSIE, MSBA, MSE, MSFE)

**The lists themselves are not included in this public copy.** They are an
internal IEOR department document ("MS Preapproved Electives - Students", a
Google Sheet behind Columbia sign-in) and are revised every year. Get the current
one from the student:

1. Ask the student for the link to the sheet (the department shares it in
   advising materials) or for a copy of its contents.
2. If you have a browser the student is signed in to, open the sheet and read the
   "CBS" and "NON-IEOR" tabs, plus "Information" and "Notes". Downloading may be
   disabled; reading the page is enough.
3. Save each tab as a CSV next to this file, named `preapproved_cbs.csv` and
   `preapproved_non_ieor.csv`, with exactly these columns:
   `course_code, course_title, MSOR, MSIE, MSBA, MSE, MSFE, comments`.
   Or keep them anywhere and pass `--cbs` / `--non-ieor` to the checker.
4. Tell the student which academic year the list you loaded is for.

Until the lists are loaded the checker returns `list_not_loaded` for courses it
would need them for. Say so to the student rather than guessing; the rule-based
verdicts (IEOR-department courses, never-approved categories) still work.

Values per program: `Elective` / `Core` = counts; `No` = does not count. MSE uses
category names (`Breadth`, `Management`, `DRO`, `Analytics`, `Analysis`) that all
mean it counts, in that MSE bucket. `Spring Cohort` = only for spring-entry cohorts.

Use `scripts/check_approval.py` rather than reading the CSVs by eye: course codes
are spelled differently in different systems (Vergil: `DROM8131B`; this list:
`DROMB8131`) and the script normalizes them.

## Rules from the sheet's Information and Notes tabs (2026-2027)

- Pre-approval does not guarantee a seat.
- A course not on the list needs approval from the academic team, requested
  through the department's course approval form **before** taking the course.
- Being offered on CBS Course Match does not mean IEOR approves it. They are
  different lists.
- MSBA and MSE students register for CBS courses through Course Match in the CBS
  ranking period, then during CBS add/drop. A select list of CBS courses open to
  MSBA/MSE is emailed each semester; a pre-approved course may still not be on it.
- MSOR, MSIE, MSFE students cross-register at the Business School.
- EMBA 7000-level courses equivalent to an approved MBA 8000-level course are
  also approved. 9000-level PhD courses require cross-registration at CBS.
- Several rows can share one code (topics courses such as COMSW4995, or
  BUECB8257). Match on the section title, not the code alone.
- Read the `comments` column: it holds exclusions such as "Cannot take if already
  taken IEOR E4525".

Never approved for any IEOR MS degree:
- Programming courses from CBS
- QMSS courses
- SPS courses (ACTU, APAN, ERMC, SUMA, TMGT, etc.)
- Undergraduate courses (1000-3000 level), unless the list explicitly approves one
- IEORE4212, IEORE4307, ORCAE2500, IEORE4003
