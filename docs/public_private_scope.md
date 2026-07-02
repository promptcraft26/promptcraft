# Public / Private Boundary

## Publicly released
- Contract catalog and source provenance for the 219-contract candidate pool.
- Complexity scores and experiment-subset summaries.
- CSV result tables corresponding to the paper's main experiments.
- Human-evaluation rubric, blank forms, and aggregate summaries.
- Minimal public verification scripts and representative artifact samples.

## Not publicly released in this package
- Full LLM invocation backend and provider-specific orchestration.
- Private prompt-engineering assets and full production prompt library.
- API keys, real deployment configuration, and provider credentials.
- Internal batch orchestration scripts and production evaluation pipelines.
- Full row-level raw annotation release beyond a small sample sheet.

These components are withheld because they contain private engineering assets,
provider-specific operational logic, or data that would be misleading if
presented as a fully reproducible open-source backend. The artifact therefore
supports **evaluation-facing verification** rather than end-to-end public rerunning
of the private generation stack.
