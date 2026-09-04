Computational geology studies persistent, independently verifiable objects derived from accumulated computational histories, where an object may preexist its discovery.

# Computational Geology

This repository is a falsification-first research program, not a protocol specification. It asks whether computational histories can function as **terrain** rather than merely as logs or ledgers: a historical substrate may contain structures that exist independently of the later act that finds, names, classifies, claims, or transfers them.

> **Research Pass 0 status:** terminology is provisional; constructions are test subjects; no supply, scarcity, ownership, or production-readiness claim is made.

## The core distinction

| Minting | Geology |
|---|---|
| intent → creation → object exists | history → latent structure exists → search → discovery |
| the issuance act brings the object into existence | discovery reveals an object in already-fixed terrain |
| candidate variation may be the production mechanism | cheap candidate variation is a grinding attack |

Discovery must not be used as a synonym for creation. The following relations are also separate:

```text
existence ≠ discovery ≠ classification ≠ claim ≠ custody ≠ ownership ≠ transfer
```

A history-derived identifier can exist without being known. A finder can report it without acquiring a right to it. A custodian can preserve its evidence without owning anything. A transfer system, if one is ever added, would be an application layered on top of these facts—not part of geological existence itself.

## Central research question

> Under what conditions can a computational history support non-mintable, retrospectively discoverable objects whose inventory is not known in advance?

The desired properties are individually definable but not assumed jointly achievable:

- deterministic existence;
- retrospective discovery;
- unknown or incompletely known inventory under a stated information and compute model;
- independent verification;
- resistance to intentional manufacture and grinding;
- stable identity;
- meaningful historical locality;
- bounded participant influence;
- permissionless prospecting; and
- classification introduced after the underlying history already exists.

[`THEORY.md`](THEORY.md) turns these into explicit predicates and counterfactual tests. It reserves “computational geological primitive” for a candidate that also passes a source-causation test and establishes an explicit historical manufacture bound; ordinary closed mint ledgers do not qualify. [`research/FALSIFICATION_CRITERIA.md`](research/FALSIFICATION_CRITERIA.md) states what would reject a candidate.

## Three source models

1. **Endogenous geology** derives from participant-controlled network activity. It is the hardest case: event spam, Sybils, selective publication, reordering, and state grinding can turn apparent discovery into disguised production.
2. **Exogenous geology** derives from an external history that participants in the application cannot economically control under stated assumptions—for example, a sufficiently buried Bitcoin history. External does not mean unbiased or immutable.
3. **Composite geology** commits local or network history together with an external consensus history. An external anchor may seal a commitment or order publications; it does not prove the completeness, honesty, or non-manufacture of the local material committed.

See [`models/SOURCE_MODELS.md`](models/SOURCE_MODELS.md).

## Motivating construction: a bounded formation

Consider a predeclared template that fixes a source, historical coordinate range, candidate schema, closure conditions, commitment rules, and interpretation version. After the interval closes, no additional source events are admissible under its extension rule. A later researcher may publish a deterministic ore definition `O` and search the fixed schema-level occurrences for qualifying structures. If the later ore also invents extraction, equivalence, or base identity, it is weak retrospective typing rather than strong preexistence of those occurrences.

This motivates—but does not by itself prove—the claim:

> **closed production ≠ known inventory**

The claim is meaningful only if boundary, extension, settlement, semantic, and evidentiary closure are distinguished; the relevant data remain available; candidate identity is canonical; and “unknown” is relative to a declared observer, information set, and resource bound. A commitment to a selected blob is not proof that the source interval is complete. If the finite history is public and the predicate is cheap, the inventory is merely not-yet-enumerated and may quickly become known.

The construction and its failure modes are developed in [`examples/BOUNDED_FORMATION.md`](examples/BOUNDED_FORMATION.md).

## Why Urbit is interesting—and insufficient by itself

Urbit supplies several real ingredients:

- persistent identities and cryptographic networking keys through Urbit ID/Azimuth;
- a layered address space of galaxies, stars, planets, moons, and comets, with mutable Azimuth sponsorship for permanent points and different control semantics for moons/comets;
- per-ship deterministic state transitions from a local Arvo event history;
- per-ship Clay revision DAGs with content-addressed commits, operator-controlled branches, and conditional data retention;
- persistent Gall agent state and inter-ship messaging over Ames; and
- software distribution through desks and network relationships.

It does **not** thereby supply a Bitcoin-like globally agreed, permanently archived event history. A ship's Arvo log is local; old log epochs can be deleted; a factory reset clears continuity; Clay histories are controlled by their ships; Ames orders messages within flows rather than across the whole network; sponsorship can change; and current documentation describes some Urbit ID layer-2 state as reconstructed locally from published batches rather than fully executed by Ethereum.

Accordingly, a star subtree is not automatically a geological “region.” A useful digital locality must be an explicit, time-indexed relation with evidence and causal consequences—not a decorative mapping from Urbit's hierarchy. See [`urbit/ARCHITECTURE.md`](urbit/ARCHITECTURE.md) and [`urbit/GEOLOGICAL_PRIMITIVES.md`](urbit/GEOLOGICAL_PRIMITIVES.md).

## GoldAtom relationship

[GoldAtom](https://github.com/gold-atom/goldatom) is a motivating case study, not the definition of this field. The reusable lesson is methodological: an attractive rarity distribution does not establish geological integrity when participants can select candidate bytes, grind state, withhold observations, preserve favorable frontiers, censor publication, or increase expected future discoveries.

GoldAtom/0's public repository describes a verifier-first proof-object prototype and explicitly leaves monetary issuance unresolved. GoldAtom/1 material remains non-normative research. This repository imports neither an unfinished GoldAtom construction nor a claim that GoldAtom has solved unknown supply. See [`research/GOLDATOM_RELATIONSHIP.md`](research/GOLDATOM_RELATIONSHIP.md).

## Repository map

| Path | Purpose |
|---|---|
| [`THEORY.md`](THEORY.md) | Formal model, definitions, propositions, and negative results |
| [`GLOSSARY.md`](GLOSSARY.md) | Provisional vocabulary and prohibited conflations |
| [`primitives/GEOLOGICAL_NETWORK_PRIMITIVES.md`](primitives/GEOLOGICAL_NETWORK_PRIMITIVES.md) | Candidate primitives and their evidence requirements |
| [`models/SOURCE_MODELS.md`](models/SOURCE_MODELS.md) | Endogenous, exogenous, and composite models |
| [`urbit/ARCHITECTURE.md`](urbit/ARCHITECTURE.md) | Source-grounded facts about relevant Urbit machinery |
| [`urbit/GEOLOGICAL_PRIMITIVES.md`](urbit/GEOLOGICAL_PRIMITIVES.md) | Urbit-specific candidates, attacks, and experiments |
| [`bitcoin/ANCHORS.md`](bitcoin/ANCHORS.md) | What Bitcoin anchoring can and cannot establish |
| [`research/THREAT_MODEL.md`](research/THREAT_MODEL.md) | Adversaries, capabilities, assets, and attack matrix |
| [`research/FALSIFICATION_CRITERIA.md`](research/FALSIFICATION_CRITERIA.md) | Candidate admission tests and fatal failures |
| [`research/UNKNOWN_SUPPLY.md`](research/UNKNOWN_SUPPLY.md) | Epistemic and computational meanings of unknown inventory |
| [`research/RELATED_WORK.md`](research/RELATED_WORK.md) | Boundary with logs, content addressing, archival IDs, and retrospective indexing |
| [`research/OPEN_PROBLEMS.md`](research/OPEN_PROBLEMS.md) | Strongest unresolved theoretical and empirical questions |
| [`research/GOLDATOM_RELATIONSHIP.md`](research/GOLDATOM_RELATIONSHIP.md) | Scope boundary with GoldAtom |
| [`examples/BOUNDED_FORMATION.md`](examples/BOUNDED_FORMATION.md) | Worked research construction and counterexamples |

## Research discipline

Every candidate should publish:

1. its exact source and canonicalization rule;
2. its participant-control and observer model;
3. its closure and finality assumptions;
4. its data-availability requirements;
5. its object identity and equivalence rules;
6. its ore predicate and assay algorithm;
7. counterfactual influence measurements, not just rarity histograms;
8. attacks that failed and attacks that succeeded; and
9. a status of **rejected**, **inconclusive**, or **survives stated tests**—never “secure” by default.

Negative results are first-class outputs. If a construction reduces to “hash user-controlled events until something rare appears,” it is mining or grinding, not geological discovery.

## Primary technical sources

The Urbit analysis relies primarily on the official documentation and source repositories for [Arvo](https://docs.urbit.org/urbit-os/kernel/arvo), [Clay](https://docs.urbit.org/urbit-os/kernel/clay/architecture), [Ames](https://docs.urbit.org/urbit-os/kernel/ames), [Urbit ID](https://docs.urbit.org/urbit-id/what-is-urbit-id), and [Azimuth](https://github.com/urbit/azimuth). Bitcoin claims are bounded by the [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf), the [Bitcoin developer block-header reference](https://developer.bitcoin.org/reference/block_chain.html), and Bitcoin Core behavior. Commitment/log comparisons use [RFC 9162 Certificate Transparency](https://www.rfc-editor.org/rfc/rfc9162.html), which is instructive precisely because an append-only Merkle commitment still requires consistency, monitoring, and availability assumptions.
