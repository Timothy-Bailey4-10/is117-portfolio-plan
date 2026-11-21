# Portfolio — Plan (Review 2)

**Owner:** Timothy Bailey ([@Timothy-Bailey4-10](https://github.com/Timothy-Bailey4-10)) · **Course:** IS117, Section 007 · **Stage:** Plan · **Due:** Nov 24, 2026, 8:30 a.m. ET

> This is my build instructions for the portfolio. I update this same file as I learn what works.
> Labels used on every check and claim: **Planned** (written, not run yet) · **Passed** / **Failed** (ran it; date + who) · **Requested** (asked someone, waiting) · **Assumption** (not validated).

---

## 0. Where this plan comes from (Research carried forward)

Career exploration already counts as my Research. I'm reusing its reader, goals and evidence. I'm not doing a new Research step.

| From my research | What it means for the portfolio |
|---|---|
| Target role: **Forward Deployed Engineer (FDE)**. Next opportunity: **software engineering internship on a team that uses AI** ([roadmap, Stage 4](https://timothy-bailey4-10.github.io/is117-ai-career-research/roadmap)) | The intro names this goal as a *goal*, not a job I hold |
| FDE postings ask for production coding, stakeholder communication, customer discovery and integrations ([skills page](https://timothy-bailey4-10.github.io/is117-ai-career-research/skills)) | Each case study shows: who it was for (discovery), what I built (coding), and how I checked it |
| "Most AI postings target 2+ years of experience. A student's job is to build proof" ([roadmap](https://timothy-bailey4-10.github.io/is117-ai-career-research/roadmap)) | Proof (live demo, repo, checks) sits one click from every project |
| Career site brand: violet `#6d4aff` → teal `#18b4c9` gradient, Inter font, "every number is linked" | I carry the same look and the same honesty rule into the portfolio |

---

## 1. Plan the main task

### Reader (persona hypothesis, **Assumption**)

**Primary reader: Dana, an engineering lead screening internship candidates for an applied-AI team.**
- Situation: skims 20+ portfolios between meetings, often on a phone, and spends about 1–2 minutes on each (**Assumption**).
- Goal: in under a minute, find one real project, see *what I personally did*, and open proof (code, live demo, checks).
- Worry: "Is this just a group project where they watched? Are these claims real?"
- What the page must help Dana decide: *is this student worth an interview for an AI-adjacent internship?*

**Secondary reader (contrast check): a classmate peer reviewer.** They follow the same path but read carefully. They test whether every link opens and whether my contribution is honest.

**Main task:** *Find a project → see my contribution → open its evidence.*

### Two ways to arrange the same content (compare two short approaches)

Both versions keep the same content: intro line, the same 3 project case studies, the same professional links, and the same contact. Only the **hierarchy** changes.

#### Specification A — "Projects first"
- **Approach:** one scrolling home page. The projects come right after a one-line intro.
- **Sections (in order):** Hero (name, "IS117 student · aiming for AI-team SWE internships / FDE", 2 buttons: *See projects*, *Résumé*) → 3 project cards → short About → Professional materials (GitHub, LinkedIn, Résumé, this site's source) → Contact.
- **Main action:** tap a project card to open its case-study page. That page has *Live demo*, *Repository* and *My contribution* at the top.
- **Brand:** violet/teal gradient name like the career site. Cards use the same bordered "role-card" look.

#### Specification B — "Skills map first"
- **Approach:** organize by the 5 FDE skills from my research (Discover → Build → Deploy → Measure → Present). Each skill links to the project that proves it.
- **Sections (in order):** Hero → skills map (5 tiles, each naming one project as proof) → project list → materials → contact.
- **Main action:** tap a skill tile to jump to the matching section of a case study.
- **Comparison:** B tells a stronger FDE story, but Dana needs one extra step before seeing a project. It also risks overclaiming, because a skill tile can look like a credential.

#### Decision: build **A**, borrowing one idea from B
I expect **A** to work better for Dana. Her task is "find a project fast", and A puts projects one tap from the top on a phone. B's skills story becomes a single line of skill tags on each project card. I'll check this in Build by timing the task in both versions (S1 check).

### User stories, essential features and checks

Every check is something a classmate can run: an action plus what they should see. **All are Planned until I run them.**

| ID | User story | Essential feature | Acceptance check | Status |
|---|---|---|---|---|
| S1 | As Dana, I want to find a relevant project quickly so I can decide whether to keep reading. | **F1:** 3 project cards (T-shirt, Group business, Portfolio) at the top of the home page. Each has a title, a one-line "who it was for", and a "Course project" label. | On a phone (≤ 400px wide), a classmate who has never seen the site opens the home page. Within **30 seconds** and **≤ 2 taps** they reach a case study and say aloud which audience it served. | Planned |
| S2 | As Dana, I want to see what *I* built versus what the team built, so I can judge my real skills. | **F2:** each case study has a "**My contribution**" box near the top. It lists my work, teammates' work (named, with GitHub usernames for the group project) and how AI helped. | The classmate opens the **Group** case study. Without scrolling past the first screen, they correctly name 2 things I built and 1 thing my teammate did. | Planned |
| S3 | As Dana, I want to open evidence for a project so I can check that the claims are real. | **F3:** an "Evidence" row on each case study: *Live demo*, *Repository*, *Checks* (test results or a review issue). Unfinished items are labeled "In progress", not dead links. | The classmate clicks every link in the Evidence row of each case study. All open to the correct page (no 404). Anything unfinished is visibly labeled. | Planned |
| S4 | As Dana, I want to open the résumé, GitHub and LinkedIn so I can follow up through my usual tools. | **F4:** a "Professional materials" section, linked in the nav, with GitHub profile, LinkedIn profile, résumé (web + PDF) and "Source code for this site". | Signed out of LinkedIn and GitHub, the classmate opens each of the 4 links. Each opens **my own** profile or file, not an editor, a search result or a draft. The PDF text is selectable and its links work. | Planned |
| S5 | As Dana, I want to know how to contact Timothy and what opportunity he wants, so I know my next step. | **F5:** an intro line stating study + interest + next opportunity, and a Contact section with a professional email link and LinkedIn. No contact form. | The classmate reads only the first screen and the Contact section. They can say what role I'm looking for and how to reach me, in one sentence each. | Planned |

- **Priority (build first):** F1 + F3 for the **T-shirt** case study end to end, since it's already live. Then F4, then the Group case study, then F2/F5 polish.
- **Saved for later (not in v1):** a dark-mode toggle, plus a filter of projects by skill. I'll add these only if the reviews ask for them.
- **Inputs and data:** none from the visitor. All content is static text and links in one `projects` data file.
- **States:** a project link is either *Live* or *In progress* (labeled, not clickable as a demo). There is a 404 page with a link home.
- **Limits:** no invented metrics, employers or reviews. "FDE" is a goal, not a title. Course projects are labeled as course projects.

### Professional materials — destinations

| Item | Destination | Status |
|---|---|---|
| GitHub profile | https://github.com/Timothy-Bailey4-10 | Exists (200 OK, checked 2026-11-21). Build step: add a short bio + portfolio link, and pin the 3 repos |
| LinkedIn profile | https://www.linkedin.com/in/timothy-bailey-20250a281/ | From my résumé. Check, Planned (S4): opens signed out and shows student status + an IS117 project |
| Résumé | `/resume/` (web page) + `/resume.pdf` on this site | Updated one-page draft: [resume/Timothy-Bailey-Resume.pdf](resume/Timothy-Bailey-Resume.pdf) (no phone; built by `resume/build_resume.py`). Its portfolio link opens once the site deploys in Build |
| Contact | `mailto:tsb32@njit.edu` + LinkedIn | From my résumé. Phone number stays **off** the public site and the web résumé |
| Repo 1 — T-shirt (individual) | https://github.com/Timothy-Bailey4-10/is117-t-shirt-assignment · live: https://timothy-bailey4-10.github.io/is117-t-shirt-assignment/ | Repo and live site open (200, checked 2026-11-21) |
| Repo 2 — Group business (shared) | https://github.com/Timothy-Bailey4-10/is-117-business-research · team: Timothy Bailey (@Timothy-Bailey4-10), Cs (@cs0759) | Repo opens. Live site returned 404 on 2026-11-21. Turning on GitHub Pages so the case study can link a working demo |
| Repo 3 — Portfolio (this site) | https://github.com/Timothy-Bailey4-10/is117-portfolio-plan · live: https://timothy-bailey4-10.github.io/is117-portfolio-plan/ | Repo created and plan pushed 2026-11-21. Site deploys in Build |
| Optional extra | Career research site: https://timothy-bailey4-10.github.io/is117-ai-career-research/ | Live (200). Could be a 4th card. My private career reflection stays in Canvas only |

### Résumé plan (from my current Fall 26 draft)

The current draft has my education (B.S. Business & Information Systems, NJIT, expected May 2028), clubs, volunteering and early HTML/Python projects. To match the course résumé checklist:
- **Add** portfolio, GitHub (`github.com/Timothy-Bailey4-10`) and LinkedIn links to the header.
- **Add 2 IS117 course projects at the top of Projects**, labeled "Course project", using action + what I did + evidence:
  - *Jersey Givers T-shirt storefront | HTML, CSS, JS | Fall 2026:* built a branded storefront and live style guide, and checked it with automated browser tests (format, lint, server and Chromium/axe checks passing).
  - *Solo Software Research (group) | HTML, CSS | Fall 2026:* name my own pages and contribution, separate from my teammate's.
- **Fit to one page:** one line currently spills onto page 2. Shorten older high-school projects (combine the three 2023 HTML/CSS sites into one line) before shrinking text.
- **Tighten claims:** "increasing engagement" (social media) needs a real number or should be cut. Fix the trailing comma and capitalization in the Student Senate bullet.
- **Web version leaves out my phone number.** The PDF I send in applications can keep it.
- **Check, Planned:** the exported PDF opens, its text is selectable, every link works, and it reads on a phone.

### Brand and honest persuasion (carried forward)

- **Promise:** "A student who builds things for real users and shows his proof."
- **Character and voice:** Sage + Everyperson. Plain, direct and specific, matching the career site's "short field guide" voice.
- **Visual:** violet `#6d4aff` (text on white: **5.15:1**, passes AA). Teal `#18b4c9` is decorative only (**2.5:1, fails as text**). Teal text uses `#0e7c8b` (**4.91:1**). Font: Inter. Gradient name in the hero.

| Principle | Actual page element | How it helps the reader | Evidence or limit |
|---|---|---|---|
| Authority (earned, not claimed) | Every claim on a case study links to its proof: repo, test output or review issue, like the career site's "every number is linked" | Dana can verify instead of trusting me | No titles, certifications or metrics I don't have. "Course project" labels stay |
| Reciprocity | Each case study opens with a 3-line "30-second summary" (who, what I built, how I checked) | Saves the reader's time whether or not they contact me | Summary must match the full case study. No invented results |

---

## 2. Research how to build it

### One React idea, using my site: **declarative UI, where the view is a function of state**

**What the [React documentary](https://www.youtube.com/watch?v=8pDqJVdNa44) showed:** before React, Facebook engineers updated the page by hand. They found an element and changed it (manual DOM mutation), and the more things that could change, the easier it was for the page to get out of sync. Jordan Walke's idea flipped this around: describe what the page *should look like* for the current data, `(state) => view`, and let React re-render and work out the minimum changes. When React was shown at JSConf 2013, people were skeptical, partly because JSX mixed markup into JavaScript. That broke the "best practice" of keeping HTML and JS in separate files. The React team argued the better boundary is the **component**, not the file type. Good developer experience, tooling and gradual adoption won people over.

**Where this shows up on my site: the mobile menu button.** On a phone, the nav collapses behind a "Menu" button. That gives the page one piece of **state**: `menuOpen` is either `true` or `false`.

*Imperative (the old way):* every click handler has to remember to update **everything** by hand.
```js
button.addEventListener("click", () => {
  nav.classList.toggle("open");
  // easy to forget: screen readers need this to stay in sync
  button.setAttribute("aria-expanded", nav.classList.contains("open"));
  button.textContent = nav.classList.contains("open") ? "Close" : "Menu";
});
```

*Declarative (React):* I describe the menu for each state once. React keeps the class, the `aria-expanded` and the label in sync on every render.
```jsx
function Nav() {
  const [menuOpen, setMenuOpen] = useState(false);   // state
  return (
    <nav className={menuOpen ? "open" : ""}>         {/* view = f(state) */}
      <button aria-expanded={menuOpen} onClick={() => setMenuOpen(!menuOpen)}>
        {menuOpen ? "Close" : "Menu"}
      </button>
      <a href="#projects">Projects</a> <a href="#materials">Résumé & profiles</a>
    </nav>
  );
}
```

**Why it matters for my reader:** Dana is often on a phone (S1), and the planned keyboard and screen-reader check (section 4) needs `aria-expanded` to tell the truth. With `(state) => view`, the button can't say "closed" while the menu is open.

**The same idea with components and props:** the documentary's "component as the boundary" point is why the three project cards are one `ProjectCard` component used three times. The data goes in as props, and the card's look and logic live together:

```jsx
function ProjectCard({ title, audience, role, demoUrl, repoUrl, status }) {
  return (
    <article className="project-card">
      <p className="label">Course project</p>
      <h3>{title}</h3>
      <p>For: {audience}</p>
      <p>My role: {role}</p>
      {status === "live"
        ? <a href={demoUrl}>Live demo</a>
        : <span>Demo in progress</span>}
      <a href={repoUrl}>Repository</a>
    </article>
  );
}
// projects.js holds the 3 projects; the page maps over them:
// projects.map(p => <ProjectCard key={p.title} {...p} />)
```

If I fix the "Live demo vs In progress" rule once, all three cards follow it. That stops a dead link from slipping into one card (S3). When the group site goes live, I change one word in `projects.js` (`status: "live"`), and the view follows the data. I don't edit the HTML by hand.

*Source note:* these points summarize the documentary, drafted with help from a written summary of it (see AI use).

### Framework comparison (fit, not the most complicated option)

| Option | Fit for this site | Static build for GitHub Pages? | Verdict |
|---|---|---|---|
| **Vite + React** | Small site; uses the React idea above directly; I can build it in small steps | Yes: `vite build` → `dist/`. Set `base` to `/<REPO>/` | **Choose** |
| Next.js (static export) | More than I need (routing, server features I won't use) | Yes, with `output: 'export'`, but extra config for image and base path | Too heavy for 4–5 pages |
| VitePress (what my career site uses) | Very fast for text pages, and I already know it | Yes | Strong fallback if React slows me down. Less practice with React components |

**Libraries for specific jobs:** none needed for v1. I'll use `react-router-dom` only if case studies need their own URLs; otherwise I'll use plain `#anchors`.

**AI claim checked against official docs:**
- *Claim (from AI):* "For a GitHub Pages project site, set Vite's `base` to `'/<REPO>/'` and deploy with GitHub Actions."
- *Official source:* [Vite — Deploying a Static Site → GitHub Pages](https://vite.dev/guide/static-deploy.html#github-pages). It says: if deploying to `https://<USERNAME>.github.io/<REPO>/`, set `base` to `'/<REPO>/'`, and select **GitHub Actions** under Settings → Pages.
- *Result:* **Confirmed** (checked 2026-11-21). For this repo: `base: '/is117-portfolio-plan/'`.

---

## 3. Plan hosting and storage

- **Hosting:** GitHub Pages from this repo, deployed by a GitHub Actions workflow on push to `main` (same pattern as my career site's `deploy.yml`).
- **Check, Planned:** `npm run build` makes `dist/index.html`, and `npm run preview` shows the site with working CSS at `/is117-portfolio-plan/`.
- **Storage:** **none.** No database, no `localStorage`, no cookies, no forms. Contact is a `mailto:` link plus LinkedIn. Nothing to clear.
- **Optional research (not needed):** Vercel would also work, but GitHub Pages is required and already familiar.

## 4. Plan for mobile, accessibility and privacy

- **Phone + keyboard (Planned):** run S1–S5 on a phone-width view (390px) and with keyboard only (Tab / Enter). Every link shows a visible focus ring.
- **Contrast:** violet text 5.15:1 (pass). Teal is never used for text. Dark-teal text 4.91:1 (pass).
- **Images:** project screenshots have alt text that says what the screenshot shows ("Jersey Givers storefront hero with size buttons"), not "screenshot".
- **One visitor mistake + recovery:** the visitor taps a demo that isn't live yet. The card shows "Demo in progress" instead of a dead link. A mistyped URL lands on a 404 page with "Back to projects".
- **Permissions:** screenshots are of my own projects. Inter is SIL OFL. The T-shirt logo uses Census map data (public domain), as already recorded in that repo.
- **Privacy / data minimization:** no phone number or home address. Only my school email (tsb32@njit.edu) and LinkedIn. The site collects nothing. My private career reflection stays in Canvas, not on this public site.

## 5. Plan how people will find it and how I'll know it works

- **Page title:** `Timothy Bailey — Student builder | IS117 Portfolio`
- **Meta description:** "NJIT Business & Information Systems student (Class of 2028) building web projects for real users, aiming for software internships on AI teams. Three course projects with live demos, code and checks."
- **Link preview (Open Graph):** that title and description, with an image of the hero (name + 3 project cards), 1200×630.
- **One social post (draft):** "I built a portfolio that shows three course projects, what I personally did in each, and the checks behind them. Feedback welcome, especially from people hiring for AI-team internships: <link>"
- **After clicking:** the reader should open one case study, then the résumé or LinkedIn.
- **How I'll know it works:** a classmate runs S1–S5 while I watch without coaching. I record where they get stuck in a GitHub issue, fix it, and have them retry. No analytics in v1.

---

## Use the plan in Build

1. Create the GitHub repo, then push this plan. **Done 2026-11-21.**
2. Scaffold Vite + React. Add `ProjectCard` + `projects.js` with **real** links only (from the destinations table).
3. Build the T-shirt case study end to end (F1 + F3), then run S1 and S3 and record the results here.
4. Add Professional materials (F4), the Group case study (F2), then intro/contact (F5).
5. Deploy with GitHub Actions, then run S1–S5 on a phone and with a keyboard. Change **Planned** to **Passed** or **Failed** with the date and the reviewer.

---

## Review and decision log

Each peer issue follows this path: issue → my decision (implement / investigate / defer / decline) → linked commit or PR mentioning `(#N)` → how I checked it → reviewer retest → close, or keep open with a next step.

| Issue | Reviewer | Their point | My decision + why | Change (commit/PR) | Retest | Status |
|---|---|---|---|---|---|---|
| (issue link added when posted) | Cs (@cs0759) | Review of PLAN.md requested 2026-11-21 | Waiting for the issue | — | — | Requested |

## AI use (identified and verified)

- **What AI did:** Claude Code (Claude Opus 5.5) read my career-research, T-shirt and business repos and the IS117 guide pages, and drafted this plan. It also checked which of my links are live (2026-11-21), computed the color-contrast ratios, and checked the Vite `base` claim against Vite's docs.
- **What I verified / decided:** I kept the simulated reader (a made-up internship screener, labeled Assumption). I supplied the documentary summary and chose the declarative-UI idea for the React section. I gave my résumé as the source for my LinkedIn, email and education, and kept my phone number off the public site. I chose the repo name `is117-portfolio-plan` and pushed it myself.
- **What AI did not do:** watch the React documentary (it wrote the React section from a summary I gave it), know my teammate's full name, or get peer feedback. It took my LinkedIn, email and education from my résumé PDF.

## Change and open-issue note (for Canvas)

- **Changed:** first version of the Plan. It carries my FDE career research into a portfolio reader (internship screener), compares a projects-first and a skills-first layout, picks projects-first, and lists 5 stories with Planned checks plus all professional-material destinations.
- **Open:** peer review from Cs (requested 2026-11-21), turning on GitHub Pages for the group site, and GitHub bio and pinned repos. The updated one-page résumé draft is in `resume/`.
