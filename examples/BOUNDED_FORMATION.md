# Example: Bounded Formation F

**Status:** Motivating research construction, not a protocol. It is deliberately presented with the assumptions and counterexamples that prevent canonization.

## 1. Construction

Let a source expose a canonical coordinate sequence. Before production of the relevant interval, publish a formation template:

```text
template-version
source-id
source-semantics-version
start-coordinate = a
end-coordinate = b
view/finality-rule
canonical archive encoding
commitment scheme
availability policy
candidate schemas allowed
```

For a public canonical source, the selected source material is derivable without a publisher:

```text
M_F = CanonicalEncode(source records at coordinates [a,b]).
```

After the end coordinate settles under the source rule:

1. any observer can derive `root = Commit(M_F)` from the precommitted template and canonical source;
2. a publisher may publish a formation manifest and closure evidence binding the template and root;
3. archives preserve query-sufficient `M_F` through the availability policy; and
4. verifiers mark each boundary, extension, settlement, semantic, and evidentiary closure condition separately.

Publication of the manifest or first root is not an existence event. If the source is private and an operator can choose which archive/template/root to reveal only after seeing it, this independence fails: the result is a publisher-created self-attested artifact unless additional evidence constrains the choice.

The formation ID hashes only the identity-bearing template/coordinates/content core. Closure certificates, signatures, settlement observations, archive locations, and availability checks are evolving records that reference that ID; they must not create aliases for the same terrain.

The template freezes each allowed candidate schema: extraction, canonicalization, equivalence, ore-independent occurrence identity, execution semantics, and test vectors. At any later time a researcher may publish ore manifest `O_v`, which defines a deterministic predicate and optional grading rule over one such schema. Prospectors search only the already-fixed `M_F`. A later definition that introduces its own occurrence grammar or partition is labeled weak retrospective typing instead.

The ore ID likewise hashes classifier semantics, not author or selection history. Commitment/reveal evidence, selector, review, and the number of attempted predicates are separate provenance records so the same classifier cannot be multiplied by republishing it.

For a qualifying occurrence `x`:

```text
occurrence-id = Hash(source-id || source-semantics || absolute-coordinate(x)
                     || candidate-schema || Hash(x))
object-id     = Hash("cg/object" || occurrence-id || ore-id)
```

A discovery report may publish a witness for this membership. Neither private discovery, publication, nor a claim is an input to these identifiers. A report demonstrates publication, not first discovery. If overlapping formations contain `x`, they reuse its occurrence ID and record separate formation-membership evidence; equivalent schemas must also alias canonically.

## 2. Conditional result

If:

- the source history and formation boundary are canonical;
- closure survives the stated finality model;
- `M_F` was not selectively omitted or privately substituted;
- raw material remains available;
- source and ore semantics are pinned;
- the candidate schema and multiplicity are canonical and fixed in the template; and
- `O_v` is deterministic;

then, once `O_v` is fixed, the object set is fixed. A later prospecting operation can reveal members without creating them.

This is the exact content of:

```text
closed production ≠ known inventory
```

The symbol means “closure does not logically imply that an observer has enumerated the inventory.” It does **not** mean closure guarantees unknownness.

## 3. Four timelines

### 3.1 Ore fixed before closure

```text
publish template + O → produce history → close F → prospect
```

Qualifying membership and the class definition both predate discovery. Participants may nevertheless target or grind `O` while producing history.

### 3.2 Ore fixed after closure

```text
publish template → produce history → close F → publish O → prospect
```

The schema-level substrate occurrences predate `O`; the typed class does not. This is retrospective classification or **metamorphism**, not evidence that the named ore category was socially fixed beforehand. If `O` also creates the candidate schema, only the raw substrate predates it.

### 3.3 Ore reads discovery state

```text
P(x) = “x has been claimed by time t”
```

This fails. Claim/publication now participates in object existence, collapsing geology into registration or allocation.

### 3.4 Ore adds a search nonce

```text
P(x,n) = Hash(x || n) < target, where prospector chooses n
```

This fails. The chosen nonce creates a new object-defining trial. It is mining/grinding even though `x` came from closed history.

## 4. Source instantiations

### 4.1 Idealized globally settled source

Assume a complete append-only source with one canonical view, permanent queryable data, fixed semantics, and no participant control over inputs. Under these assumptions, the formation cleanly demonstrates discovery non-creation.

The assumptions do nearly all the work and are not shown to exist in a real network.

### 4.2 Local Urbit Arvo interval

Possible coordinates are `(ship, rift, event-number)`. A ship can deterministically replay retained events into state.

Immediate failures:

- the log is controlled and stored locally;
- a ship chooses much of its input activity;
- old epochs may be chopped;
- a factory reset clears the local log and continuity;
- another observer does not automatically possess the same event sequence;
- a checkpoint or state export does not prove event completeness; and
- protocol/runtime versioning is necessary for replay.

Result: useful private terrain or self-attested archive, not a globally canonical manufacture-resistant formation.

### 4.3 Urbit Clay desk interval

A candidate external coordinate would need at least `(ship, life/rift, desk, commit-hash, path, witnessed-assignment)`. Clay's native `$beam` omits continuity, and its commit hash binds content/parents/a host-clock time but not the publishing ship, desk, revision number, author, or signature. Those contextual relations therefore need separate evidence.

Immediate failures:

- the desk owner can create commits and branches strategically;
- commit dates originate in the host clock and are not external consensus time;
- source analysis predicts that a hard recreation of an existing desk may continue the revision counter with an empty parent list, so revision intervals must not be assumed to imply uninterrupted ancestry without runtime confirmation;
- merges can import/reuse commit content under a new desk/revision context;
- resets/breaches can rebind the same `(ship, desk, revision)` namespace across continuity;
- old page bodies can be deleted while commit structure/hashes remain, and backfill depends on a reachable holder;
- remote availability depends on publishers/archives;
- a branch can be published selectively; and
- “global namespace” does not mean global replication or one canonical cross-ship history.

Result: useful content/ancestry integrity if commits, blobs, continuity, and publication context are exported and witnessed; weak intrinsic locality, completeness, availability, and manufacture resistance.

### 4.4 Bitcoin header interval

Possible coordinates are block heights on the active most-work chain after a declared burial rule.

Strengths:

- shared canonicalization and costly rewrite assumptions;
- compact, public, deterministic header material; and
- formation boundaries independent of an ordinary Urbit user's local event choices.

Limits:

- miners search many headers, choose transactions, change nonce/coinbase/Merkle root and bounded timestamps, and may withhold blocks;
- closure is probabilistic and view-dependent under reorganization/eclipsing;
- past header intervals are readily enumerable; and
- Bitcoin locality may have little semantic relation to Urbit activity.

Result: plausible exogenous historical terrain under explicit miner/finality assumptions, but not unbiased randomness or inherently unknown inventory.

### 4.5 Urbit archive sealed in Bitcoin

Commit `Hash(template || Urbit archive root || semantics)` in a Bitcoin transaction before a deadline.

Added property: later substitution of that committed archive is detectable, and Bitcoin provides an external publication coordinate after sufficient burial.

Still missing:

- proof that the Urbit archive contains all relevant events;
- proof that it was not one of many privately tried archives;
- future availability of the archive;
- a global Urbit event order;
- resistance to Bitcoin censorship/reorganization; and
- a non-ad-hoc ore-selection process.

Result: the strongest composite example in Pass 0, but only an externally sealed claim about local history.

## 5. Counterexamples

### Counterexample A — private roots

The publisher constructs `F1...Fk`, computes each root and future inventory under known ore `O`, and anchors only the favorable one. The external seal is valid. Manufacture resistance fails because eligibility among roots was not unique before outcomes were known.

### Counterexample B — complete but spammed

The publisher commits every event but can create a million zero-cost events. If every event supplies a candidate, inventory is elastic to spam. Completeness does not solve endogenous supply control.

### Counterexample C — later singleton class

After closure, a researcher chooses a predicate accepting one favored occurrence. Retrospective classification succeeds; meaningful rarity fails because arbitrary predicate search was unconstrained.

### Counterexample D — root without archive

The root remains in Bitcoin after the Urbit archive is lost. An already identified object may remain assayable only if its candidate data, ore inputs or execution witness, source/view evidence, and necessary inclusion proof survive; new ore predicates cannot search undisclosed leaves. The formation is committed but eroded.

### Counterexample E — moving region

The manifest says “all events in star S's region” but does not time-index or choose among prefix, spawning, sponsorship, OTA, or routing relations. Different honest implementations select different ships. Deterministic existence fails.

### Counterexample F — hidden discovery

One prospector fully enumerates `M_F` but publishes only two finds. Existence is fixed; public discovery count is not a statistically justified estimate of supply.

## 6. Minimal experiment

A safe next experiment would use deliberately tiny, valueless formations:

1. generate several fully known event archives;
2. publish canonical manifests and roots;
3. define one ore before closure and several after closure;
4. implement two independent enumerators/assayers;
5. verify exact inventories;
6. introduce selective roots, missing leaves, alternate encodings, reordering, and replay;
7. record `accept`, `reject`, and `indeterminate` outcomes; and
8. preserve every counterexample.

The goal is to validate semantics and disprove overclaims—not to issue an object of value.

## 7. Pass 0 verdict

The bounded formation is a coherent framework for separating historical substrate, later classification, and discovery. Its strongest general result is post-closure extension invariance under strong assumptions. It can still be a relabeled mint ledger unless the source-causation test passes, and it does not solve endogenous manufacture, completeness, durable availability, global Urbit canonicality, meaningful post-hoc classification, or unknown inventory.
