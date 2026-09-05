# Candidate Geological Primitives on Urbit

**Status:** Research Pass 0. This document separates existing Urbit behavior from additions proposed for experiments and from speculation. It defines no protocol, asset, token, ownership rule, or production deployment.

No candidate in this document establishes a G8 historical-manufacture bound, Bitcoin-like global consensus for Urbit history, or an unknown inventory. At most, the candidates identify historical material that could be closed and assayed under explicit archive, witness, source-view, and version assumptions. See [`THEORY.md`](../THEORY.md) for G1–G8, GP/U, and the H0–H4 evaluation levels.

## 1. Evidence discipline

The labels below are normative for this document:

- **Existing** means behavior documented or implemented by the cited Urbit, Azimuth, or Bitcoin source.
- **Proposed** means machinery this repository suggests constructing or testing. Urbit does not currently provide the resulting guarantee.
- **Speculative** means a research direction whose feasibility or value has not been established.

An existing substrate plus a proposed commitment does not inherit properties that neither component supplies. In particular:

```text
deterministic local replay != global consensus
content address             != authenticated authorship or locality
external timestamp          != complete local history
two signatures              != non-manufacturability
closed finite archive       != unknown inventory
```

## 2. Candidate matrix

| Candidate formation or evidence | Existing substrate | Proposed addition | Strongest defensible Pass 0 target | Decisive limitation |
|---|---|---|---|---|
| Externally witnessed Clay formation | per-ship desks, commit DAGs, content-addressed pages | canonical export, contextual envelope, independent archive, closure receipts | H1 retrospective object; possibly H2 only for source-distinct patterns | desk operator chooses history, branches, dates, and publication; witnesses do not prove completeness |
| Archived Arvo event interval or epoch | deterministic per-ship event/state transition, totally ordered local log | event-range manifest, full archive, replay semantics, external closure evidence | H1 for replayable event patterns; case-specific G7 test | operator controls admitted inputs, can retain alternatives or reset, and ordinary maintenance can remove epochs |
| Bilaterally receipted interaction formation | identity-aware peer messaging and per-flow order | application-level canonical receipts signed by both parties and archived | H1 target; H2 only if a later pattern also passes G7 | receipt creation is intentional; peers can collude, spam, grind, refuse, or publish selectively |
| Time-indexed Azimuth sponsorship formation | Ethereum records plus Urbit's L1/L2 identity semantics | pinned replay manifest and active-chain/finality rule | H0 target; H2 only after satisfying H1 and G7 for a separately defined pattern | native spawn is creation; topology actions are strategic; L2 interpretation and roller behavior must be pinned |
| Urbit archive with a Bitcoin commitment | local archive root plus Bitcoin transaction inclusion | canonical manifest, inclusion proof, reorganization policy, retained preimage | probabilistically settled public commitment coordinate | Bitcoin proves neither local completeness nor availability and does not remove pre-anchor grinding |
| Fault, unconformity, and erosion evidence | rifts, event ranges, Clay ancestry, commitments, archive status | typed discontinuity records with positive evidence | provenance and invalid/indeterminate assay states | a missing response is not proof of a historical gap; markers do not create scarcity |

These are not H3 or H4 constructions. Labels such as “formation” in this table name research candidates, not admitted computational geological primitives.

For source-model purposes, the body of a Clay or Arvo formation remains **endogenous** even when an outside witness signs its root; the evidence package then becomes composite, not exogenous terrain. Bilateral transcripts are multi-party endogenous history unless an external source is incorporated. Azimuth topology history combines participant-selected identity actions with Ethereum ordering and Urbit-side interpretation, so the proposed formation is composite. An Urbit root in Bitcoin is also composite. Discontinuity markers inherit the model of the evidence they describe.

## 3. Locality must be a typed, time-indexed relation

### 3.1 Candidate locality record

**Proposed.** A useful Urbit locality record would have a form such as:

```text
urbit-locality-version
relation-type
source-id and admissible source view
subject identity at the coordinate
counterparty, parent, sponsor, or contributor set
valid-from / valid-through
rift and, where key-sensitive, life
source-local coordinate
evidence commitment
interpretation versions
```

The `relation-type` is mandatory. “Near star S” is otherwise ambiguous among a numeric prefix, spawning provenance, effective sponsorship, OTA source, network route, or shared committed activity.

Candidate relations have different strengths:

| Relation | What exists today | What it can mean | What it cannot mean by itself |
|---|---|---|---|
| `prefix-of` | deterministic Urbit point arithmetic | stable syntactic region of the point namespace | shared activity, sponsorship, routing, or common history |
| `spawned-by` | Azimuth activation history | provenance of an intentional identity-creation event | non-mintability or current sponsorship |
| `sponsored-by-at` | effective sponsor under pinned L1/L2 Azimuth state | topology membership at one interpreted chain view | permanent membership, shared ship data, or current OTA source |
| `event-of` | retained Arvo history for one pier/continuity | local causal and ordinal location | a globally ordered Urbit event |
| `published-on-desk` | local mapping from ship/desk/revision to commit | contextual publication if separately exported and authenticated | a property intrinsic to the Clay commit hash |
| `interacted-with` | application events at one or both peers | shared history only with durable evidence from both sides | a public transcript or global network observation |

Locality is useful only if the relation exists under Urbit/source semantics independently of the geological overlay and materially changes historical admission, causation, producer/observer control, or availability assumptions. Assay behavior alone cannot turn a freely copied label into locality. Current IP address, NAT path, relay route, or self-report is not durable historical locality. Current sponsorship must not be projected backward over prior states.

### 3.2 Why a Clay commit hash has no intrinsic ship locality

**Existing.** A finalized Clay `$yaki` contains a parent-hash list, a map from paths to content hashes, its commit hash, and a date. Current `+make-yaki` derives the digest from the parents, content map, and date. Ship, desk, aeon/revision number, author, and signature are absent from that hash input. See the pinned [`$tako` and `$yaki` types](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/data-types.md#L1018-L1026) and [`$yaki` fields](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/data-types.md#L1145-L1160), together with pinned [`+make-yaki`](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/lull.hoon#L2749-L2757).

The date is the local Arvo event time. Arvo's formal interface receives current time with each input, and its state records `now` as current event time; this is deterministic replay input, not an independently agreed timestamp. See the pinned [Arvo formal interface](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/README.md#L179-L188) and [state fields](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/README.md#L381-L385).

**Consequence.** A bare `$tako` can identify content/ancestry/date structure under pinned hash semantics, but it cannot prove “authored by ship P on desk D at revision R.” That claim needs a separately authenticated envelope and evidence for the contextual mapping. Clay's “global” namespace is addressability and caching, not a signature over that envelope or a global commit selection rule.

Commit reuse across contexts is supported behavior rather than merely a theoretical collision. Clay's `%init` merge strategy assigns a source commit to a destination desk, and `%fine` may assign the next destination revision number to an existing source commit. See the pinned [merge strategies](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/using.md#L50-L80). This is useful content sharing, but it confirms that desk membership and revision number are external relations to `$tako`.

## 4. Exported and externally witnessed Clay formation

### 4.1 Construction sketch

**Existing.** Clay gives each ship independently controlled desks, commit parentage, numbered revisions, and content-addressed pages. Commit histories can be merged and foreign desks can be fetched or cached. It does not make one branch globally canonical.

**Proposed.** Before production begins, publish a formation template that fixes:

```text
source-context       = (ship, desk, rift, source/version identifiers)
domain               = an ancestry-checked commit range or explicit commit set
content              = every yaki plus every required lobe/page preimage
context-map          = aeon -> tako for the declared interval
semantics            = Clay/Arvo/kernel/kelvin and canonical serialization
candidate-schemas    = extraction/equivalence/occurrence identity fixed pre-interval
closure-coordinate   = a non-Clay witness or external anchor rule
availability-policy  = named independent archives and failure behavior
equivocation-rule    = conflicting envelopes for one interval are fault evidence
```

At closure, the publisher emits an authenticated envelope binding the context and a canonical archive root. Independent witnesses fetch the full body, verify the declared map and ancestry, recompute hashes, and retain both body and envelope. A witness receipt means only “this witness received and checked these bytes by this coordinate under this procedure.”

Future ore manifests may classify canonical structures under those fixed schemas. A later ore that invents its own extractor or occurrence partition is only weak retrospective typing. Discovery records remain outside the formation so that adding one cannot change its occurrence set.

### 4.2 What the addition could establish

Under an explicit signer/witness trust model, the construction can provide:

- stable reference to one disclosed Clay history and its required blobs;
- detectable post-closure mutation relative to the signed root;
- reproducible assays on retained bytes and pinned semantics;
- contextual locality to the declared ship/desk only through the envelope; and
- detectable publisher equivocation if conflicting signed envelopes become visible to a common auditor.

It does **not** show that the disclosed branch was the only privately prepared branch, that every relevant action entered Clay, or that the publisher's event time was truthful. A threshold of witnesses improves availability only under assumptions about independence, retention, and retrieval.

### 4.3 Ancestry is not implied by an aeon interval

**Status qualification.** The cited generator/helper/revision paths are existing code. The resulting empty-parent commit at the next numbered revision is a source-grounded prediction that still requires the runtime experiment in §12 E2; it is not reported here as reproduced behavior.

The current `|new-desk` generator can overwrite an existing desk with `=hard &`. It passes no parent to Clay's `%park` operation, while the ordinary commit path assigns the next `let.dom` revision. The source therefore predicts a later numbered revision whose commit has an empty parent list. See pinned [`|new-desk`](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/gen/hood/clay/new-desk.hoon#L11-L27), the [`new-desk:cloy` helper](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/zuse.hoon#L4451-L4459), and Clay's [revision increment](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L1870-L1888).

**Consequence.** A descriptor such as “revisions 20 through 40” must not infer that every later numbered commit descends from every earlier one. The assay must inspect the exported `aeon -> tako` map and parent DAG, then reject or mark an explicit unconformity when the template requires continuous ancestry.

### 4.4 Erosion and manipulation limits

**Existing.** Clay exposes tombstoning of old revision data; `%all` may tombstone material not used by current desk revisions. See the pinned [tombstone task](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/tasks.md#L351-L388).

**Failure modes.** The desk operator can:

- create event or file variants before committing;
- choose a favorable branch, parent structure, path encoding, or commit time;
- keep private branches and publish only one;
- generate many desks or identities;
- sign different roots for separated witnesses;
- omit application history that never entered the exported desk; or
- stop serving blobs after a commitment.

External witnesses can make some later alteration or equivocation detectable. They do not supply G8 or source completeness. If the ore search is finite, public, and efficiently enumerable, this construction also supplies no durable unknown-inventory property.

## 5. Archived Arvo event-interval formation

### 5.1 Construction sketch

**Existing.** One ship's event log is a totally ordered sequence and its state is a pure function of that sequence. Current Vere stores portions in epoch files, usually beginning new epochs around runtime upgrades. The `chop` utility deletes epochs older than the newest two, making replay from the beginning impossible. See the pinned [Vere event-log and epoch description](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/running/vere.md#L139-L159). Arvo documentation separately permits snapshots followed by deletion of old log material ([pinned source](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/README.md#L86-L96)).

**Proposed.** Export a bounded event range together with:

- the ship and rift to which the events belong;
- exact start/end event ordinals and epoch-file boundaries;
- boot/checkpoint state needed to replay the range;
- every event noun and time/entropy input required by the pinned transition;
- runtime, kernel, vane, jet, and upgrade semantics sufficient for reproduction;
- a terminal state commitment and independent closure receipt; and
- archive replicas with an explicit retrieval test.

An epoch file boundary is an operational storage boundary, not a protocol finality rule. Formation closure must be defined separately.

### 5.2 Defensible and indefensible claims

With a complete archive and exact semantics, two researchers may be able to replay the disclosed range and test later predicates over its events or derived states. This is stronger terrain than a current-state snapshot for classifiers not anticipated when the snapshot was made.

It remains a local, endogenous history. The operator controls many admitted inputs and may maintain alternative piers, withhold events, delay publication, manipulate local-time inputs, or reset continuity. A factory reset clears the ship's event log and increments the relevant continuity context; `@p` alone cannot name a continuous historical locality. See [life and rift](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/life-and-rift.md#L16-L42) and the [factory-reset behavior](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/id/guide-to-resets.md#L16-L49).

A snapshot that preserves current state but not the old events cannot support arbitrary later event-level ore definitions. Calling the missing events “unknown reserves” would contradict permissionless prospectability, even if a retained object-specific witness can still support individual verification.

## 6. Bilaterally receipted interaction formation

### 6.1 Construction sketch

**Existing.** Legacy Ames semantics provide only-once delivery to the destination vane and total order within a flow. Order across flows is unspecified, and the guarantees do not survive a breach. These are delivery properties, not durable, third-party-verifiable receipts. See the pinned [Ames guarantees](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/ames/README.md#L42-L60) and [flow ordering](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/ames/README.md#L158-L179).

Release [`408k`](https://github.com/urbit/urbit/releases/tag/408k) incorporated Mesa/directed messaging from the associated [implementation change](https://github.com/urbit/urbit/pull/7208), but its note described a staged/manual first rollout. The later [`408k-1`](https://github.com/urbit/urbit/releases/tag/408k-1) note says it does nothing for ships already on 408, and [`408k-2`](https://github.com/urbit/urbit/releases/tag/408k-2) records further Mesa fixes without proving network-wide activation. Transport heterogeneity is therefore an empirical concern. The proposed transcript must pin applicable networking semantics and obtain evidence at the application layer rather than assume every peer or release exposes legacy Ames behavior.

**Proposed.** Two application agents could maintain a hash-chained transcript in which each receipt commits to:

```text
receipt-version
both @p identities and relevant rift/life values
application and transcript identifiers
prior mutually accepted receipt
local sequence coordinates at both peers
canonical application-event digest
both parties' independently verifiable signatures
semantics and close rule
```

Each party and at least one independent archive would retain the receipt bodies. The transcript would state an explicit partial order; it must not derive a global order from unrelated Ames flows. Closure might require both parties' signatures over one terminal root plus a predetermined deadline or external coordinate.

### 6.2 Causal classification

The receipt is intentionally created by the parties. It is evidentiary stratum material, not itself a retrospectively discovered fossil. A candidate geological object would instead be a source-distinct pattern over a transcript already closed before its ore definition or discovery. That pattern must still pass G7 and G8 independently.

If at least one party honestly signs one transcript and preserves it, later unilateral rewriting can be detected relative to that transcript. This does not show that all interactions were recorded, that either party signed promptly, or that private alternative interactions never occurred.

### 6.3 Attacks

- Both parties can collude to generate many candidate interactions or transcripts.
- One party can refuse to sign an unfavorable event or terminal root.
- The pair can keep multiple private chains and selectively publish.
- Sybil counterparties turn “bilateral” into unilateral control at low cost unless identity control is bounded.
- Concurrent Ames flows supply no canonical cross-flow order.
- A breach separates continuity; replay across it must fail or become an explicit new segment.
- Public-key signatures, key-version lookup, canonical encoding, and archival availability are new requirements, not inherited from packet acknowledgement.

This candidate can authenticate evidence of a bilateral historical relation more meaningful than a numeric prefix, but the receipt does not create that locality and the construction has no manufacture-resistance result.

## 7. Time-indexed Azimuth sponsorship formation

### 7.1 Existing topology and interpretation

**Existing.** Azimuth point spawning checks authority and unused state. Direct spawn activates and assigns the point; indirect spawn records allocation/holder state but deliberately leaves activation for later. Both paths are intentional allocation/creation operations, not geological discovery. See pinned [`spawn`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Ecliptic.sol#L360-L460).

Sponsorship may change through escape, adoption, and detachment. More importantly, Urbit ID's naive-rollup documentation states that L2 batches are published to Ethereum but interpreted by `/lib/naive.hoon` on each ship; Ethereum does not execute those L2 state transitions. The L1 sponsor can permanently differ from the effective L2-aware sponsor. See the pinned [L1/L2 process](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/l2/README.md#L32-L58) and [Azimuth state distinction](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/l2/README.md#L95-L117).

### 7.2 Construction sketch

**Proposed.** A topology formation could bind:

```text
Ethereum network/genesis and active-chain view
start/end block coordinates and finality/reorganization policy
Azimuth contract addresses and code versions
complete relevant L1 logs and L2 batch bytes
exact naive.hoon and bytestring semantics
event ordering and invalid-batch behavior
effective sponsorship graph at each declared state
archive and independent replay requirements
```

Locality could then mean `sponsored-by-at(point, sponsor, interpreted-state-coordinate)`. It must include the source view and L2 semantics, not only an Ethereum contract query or a present-day sponsor.

### 7.3 Limits

An individual spawned point fails G7 if it is simply renamed a fossil: direct spawn intentionally allocates and activates a point, while indirect spawn intentionally records its allocation and holder without activating it. An individual sponsorship edge is likewise a native intentional state transition. A later pattern across already fixed topology history may begin at H0 and can reach H2 only after satisfying H1 plus G7; it needs its own occurrence identity, equivalence rule, and causal analysis.

Urbit participants can strategically spawn eligible points, escape, adopt, detach, transact through controlled identities, or coordinate with rollers. Rollers choose which submitted L2 transactions to batch and when to publish. A finite, public block interval with a fixed, effectively enumerable candidate schema and total decidable predicate is enumerable. This construction therefore provides authenticated, time-indexed topology under stated chain and interpreter assumptions—not unknown supply or G8.

### 7.4 Star regions

**Speculative.** A predetermined set such as “all points effectively sponsored by star S at interpreted state Q” could scope contributors to another formation. This is more precise than “S's region,” but the membership itself is strategic and time-varying. It does not show that members share data, routing, software, economic conditions, or a common history.

An opt-in formation jointly committed by those members would be a new multi-party primitive. Its threshold, admission, completeness, Sybil, withholding, and liveness assumptions would require separate analysis. Urbit's hierarchy does not supply those guarantees automatically.

### 7.5 Moons and comets are large identity-variation surfaces

**Existing.** Official documentation says each planet has `2^32` moon coordinates, and a moon's public key is maintained by its parent rather than Azimuth. The parent generates and can change the moon's networking keys. See the pinned [address-space description](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/hoon-school/C-azimuth.md#L28-L36) and [moon key custody](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/cryptography.md#L30-L44). Moon identity samples therefore cannot be treated as independent scarce participants when one parent can generate a very large family.

Current Vere documentation describes comets as quickly generated by anyone, virtually unlimited, and free. The cryptography documentation describes comet generation as guessing a private key whose public-key-derived `@p` matches an allowed star suffix—a search process that is itself an obvious grinding surface. See [booting a comet](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/running/vere.md#L32-L44) and [comet key generation](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/cryptography.md#L36-L48).

The same pinned documentation tree is internally inconsistent about exact comet cardinality and sponsorship language: one overview says `2^64` free identities with no sponsorship, while Hoon School describes the upper 128-bit address space and star selection from a sponsor list. Compare [What is Urbit ID?](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/what-is-urbit-id.md#L22-L32) with [Hoon School's comet section](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/hoon-school/C-azimuth.md#L117-L129). A construction depending on those exact semantics must pin and test deployed code instead of choosing favorable prose.

**Consequence.** Any rarity, voting weight, witness threshold, locality claim, or event quota that counts moons or comets as one-independent-identity-per-sample fails by default. It needs a controller-equivalence rule and a measured generation-cost/control model; otherwise moon/comet multiplication converts apparent network diversity into one actor's search budget.

## 8. Urbit archive with a Bitcoin commitment

### 8.1 Construction sketch

**Proposed.** Compute a canonical root over one of the archive formats above and publish a formation-manifest commitment in a Bitcoin transaction. The manifest must fix the Bitcoin network, serialization, transaction/block coordinate, active-chain rule, minimum burial or cumulative-work condition, behavior on reorganization, and off-chain archive policy.

A sufficiently buried inclusion can then serve as a public, probabilistically settled “no later than this chain coordinate” commitment under Bitcoin's security assumptions. See [`bitcoin/ANCHORS.md`](../bitcoin/ANCHORS.md) and the primary [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf).

### 8.2 What is and is not gained

The Bitcoin record can make substitution of a different local root after inclusion detectable and can order included commitments in a widely verified external history. It cannot establish:

- completeness or truth of the Urbit archive;
- an accurate date for internal Clay or Arvo events;
- uniqueness of the publisher's pre-anchor candidate archive;
- absence of other anchored or unanchored roots;
- availability of the committed preimage;
- object-specific proof-of-work; or
- resistance to local event grinding, selective publication, or witness collusion.

Bitcoin producers also choose transaction inclusion/order and manipulate valid header candidate fields within protocol bounds. Reorganizations and stale/eclipsed views require explicit invalid, branch-qualified, or reclose behavior. The [Bitcoin block-header reference](https://developer.bitcoin.org/reference/block_chain.html#block-headers) documents miner-controlled header fields and timestamp bounds.

**Conclusion.** This is a composite commitment construction. Bitcoin contributes an external canonicalization and replacement-cost assumption for the commitment record; it does not turn the committed Urbit preimage into exogenous history.

## 9. Faults, unconformities, erosion, and later classification

These terms remain hypotheses. The useful distinction is evidentiary, not metaphorical.

| Candidate marker | Positive evidence required | Proposed assay consequence |
|---|---|---|
| **fault** | incompatible signed roots for one declared interval; branch replacement; or conflicting source views beyond the view rule | preserve both claims, reject closure, or branch-qualify identities |
| **unconformity** | an ancestry break, rift boundary, missing required ordinal range, or declared semantic discontinuity | split the formation or mark the coordinate outside the continuous domain |
| **erosion** | a valid commitment remains but required event/page preimages fail the stated archive-retrieval policy | return `indeterminate`, not “no object” or “unknown reserve” |
| **intrusion** | an externally authenticated record is incorporated into the formation | apply the external source's separate view/finality assumptions |
| **metamorphism** | a new ore version classifies old fixed occurrences without changing their IDs or formation | add a typed classification; do not rewrite occurrence existence |

**Existing indicators** include Azimuth `rift` increments, retained Clay parent structure, event ordinals, and surviving content commitments. **Proposed markers** interpret those indicators under a formation manifest. A rift proves a recorded continuity transition under its source view; it does not reconstruct the erased pier. A missing Clay query or absent witness response is not by itself proof that bytes never existed.

The hard-desk case is a concrete unconformity candidate: if the exported aeon map shows a later root commit with no ancestry to the prior head, a continuous-ancestry formation must not silently bridge it. Tombstoned content under a surviving `$tako` is a concrete erosion candidate if no declared archive can supply the preimage.

## 10. Gall and desks are tools, not trust transitions

### 10.1 What exists

Gall agents are persistent local state machines managed inside Arvo. Most application state is not ordinarily stored as Clay revision history. On upgrade, an agent's `+on-save` exports state and the new `+on-load` may migrate it. See the pinned [Gall overview](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/app-school/README.md#L22-L32), [where application data live](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/app-school/1-arvo.md#L63-L71), and the [upgrade lifecycle](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/app-school/4-lifecycle.md#L18-L32).

Clay desks can distribute agent source, marks, libraries, manifests, and test vectors. Installing from a publishing desk does not make that desk's data or code globally canonical.

### 10.2 What could be built

**Proposed experimental roles:**

- a formation recorder that exports canonical event or Clay material;
- a witness agent that verifies, countersigns, and replicates a complete body;
- a prospector that indexes a fixed formation under a pinned ore manifest;
- an assay agent that returns `accept`, `reject`, or `indeterminate`; and
- a fault monitor that compares signed roots and source views.

Every result should be reproducible outside the originating Gall state. An ore package should pin its desk commit, dependency closure, kernel/kelvin requirements, serialization, resource rules, and test vectors. A mutable app name, desk name, sponsor, or OTA source is not a semantics identifier.

Gall and desks add implementation and distribution mechanisms. They add no global consensus, archive permanence, objective timestamp, source completeness, or manufacture-resistance bound.

## 11. Cross-cutting falsification priorities

Any Urbit candidate should be rejected or narrowed if one of these attacks succeeds under its claimed model:

1. **Private-fork selection:** operate multiple piers or desk branches and publish the one with a desired predicate outcome.
2. **Event multiplication:** create cheap pokes, files, commits, peers, flows, or identities until a rare predicate passes.
3. **Withholding:** preserve a favorable state/frontier by delaying an event, receipt, root, batch, or archive.
4. **Selective witnessing:** show inconsistent but internally valid roots to isolated witnesses.
5. **Context stripping:** reuse one Clay `$tako` under different ship/desk/aeon claims or omit `rift` across a reset.
6. **Ordering substitution:** treat per-flow Ames order, local Arvo order, Clay ancestry, and Ethereum/Bitcoin order as interchangeable.
7. **Timestamp boundary gaming:** use local Arvo/Clay time or external miner time as if it were an exact common clock.
8. **Erosion:** retain only a digest, current state, or snapshot, then claim future permissionless prospecting remains possible.
9. **Semantic drift:** change kernel, marks, agent migration, `naive.hoon`, ore code, or canonical encoding and obtain a different result.
10. **Topology substitution:** swap numeric prefix, spawn parent, sponsor, OTA source, route, and actual participant set without changing the label “region.”
11. **Relabeling:** call an intentionally spawned point, signed receipt, or uploaded commit a fossil merely because someone classifies it later.
12. **Complete scan:** exhaust the public bounded domain and falsify a strong unknown-inventory claim.
13. **Moon/comet multiplication:** let one controller create moon or comet identities until identity-counted locality, witness diversity, or a rare predicate is achieved.
14. **Key compromise/backdating:** sign a past-looking envelope with a current or retired compromised key; require authorization-at-coordinate plus independent temporal evidence rather than treating signature validity as historical time.

If the optimal strategy is “vary an admissible Urbit event or history until its hash passes,” the mechanism is grinding/mining, not geological discovery.

## 12. Proposed experiments

These experiments are deliberately diagnostic. None creates a production protocol.

### E1 — Clay contextual export

On a pinned Urbit release, export one desk's aeon map, reachable `$yaki` DAG, and every live page preimage. Have two independent implementations recompute the same formation and occurrence IDs. Then remove the contextual envelope and demonstrate exactly which ship/desk/revision claims can no longer be authenticated from `$tako` alone.

### E2 — Hard-desk ancestry break

Create several revisions, run `|new-desk` with `=hard &` on the same name, and record the next revision. Verify whether the new commit has no parent while the revision number advances. Require a continuous-ancestry formation to reject or split at that point.

### E3 — Clay erosion

Close and replicate a formation, then tombstone locally eligible old pages. Test three states separately: original ship unavailable, one external archive available, and all preimages unavailable. The assay must return `indeterminate` in the last state and must not infer an empty inventory.

### E4 — Event replay and `chop`

Archive an Arvo event range with all pinned dependencies, reproduce its terminal state independently, and run an ore predicate not anticipated at closure. After `chop`, measure which results remain derivable from the current checkpoint and which require the external event archive.

### E5 — Witness split view

Give two honest witnesses different signed Clay or event roots for the same interval. Measure whether and when gossip reveals the conflict. Do not record “globally closed” before the view rule resolves it.

### E6 — Bilateral transcript adversary

Test refusal to countersign, parallel private transcripts, replay across `life`/`rift`, concurrent Ames flows, Sybil peers, and two-party collusion. Measure event-volume and target-outcome amplification rather than only receipt validity.

### E7 — Independent Azimuth L2 replay

From one pinned Ethereum interval, reconstruct effective sponsorship with two independent implementations using pinned batch and `naive.hoon` semantics. Exercise mixed L1/L2 escape, adoption, detach, reordering, invalid batch, and reorganization cases. Treat any permanent disagreement as view or semantics failure.

### E8 — Locality substitution

For the same planet, independently vary prefix parent, spawn provenance, effective sponsor, OTA source, hosting peer, and observed route. Add many moons controlled by that planet and cheaply generated comets. Require each ore/locality rule to name exactly one relation and historical coordinate, and require witness rules to collapse common control.

### E9 — Composite anchor failure

Anchor a canonical archive root, then test multiple candidate roots, commitment censorship, archive loss, stale Bitcoin view, and anchor reorganization. Verify that burial changes only the stated external settlement assumption and never upgrades local completeness.

### E10 — Enumeration and influence

For every bounded example, implement the fastest complete scan and an adversarial generator that controls all realistic event variants. Report exact inventory cost, `1-(1-p)^k` amplification where applicable, cumulative influence, and strategic withholding. Do not infer integrity from a rarity histogram.

## 13. Strongest Pass 0 conclusions

1. Urbit is a promising laboratory for **local and composite historical evidence** because it combines persistent identity coordinates, deterministic per-ship state transitions, revision structures, and independently running participants.
2. None of those properties gives Urbit a global, complete, immutable, or permanently available network history.
3. The strongest limited constructions are externally archived and witnessed local formations, bilaterally evidenced shared transcripts, and time-indexed topology formations reconstructed under pinned external-chain semantics.
4. The strongest locality candidates are typed relations at explicit historical views. A star subtree, Clay hash, current sponsor, or route is not a region without the relation and evidence that make it causally relevant.
5. A Bitcoin commitment can strengthen public ordering and post-publication binding of an Urbit archive root, but not local completeness, pre-anchor uniqueness, or G8.
6. Every finite, public Urbit formation with a fixed, finite/effectively enumerable candidate schema and total decidable ore can be enumerated. Future freedom to invent ores means future classifications are open, not that one fixed supply is unknowable.
7. No candidate here proves bounded participant influence. The default adversarial expectation for ship-controlled history is grinding, withholding, selective publication, and event-volume amplification until evidence shows otherwise.

## 14. Assumptions requiring independent verification

- reproducibility of complete Arvo replay across currently supported Vere, jet, and kernel versions;
- exact event material present in epochs versus checkpoints, and what a third-party archive must retain;
- current Clay garbage-collection behavior for commit nodes, aeon maps, and page preimages;
- the `|new-desk =hard &` ancestry break on a running ship at the pinned code revision;
- whether a canonical, complete Clay export can be produced without relying on private in-memory state;
- cryptographic identity and third-party verification semantics suitable for proposed bilateral receipts;
- full independent reconstruction of historical L2-aware Azimuth state from Ethereum data and pinned interpreter code;
- deployed contract/code addresses and current upgrade history, rather than repository source alone;
- current Mesa/directed-messaging authentication, replay, ordering, and breach behavior during network migration; and
- quantitative participant-influence bounds for every event, identity, branch, witness, and anchor control surface.

Until those assumptions are tested, these constructions are research instruments, not claims about existing Urbit geology.

## 15. Primary-source pins

- Urbit documentation at [`f6bfd25b0ab738930f799f77de93d8b1f7979b09`](https://github.com/urbit/docs.urbit.org/tree/f6bfd25b0ab738930f799f77de93d8b1f7979b09).
- Urbit/Arvo source at [`08026c84b29e9ba47b1764d109f5a646e1db7ff2`](https://github.com/urbit/urbit/tree/08026c84b29e9ba47b1764d109f5a646e1db7ff2).
- Azimuth contracts at [`bcf1d7bcf64cd73a3688434feb786be39a116819`](https://github.com/urbit/azimuth/tree/bcf1d7bcf64cd73a3688434feb786be39a116819).
- Satoshi Nakamoto, [*Bitcoin: A Peer-to-Peer Electronic Cash System*](https://bitcoin.org/bitcoin.pdf).
- Bitcoin Project, [Block Chain Reference: Block Headers](https://developer.bitcoin.org/reference/block_chain.html#block-headers).
