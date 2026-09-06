# The Unknown-Inventory Problem

**Status:** Research Pass 0. No construction in this repository is claimed to have proven unknown supply.

## 1. Why the phrase is dangerous

“Unknown supply” can describe ignorance, computational difficulty, data loss, view disagreement, or a class that has not yet been defined. These are not interchangeable. A useful claim must be written as:

```text
Inventory N(F,Q,O,H*) is unknown to observer i at time t,
given information I(i,t) and resource bound R(i,t),
under source and semantics assumptions A.
```

Without these parameters, unknownness is not falsifiable. A report must also distinguish three questions: whether the **cardinality** is known, whether all **member identities/localities** are known, and whether the **public discovery catalog** is complete. One may know a count without knowing the members, or know many members without knowing the count. Catalog incompleteness is a disclosure fact, not by itself unknownness of the underlying object set, and cannot satisfy the H4 central-target criterion.

## 2. Inventory is class-relative

There is no supply number for “all interesting structures in history.” For each formation `F`, candidate schema `Q`, ore definition `O`, and admissible view `H*`:

```text
N(F,Q,O,H*) = |Objects(F,Q,O,H*)|.
```

Changing the candidate schema, predicate, coordinate domain, or semantics version changes the inventory being discussed. An open-ended promise that future researchers may define new ore classes creates an open-ended family of inventories, not one hidden aggregate reserve.

## 3. Taxonomy

| Type | Meaning | Can support independent geology? | Main failure |
|---|---|---:|---|
| Unenumerated | Exact inventory is fixed and cheap enough to compute, but no complete public scan has been performed. | Yes, weakly | Unknownness may disappear immediately. |
| Resource-bounded | Exact inventory is fixed, but complete search exceeds a stated compute/time/memory budget. | Potentially | Search cost may simply be proof-of-work; parallel enumeration converges. |
| Information-limited | Observer lacks some formation material. | Disclosed-member verification may survive; permissionless prospecting does not | Search and complete-inventory claims depend on privileged data. |
| View-dependent | Observers have different admissible histories. | Not as one shared inventory | No canonical object set. |
| Predicate-open | The ore definition has not been chosen. | Only per future ore | No present inventory exists to be unknown. |
| Strategically concealed | Prospectors know objects but withhold discoveries. | Existence may survive | Discovery count is a biased lower bound. |
| Eroded | Commitments survive but searchable source data are gone. | Only for retained witnesses | Undiscovered structures are no longer prospectable. |

## 4. Eventual-enumeration theorem

Let a formation be finite and public. Let a fixed candidate schema `Q` halt with a finite occurrence list under total, decidable extraction, canonicalization, equivalence, and identity rules. Let the ore predicate and grade/assay rules be total and decidable. Then a complete algorithm can evaluate every occurrence and return the exact ore-relative inventory.

This theorem is elementary but restrictive. A construction claiming permanently unknowable reserves must give up or resource-bound at least one of:

- finite formation;
- public/query-sufficient data;
- effective candidate enumeration;
- total decidable assay; or
- feasible aggregate computation.

Giving up public data conflicts with permissionless prospecting. Giving up decidable assay conflicts with independent verification. An enormous candidate domain can preserve temporary uncertainty but must still resist user-controlled expansion and must define canonical deduplication.

## 5. Search–verification asymmetry

The most plausible technical route is an asymmetric problem:

- finding a valid witness in fixed material is expensive;
- checking one witness is cheap; and
- the searcher cannot vary the source material or ore definition.

This can yield resource-bounded undiscovered inventory. It does not automatically yield durable scarcity:

1. aggregate parallel search can eventually exhaust the domain;
2. specialized hardware may centralize discoveries;
3. if search attempts themselves alter admissible history, the mechanism becomes mining;
4. if many encodings or overlapping witnesses identify the same occurrence, apparent supply expands;
5. if negative results are not provable, nobody knows how much of the domain has been searched; and
6. attaching ownership to first publication introduces disclosure and censorship games.

Expensive search over terrain fixed under stated closure assumptions can be geological in the causal sense while resembling proof-of-work in economic behavior. The repository should report both facts.

## 6. Closed production ≠ known inventory

For a bounded formation, closure fixes source material under stated assumptions. Once an ore definition is also fixed, object membership is determined even if a scan remains incomplete.

Necessary assumptions include:

1. canonical formation coordinates and boundary;
2. a finality rule that marks later changes as failure, not silent replacement;
3. commitment to query-sufficient source material;
4. continuing availability of query-sufficient material for future prospecting; object-specific evidence is sufficient only for already identified candidates;
5. a pinned source and ore semantics version;
6. a finite or otherwise well-defined candidate grammar;
7. a candidate schema with canonical equivalence and occurrence identity fixed before closure for any strong-preexistence claim;
8. a fixed ore predicate for the inventory being discussed;
9. an explicit observer/information/resource model; and
10. no unmodeled ability to manufacture or suppress formation inputs.

These assumptions show only how closure and incomplete knowledge can coexist. They do not show that either condition holds for Urbit, Bitcoin, or a composite construction.

## 7. Later ore definitions

Suppose formation `F` closes at `t0` and ore `O` is published at `t1 > t0`.

- At `t0`, the substrate and any occurrences under a predeclared candidate schema exist.
- At `t1`, `O` defines a deterministic extension over those occurrences.
- After `t1`, prospectors may discover members of that extension.

It is defensible to say the qualifying structures are **retrospectively located in older history**. It is not defensible to say that the realized ore-relative inventory existed before `O` unless the actual `O` was fixed earlier, perhaps by a binding commitment. A predeclared family with an independently sampled post-closure `O` can reduce producer targeting, but it still yields non-adaptive retrospective classification rather than strong prior existence of that typed class. If `O` also introduces candidate extraction, equivalence, or occurrence identity, only the substrate—not that occurrence partition—predates `O`; this is weak retrospective typing.

An occurrence should therefore have an ore-independent ID, while an ore-qualified object ID should bind `(occurrence-id, ore-id)`, with all classifier version semantics already committed by `ore-id`. Formation membership is separate evidence so overlapping wrappers cannot multiply one object. Equivalent candidate schemas need canonical aliases; inventories from genuinely different schemas remain separately scoped.

## 8. Commitments after erosion

A formation root can preserve evidence that a disclosed witness belongs to a previously committed dataset. It cannot be searched without the leaves or a query-serving archive. After pruning:

- already identified objects may remain assayable if their candidate data, ore inputs or execution witness, source/view evidence, and necessary inclusion proofs are all retained;
- undiscovered objects may become impossible to prospect;
- completeness of the archive may be unknowable; and
- a later ore predicate may be impossible to evaluate.

Thus an open-ended classification program requires **query-sufficient raw history**, not merely a durable digest.

## 9. Supply statements permitted at Pass 0

Prefer bounded statements such as:

- “The object set is fixed conditional on formation closure and ore version `v`.”
- “No complete enumeration is published as of date `t`.”
- “The reference scan searched fraction `f` of the canonical candidate domain.”
- “Estimated complete-enumeration cost is `C` under benchmark `B`; this is not a hardness proof.”
- “Public discovery count is a lower bound because private discovery is possible.”
- “Historical candidates are enumerable; future outcomes remain unknown.”

Avoid:

- “the reserves are unknowable” for a finite public domain;
- “supply is unknown” when the predicate has not been fixed;
- “lost history contains undiscovered objects” when no assay can recover them; and
- extrapolating a rarity distribution into a manufacture-resistance claim.

## 10. Required falsification work

Any future unknown-inventory claim should ship with:

1. a complete reference enumerator, even if impractical at target scale;
2. toy formations whose exact inventories are known;
3. independent optimized enumeration attempts;
4. deduplication and overlap adversaries;
5. benchmarks across commodity and specialized hardware;
6. search-progress disclosure semantics;
7. private-discovery/withholding analysis; and
8. a clear statement of what event would cause the unknownness claim to expire.
