# Theory of Computational Geology

**Status:** Research Pass 0. Definitions are provisional and intended to be attacked. This document specifies a research problem, not a protocol, asset, or supply claim.

## 1. Claim discipline

Computational geology is not the observation that historical bytes can be hashed. It is the stronger possibility that a sufficiently fixed computational history can support objects for which:

1. the source material predates the act of finding the object;
2. finding, announcing, or claiming the object does not cause it to exist;
3. independent parties can determine whether the same object exists;
4. object identity remains stable across observations;
5. the source's participants cannot cheaply manufacture additional qualifying objects; and
6. any statement that inventory is unknown names the observer, information, time, and computational bound under which it is unknown.

The word **geology** is therefore a hypothesis about causal structure, not an aesthetic label for rare hashes.

## 2. System model

### 2.1 History source

A history source is modeled provisionally as

```text
S = (E, V, K, ≺, A, Π)
```

where:

- `E` is a domain of possible events or records;
- `V` is a validity relation for events and histories;
- `K` is a canonicalization or view-selection rule;
- `≺` is the source's ordering relation, which may be total or partial;
- `A` is an availability model for records and witnesses; and
- `Π` is the versioned interpretation semantics.

At observation time `t`, observer `i` has a view `H(i,t)`. Two observers need not have the same view. A candidate must state what evidence makes a view **admissible**, when two views are considered equivalent, and what finality or stabilization assumption permits a researcher to write `H*` for the history used by an assay.

This notation does not assume a blockchain. A local event log, a revision DAG, a transparency log, a collection of signed transcripts, and a proof-of-work chain have different `K`, `A`, and adversary models.

### 2.2 Historical coordinates

A coordinate is a canonical reference into a history: for example, `(source-id, block-height, transaction-index)`, `(ship, event-number)`, or `(ship, desk, commit-id, path)`. A coordinate is meaningful only if its referent and interpretation are stable under the stated source model.

Human-readable timestamps are not automatically coordinates. If participants can move timestamps within an acceptance window, then time-based locality inherits that discretion.

### 2.3 Formation template, realization, and closure

A **formation template** fixes the selection rule before the source interval is realized:

```text
φ = (source-id, domain-rule, boundary-rule, view-rule, semantics,
     candidate-schema-registry, availability-policy)
```

For source history `H`, it determines material `Mφ(H)`. The identity-bearing realized formation core is

```text
Fφ(H) = (φ, canonical-source-coordinates, content-commitment)
```

Its identifier is derived from that canonical core without an embedded ID field. Closure certificates, settlement observations, signatures, archive locations, and availability checks are evolving, observer-relative typed records that reference the formation ID; they do not participate in it. For a public canonical source, `Fφ(H)` is derivable whether or not anyone publishes a manifest or discovers an object. Publication adds evidence and availability; it does not create the formation. If an operator chooses the interval, archive, or template after seeing outcomes, that choice is part of the adversary strategy. A private archive for which only its operator can choose and publish a root is merely a publisher-created, self-attested artifact until independent evidence establishes a stronger source relation. Write `Material(F,H*)` for the canonical records selected by realized formation `F` from admissible view `H*`; when `F = Fφ(H*)`, this is `Mφ(H*)`.

The word **closure** hides several distinct claims:

1. **boundary closure:** the coordinate-selection rule has reached its fixed endpoint;
2. **extension closure:** no source-valid record can later be inserted into or removed from that coordinate domain;
3. **settlement closure:** the probability that the selected canonical view changes is at most a declared `ε` over horizon `τ`, under a stated adversary and observer model;
4. **semantic closure:** source, extraction, and serialization semantics are pinned rather than silently upgraded; and
5. **evidentiary closure:** a commitment binds a named publisher or source view to particular bytes.

A candidate must say which sense it means. A formation called closed is invalidated—not still “closed” under a revocable label—if its declared extension, settlement, or semantic condition fails. Evidentiary closure alone neither proves that a selected blob is the complete source interval nor prevents the publisher from having prepared alternatives. Availability is an independent continuing property, not a consequence of closure.

### 2.4 Candidate schema and ore definition

A **candidate schema** is a versioned deterministic occurrence grammar:

```text
Q = (formation-domain, extractor, canonicalization, equivalence-rule,
     occurrence-identity, execution-semantics, test-vectors)
```

Derive `schema-id` from a domain separator and canonical `Q` without an embedded ID field. It determines which source structures are candidate occurrences and when two witnesses refer to the same occurrence. For **prior existence of schema-level occurrences**, `Q` must be fixed in `φ` before closure. A later definition that introduces its own extractor, partition, equivalence rule, or occurrence identity creates a new way of typing old substrate; this repository calls that **weak retrospective typing**, not proof that those particular occurrences preexisted their schema.

An **ore definition** has an identity-bearing semantic core: a versioned deterministic classifier over one fixed schema.

```text
O = (eligible-formation-types, schema-id, predicate, parameters,
     grade-rule, assay-procedure, runtime-semantics, resource-rule,
     test-vectors)
```

For a fixed schema, `P_O(x, M)` accepts or rejects occurrences and the optional grade rule describes accepted instances. An ore definition is incomplete if it leaves any validity-relevant choice to the prospector or verifier: parameters, traversal order, tie breaking, missing-data behavior, runtime version, resource limits, or test-vector interpretation. The ore identifier is derived from this canonical semantic core without an embedded ID field. Author, commitment/reveal time, selector, selection distribution, trial count, and review history are typed provenance records referring to `ore-id`; they evolve and must not alias an identical classifier. If an application needs to name one selection event, it uses a separate evaluation ID.

### 2.5 Occurrence identity, object set, and inventory

An occurrence identifier should be based on an absolute authenticated source coordinate and canonical occurrence content under fixed schema `Q`, not on whichever formation or ore happens to include it:

```text
OccurrenceID(x) = Hash(source-id || source-semantics-version
                       || canonical-source-coordinate(x)
                       || candidate-schema-id || canonical-content(x))
```

If two overlapping formations contain the same canonical occurrence, they must not manufacture two base occurrences merely by wrapping it twice. Formation membership is a relation attached to the occurrence. Branch identity belongs in the source coordinate when the source is not yet canonical. Because the schema ID participates in identity, equivalent schema encodings also require an alias/canonicalization rule; inventories from genuinely different schemas are scoped separately and cannot be added as one supply.

For fixed `F`, `Q`, `O`, and admissible `H*`, define

```text
Objects(F,Q,O,H*) = {
  TypedID_O(OccurrenceID([x]~Q), ore-id)
  : x ∈ Extract_Q(Material(F,H*)) and P_O(x, Material(F,H*))
}
```

where `[x]~Q` is the schema-level equivalence class of candidate `x`. The inventory comprises this member set and its cardinality; write the inventory size as

```text
N(F,Q,O,H*) = |Objects(F,Q,O,H*)|.
```

This set exists mathematically once the formation, ore definition, and admissible view are fixed, whether or not anyone has enumerated it. That statement alone says nothing about scarcity, economic value, manufacture resistance, ownership, or whether `N` is hard to calculate. Typed IDs from different ore definitions or equivalent formation wrappers must never be summed as one global supply.

### 2.6 Discovery, publication, and assay

A **discovery** is an observer-relative epistemic event: observer `i` obtains a candidate and sufficient evidence to make an assay accept. A private discovery need leave no public trace and its actual first time is generally unverifiable.

A **discovery report** is a publication record

```text
R = (formation-id, ore-id, object-id, witness, assay-evidence, reporter, publication-coordinate)
```

such that the assay accepts the witness for the object under `F`, `Q`, and `O`. The report proves publication under the registry's assumptions, not first discovery. A discovery or report changes knowledge and perhaps a registry; neither may change `Objects(F,Q,O,H*)`.

An **assay** is a deterministic decision procedure over a candidate, witness, formation descriptor, ore definition, and admissible source evidence. Reproducibility means honest verifiers with the same inputs agree. **Independent verification** additionally means a verifier need not trust the discoverer for those inputs: it validates source membership and the selected view using enumerated trust anchors and obtains sufficient evidence under the stated availability model. A publisher's signature over its own private archive is self-attestation, not independent verification. Independence does not imply that every verifier stores the full archive.

### 2.7 Claims, custody, ownership, and transfer

These are relations external to existence:

- `Claim(c,o,t)`: claimant `c` asserts a relation to object `o` at time `t`.
- `Custody(c,w,t)`: custodian `c` controls a witness, archive, or key associated with `o`.
- `Own(c,o,t,R)`: rule system `R` recognizes `c` as owner of `o`.
- `Transfer(c1,c2,x,t,R)`: `R` changes recognized ownership, control, or custody of named subject `x`—such as an object right, witness, archive, or key.

None follows from `o ∈ Objects(F,Q,O,H*)`. A “first discoverer owns it” rule would be an additional allocation protocol with latency, censorship, reorganization, and strategic non-discovery problems.

## 3. Prerequisites and the central definition

G1–G6 below define a **retrospectively indexed historical object**. They are prerequisites, not enough to earn the word geological: an NFT mint ledger, issuance log, or user-upload service could otherwise be closed and indexed after the fact.

### G1 — Historical precedence

The formation material on which an object depends is fixed before the object-defining prospecting computation begins. Reporting may occur later and private discovery may never be reported.

### G2 — Discovery non-creation

Define a source projection `πsrc` that erases discovery reports, publication registries, claims, and rights-layer events. For any two admissible histories with the same object-source projection but different appended, removed, delayed, duplicated, or reordered overlay records, the formation projection and `Objects` set are identical. Formation extraction and ore predicates are forbidden to read those overlay records. This test is substantive even when a registry shares storage with the source; it is not satisfied merely by holding all history fixed by definition.

### G3 — Reproducible deterministic assay

All validity-relevant encodings, rules, and evidence are fixed enough that honest verifiers given the same inputs agree.

### G4 — Stable identity

Equivalent witnesses resolve to one identifier; replay, alternative serialization, overlapping windows, or proof format changes do not multiply one underlying structure.

### G5 — Historical locality

The object's coordinates refer to authenticated relations that exist under source semantics independently of the geological overlay. The relation must materially constrain historical admission, causation, observation, participant control, or availability. A freely chosen label does not qualify, and making an assay branch on a signed label cannot bootstrap locality.

### G6 — Independently obtainable durable evidence

The material required to assay source membership and the selected view remains obtainable without trusting the discoverer, or a sufficient proof system makes validation possible without the raw material under explicitly enumerated trust anchors. Missing history cannot be counted as “unknown reserves” while claiming permissionless prospectability; object-specific proofs may preserve independent verification only for the candidates they cover.

### G7 — Source-causal separability

The alleged geological object is not merely a source-native issued object renamed after the fact. Remove the geological classifier, discovery registry, and rights layer from the model. The source occurrence and its native historical relations must still exist, and no native operation may define that same alleged object as being brought into existence by an issuance/mint/upload action.

This does not prohibit studying patterns inside mint ledgers. Naming a pattern occurrence as distinct from the natively minted token is necessary, but it is not sufficient. After fixing the ore and information timeline, the beneficiary's prospecting computation must operate on source material whose closure is independent of that search. If its object-targeting procedure is:

```text
choose or create admissible source input → evaluate predicate
→ discard/withhold on failure → repeat until success → publish
```

then the candidate fails G7 as production, mining, or grinding regardless of how costly each iteration is. A candidate that survives this causal test must still face G8's residual participant-control bound.

### G8 — Historical manufacture bound

Under an explicit adversary, coalition, budget, security parameter, probability, information timeline, ore-selection process, and horizon model, participant interventions before closure remain below a stated nontrivial threshold or scaling law `ε(B,λ,τ)` for object count and targeted outcomes. Every finite formation has some vacuous finite bound; that is not resistance. The threshold must be justified relative to the claimed use and compared with honest baseline variation. Merely pricing an issuance action or fixing the history afterward does not satisfy this condition.

**Definition.** This repository reserves **computational geological primitive** for a candidate satisfying G1–G8 under stated assumptions and reproduced tests. G1–G7 without G8 may be called a **geological candidate** or **retrospective historical object**, never manufacture-resistant geology.

No construction in Research Pass 0 satisfies G8.

### The stronger central-target conjunction

G1–G8 define the base manufacture-bounded geological construction. The project's central question asks whether two further properties can coexist with that base:

**GP — Permissionless prospectability.** During a declared availability interval, a fresh unprivileged party can obtain query-sufficient formation material and run any admitted ore under public rules without consent from the formation publisher, prior discoverers, claimants, or a privileged witness service. The property names access costs, rate assumptions, and the behavior after erosion.

**U — Falsifiable inventory uncertainty.** A statement `U(F,Q,O,H*,d,i,t,I,R,A)` binds the formation, schema, ore, and admissible view, then identifies an actual object-set dimension `d` (cardinality or at least one member identity/locality), observer or observer class `i`, time `t`, available information `I`, resource bound `R`, and assumptions `A`. It also states a challenge procedure and expiry condition. Incomplete public discovery catalogs are separate disclosure-state claims and cannot satisfy `U`; otherwise one hidden report would trivialize the central question. Predicate openness, missing data, and disagreement are not silently substituted for resource-bounded uncertainty.

A **central-target construction** is a G1–G8 construction that additionally demonstrates GP and one nontrivial, independently tested `U` claim. No candidate in Research Pass 0 does so. Keeping GP and `U` explicit allows a base geological construction to be studied without pretending that every such construction has unknown inventory.

## 4. Non-mintability and influence

### 4.1 Two meanings that must not be conflated

1. **Discovery non-creation:** the act of prospecting or claiming does not change the object set. This is G2 and can be achieved even on participant-controlled history.
2. **Historical non-manufacturability:** before closure, participants cannot cheaply alter the source history to increase or target the eventual object set. This is much stronger.

A construction may satisfy the first while failing the second completely.

This repository reserves unqualified **non-mintable** for a construction that also establishes G7 and a nontrivial G8 bound. The weaker property should be called discovery-independent or post-closure invariant.

### 4.2 Intervention and information model

Let actor or coalition `a` have capability budget `B` and adaptive strategy `σ`. Capabilities can include adding valid events, creating identities, choosing encodings, reordering, censoring, withholding, publishing one of several histories, manipulating timestamps, selecting a template or boundary, or influencing an external anchor.

Let `H⁰` be a baseline random history process and `Hᵃ` the process under intervention. Keep a predeclared formation template `φ` fixed, then compare the different realizations it induces; holding a realized descriptor and content root fixed while varying history would be ill-defined. Write

```text
Z(φ,Q,O,H) = Objects(Fφ(H), Q, O, K(H))

Δcount(a,B) = supσ | E[|Z(φ,Q,O,Hᵃ)|] - E[|Z(φ,Q,O,H⁰)|] |

Δtarget(a,B,T) = supσ |
  Pr[Z(φ,Q,O,Hᵃ) intersects T]
  - Pr[Z(φ,Q,O,H⁰) intersects T]
|
```

and measure a distributional distance over object identities and localities. `T` may be a set valuable to the attacker. If the actor is allowed to choose among templates, boundaries, realizations, or roots, those choices move inside `σ`; the experiment must not quietly condition on the favorable one that was published. A small change in total count can conceal near-total control over which objects exist.

An adversary model also needs an information filtration `I_t`: what the actor knows before each admissible choice. At least four ore timelines differ:

1. **predeclared ore:** producers know `O` while producing history and can target it;
2. **committed-hidden ore:** `O` is credibly committed before production and revealed after closure, limiting targeting only if secrecy and binding hold;
3. **independently sampled later ore:** an unpredictable process chooses `O` after closure from a predeclared family; and
4. **adaptive post-hoc ore:** a classifier sees the realized history and then chooses `O`, enabling predicate search and multiple-testing bias.

These are not interchangeable. If arbitrary future ore definitions are permitted and an actor can cheaply choose between two distinguishable admissible histories, no universal endogenous manufacture-resistance claim can hold: some later predicate can distinguish the controlled difference. A bounded claim must therefore quantify over a fixed ore, a predeclared family and selection distribution, or an explicit complexity/multiple-testing model.

Every bound must name:

- the probability space;
- baseline behavior;
- coalition and capabilities;
- economic or computational budget;
- adaptive information available at each choice;
- candidate-schema and ore commitment/reveal times;
- who chooses the ore and from what family;
- time horizon;
- single-event and cumulative effects; and
- whether withholding preserves a favorable state or frontier into future periods.

No such general bound is established in Research Pass 0.

### 4.3 Reduction-to-grinding test

Suppose a participant can produce `k` independently varying admissible candidates before publication, each passing a rare predicate with probability `p`, and publish a passing candidate if one exists. Its effective success probability is

```text
1 - (1-p)^k.
```

As `k` grows, apparent rarity disappears. If the construction's practical algorithm is “vary participant-controlled events until a qualifying hash appears,” the construction is mining or grinding. Calling the events strata does not change its causal structure.

Fees, rate limits, or identity costs may price the grinding but do not convert creation into discovery. They belong in the influence model.

## 5. Unknown inventory

“Unknown supply” is not a single property. At time `t`, inventory may be:

1. **Unenumerated:** fixed and cheaply computable, but nobody has completed or published the scan.
2. **Computationally hidden:** fixed, but enumeration exceeds a declared feasible compute budget while individual assays remain cheaper.
3. **Information-limited:** some source material is unavailable to the observer.
4. **View-dependent:** observers disagree on the history or interpretation.
5. **Predicate-open:** future researchers have not yet chosen which ore definitions to apply.

Only the first two plausibly coexist with both independent verification **and permissionless prospecting over query-sufficient public material**. Information-limited systems may independently verify disclosed members through commitments or proofs, but they do not provide permissionless search or a complete-inventory claim. View divergence is a defect unless the primitive explicitly studies observer-relative artifacts. Predicate openness means there is no single inventory to count; it must not be advertised as mysterious fixed supply.

### Enumerability lemma

Assume:

1. `F` is finite and completely public;
2. `O` is fixed;
3. `Extract_Q(M)` is finite and efficiently enumerable;
4. `P_O`, equivalence, and identity are efficiently computable; and
5. no secret witness is required.

Then `Objects(F,Q,O,H*)` and `N(F,Q,O,H*)` are efficiently enumerable up to the size of the candidate domain.

**Consequence:** strong, durable inventory uncertainty cannot be obtained merely by hashing a public finite history. It requires a very large search space, asymmetric discovery evidence, unavailable information, an open-ended candidate domain, or some other added assumption. Each option creates a corresponding verification, manufacture, or availability problem.

This is not a proof that computational geology is impossible. It is a requirement to say exactly which kind of uncertainty is being claimed and what pays for it.

See [`research/UNKNOWN_SUPPLY.md`](research/UNKNOWN_SUPPLY.md).

## 6. Closed production does not imply known inventory

### Proposition (conditional)

Let template `φ` have a fixed candidate schema `Q`, let its realization `Fφ(H*)` satisfy declared boundary, extension, settlement, and semantic closure conditions, and let `O` be deterministic and versioned. If the extracted material is stable, then `Objects(Fφ(H*),Q,O,H*)` is fixed when `O` is fixed, even if no observer has enumerated it.

### Proof sketch

The fixed template and closure assumptions fix the admissible material and schema-level occurrence set. A deterministic predicate and typed identity rule therefore map those occurrences to one fixed ore-relative set. Discovery evaluates or reveals membership; it does not add elements. Whether any observer knows the complete set is an epistemic and computational question.

### What the proposition does not show

- that the formation was honestly or completely recorded before closure;
- that participants could not grind its contents;
- that the finality assumption will hold;
- that the committed material remains available;
- that the ore definition existed before the history or was selected without post-hoc bias;
- that enumeration is difficult;
- that later protocol semantics will preserve the interpretation; or
- that any object has an owner or value.

If `O` is introduced after closure, the **substrate** clearly predates the classification. Whether an ore-relative object “already existed” before its class was defined requires separating these cases:

- **weak retrospective existence:** once `O` is fixed, its extension is determined entirely by older material;
- **strong ore-relative prior existence:** the candidate schema and the actual `O` (possibly committed but hidden) were fixed before closure, so the typed membership rule already existed;
- **non-adaptive retrospective classification:** `Q` was fixed before closure and a later unpredictable process selected `O` from a predeclared family; this limits producer targeting but the realized typed class was not fixed earlier; and
- **adaptive retrospective classification:** a classifier selected `O` after inspecting the realized formation, so both multiple testing and economic selection must be counted.

Retrospective readings support later scientific classification of old substrate. If the later classifier also supplies the candidate schema, only the raw substrate—not the occurrence partition—predates classification. Strong ore-relative prior existence requires both the schema and actual ore to be fixed before closure. Research must state which reading it uses.

## 7. Classification and metamorphism

Later classification can reveal real properties of older history, but unrestricted post-hoc classifiers can manufacture arbitrary rarity. After observing `M`, a classifier can define “ore” as exactly one favored coordinate, or create one singleton class per record. Those classes are deterministic and retrospective but provide no ex ante scarcity evidence.

Therefore a post-closure ore definition should be evaluated along at least four axes:

1. **Descriptive legitimacy:** does it express a compressible structural relation rather than enumerate desired answers?
2. **Complexity:** how many degrees of freedom were chosen after inspecting the formation?
3. **Robustness:** does the property survive small, non-adversarial changes in encoding or boundaries?
4. **Economic neutrality:** did classifiers or claimants have incentives to choose a predicate that privileges known holdings?

Possible controls include a restricted ore language, complexity penalties, multiple-testing correction, preregistered ore families, independently sampled predicates, independent replication, and a quarantine period between classification and any rights system. These controls govern recognition; they do not make the underlying history less manipulable.

## 8. Source-model taxonomy

### 8.1 Endogenous geology

`Material(F,H*)` is produced by the same participants who may benefit from its objects. Examples include application events, messages, local state transitions, or identities created inside the candidate network.

The default presumption is manipulability. A candidate must address event spam, Sybils, choice of event contents, timing, reordering, selective publication, private forks, and history deletion. Determinism after publication is insufficient.

### 8.2 Exogenous geology

The formation is derived from a history outside the application's direct control. Exogeneity is economic and adversarial, not categorical: Bitcoin miners can vary headers, choose transactions and timestamps within rules, withhold blocks, censor commitments, and participate in the application. The question is whether manipulating the geological predicate costs enough, under explicit assumptions, to bound influence.

### 8.3 Composite geology

The formation commits local/network material to an external history. A composite can add:

- external ordering and a public cutoff;
- tamper evidence after commitment;
- shared reference points across otherwise local histories; and
- a way to compare independently published commitments.

It does not automatically add:

- completeness of the committed local history;
- truth of local timestamps or claimed authorship;
- resistance to pre-commitment grinding;
- availability of preimages;
- one global view of unanchored events; or
- ownership.

Composite constructions are useful exactly when these gains and non-gains are separated.

## 9. Locality

Digital locality is not physical distance and should not be accepted merely because a system has a tree-shaped namespace. A locality function

```text
L(o) -> authenticated coordinates and relations
```

is meaningful only when the relation exists under source semantics without the geology overlay and changing it changes at least one of:

- which historical events causally contributed to `o`;
- which parties could observe, produce, route, or witness the material;
- which source commitments authenticate it;
- which availability/finality assumptions apply.

Assay behavior may test these consequences, but cannot create locality merely by branching on an authenticated, time-indexed, or expensive label.

Locality should generally be time-indexed. Membership in a star's sponsorship subtree, a software-update lineage, or a peer relationship can change. A static label that can be cheaply copied is **synthetic locality** and fails G5.

## 10. Negative results preserved at Pass 0

1. **Rare hash ≠ geological integrity.** A rarity histogram says nothing about participant influence.
2. **Commitment ≠ complete history.** A root binds disclosed bytes but does not prove omitted events never occurred.
3. **Determinism ≠ consensus.** Two parties can deterministically process different valid-looking inputs.
4. **Persistence ≠ archival permanence.** A state machine can preserve current state while pruning the events needed for historical prospecting.
5. **Unknown because lost ≠ unknown reserve.** Data unavailability defeats permissionless prospectability even when a retained object-specific witness can still support individual verification.
6. **Hierarchy ≠ locality.** Address prefixes or sponsorship labels matter only if authenticated, time-indexed, and causally relevant.
7. **Later classification ≠ prior scarcity.** Predicate freedom can create arbitrary rare classes after the fact.
8. **First discovery ≠ ownership.** Adding that rule creates an allocation race and strategic disclosure incentives.
9. **External anchoring ≠ unbiased randomness.** Block producers retain bounded but real selection, withholding, ordering, and censorship powers.
10. **A per-event bound ≠ a lifetime bound.** Small recurrent influence can accumulate or preserve advantageous state across formations.

## 11. Evaluation levels

To prevent architecture from outrunning evidence, candidates may be described at one of five non-normative, cumulative levels: reaching a higher level entails every lower level.

| Level | Minimum claim |
|---|---|
| `H0 — historical pattern` | A deterministic predicate finds structures in recorded history. |
| `H1 — retrospective object` | G1–G6 survive stated tests; this may still be a relabeled issuance log. |
| `H2 — geological candidate` | G7 also survives; source-native creation is not being renamed as discovery. |
| `H3 — manufacture-bounded geological primitive` | G8 has an explicit, independently reproduced single-event and cumulative influence bound. |
| `H4 — central-target construction` | H3 plus GP permissionless prospectability and a nontrivial reproduced `U(F,Q,O,H*,d,i,t,I,R,A)` inventory-uncertainty claim. |

No candidate in this repository is assigned H3 or H4 in Research Pass 0.

## 12. Research workflow

The preferred loop is:

```text
define source → define object → generate candidate → attack controls
→ search for counterexample → measure influence → revise or reject
```

Distributional beauty, evocative terminology, and working software come after the causal and adversarial model. A failed construction remains documented with the smallest counterexample that kills it.
