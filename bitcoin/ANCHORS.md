# Bitcoin as an External History and Anchor

**Status:** Research Pass 0 source analysis. This document proposes no Bitcoin transaction format and makes no claim that Bitcoin-derived objects have unknown supply.

## 1. Properties actually available

Bitcoin supplies a public sequence of proof-of-work block headers selected by a most-work chain rule. Each 80-byte header commits to its predecessor and to the block's transaction Merkle root. The header also contains a miner-selected timestamp, difficulty encoding, and nonce. The [Bitcoin developer reference](https://developer.bitcoin.org/reference/block_chain.html#block-headers) documents these fields and explicitly notes that miners may update the time or coinbase/Merkle root after exhausting nonce values.

The [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf) describes the security claim conditionally: changing an older record requires redoing its work and later work, and the chance of a slower attacker catching up decreases as blocks accumulate. It also describes temporary competing branches and nodes switching when one accumulates more work. The correct research term is therefore **probabilistically settled under an active-chain view**, not absolutely immutable.

Bitcoin can contribute:

- widely shared block-height coordinates;
- transaction ordering within a canonical block/chain view;
- chain-relative publication evidence that a digest or commitment record existed by inclusion; inferring that a matching preimage already existed additionally requires a specified canonical encoding and binding, preimage-resistant commitment construction;
- transaction-ID inclusion proofs via the header's Merkle root; witness bytes require separate SegWit witness-commitment evidence as specified by [BIP 141](https://bips.dev/141/#commitment-structure);
- a costly history-replacement condition; and
- deterministic header material available to independent full-node verifiers.

It does not directly know whether an external archive is complete, truthful, available, or unmanipulated.

## 2. Two distinct uses

### 2.1 Publication anchor

A transaction commits to a formation manifest or root. After a declared amount of burial, the anchor supplies evidence that the commitment was included in Bitcoin's active history.

This can establish:

- a public cutoff;
- ordering among included commitments;
- a chain-relative “no later than” coordinate; and
- tamper evidence for a later-disclosed matching preimage.

It cannot establish:

- that the preimage contains all local events;
- that the publisher generated only one candidate preimage;
- that internal timestamps or authorship are accurate;
- that anyone still stores the preimage; or
- that the local source follows Bitcoin consensus.

### 2.2 Source terrain

The block headers or committed transaction records themselves form the formation material. Here Bitcoin supplies both the material and its canonicalization rule.

For header-only terrain this reduces an ordinary application user's direct control over the bytes; for transaction terrain, submitters still choose their transaction bytes and miners choose inclusion/order. In both cases the adversary analysis moves to miners, mining pools, transaction submitters, and chain-view providers rather than disappearing. Historical header domains are finite and public, so simple ore predicates are exhaustively enumerable.

The two uses must not be conflated. An Urbit archive committed in Bitcoin is still an Urbit-derived composite formation, not Bitcoin-native history.

## 3. Miner control surface

For a candidate block, a producer may influence:

- nonce;
- coinbase data and therefore Merkle root;
- transaction selection and ordering;
- header version within valid rules;
- timestamp within consensus/policy bounds;
- whether and when to publish a valid block; and
- which application commitments to include.

The [block-header reference](https://developer.bitcoin.org/reference/block_chain.html#block-headers) states that the timestamp is according to the miner, must exceed the median of the prior 11 blocks, and is rejected if too far in the future according to node time. It is therefore not a precise external clock. Current consensus behavior must ultimately be checked against a declared Bitcoin Core release or commit in the [Bitcoin Core source](https://github.com/bitcoin/bitcoin), not inherited indefinitely from explanatory documentation.

Mining a valid block already entails exploring a large header-candidate space. A geological predicate over selected header bits may give producers additional option value: discard, delay, or choose among candidate blocks when the derived object is valuable enough. A one-block hash is not an unbiased random beacon merely because manipulating it is costly.

## 4. Reorganization and view semantics

A formation descriptor using Bitcoin should include at least:

```text
network/genesis identifier
start and end heights
exact header/transaction serialization
active-chain selection rule
minimum burial or cumulative-chainwork rule
behavior on reorganization
node/view assumptions
data-retention requirements
```

Possible reorganization policies include:

1. **invalidate:** the formation and its objects become invalid when an anchor leaves the active chain;
2. **branch:** retain branch-qualified identities and mark the former branch noncanonical;
3. **reclose:** build a new formation from the replacement history and never pretend IDs stayed unchanged.

Silently keeping an unqualified object ID while changing its historical preimage violates stable identity.

An eclipsed or stale verifier can accept a minority or obsolete view. Independent verification means using a declared validating view; it does not eliminate network-view attacks.

## 5. Shared work is not object substance

Bitcoin chainwork protects the chain as a whole. Deriving many geological objects from one interval does not divide that work into exclusive, atom-specific production costs. An assay should report separately:

- external chain/burial evidence;
- predicate rarity, if statistically justified;
- any object-specific search work; and
- local archive/witness evidence.

Adding these into one “total work per object” number would double-count shared security.

## 6. Data availability

A Bitcoin transaction can record a short digest while the formation data live elsewhere. If that archive disappears, the included digest does not reconstruct it. Bitcoin full nodes validate the containing transaction and block under consensus rules; they do not thereby validate the application's encoding or preimage semantics, and transaction inclusion is not a data-availability proof for an arbitrary off-chain preimage.

This mirrors a broader commitment-system limit. [RFC 9162 Certificate Transparency](https://www.rfc-editor.org/rfc/rfc9162.html) uses Merkle trees for inclusion and append-only consistency but still requires logs to retain submitted material and notes that inconsistent views can defeat auditing absent additional mechanisms. The lesson is not that Bitcoin has Certificate Transparency's trust model; it is that cryptographic binding, consistency, availability, and global view are separate properties.

## 7. Anchor attacks to simulate

| Attack | Experiment |
|---|---|
| Header selection | Give a miner `k` consensus-valid candidate blocks—or model ordinary trials plus discarding a predicate-failing valid block—and measure target-predicate amplification. |
| Conditional withholding | Compare block reward/orphan cost with the application value of a favored geological outcome. |
| Commitment censorship | Exclude selected formation roots from bounded publication windows. |
| Transaction-order bias | Permute included commitments and test whether identity, locality, or eligibility changes. |
| Timestamp boundary | Move a valid timestamp across an application-defined stratum boundary. |
| Reorganization | Replace anchors at every tested burial depth and require explicit invalid/branch states. |
| Verifier eclipse | Feed an internally valid stale/minority chain to the assay client. |
| Archive loss | Preserve transaction/root but remove the off-chain formation body. |
| Cross-role coalition | Give one actor control over local root selection and some external block production. |

No fixed confirmation depth proves absolute finality. Any numerical manipulation bound is an economic/security result requiring independent review and updated network assumptions.

## 8. Strongest defensible Pass 0 statement

> A sufficiently buried Bitcoin inclusion of a binding, preimage-resistant commitment can serve as a public, probabilistically settled commitment coordinate for a canonically encoded formation under an explicit active-chain and verifier-view model.

This statement does not imply that the formation is complete, available, non-mintable, unknown in inventory, or immune to miner influence.

## 9. Primary sources

- Satoshi Nakamoto, [*Bitcoin: A Peer-to-Peer Electronic Cash System*](https://bitcoin.org/bitcoin.pdf), especially §§3–5 and §11.
- Bitcoin Project, [Block Chain Reference: Block Headers](https://developer.bitcoin.org/reference/block_chain.html#block-headers).
- Bitcoin Improvement Proposals, [BIP 141: Segregated Witness commitment structure](https://bips.dev/141/#commitment-structure).
- Bitcoin Core, [source repository](https://github.com/bitcoin/bitcoin) (pin a release/commit for any implementation or theorem dependent on exact consensus behavior).
- IETF, [RFC 9162: Certificate Transparency Version 2.0](https://www.rfc-editor.org/rfc/rfc9162.html), used only for the separability of inclusion, consistency, availability, and view assumptions.
