# Relationship to GoldAtom

**Status:** Research Pass 0. GoldAtom is one motivating case study, not the definition, foundation, or reference implementation of computational geology.

**Source basis:** This note reviews the public GoldAtom repository at commit [`0184b2b74dc280e53672f0e9405f0d74b4a07125`](https://github.com/gold-atom/goldatom/tree/0184b2b74dc280e53672f0e9405f0d74b4a07125). It does not independently reproduce GoldAtom's validation runs or endorse its economic proposals.

## 1. The boundary

GoldAtom and computational geology ask related but non-identical questions.

GoldAtom/0 specifies an intentional lifecycle involving a claim, atom-specific local work, a Bitcoin transaction that mints an atom, and a UTXO title chain. Its atoms therefore follow the causal shape of minting:

```text
intent -> protocol actions -> mint -> atom and title exist
```

They are not examples of latent historical objects whose existence precedes discovery. The public GoldAtom materials describe version zero as a verified **object layer** under tested conditions: object-level non-reuse, portable verification against Bitcoin history, and independently checkable provenance. They expressly do not claim a monetary issuance solution or aggregate scarcity. See the pinned [project boundary](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/PROJECT-CONTEXT.md), [README](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/README.md), [version-zero specification](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/SPEC-0.md), and [validation report](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/VALIDATION.md).

GoldAtom/1 asks whether claimant-independent relations among proof histories can determine rare opportunities before allocation. That question overlaps computational geology. The source is equally clear, however, that GoldAtom/1 is a **non-normative, unimplemented research specification that is not safe for public funds** and does not constitute a completed scarcity proof. It leaves source-producer manipulation, censorship, concentration, data availability, and parameter governance unresolved. See the pinned [GoldAtom/1 candidate](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/SPEC-1.md).

Accordingly:

- GoldAtom/0 provides an informative worked example of separating object validity, provenance, title, and aggregate issuance.
- GoldAtom/0 atoms are minted protocol objects, not fossils under the definitions in this repository.
- GoldAtom/1 provides attacks and research questions, not established geological constructions.
- A pattern found retrospectively *inside* GoldAtom history could be a separate geological candidate, but it would have to satisfy the same source-causation and manufacture-resistance tests as any other endogenous history.
- Computational geology has no necessary monetary, token, proof-of-work, or Bitcoin component.

## 2. What Research Pass 0 imports

This repository imports methodological lessons, especially negative ones. It does not import GoldAtom protocol objects.

### 2.1 A valid object is not a scarce inventory

GoldAtom's project boundary distinguishes object-level non-reuse from aggregate issuance. A single claim may be single-use and a single title may resolve uniquely while actors remain free to create many claims or perform more work. In computational-geology terms, stable identity and non-duplication are necessary assay properties; they do not bound `N(F,Q,O,H*)` or participant influence over it.

This is why [`THEORY.md`](../THEORY.md) treats existence, discovery, classification, claim, custody, ownership, and transfer as separate relations. A title system can be coherent while the purported geological supply claim is false.

### 2.2 Apparent rarity can be manufactured through multiplicity

For a predicate that accepts one independent candidate with probability `p`, an actor able to choose among `M` cheap variants has success probability

```text
p_effective = 1 - (1 - p)^M.
```

The GoldAtom issuance stress model gives the concrete example `p = 1/4096`: `10,000` claimant-controlled variants raise the chance of at least one pass from about `0.02441%` to about `91.30%`. The relevant source bytes may be keys, transaction identifiers, salts, ordering choices, selected heights, encodings, or any other inexpensive degree of freedom. See the pinned [issuance stress model](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/ISSUANCE-SIMULATION-0.md).

The independent-trial formula is illustrative rather than universal: real variants may be correlated. The general requirement is stronger. Every candidate must enumerate participant-controlled degrees of freedom and measure the best adaptive strategy, not infer integrity from the marginal distribution of one advertised input. If a user can vary admissible events until a rare hash predicate passes, the mechanism is mining or grinding rather than geological discovery.

### 2.3 Source producers are participants in the threat model

“Claimant-independent” does not mean manipulation-independent. A Bitcoin block producer can select transactions, vary valid headers, reorder admissible inputs, censor records, and sometimes withhold a valid block. A multi-source construction can move selective power to the last revealer rather than remove it. GoldAtom's [threat model](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/THREAT-MODEL.md) and [GoldAtom/1 candidate](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/SPEC-1.md) preserve these as unresolved attacks.

Computational-geology models must therefore include every actor who can influence formation inputs—not only the eventual prospector. Calling a history exogenous changes the cost model; it does not eliminate source-miner, operator, sequencer, archive, or governance power.

### 2.4 Withholding creates hidden option value

A public history shows the published path, not necessarily all paths an actor evaluated. An actor may suppress unfavorable candidates, preserve a favorable intermediate state or “frontier,” branch privately, wait for later information, and publish only the best extension. A one-event bias bound can therefore understate cumulative control.

An adequate intervention analysis must include:

- unpublished attempts and discarded histories;
- the cost and duration of keeping alternative frontiers alive;
- information learned before each publish/withhold choice;
- whether a favorable state can be carried across intervals;
- coalition control over ordering and admission; and
- cumulative effects across the entire formation, not only one nominal event.

Closure fixes the path that survived; it does not retroactively make the production process uncontrollable.

### 2.5 Censorship affects different relations differently

Censorship before formation closure can change which source events—and therefore which occurrences—exist in the accepted history. Censorship after closure should not change geological existence, but it can delay discovery publication, exclude a claim, change an allocation contest, or prevent observers from obtaining witnesses. These are different failures.

GoldAtom's finite mint windows and proposed allocation windows make inclusion censorship explicit. Computational geology does not inherit those mechanisms, but it inherits the discipline of stating whether censorship affects substrate, discovery, classification, claim, custody, or ownership.

### 2.6 Shared anchoring work is not per-object substance

A Bitcoin block can order and bury many unrelated commitments. The same accumulated chainwork contributes revision resistance to all of them. Multiplying that shared chainwork by the number of derived objects would turn shared security into fictitious object-specific production. GoldAtom/0's assay keeps atom-specific local expected work and shared Bitcoin burial as separate dimensions; its [specification](https://github.com/gold-atom/goldatom/blob/0184b2b74dc280e53672f0e9405f0d74b4a07125/SPEC-0.md) explicitly forbids adding them into one work quantity.

The broader lesson is not that computational geology needs per-object work. It is that provenance vectors must preserve the type and scope of each fact. An external anchor may support ordering or revision-resistance under its own assumptions. It does not make local history complete, make an occurrence exclusive, or confer the anchor's total cost on every fossil.

### 2.7 Unknown future realizations are not unknown historical reserves

For a finite public formation, an effective candidate extractor, and a total decidable ore predicate, the historical object set can in principle be enumerated. Before future source events occur, their outcomes may be genuinely unknown; after a fixed historical interval and ore definition are public, failure to run the enumeration is observer-relative ignorance.

GoldAtom/1 states this limit directly: its past cryptographic strata are enumerable, so it can at most claim unknown future realizations, not unknowable historical reserves. Computational geology preserves that negative result in [`UNKNOWN_SUPPLY.md`](UNKNOWN_SUPPLY.md). Making exhaustive search expensive can create resource-bounded unknownness, but if the expensive operation is simply repeated hashing it may reproduce proof-of-work economics rather than establish a natural finite reserve.

### 2.8 A rarity histogram is not an integrity proof

A visually persuasive long-tail distribution can coexist with cheap candidate multiplication, selective publication, incomplete archives, semantic changes, or correlated source control. Statistical rarity must be conditioned on the adversary's full choice set and the source's actual production process. It cannot substitute for causal analysis, availability evidence, or a manufacture bound.

## 3. Concept mapping

| GoldAtom element | Reusable lesson | Computational-geology treatment | Boundary retained here |
|---|---|---|---|
| GoldAtom/0 claim and mint | Canonical encodings and single-use transitions can support independently assayable objects. | Useful comparison for witness and identity design. | The mint creates a GoldAtom atom; it is not geological discovery. |
| AtomID and proof bundle | Stable identifiers and portable evidence require exact semantics and retained data. | Separate occurrence identity, typed object identity, and witness availability. | A unique ID does not imply aggregate scarcity or historical non-manufacturability. |
| UTXO title chain | Current title can be tracked separately from object validity. | Model claim, custody, ownership, and transfer as external typed relations. | No title or first-publication rule follows from existence. |
| Atom-specific local work | Object-specific cost can be independently measured. | Cost may be an assay dimension or an adversarial budget. | Costly production is not non-mintability and need not define ore. |
| Bitcoin challenge and burial | External history can supply ordering and conditional revision resistance. | Treat as an exogenous source or a component of a composite formation. | Bitcoin work is shared; block producers retain selection, withholding, reordering, and censorship powers. |
| Proof-intersection gate | Existence should not depend on claimant-controlled variants. | Test fixed-history predicates as possible ore definitions. | Rarity is not integrity; historical gates may be exhaustively enumerable. |
| Proposed vein allocation | Existence and allocation must be separated. | Keep discoveries and claims outside `Objects(F,Q,O,H*)`. | No auction, ticket, winner, or ownership mechanism is adopted. |
| GoldAtom/1 falsification workflow | Attractive constructions should face a common adversarial harness and failed designs should remain visible. | Use [`THREAT_MODEL.md`](THREAT_MODEL.md) and [`FALSIFICATION_CRITERIA.md`](FALSIFICATION_CRITERIA.md). | GoldAtom/1's proposed answer is not inherited. |

## 4. Explicit non-import list

Research Pass 0 does **not** import or endorse:

- GoldAtom/0 atom, claim, challenge, mint, transfer, or title encodings;
- GoldAtom/1 “vein,” Proof-Cast Ticket, auction, epoch, or settlement constructions;
- a Bitcoin, multi-chain, local-work, issuance, or monetary requirement;
- GoldAtom profile parameters, probability targets, work functions, or economic assumptions;
- any claim of fixed supply, unknown supply, fair distribution, manipulation resistance, or production readiness; or
- any conclusion that GoldAtom has solved computational geology.

The GoldAtom repositories remain independent. This repository neither modifies them nor makes them normative dependencies.

## 5. Research use and stopping rule

GoldAtom remains useful as a regression case for claims made here. Any candidate computational-geology primitive should answer at least these questions inherited from its failures:

1. Which bytes and source events can every interested actor vary, suppress, reorder, or delay?
2. How does the best success probability change with multiplicity, withholding, and maintained frontiers?
3. Does source-producer influence remain bounded over the full formation horizon?
4. Is the object latent in history, or is an issuance action merely being renamed as discovery?
5. Which evidence is object-specific, which is shared, and which is only a later claim or title?
6. Can the historical inventory be enumerated once the formation and ore are fixed?
7. What observation would falsify the proposed manufacture bound?

If those questions do not have explicit, testable answers, the candidate should remain a documented negative result. A beautiful rarity distribution is not evidence of geological integrity.
