# Open Science Toolbox
---

## Agenda

**Today we are going to create a reproducible software & data project.**

When we say “reproducibility” we are going to focus on:
- Can someone else run your code and get the same result?
- Can you rerun it six months later and understand what you did?
- Reproducibility requires:
    - Transparent data sources
    - Stable software/programming environments

---
## Project Overview

“It is hotter in Sacramento, CA in 2024 than it was in previous years.”

1. Find available data (that we may use)
2. Write reproducible analytical code
3. Track code with Git
4. Upload code to GitHub
5. Verify cross platform reproducibility via GitHub Actions

---
## Finding Public Datasets

**Look for datasets with:**
- Clear licensing (e.g. CC0, CC-BY)
- Documentation: README, schema, units
- Credible source (govt, research lab, public registry)
- A DOI

**Examples:**
- zenodo.org → Search by keyword or community
- data.gov → Filter by format and update date

---

### Data Red Flags

- No stated license
- Missing metadata
- No data provenance
- XLSX/HTML formats without consistent structure
- "Download link expired" or private files
- Clear bias or conflict of interest 
      (e.g. for-profit institution promoting a dataset whose results benefit their interests)

---

## Software & Data Licensing

*By licensing your code, data, and other materials you enable others to interact with your work.*

Additional Resources
- [OSS Licensing for Researchers & Educators](https://gw-ospo.github.io/oss-licensing/intro.html)

---

### Software License Types

**Open-source Permissive Licenses**
- Grants users broad freedoms to use, modify, and distribute the licensed software.
    - [MIT](http://choosealicense.com/licenses/mit/)
    - [BSD](https://opensource.org/license/bsd-3-clause)
    - [Apache](https://choosealicense.com/licenses/apache-2.0/)

**Open-source Copyleft Licenses**
- Modifications/Derivations of the original work must be shared under the same license. “Share-alike”
    - [GNU General Public License (GPL)](https://choosealicense.com/licenses/gpl-3.0/)
    - [Mozilla Public License (MPL)](https://choosealicense.com/licenses/mpl-2.0/)

**Proprietary Licenses**
- Most restrictive, often only allows the use of software with no rights to modify or redistribute.

---
### Data & Other media License Types

*Creative Commons Licenses are often preferred due*

These licenses do not have statments about source code distribution and therefore are not fit for software.
    - [Can I apply a Creative Commons license to software?](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software)
**Creative Commons License Clauses**
BY: credit must be given to the creator.
SA: Adaptations must be shared under the same terms.
NC: Only noncommercial uses of the work are permitted.
SA: Adaptations must be shared under the same terms.
ND: No derivatives or adaptations of the work are permitted.

**Creative Commons Licenses**
1. CC BY
2. CC BY-SA
3. CC BY-NC
4. CC BY-NC-SA
5. CC BY-ND
6. CC BY-NC-ND
7.  CC0 (aka CC Zero)

https://creativecommons.org/share-your-work/cclicenses/

---
### What License(s) Do I Choose?

- Software           → https://opensource.org/licenses; https://choosealicense.com/
- Data & Other media → https://creativecommons.org/chooser/

---

## Transparent & Reproducible Code

### Why Use Programming At All?
- Transparency
- Repetition & Automation
- Scalability

**The Commandline**: a tool as flexible as the research you do
- You might process genomic data today and scrape web archives tomorrow.
- Tools change rapidly, but data still needs to be moved, cleaned, and transformed.
- The command line gives you:
    - A universal interface to almost anything: Python, R, LaTeX, image processing, simulations, etc.
    - Scripting power for automating tedious tasks and chaining tools together.
    - Cross-platform compatibility: works on macOS, Linux, Windows (via WSL or Git Bash).
    - Learning it pays off across projects, disciplines, and even careers.

---
### How to write “reproducible” software

Specify/capture the environment
- pixi
- Docker/Podman

Cross-platform Languages
- Python, R, Rust over platform-dependent shell scrpts
    - If you do rely on shell scripts, package them with Docker

Verify your code runs start → end and produces the expected results/artifacts

This idea favors script-based workflows over [Jupyter](https://jupyter.org/) notebook-based workflows.
> "In a sample of 936 published notebooks that would be executable in
> principle, we found that 73% of them would not be reproducible with
> straightforward approaches, requiring humans to infer (and often guess) the
> order in which the authors created the cells."
[Assessing and restoring reproducibility of Jupyter notebooks](https://dl.acm.org/doi/abs/10.1145/3324884.3416585)

However to enhance the reproducibility of your jupyter notebooks you can:
1. Use [`jupyter --execute …`](https://docs.jupyter.org/en/latest/running.html#using-a-command-line-interface)
2. Save a markdown copy of the notebook (for accessibility; [Jupytext](https://jupytext.readthedocs.io/en/latest/))

**[Marimo](https://marimo.io/) has overcome many of the above**

Dont Forget to:
- Document your work! (create a README)
- License your work (create a LICENSE)
- Receive a DOI by uploading a working snapshot to an archive repository (create or update your CITATION.cff)

---
### Version Control (Git)

**Nouns**
- Repository ⇒ A computer folder that is under version control
- Commit     ⇒ A “snapshot” of a given repository

**Basic Verbs/Commands**
- init     ⇒ “Begin tracking this folder with version control.”
- status   ⇒ “Do I have pending changes not part of a snapshot?”
- add      ⇒ “In my next snapshot, I want to incorporate these files.”
- restore  ⇒ “Undo pending changes for some file(s).”
- commit   ⇒ “Create a snapshot of the files I have ‘added’.”
- log      ⇒ “View the timeline of all snapshots.”
- checkout ⇒ “Go to a specific snapshot.”

---
### Sharing Code
- Upload to GitHub
- Add a software license (LICENSE)
- Document your code (README)
    - what it does
    - how to install it
    - how to use it
- Make it citeable (Zenodo & CITATION.cff)

---
### Automated CI

Use [GitHub Actions](https://github.com/features/actions) to test your software on different platforms
- ubuntu-latest, windows-latest, macos-latest

You will need to balance these workflows:
- Actions should finish within a few minutes
- Actions should not exceed ~10 GB of storage

Meaning, you may need to operate on a subset of data or provide other shortcuts to your computations
- Pixi (GH Action) https://github.com/marketplace/actions/setup-pixi

### Upload a Snapshot

Use any archive service (like [Zenodo](https://zenodo.org) 
