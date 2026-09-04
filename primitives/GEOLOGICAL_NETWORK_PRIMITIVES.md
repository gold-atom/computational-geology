# Geological Network Primitives

**Status:** Provisional research vocabulary and candidate interfaces. None is canonized, implemented, or admitted as manufacture-resistant.

The primitives below are deliberately smaller than a token system. They describe historical evidence and operations; ownership and transfer are optional external layers.

## 1. Stratum commitment

### Purpose

Bind a source identity and bounded historical slice to a canonical content commitment.

### Candidate fields

```text
stratum-version
source-id
source-protocol-version
coordinate-start
coordinate-end
view/canonicalization-rule
content-encoding
content-root
canonical-parent-stratum-ids[]
```

These fields form the identity-bearing canonical **stratum core**. Derive

```text
stratum-id = Hash("cg/stratum" || canonical-stratum-core-without-id)
```

An identity-bearing parent list is permitted only when the source/template fixes one canonical parent rule. Otherwise lineage assertions are separate typed edges. Publisher signatures, witness attestations, archive locations, retention checks, and later availability observations likewise refer to `stratum-id` without changing it. Mutable or actor-chosen metadata must not alias the stratum or create grinding variants in downstream formation IDs.

### Potentially establishes

- later bytes can be checked against a prior digest;
- strata can name parents or boundaries; and
- independent observers can refer to the same declared slice.

### Does not establish

- that every relevant event was included;
- that the publisher did not prepare multiple roots;
- that the source order or timestamps are truthful;
- that the preimage remains available; or
- that rare structures were not manufactured before commitment.

**Pass 0 status:** useful evidentiary primitive; not geological integrity by itself.

## 2. Formation manifest

### Purpose

Turn one or more strata into a deterministic, bounded prospecting domain.

### Candidate fields

```text
formation-version
stratum-ids[]
selection-rule
boundary-rule
closure/finality-rule
missing-data-rule
semantics-bundle-id
candidate-schema-registry
availability-policy
```

Derive `formation-id` from a domain separator plus the identity-bearing canonical core—template, selected source coordinates, stratum/content roots, and pinned semantics—**without an ID field**. An ID cannot hash a representation containing itself. Closure certificates, signatures, settlement observations, archive locations, and availability checks are evolving typed records that reference this ID rather than changing it. For a public canonical source and predeclared template, the ID and body should be derivable from source history whether or not a publisher announces them; publication is evidence, not creation. For a private publisher-selected archive this independence is absent and must not be implied. A verifier needs a positive **indeterminate** state for unavailable evidence; missing history should not silently mean that no object exists.

### Main attacks

- ambiguous endpoints;
- post-hoc choice among equivalent formations;
- late roots or branch substitution;
- external-anchor reorganization;
- formation aliasing through alternate manifests; and
- later semantics interpreting the same root differently.

**Pass 0 status:** definition target. Closure remains source-relative.

### Candidate-schema registry requirement

Each registered schema needs an identity-bearing semantic core fixed before closure for prior-existence claims:

```text
eligible-formation-types
extractor and candidate grammar
canonicalization
equivalence rule
occurrence-identity rule
execution/resource semantics
test vectors
```

Derive `candidate-schema-id = Hash("cg/schema" || canonical-schema-core-without-id)`. Authorship, registration, review, and implementation locations are separate provenance records. Equivalent encodings need an alias/canonicalization rule; genuinely different schemas define separately scoped occurrence universes.

## 3. Occurrence identifier

### Purpose

Name canonical source structure before any ore class is applied.

### Candidate derivation

```text
occurrence-id = Hash(
  domain-separator
  || source-id
  || source-semantics-version
  || canonical-absolute-coordinate
  || candidate-schema-id
  || canonical-content-commitment
)
```

The coordinate/content balance matters. Identical bytes at two authenticated coordinates may be two occurrences; several windows or serializations around one coordinate may be one. The candidate schema must decide. For a strong preexistence claim, the formation template freezes the candidate universe, canonicalization, equivalence rule, and ore-independent occurrence identity before closure. If a later ore supplies those choices, it performs weak retrospective typing rather than merely classifying preexisting occurrences. Overlapping formation manifests that include one absolute occurrence must resolve to the same base ID; formation membership is separate evidence.

**Pass 0 status:** necessary for stable provenance; multiplicity rules remain open by data type.

## 4. Ore manifest

### Purpose

Publish a reproducible classifier for historical occurrences.

### Candidate fields

```text
ore-semantics-version
eligible-formation-types
candidate-schema-id
predicate-code/commitment
runtime-semantics-id
parameters
grade-rule
resource-limit/nontermination-rule
test-vectors
```

Derive `ore-id` from a domain separator and the canonical semantic core—including every validity-relevant version choice—without an ID field. Publisher release labels and presentation-only revisions are excluded: identical canonical classifier semantics retain one `ore-id`. Record when and by whom the ore was committed, revealed, or selected, what history was visible at selection time, and how many alternatives were tried as separate, evolving provenance records referencing `ore-id`. An evaluation ID may name one selection event without multiplying the base classifier identity.

An ore-qualified object identifier should bind the occurrence and ore semantic identity:

```text
object-id = Hash("cg/object" || occurrence-id || ore-id)
```

This prevents a later ore from rewriting the occurrence's identity while admitting that one occurrence may satisfy several classes. Typed IDs from distinct ore classes are contextual classifications and cannot be added together as a global inventory.

### Main attacks

- singleton whitelists and post-hoc overfitting;
- hidden parameter search;
- nondeterministic runtime behavior;
- nontermination/denial of assay;
- classifiers that read claims, discoveries, or later randomness; and
- alternative ore encodings that multiply typed IDs.

**Pass 0 status:** deterministic classification is straightforward; non-ad-hoc classification is unresolved.

## 5. Assay bundle

### Purpose

Allow a verifier to check one candidate without trusting the discoverer.

### Candidate contents

- formation and ore manifests;
- canonical occurrence coordinate;
- source evidence and content;
- inclusion/consistency/finality evidence where applicable;
- classifier execution witness or reproducible inputs;
- expected object ID and grade; and
- explicit dependencies that must be fetched independently.

### Required result states

```text
accept | reject | indeterminate
```

`indeterminate` covers missing archive data, unresolved source view, unsupported pinned semantics, or insufficient finality. Treating those as `reject` confuses observer knowledge with nonexistence.

**Pass 0 status:** implementable in toy settings; source completeness and availability remain external assumptions.

## 6. Discovery record

### Purpose

Record that an actor published an assayable witness by some registry coordinate.

### Candidate fields

```text
object-id
assay-bundle-commitment
publisher
registry-id
registry-coordinate
observed-time
signature
```

The record can support **publication priority in that registry**. It cannot prove earliest private discovery, create the object, or assign ownership.

### Main attacks

- copied witness/front-running;
- registry censorship or reordering;
- private discovery;
- conflicting clocks; and
- reorganization of the registry.

**Pass 0 status:** optional provenance primitive only.

## 7. Typed provenance graph

### Purpose

Represent relations without compressing them into a generic token history.

### Candidate edge types

```text
formed-from
located-at
classified-as
discovery-reported-by
published-by
claimed-by
witness-held-by
custody-claimed-under(rule-system)-by
owned-under(rule-system)-by
custody-transferred-under(rule-system)-to
ownership-transferred-under(rule-system)-to
reclassified-by
evidence-eroded-at
```

Every edge should name its subject type, evidence, observer/view, validity interval, and revocation or supersession semantics. `discovery-reported-by` proves only an attributed report, not first private discovery. Custody and transfer edges must name the governing rule system and whether their subject is a witness, archive, key, or recognized right. The graph may contain conflicting claims without changing occurrence existence.

**Pass 0 status:** conceptual data model; no rights system proposed.

## 8. Locality descriptor

### Purpose

Bind an object to operational historical relations rather than a decorative place name.

### Candidate structure

```text
locality-version
source-coordinate
identity-at-coordinate
topology-relation-type
topology-counterparty/set
valid-from / valid-through
relation-evidence
source-view
```

Useful relation types might include authenticated causal parentage, sponsorship at an anchored state, a committed software lineage, or a bilateral interaction witnessed by both parties. IP address, current route, self-reported label, or numeric prefix alone should not be promoted to historical proximity.

**Pass 0 status:** unresolved; Urbit offers several distinct coordinate systems but no ready-made shared-history locality.

## 9. Fault proof

### Purpose

Preserve evidence that two commitments or histories expected to agree instead diverge.

### Candidate forms

- two signed roots for one publisher/interval;
- a consistency proof failure;
- a source reorganization replacing a formation boundary;
- two semantics versions producing different assay outcomes; or
- bilateral receipts inconsistent with a published regional root.

A fault proof should invalidate or branch the affected formation, not be cosmetically added while retaining a false canonicality claim.

**Pass 0 status:** promising negative-evidence primitive.

## 10. Erosion record

### Purpose

State that some historical material or witness-generating ability has been lost while identifying what evidence survives.

```text
affected-strata/formations
last-verified-availability
missing-material
surviving-roots/proofs
which assays remain possible
which future classifications are no longer evaluable
attestation/evidence
```

Erosion records make data loss explicit; they do not restore permissionless prospecting.

**Pass 0 status:** useful honesty mechanism, not a cure for archival failure.

## 11. Composite seal

### Purpose

Bind a local formation manifest to an external history coordinate.

### Candidate derivation

```text
seal-commitment = Hash(
  "cg/composite-seal"
  || formation-manifest
  || local-root
  || source-semantics-id
  || intended-anchor-system
)
```

The external inclusion proof and chain-view/finality evidence are separate parts of the assay.

### Potentially establishes

- the commitment was published no later than an external coordinate;
- later local substitution is detectable; and
- otherwise independent publishers share a cutoff reference.

### Does not establish

- local completeness, availability, or honest construction;
- unbiased anchor fields;
- permanent external finality; or
- manufacture resistance.

**Pass 0 status:** strongest generic composite building block considered, still only an evidentiary seal.

## 12. Primitive dependency sketch

```text
history source
  → stratum commitment
  → formation manifest
  → occurrence identifier
  → ore manifest
  → assay bundle
  → optional discovery record
  → typed provenance graph
```

A composite seal can attach at the stratum or formation layer. Fault and erosion records can qualify any later layer. Nothing in this dependency chain requires or implies a currency, token, owner, or transfer system.

## 13. Admission rule

A primitive should remain labeled **proposed** until:

1. canonical encodings and semantics exist;
2. toy vectors include invalid and indeterminate cases;
3. independent implementations agree;
4. the threat-model tests are run;
5. successful counterexamples are preserved; and
6. its claim is narrowed to exactly the properties reproduced.
