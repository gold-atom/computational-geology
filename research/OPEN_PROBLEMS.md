# Open Problems

**Status:** Research Pass 0. Ordered roughly by logical priority, not implementation convenience.

## Tier 1 — Questions that determine whether the field is nontrivial

### 1. Manufacture-resistant endogenous history

Can participant-generated histories expose discoverable structures while giving every participant or coalition a meaningful cumulative influence bound? The bound must include event creation, content choice, Sybils, withholding, reordering, private forks, and favorable-frontier preservation.

### 2. Verification–enumeration separation

Can one obtain cheap independent assay and expensive complete inventory enumeration over a fixed public formation without merely recreating a proof-of-work race? What hardness assumption survives specialized hardware and global parallel search?

### 3. Nontrivial post-hoc classification

Can future ore definitions remain expressive without allowing classifiers to select arbitrary desired subsets? Candidate approaches—restricted languages, description-length/multiple-testing correction, committed-hidden ores, independently sampled later ores from preregistered families, or replication standards—need formal comparison. These timelines give different existence claims: only an actual ore fixed before closure supports strong ore-relative prior existence.

### 4. Complete local-history commitment

Can a local or peer-to-peer source prove that a committed interval is complete, not merely that disclosed leaves were included, without introducing a global sequencer or universal replication?

### 5. Strong digital locality

Can locality be defined as a causal/network property resistant to cheap relabeling and migration? A useful definition must survive changing ownership, sponsorship, routing, software source, and hosting.

## Tier 2 — Formal properties

### 6. Best influence metric

Inventory count alone is inadequate. Which combination of total variation, targeted-object probability, spatial concentration, and horizon-dependent count captures geological manufacture?

### 7. Single-event to cumulative bounds

Under what conditions does a per-event influence bound compose over an adaptive lifetime? How should stateful frontiers and strategic non-events be modeled?

### 8. Canonical candidate decomposition

How should overlapping windows, nested patterns, isomorphic subgraphs, and alternative encodings be quotiented so one occurrence has one identity without suppressing legitimately distinct objects? Which candidate-schema choices must be frozen in the formation template, and how should equivalent schemas alias without creating duplicate base occurrences?

### 9. Closure under probabilistic finality

How should boundary, extension, settlement, semantic, and evidentiary closure compose? For probabilistic sources, should a formation carry a continuously updated reversal risk or become invalid after a reorganization? Can object identifiers remain stable without hiding the failure, and what quantified `ε` over horizon `τ` is meaningful?

### 10. Semantic version persistence

How can an assay pin old source/runtime semantics for decades? Is preserving code sufficient, or are compiler, virtual machine, boot state, and nondeterministic input rules also required?

### 11. Ore-family aggregation

Is there any principled aggregate notion of inventory across multiple classifications, or must every supply statement remain scoped to one ore version?

### 12. Negative evidence

Can a prospector prove a region was searched completely, or prove non-discovery, without revealing prohibitive intermediate work or trusting an indexer?

## Tier 3 — Urbit-specific questions

### 13. What is the durable Urbit substrate?

Exactly which Arvo events, Clay commits/blobs, Gall states, Ames flow records, and Azimuth/L2 inputs survive normal maintenance, `chop`, app uninstall, OTA upgrades, pier migration, and factory reset? Documentation must be checked against current Vere and Arvo implementations.

### 14. Independent reconstruction

Given a ship's published materials, can another party reconstruct a historical Clay desk or selected Gall transition without trusting a current-state export? What boot image, event epochs, blobs, entropy, and runtime versions are necessary?

### 15. Cross-ship event evidence

Do current Ames/Gall artifacts expose durable bilateral evidence of message occurrence and ordering, or would a new signed-receipt primitive be required? Ames delivery guarantees alone do not imply public historical evidence.

### 16. Region semantics

Which, if any, Urbit relation should define a region: numeric prefix, spawning provenance, sponsorship at time `t`, OTA lineage, relay relationship, or an explicit opt-in formation? Can historical membership be reconstructed independently across L1 and L2 state?

### 17. Urbit ID L2 auditability

What is the complete, current data-availability and replay story for naive-rollup batches? Can an independent new ship derive historical effective sponsorship and key state from Ethereum plus public batch data alone?

### 18. Breach-aware identity

Should pre- and post-rift history be one locality with an unconformity, two localities, or related formations? What evidence survives the reset besides external Azimuth state and third-party archives?

### 19. Desk-history publication

Can Clay expose canonical commit identities, parentage, content proofs, and availability commitments suitable for third-party assay, or is a separate export format required?

### 20. Gall assay determinism

Could a Gall agent execute ore predicates reproducibly across ships while pinning code, kernel kelvin, inputs, and resource limits? How are nontermination and version migration represented?

## Tier 4 — Composite and external-source questions

### 21. External seal design

What is the minimal external commitment needed to close an Urbit formation without importing claims about local completeness? Compare transaction commitment, header-derived schedule, and independent witness roots.

### 22. Block-producer influence

How much can miners change a candidate's count or identity through header search, coinbase/transaction choice, timestamp selection, withholding, censorship, and reorganization? Bounds must be value-sensitive.

### 23. Multi-anchor composition

When do multiple external sources reduce control, and when do they add weak-chain bribery, correlated failure, last-revealer choice, and finality mismatch?

### 24. Availability after anchoring

What replication, erasure coding, challenge sampling, or archival market is sufficient for decades of later classification? A commitment without leaves cannot support future prospecting.

## Tier 5 — Discovery and social layers

### 25. Discovery priority without ownership

Can priority be recorded fairly despite private finds, latency, censorship, and copied witnesses while remaining explicitly separate from rights?

### 26. Strategic disclosure

How should public reserve estimates account for prospectors who conceal discoveries? Is any unbiased sampling mechanism available?

### 27. Provenance through erosion and migration

What typed evidence remains valid when archives move, custodians change, formats upgrade, or only commitments survive?

### 28. Governance without semantic capture

Who may approve ore languages, source versions, or deprecated assays, and how can governance avoid retroactively privileging known discoveries?

## Immediate empirical program

1. Build tiny, fully enumerable formations and differential assay implementations.
2. Measure opportunity multiplicity under realistic Urbit event/desk controls.
3. Trace one current Urbit ship through Clay commits, Gall transitions, event epochs, `chop`, OTA, and a test reset.
4. Attempt independent reconstruction from deliberately limited artifacts.
5. Model a star “region” under every plausible relation and find the smallest divergence example.
6. Anchor a toy archive root externally, then demonstrate selective omission and data-loss failures.
7. Run an independent counterexample hunt before designing any rights, token, or economic layer.

## Assumptions requiring independent verification

- current Vere event-epoch and `chop` behavior across supported versions;
- exact persistence and garbage-collection behavior of old Clay commits and blobs;
- whether remote Clay history is durably retrievable after a publisher stops serving it;
- current Ames peer-discovery and relay roles versus documentation describing future star behavior;
- full public reconstructability of Urbit ID layer-2 state and historical batches;
- behavior of app state across uninstall, reinstall, suspension, and incompatible `+on-load` migrations;
- every proposed Bitcoin manipulation bound; and
- all claims of source independence in a composite construction.
