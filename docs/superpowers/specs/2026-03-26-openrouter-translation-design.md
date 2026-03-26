# OpenRouter Daily Chinese Translation Design

Date: 2026-03-26

## Context

This repository tracks daily arXiv papers related to speech, audio, and music. The current repository already stores per-day paper JSON files under `papers/YYYY-MM-DD/` and publishes a daily `README.md`.

The user-approved goal is to extend the daily GitHub Actions workflow so that each day's paper abstracts are translated into Chinese by calling OpenRouter with the model `stepfun/step-3.5-flash:free`, then committed back to the repository automatically.

## User-Approved Decisions

- Run automatically in GitHub Actions every day.
- Skip per-paper translation failures and continue processing the rest of the day.
- Store Chinese abstracts in each paper JSON as `summary_zh`.
- Show only Chinese abstracts in daily `README.md`.
- Keep the English original in JSON and do not show it in `README.md`.

## Goals

- Preserve the current daily archive layout under `papers/YYYY-MM-DD/`.
- Add a reliable translation stage that can be rerun independently from paper fetching.
- Keep partial progress when OpenRouter free-tier calls fail or rate-limit.
- Generate a readable daily `README.md` that prefers Chinese summaries.
- Avoid mixing fetch logic, translation logic, and render logic in one step.

## Non-Goals

- No full-title translation requirement in this change.
- No retry-until-success workflow that blocks the daily commit.
- No historical backfill for old dates in the initial implementation.
- No dependence on nonstandard local tooling such as `openclaw`.

## Recommended Architecture

Use a three-stage daily pipeline:

1. Fetch
   Fetch and filter new arXiv papers, then write normalized English JSON files to `papers/YYYY-MM-DD/`.
2. Translate
   Iterate through the day's JSON files and call OpenRouter for each paper's abstract. On success, write `summary_zh` and translation metadata back to that paper JSON. On failure, log and continue.
3. Render
   Generate `papers/YYYY-MM-DD/README.md`, refresh the root `README.md`, and update `papers/latest` to the newest date.

This architecture keeps translation failures isolated from the fetch stage and makes rendering repeatable without re-fetching or re-translating.

## Component Responsibilities

### `arxiv_monitor.py`

- Remains the fetch entry point.
- Responsible for fetching papers, applying category and keyword filtering, and writing the base JSON schema.
- Should not own translation or Markdown rendering logic after the change.

### `translate_papers.py`

- Becomes the OpenRouter translation stage.
- Reads one day directory, finds paper JSON files, and translates abstracts one paper at a time.
- Adds `summary_zh`, `translation_model`, and `translation_updated_at` when translation succeeds.
- Leaves papers untouched when translation fails.

### `render_daily.py`

- New module focused only on Markdown and index generation.
- Builds the daily `README.md` from the day's JSON files.
- Updates the root `README.md` summary table.
- Refreshes `papers/latest` to point to the latest date directory.

## Data Model

Each paper JSON should preserve the current core fields:

- `id`
- `title`
- `authors`
- `summary`
- `published`
- `link`
- `pdf`
- `category`
- `fetched_at`

Add these translation fields:

- `summary_zh`: translated Chinese abstract
- `translation_model`: `stepfun/step-3.5-flash:free`
- `translation_updated_at`: ISO timestamp for the last successful translation update

If translation fails, `summary_zh` should be absent or empty. Error messages should not be stored in `summary_zh`.

## OpenRouter Integration

The translation stage will call OpenRouter's chat completions endpoint with:

- Base URL: `https://openrouter.ai/api/v1/chat/completions`
- Model: `stepfun/step-3.5-flash:free`
- Auth: `Authorization: Bearer ${OPENROUTER_API_KEY}`

Prompting should be constrained to translation-only behavior:

- Input: English abstract and optionally the title for context
- Output: Chinese abstract only
- No explanations, no Markdown wrappers, no extra labels

The implementation should set explicit request timeouts and treat malformed responses as per-paper failures.

## Failure Handling

The approved failure policy is per-paper tolerance:

- Network failures, timeouts, 429 responses, and 5xx responses affect only the current paper.
- The job continues with the next paper.
- The day still renders and commits even if some papers are untranslated.
- The daily `README.md` shows a short placeholder for untranslated papers, for example: `中文摘要翻译失败，请查看原文 JSON。`

This keeps the daily archive usable even when the free model is unstable.

## GitHub Actions Changes

The workflow should run these steps in order:

1. Install Python dependencies
2. `python arxiv_monitor.py`
3. `python translate_papers.py today`
4. `python render_daily.py today`
5. Commit and push changes if the worktree changed

Required repository secret:

- `OPENROUTER_API_KEY`

The workflow must not fail the entire day solely because a subset of translations failed.

## Testing Strategy

Implementation should start with tests that verify:

- Successful translation writes `summary_zh` and translation metadata into JSON.
- Translation failure for one paper does not stop translation of the next paper.
- The OpenRouter request uses `stepfun/step-3.5-flash:free`.
- Rendering prefers `summary_zh` in the daily `README.md`.
- Rendering falls back to a placeholder message when `summary_zh` is missing.

Tests should avoid live network calls by stubbing the HTTP request layer.

## Risks And Mitigations

### Free-tier instability

Risk:
OpenRouter free models may return intermittent failures or rate limits.

Mitigation:
Per-paper error handling, explicit timeouts, and render-time fallback copy.

### Schema drift across old and new data

Risk:
Older JSON files do not all have the same field shapes.

Mitigation:
Keep renderer defensive and limit the new translation stage to the target date directory only.

### Existing script drift

Risk:
The current repository output format has already diverged from some code paths in `arxiv_monitor.py`.

Mitigation:
Avoid expanding those mixed responsibilities further. Keep fetch, translate, and render clearly separated.

## Rollout

The initial rollout should target only the daily automated pipeline for new dates. Historical backfill can be a separate utility later if needed.
