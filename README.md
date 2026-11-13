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

## Prompt templates / 提示词模版

Copy one, replace the parts in [brackets], and delete any optional line you do not need. Only the program, entry term and target term are required; anything you leave out is not treated as a constraint.

复制其中一个，替换 [方括号] 里的内容，用不到的可选行直接删掉。必填的只有项目、入学学期和目标学期；没写的偏好不会被当成限制。

### 1. Plan next term's courses / 选下学期的课

English:

```
I'm a Columbia [program, e.g. MSBA] student who entered in [entry term, e.g. Fall 2026].
Help me choose courses for [target term, e.g. Spring 2027]. I want to take [number] credits.

Courses taken or in progress: [list them, or write "read them from my degree audit"]

Interests: [e.g. AI, marketing analytics]
Times I cannot attend: [e.g. Fridays; before 9am; after 9pm]
Format: [lecture / seminar / project-based, or no preference] (optional)
Exams and assignments: [e.g. prefer no final exam; projects and papers are fine] (optional)
Attendance: [e.g. prefer no mandatory attendance] (optional)
Half-term courses: [fine / avoid] (optional)
Must take or must avoid: [course title or code] (optional)

Give me [2-3] concrete weekly timetables, each with backups in case I don't get a seat.
```

中文：

```
我是哥大 [项目，例如 MSBA] 的学生，[入学学期，例如 2026 Fall] 入学。
帮我选 [目标学期，例如 Spring 2027] 的课，想修 [学分数] 学分。

已修或在修的课：[列出课程，或写"请从我的 degree audit 里读"]

兴趣方向：[例如 AI、marketing analytics]
不能上课的时间：[例如 周五全天；早上 9 点前；晚上 9 点后]
上课形式：[lecture / seminar / project 均可，或指定]（可选）
考试和作业：[例如 尽量不要 final，可以接受 project 和 paper]（可选）
出勤要求：[例如 不要强制出勤]（可选）
半学期课程：[可以 / 不要]（可选）
一定要上或一定不上的课：[课名或课号]（可选）

请给我 [2–3] 套具体的周课表，每套都要有选不上时的 backup。
```

### 2. Check whether I can graduate / 检查能不能毕业

English:

```
I'm a Columbia [program] student who entered in [entry term] and plan to graduate in [graduation term].
Please read my degree audit and tell me whether I meet the graduation requirements,
what is still missing, and anything I should confirm with my advisor.
```

中文：

```
我是哥大 [项目] 的学生，[入学学期] 入学，计划 [毕业学期] 毕业。
请读我的 degree audit，告诉我是否满足毕业要求、还差什么，
以及有哪些需要我找 advisor 确认的地方。
```

### 3. Find a replacement for a course I didn't get / 某门课没选上，找替代

English:

```
I'm a Columbia [program] student who entered in [entry term], registering for [target term].
I didn't get into [Course Title (CODE)]. I am already registered for: [courses and sections].
Find [number] replacements that count toward the same requirement
and do not clash with the courses I already have. Other preferences: [as in template 1, optional]
```

中文：

```
我是哥大 [项目] 的学生，[入学学期] 入学，正在选 [目标学期] 的课。
[课名（课号）] 没选上。我已经选了：[列出已选课程和 section]。
请找 [数量] 门能替代它的课：要算进同一类毕业要求，
而且和我已选的课时间不冲突。其他要求：[同模版一的偏好，可选]
```

### Notes / 说明

- "Times I cannot attend" is a hard filter; exam, format and attendance lines are preferences that only affect ranking.
  "不能上课的时间"是硬性条件，会直接筛掉课；考试、形式和出勤是偏好，只影响排序。
- If your program is not one of the bundled ones (currently the IEOR master's programs, 2026-2027), also upload your program's degree requirements and its list of approved courses.
  不在内置范围内的项目（目前是 IEOR 系硕士项目，2026–2027 学年），请同时上传你们项目的毕业要求和可选课程名单。
- Reading your degree audit or Vergil requires you to sign in yourself in the browser; see below.
  读取 degree audit 或 Vergil 需要你自己在浏览器里登录，见下文。

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
