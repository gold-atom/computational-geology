# Falsification Criteria

**Status:** Research Pass 0 admission framework. Passing a listed test means only that the test did not falsify the candidate under its declared model.

## 1. Required candidate dossier

No candidate should be called geological until it provides a machine-readable or mathematically precise account of:

1. source identifier and protocol version;
2. admissible history and canonical-view rule;
3. formation coordinates, boundary, and closure condition;
4. commitment and data-availability policy;
5. candidate grammar, schema commitment time, canonical serialization, equivalence, and occurrence identity;
6. ore predicate, selection family/timeline, grade rule, typed identity, and assay;
7. locality function;
8. observer, adversary, and resource models;
9. separate discovery, publication, classification, claim, custody, ownership, and transfer records, if any;
10. permissionless prospecting access, cost/rate, and erosion behavior;
11. key-version, authorization-at-coordinate, compromise, and revocation semantics;
12. upgrade and deprecation behavior; and
13. explicit claimed properties and non-claims.

A diagram or prose metaphor is not a substitute for these fields.

## 2. Fatal tests

### F1 — Discovery invariance

**Test:** define an object-source projection that erases discovery reports, publication-registry, claim, and rights records. Compare admissible histories with the same projected source material but appended, removed, reordered, duplicated, or delayed overlay records; forbid formation extraction and ore execution from reading the overlay.

**Reject if:** membership in the underlying object set changes. The mechanism is creating or allocating objects, not discovering them.

### F2 — Variant amplification

**Test:** Enumerate every byte, identity, path, event, boundary, branch, or serialization an interested participant may select. Measure success as the number of variants grows.

**Reject manufacture-resistance claim if:** cheap multiplicity amplifies success materially, including behavior approximating `1-(1-p)^k`.

### F3 — Event-volume elasticity

**Test:** Compare honest activity with adversarial event spam and Sybil activity at equal declared cost.

**Reject bounded-influence claim if:** a participant can scale inventory or target probability primarily by creating more admissible source surface.

### F4 — Withholding and frontier

**Test:** Give an actor advance knowledge of its own valid event and the option to publish, delay, or discard it. Evaluate the entire future horizon, not only the next formation.

**Reject claimed bound if:** withholding raises expected future discoveries, targets their identities, or preserves a favorable state beyond the bound.

### F5 — Selective-publication completeness

**Test:** Let a history operator commit two different subsets or private branches, each internally valid.

**Reject formation-integrity claim if:** verifiers cannot determine which is complete/canonical from evidence independent of the operator.

### F6 — View convergence

**Test:** Present honest verifiers with all admissible forks, roots, lag states, and missing-data conditions allowed by the model.

**Reject independent-object claim if:** they can permanently accept incompatible object sets without an explicit unresolved state.

### F7 — Closure challenge

**Test:** exercise reorganization, reset, branch replacement, late event admission, timestamp edge cases, and semantic upgrades after purported closure.

**Reject closure claim if:** material changes while the system continues to label the same formation closed rather than invalidating it or assigning a new, branch-qualified or superseding formation identity.

### F8 — Replay and equivalence

**Test:** replay the same occurrence across paths, desks, views, proof formats, overlapping windows, and claims under the same pinned candidate schema, ore, and semantics version; separately exercise every declared version transition.

**Reject stable-identity claim if:** more than one valid object ID is produced for one equivalence class under the same pinned version, distinct occurrences collapse unintentionally, or a version transition silently inherits identity without an explicit alias, migration, or branch relation.

### F9 — Availability / erosion

**Test:** remove full event logs, old Clay blobs, archives, indexers, or anchor transaction bodies while leaving checkpoints or roots.

**Reject permissionless-prospectability claim if:** a fresh unprivileged party cannot retrieve query-sufficient terrain and search admitted ores under the stated access and replication assumptions. Independently reject individual-verification claims when a supplied candidate lacks sufficient source/view, membership, and assay evidence.

### F10 — Locality substitution

**Test:** vary address prefix, spawning parent, current sponsor, OTA source, relay, hosting site, and observed peer relationships independently where the platform allows.

**Reject locality claim if:** the candidate silently substitutes among them or accepts a cheaply self-assigned relation as historical location.

### F11 — Classifier overfitting

**Test:** allow the ore author the same knowledge and degrees of freedom available in practice. Search for predicates that isolate chosen objects or holdings.

**Reject rarity-significance claim if:** comparable predicates routinely create equally “rare” desired results and the selection multiplicity is unreported.

### F12 — Supply enumeration

**Test:** implement the most efficient complete scan of the public finite candidate domain, with parallel indexing, precomputation, and equivalence deduplication.

**Reject strong unknown-inventory claim if:** exact membership or count is recoverable inside the claimed observer/resource bound. Reclassify as unenumerated if appropriate.

### F13 — Strategic non-discovery

**Test:** let discoverers privately inventory objects and disclose only a chosen subset.

**Reject any claim that public discovery count estimates existence count if:** strategic withholding causes material bias without an explicit sampling model.

### F14 — Rights separation

**Test:** construct cases with different discoverer, claimant, witness custodian, signing-key holder, and rule-system owner.

**Reject provenance model if:** it cannot represent all parties without contradiction or treats one relation as automatic proof of another.

### F15 — External-source influence

**Test:** give external block producers their real choices: candidate headers, transaction sets/order, timestamp range, withholding, censorship, and reorganization power. Compare manipulation cost with prospective value.

**Reject exogeneity or influence claim if:** the declared bound omits a profitable or feasible strategy.

### F16 — Composite-correlation

**Test:** correlate control of local publishers, witnesses, indexers, anchors, and classifiers rather than multiplying independent failure probabilities.

**Reject composite security calculation if:** its claimed gain disappears under plausible common control or shared incentives.

### F17 — Semantic persistence

**Test:** run historical formations under every supported source, ore, serialization, and runtime version.

**Reject deterministic-assay claim if:** results differ without a version-pinned outcome, explicit migration proof, or terminal unsupported status.

### F18 — Reduction to mining

**Test:** write the beneficiary's optimal procedure as pseudocode.

**Reject the term geological discovery if it reduces to:**

```text
repeat:
    choose or create admissible source input
    evaluate rare predicate
until success
publish successful input
```

Pricing each loop iteration changes economics, not causality.

### F19 — Source-causation / relabeling

**Test:** Remove the geological overlay and inspect native source semantics. Ask whether the alleged object is the same thing a source-native mint, issuance, upload, registration, or identity-spawn operation intentionally brings into existence.

**Reject geological label if:** the construction merely waits for an ordinary issued object ledger to close and then renames those issued objects “fossils.” Historical patterns *within* such a ledger may be separate candidates, but must have their own occurrence identities and influence analysis.

### F20 — Cross-formation and cross-ore aliasing

**Test:** wrap one source occurrence in overlapping formations; vary noncanonical stratum-parent or manifest metadata over identical material; express equivalent predicates through alternate manifests/encodings; and classify the same occurrence under many genuinely different ores.

**Reject stable-supply claim if:** wrappers or equivalent ore encodings multiply base occurrences. Never aggregate typed IDs across distinct ore classes as though they were interchangeable units.

### F21 — Candidate-schema freeze

**Test:** after closure, vary the candidate extractor, windowing, canonicalization, equivalence relation, and occurrence identity while leaving the historical bytes fixed.

**Reject prior-existence claim for schema-level occurrences if:** these later choices create or repartition the alleged base occurrences. Reclassify the result as weak retrospective typing. If equivalent schema encodings create duplicate IDs, reject stable identity; never aggregate genuinely different schema inventories as one supply.

### F22 — Ore timeline and multiple testing

**Test:** reproduce what producers and classifiers knew at every choice. Compare a predeclared ore, a credibly committed-hidden ore, an independently sampled later ore from a fixed family, and an adaptive post-hoc ore. Count all predicates and parameters tried, including unpublished failures.

**Reject manufacture-resistance or rarity-significance claim if:** it depends on hiding the actual information timeline, lets the relevant actor select a favorable predicate/history pairing, or omits multiple-testing cost.

### F23 — Closure decomposition

**Test:** challenge boundary, extension, settlement, semantic, and evidentiary closure independently. For probabilistic settlement, test the declared reversal bound `ε` over horizon `τ`. For evidentiary closure, supply a correctly committed but incomplete source subset.

**Reject unqualified closure claim if:** one kind of closure is used as proof of another, a violated finality condition leaves the formation silently labeled closed, or a publisher-selected root is treated as completeness evidence.

### F24 — Independent-source verification

**Test:** remove trust in the discoverer and archive publisher. Ask a fresh verifier to validate source membership and canonical view using only declared trust anchors and obtainable evidence.

**Reject independent-verification claim if:** same-input execution is reproducible but source evidence is only the publisher's self-attestation, or required inputs cannot be obtained under the availability policy.

### F25 — Future-dependency / oracle

**Test:** hold the closed formation and semantic ore core fixed, then vary later randomness, wall clock, mutable URLs/oracles, discovery registries, claims, and external state read during assay.

**Reject retrospective-existence claim if:** object membership changes with any input not fixed by the formation, schema, and ore. Reclassify the result as later creation, registration, or a view-relative live query.

### F26 — Permissionless prospecting

**Test:** introduce a fresh unprivileged party with no relationship to the publisher, discoverers, claimants, archives, or witness service. Require it to obtain query-sufficient terrain and run a newly admitted ore under the declared access cost and rate limits; repeat after each permitted erosion event.

**Reject permissionless-prospectability claim if:** the party can only verify a supplied witness, needs operator consent or a secret, cannot retrieve the candidate terrain, or faces access outside the stated bound.

### F27 — Key compromise and backdating

**Test:** compromise a current or retired signing key, create a valid past-looking envelope or receipt, rotate `life`/`rift`, revoke authorization, and present evidence before and after an independently witnessed publication coordinate.

**Reject historical-authorship, time, or locality claim if:** a valid signature is treated as proof that the message existed at its claimed date or was authorized at the historical coordinate without key-version lookup and temporal evidence. A signature authenticates a key/message relation, not an unqualified past event.

## 3. Cross-property impossibility checks

### Public enumerability check

If the formation is finite/public, the candidate domain enumerable, and the predicate total and decidable, exact inventory is computable eventually. A contrary claim must identify which premise fails and the cost of that failure.

### Availability–mystery check

If inventory is unknown because formation material is secret, missing, or pruned, explain how permissionless prospectors search it and how independent verifiers reject fabricated witnesses. If they cannot, the properties do not coexist.

### Post-hoc classification check

If arbitrary future predicates are permitted, there is no single future inventory. Inventory is defined per ore version at classification time. Claims of a pre-existing aggregate supply should be rejected.

### Endogenous control check

If every bit of source material is controlled by beneficiaries and there is no independently constrained admission process, strong manufacture resistance requires an explicit reason beyond hashing or signatures. Without one, presume failure.

## 4. Status vocabulary

Every evaluated property receives one status:

- **rejected:** a counterexample violates the claim under its own model;
- **inconclusive:** model, evidence, implementation, or resource bounds are missing;
- **survives stated tests:** tested attacks did not falsify it under named assumptions;
- **independently reproduced:** a separate implementation/adversarial team obtained the same result.

Avoid **secure**, **solved**, **immutable**, **unknown supply**, and **non-mintable** without the exact qualifier being evaluated.

## 5. Evidence hierarchy

From weakest to strongest:

1. attractive examples or rarity distributions;
2. deterministic test vectors;
3. adversarial simulation with declared model;
4. minimal counterexample search;
5. proof under explicit assumptions;
6. independent implementation and reproduction;
7. sustained public attack with preserved failures.

Evidence at one layer does not inherit claims from the next. A working indexer can demonstrate reproducibility while the primitive's manufacture-resistance theorem remains false.

## 6. Research Pass 0 verdict

No construction is admitted as a computational geological primitive under G1–G8, and none reaches H4. The bounded-formation example survives discovery invariance only **conditional on** a stable closed source, fixed candidate schema, and fixed ore semantics; it remains inconclusive or fails on source causation, completeness, endogenous manipulation, permissionless prospectability, availability, global view, and durable unknown-inventory claims depending on its source model.
