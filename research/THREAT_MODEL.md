# Threat Model

**Status:** Research Pass 0. This document defines attacks that candidates must face. It does not assert that any candidate withstands them.

## 1. Security objectives

A geological primitive may claim some or all of the following assets. Each must be evaluated separately:

1. **Formation integrity:** the assayed material matches the declared historical domain.
2. **Closure:** separately justified boundary, extension, probabilistic settlement, semantic, and evidentiary closure conditions.
3. **View convergence:** honest verifiers identify the same formation material.
4. **Availability:** required material and witnesses remain obtainable.
5. **Discovery non-creation:** discovery and claim operations do not alter the object set.
6. **Manufacture resistance:** participants cannot cheaply increase count or target identities/localities before closure.
7. **Identity uniqueness:** equivalent witnesses and replays do not multiply one occurrence.
8. **Locality integrity:** locality statements correspond to authenticated, time-indexed relations.
9. **Assay reproducibility:** verifiers agree under pinned semantics and equal inputs.
10. **Independent verification:** verifiers validate source membership/view without trusting the discoverer or a self-attesting archive publisher.
11. **Permissionless prospectability:** a fresh unprivileged party can retrieve query-sufficient terrain and search admitted ores under declared access bounds.
12. **Provenance typing:** origin, discovery, publication, classification, custody, claim, ownership, and transfer remain distinct.

Preserving one asset does not imply another. A Merkle proof may establish inclusion while saying nothing about completeness; a stable object identifier may survive while its source archive disappears.

## 2. Trust boundaries

Every candidate must identify which components are trusted for which property:

| Boundary | Question |
|---|---|
| Source validity | Who decides which events are valid? |
| Source ordering | Who can order or reorder valid events? |
| View selection | How do observers choose among histories? |
| Formation publisher | Can it omit, fork, or grind material before committing? |
| Candidate-schema author | Was extraction/equivalence/identity fixed before closure, and can equivalent schemas alias occurrences? |
| Archive/custodian | Can it delete the committed preimage or selectively serve it? |
| Ore publisher | Can it choose predicates after seeing favorable outcomes? |
| Assay implementation | Are encodings, versions, and error behavior independently reproducible? |
| Discovery registry | Can it censor, reorder, or front-run reports? |
| External anchor | Who produces blocks, chooses transactions, and supplies the verifier's chain view? |
| Upgrade authority | Who can change historical interpretation or supported proof rules? |
| Rights layer | What system, if any, recognizes claims, custody, ownership, and transfers? |
| Key/authorization history | Which key was authorized at the historical coordinate, and what bounds compromise or backdating? |

## 3. Adversaries

### A1 — Event author

Controls contents, timing, number, and sometimes ordering of otherwise valid local events. It may repeatedly try candidate events before publication.

### A2 — Sybil coalition

Creates many identities, ships, accounts, desks, applications, or claims to expand the candidate surface or fake locality.

### A3 — History operator

Controls a local event log, revision graph, checkpoint process, or formation publisher. It may maintain private forks, commit selectively, or destroy old material.

### A4 — Network intermediary

Can delay, drop, relay, reorder across flows, or selectively expose messages. In an Urbit setting this may include sponsors, galaxies, hosting providers, or application publishers, but their actual capabilities must be derived from the deployed architecture rather than rank names.

### A5 — Prospector/indexer

Can search privately, strategically delay discoveries, publish only favorable objects, flood a registry, or exploit implementation differences.

### A6 — Classifier

Observes a formation before selecting an ore definition, boundary, encoding, or significance threshold. It may overfit a predicate to desired holdings or narratives.

### A7 — Claimant or rights operator

Attempts to turn discovery into creation, duplicate claims, front-run disclosures, confuse key control with ownership, or rewrite provenance during transfer.

### A8 — External block producer

Selects and orders transactions, chooses coinbase data and any transactions it creates itself, selects timestamps within consensus bounds, and decides whether to publish a valid block candidate. It may censor anchors or withhold favorable histories.

### A9 — Verifier-view attacker

Eclipses or supplies a stale, pruned, minority-fork, or inconsistent view to a verifier.

### A10 — Protocol upgrader

Changes source validity, serialization, canonicalization, ore execution, or historical APIs. An honest upgrade can still make old assays non-reproducible.

### A11 — Composite coalition

Controls roles across layers—for example, a local history publisher and an external block producer. Independence assumptions must be tested for correlated control.

### A12 — Key-compromise attacker

Obtains a current or retired source/witness key and signs past-looking formation envelopes, receipts, locality claims, or archive statements. It exploits missing key-version, authorization-at-coordinate, revocation, and independent publication-time evidence.

## 4. Attack matrix

| Attack | Mechanism | Geological property at risk | Minimum falsifying observation |
|---|---|---|---|
| Grinding | Vary user-controlled bytes until a rare predicate passes. | Manufacture resistance | Success probability scales as `1-(1-p)^k` over cheap variants. |
| Event spam | Increase admissible event count to increase candidate windows or combinations. | Bounded influence, inventory law | Expected discoveries grow materially with attacker-generated volume absent corresponding fixed terrain. |
| Sybil creation | Multiply identities, namespaces, or “regions.” | Locality, bounded influence | One actor can multiply eligibility or object count more cheaply than the claimed bound. |
| Withholding | Keep a qualifying or state-changing record private until release is advantageous. | Canonicality, fairness, future inventory | Selective reveal improves expected count, target identity, or future state. |
| Favorable-frontier preservation | Suppress a new record so an older advantageous record remains the state from which future predicates are evaluated. | Cumulative influence | A single intervention affects multiple later formation opportunities beyond the claimed horizon. |
| Selective publication | Commit only a favorable subset of a locally known history. | Completeness, view convergence, manufacture resistance | Two publisher-selected source projections both satisfy validation with different inventories. |
| Timestamp manipulation | Choose accepted timestamps or observation times to move events between strata. | Closure, locality | An actor can change formation membership without changing underlying causal order. |
| Reordering | Permute admissible events, transactions, commits, or cross-flow messages. | Identity, predicate outcome | Multiple valid orders yield materially different object sets without a canonical rule. |
| Replay | Reuse the same occurrence, packet, proof, or serialization in multiple contexts. | Stable identity, supply | Equivalent witnesses produce more than one accepted object ID. |
| Alternative encoding | Change semantically irrelevant bytes, path forms, or proof containers. | Stable identity, manufacture resistance | Encoding multiplicity creates independent predicate trials or identities. |
| History rewriting | Replace a closed-looking local fork, revision branch, or external chain segment. | Closure, provenance | Previously valid objects change without a declared finality failure state. |
| Pruning / erosion | Delete events or preimages while retaining current state or roots. | Availability, retrospective discovery, permissionless prospectability | A fresh unprivileged party cannot retrieve query-sufficient terrain for search; retained evidence may still permit verification of one already identified object. |
| Observer dependence | Serve different histories, roots, or archives to different verifiers. | View convergence | Honest verifiers accept incompatible object sets from locally valid evidence. |
| Classification gaming | Select predicate, boundary, or complexity after viewing desired results. | Meaningful rarity | A classifier can cheaply isolate any selected occurrence or holding as “rare.” |
| Supply enumeration | Exhaustively scan a fixed public candidate domain. | Strong unknown-inventory claim | Complete inventory is derived within the resources the claim said were insufficient. |
| Cheap synthetic locality | Copy a label, create a subtree, change sponsor, or self-report a location. | Locality integrity | Locality can be acquired without participating in the claimed historical relation. |
| Strategic non-discovery | Withhold a witness to affect perceived supply, price, priority, or later classification. | Reported inventory, discovery fairness | Public discovery count is materially controllable even though existence is fixed. |
| Claim/existence confusion | Treat registration or first publication as the event that creates the object. | Discovery non-creation | Removing the claim changes whether an assay says the historical object exists. |
| Claim/ownership confusion | Treat finder, signer, custodian, or key holder as owner without a named rule system. | Provenance, rights correctness | Two distinct relations are represented by one untyped “owner” field. |
| External-anchor grinding | Block producer searches or selects among valid anchor states. | Exogeneity, bounded influence | Conditional withholding or candidate selection materially biases object outcomes. |
| External-anchor censorship | Exclude commitments, discoveries, or settlements from bounded windows. | Closure, publication, allocation | One producer/coalition can make valid material invisible or ineligible. |
| Anchor reorganization | Replace the chain segment containing a boundary or commitment. | Closure, stable identity | Objects silently retain “final” status after their anchor leaves the canonical view. |
| Protocol semantic change | New software interprets old bytes, paths, types, or proofs differently. | Assay determinism, identity | Supported versions disagree without an explicit migration or invalidation rule. |
| Composite correlation | One coalition influences both local material and external seal. | Claimed independence | Security calculation assumes independent sources that are strategically coupled. |
| Schema gaming | Define extraction, windowing, equivalence, or occurrence identity after seeing history. | Prior existence, stable identity | Later schema choices create/repartition occurrences or equivalent schemas multiply IDs. |
| Manifest-metadata malleability | Put publisher names, signatures, archive URLs, or an ID itself into a supposedly canonical identity core. | Stable identity, grinding resistance | Mutable metadata or self-reference produces aliases or cheap trials over identical material. |
| Closure substitution | Use a reached endpoint, root, or confirmation count as proof of every closure dimension. | Formation integrity, finality | A committed subset passes while source completeness fails, or semantics/view later change without explicit invalidation. |
| Future oracle dependence | Let assay read later randomness, clocks, registries, URLs, or mutable external state. | Prior existence, discovery non-creation | Membership changes while formation/schema/ore core remain fixed. |
| Privileged prospecting | Reveal witnesses selectively while withholding query-sufficient terrain. | Permissionless prospectability, reserve claims | A fresh verifier can check one supplied proof but cannot independently search a new ore. |
| Key compromise / backdating | Use a compromised current or retired key to sign a past-looking envelope or receipt. | Provenance, locality, closure time | Signature verifies although authorization-at-coordinate or independent temporal evidence fails. |

## 5. Counterexamples every proposal should run

### 5.1 User-controlled rare event

```text
event = (payload, nonce)
object exists iff Hash(event) < target
```

If `nonce` or equivalent payload freedom is controlled by the beneficiary, this is direct proof-of-work search. The history only records the winning attempt; it does not transform production into discovery.

### 5.2 Selective commitment

An operator observes events `e1...en`, chooses a favorable subset `J`, and publishes `root(J)`. Binding holds perfectly, but completeness fails. Any construction that treats the root as “the history” without a completeness mechanism inherits this failure.

### 5.3 Private-fork choice

An operator builds several locally valid Clay commit branches or event sequences, assays each, and publishes the most favorable branch. Revision control makes ancestry inspectable after publication; it does not prevent private branch selection.

### 5.4 Post-hoc singleton ore

After seeing the formation, a classifier defines `P(x) = true` only for a favored occurrence. Inventory is one, but no meaningful scarcity proposition follows. A rarity calculation must include the number and freedom of predicates searched.

### 5.5 Lost-reserve fallacy

A commitment survives but its archive is pruned. The system calls undiscoverable preimages “unknown reserves.” This is unfalsifiable absence, not permissionless geology, because new prospectors cannot search. Individual verification survives only for identified candidates whose source/view, membership, and assay evidence was retained.

### 5.6 Dynamic-region substitution

A candidate defines a “star region” without saying whether it means numeric prefix, original spawning parent, current sponsor, update source, relay path, or observed communication set. These relations differ and can change. Substituting one for another invalidates locality claims.

### 5.7 First-finder allocation

The first registry entry is called ownership. A watcher copies or censors a discovery and wins the race. The underlying object's existence is intact; the allocation rule has failed.

## 6. Quantities to measure

Candidate reports should include, where meaningful:

- number and cost of participant-selectable variants;
- marginal and cumulative change in expected inventory;
- change in probability of a targeted identity or locality;
- maximum effect of one withheld event and an adaptive sequence;
- duration for which a favorable frontier can be preserved;
- fraction of source material independently witnessed;
- probability and duration of view disagreement;
- archive replication and recovery assumptions;
- ore-description complexity and number of predicates searched;
- candidate-schema variants and the full ore commitment/reveal information timeline;
- complete-enumeration cost versus single-assay cost; and
- external-source manipulation cost relative to object value.

Rarity histograms are diagnostic outputs, never security evidence by themselves.

A signature proves that a key signed a message under the signature scheme. Without historical key authorization and independently constrained temporal evidence, it does not prove when the message existed, who controlled the key earlier, or that the signed locality/history was complete.

## 7. Out of scope for Pass 0

This repository does not define economic value, token issuance, market fairness, legal ownership, or a production security parameter. If later work attaches rights or value to discoveries, it must add frontrunning, bribery, fee markets, MEV, economic exploitation of key compromise, and governance capture to the model rather than retroactively treating this threat model as sufficient.
