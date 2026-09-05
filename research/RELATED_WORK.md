# Related Work and Research Boundary

**Status:** Research Pass 0. This is a boundary map, not a claim of novelty, priority, or protocol completeness.

Computational geology draws on established work in commitments, authenticated histories, content-derived identity, archival provenance, consensus, and retrospective indexing. None of those mechanisms becomes geological merely by changing its vocabulary. The research question is whether a construction can combine historical precedence and stable identity with independent assay, meaningful locality, continuing evidence, and an explicit bound on participants' ability to manufacture qualifying occurrences.

## 1. The boundary in one table

| Adjacent system | What it actually provides | What it does **not** establish |
|---|---|---|
| [Haber–Stornetta digital time-stamping](https://doi.org/10.1007/BF00196791) | Hash-linked and distributed certificates can make later alteration or false dating detectable under stated cryptographic and trust assumptions. This is foundational evidence of historical precedence. | A timestamp does not show that the submitted document was the unique, truthful, or complete source record. The client may choose and test many inputs before submission; the scheme does not bound manufacture of rare input properties. It also does not preserve the preimage automatically or define a natural network locality beyond the timestamp evidence. |
| [Crosby–Wallach tamper-evident logging](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident) | Authenticated log structures support efficient evidence about membership and log evolution even when the logger is not fully trusted. | Tamper evidence is evidence about changes to what was recorded, not proof that every relevant event was recorded, honestly generated, or kept available. A logger or event producer may omit, reorder where permitted, or deliberately manufacture inputs unless another model prevents it. |
| [Certificate Transparency, RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html) | Signed tree heads, Merkle inclusion proofs, and consistency proofs make one log view auditable as append-only. Monitors can enumerate entries, verify roots, and treat prolonged unavailability or failed consistency as misbehavior. | CT does not itself detect certificate misissuance, guarantee that all certificates were submitted, or eliminate split-view attacks: the RFC explicitly requires monitoring and treats each log as trusted absent out-of-scope anti-equivocation mechanisms. Certificates and submissions are intentionally created, so logged entries are not non-mintable fossils. If the log is available, its entry inventory is enumerable rather than intrinsically unknown. |
| [Git's object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) | Blobs, trees, and commits have content-derived names; commits bind snapshot trees, parent references, author data, timestamps, and messages into a Merkle-like DAG. This is useful machinery for stable identity and relative historical structure. | A Git repository has no protocol-wide canonical view or finality. Users deliberately create commits, can choose metadata and parent structure, move refs, rewrite visible history, and manufacture arbitrarily many candidates. Objects that become unreachable may be removed by [`git gc`](https://git-scm.com/docs/git-gc). A hash identifies bytes; it does not prove source completeness, durable availability, non-mintability, or independently meaningful locality. |
| [SWHIDs](https://www.swhid.org/specification/v1.2/) and the [Software Heritage data model](https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html) | Type-specific intrinsic identifiers name contents, directories, revisions, releases, and snapshots. Optional origin, visit, anchor, path, and fragment qualifiers express context without changing the core object identity. The archive's Merkle DAG supports deduplication and durable citation. | The SWHID specification expressly places archival and resolution systems outside its scope. An intrinsic name alone does not prove that an object remains retrievable, that an origin was completely captured, or that a claimed origin caused the bytes. Software authors and repositories can create unlimited inputs. Archive-scale search can reveal old structures, but an unperformed query is not a manufacture bound or a proof of unknown inventory. |
| [Bitcoin's proof-of-work history](https://bitcoin.org/bitcoin.pdf) | A work-weighted chain gives a shared, probabilistically stabilizing order of accepted transactions; block headers commit to transaction Merkle roots. Sufficiently buried block coordinates can therefore serve as exogenous commitments under explicit chain-selection and reorganization assumptions. | Bitcoin does not attest that an external or local history committed into it was complete or truthful. Transaction creators choose their own transaction bytes and scripts; miners choose transaction selection and ordering, coinbase and valid header candidates, and publication. Proof of inclusion is not proof of source non-manufacture or data availability outside the committed Bitcoin data. Finality remains probabilistic, not absolute. |
| [Ordinal Theory](https://docs.ordinals.com/overview.html) and [inscriptions](https://docs.ordinals.com/inscriptions.html) | A later deterministic convention assigns and tracks satoshi serial numbers through historical Bitcoin transaction order. Its rarity taxonomy illustrates retrospective classification of already-recorded positions. | This does not by itself show that the ore-relative types existed before the convention, nor that inventory is unknown: the named rarity classes follow declared periodic rules. Satoshis are natively issued by Bitcoin, and inscriptions are intentionally created by commit/reveal transactions and identified from their reveal transaction. Relabeling either as fossils would collapse issuance or creation into discovery. |

## 2. Append-only is not complete, available, or geological

An authenticated append-only history can answer a conditional question:

> Given trusted checkpoint `r_n`, does this leaf belong to the committed prefix, and is later checkpoint `r_m` a consistent extension?

It does not answer three different questions:

1. **Source completeness:** did every event in the purported source domain enter the log?
2. **Source truth:** did logged statements correspond to external events as claimed?
3. **Continuing availability:** can a future prospector retrieve enough material to search or assay later predicates?

RFC 9162 makes this separation unusually explicit. A log must serve data and monitors must inspect new entries; inconsistent views remain a distinct threat. A formation commitment should inherit this discipline: membership and consistency proofs bind a view, while completeness, canonicality, and availability require separate evidence and adversary assumptions.

Log entries also normally arise from deliberate submission. They therefore resemble records created by an append operation. A pattern *across* a closed log may be retrospectively indexed, but it is only a geological candidate if the pattern has ore-independent occurrence identity and survives the source-causation and manufacture-bound tests in [`THEORY.md`](../THEORY.md).

## 3. Content addressing is identity, not scarcity

Git and SWHIDs demonstrate a strong and reusable separation:

- intrinsic identifiers can remain stable across repositories and observations;
- contextual qualifiers can describe a path, origin, visit, or snapshot without changing the underlying content identity; and
- retention and resolvability are separate from identifier validity.

This separation informs the repository's distinction between occurrence identity, formation membership, provenance, and custody. It also supplies a counterexample to “rare-looking hash means scarce object.” An actor can cheaply vary content until its content identifier satisfies a visual or numeric predicate. Collision resistance prevents finding two inputs with the same identifier; it does not prevent sampling many different identifiers. Without a bound on candidate control, rare hash prefixes are grinding outcomes.

## 4. Retrospective indexing is not necessarily prior existence

Ordinal Theory is a useful nearby example because a later rule can deterministically traverse old Bitcoin history and assign stable serial positions. That establishes reproducible retrospective indexing under a chosen convention. It leaves two questions open:

1. Did the indexed base occurrence have an identity independent of the later convention?
2. Could source participants intentionally affect which occurrences would satisfy the later class?

If a later rule introduces the extractor, equivalence relation, and occurrence identity, the rule creates a new typing of old substrate. This repository calls that **weak retrospective typing**, not proof that the typed object existed before the rule. If an inscription is brought into existence by a reveal transaction, retrospective discovery language is simply incorrect for the inscription itself.

## 5. What is not new, and what remains to be tested

This research does **not** claim novelty for:

- hash chains, Merkle trees, authenticated dictionaries, inclusion proofs, or consistency proofs;
- append-only and tamper-evident logs;
- content-addressed objects or Merkle DAGs;
- intrinsic persistent identifiers and provenance qualifiers;
- proof-of-work ordering or external timestamp anchors;
- deterministic indexing of old data; or
- post-hoc classification and archival search.

The potentially distinct contribution is a falsification framework for a narrower conjunction: a source-fixed occurrence that preexists its discovery, has stable independently assayable identity and historical locality, remains prospectable, and is not cheaply manufacturable by relevant source participants under a quantified model. The framework also refuses to equate existence with discovery, classification, claim, custody, ownership, or transfer.

Whether any construction satisfies that conjunction is unresolved. Establishing novelty would additionally require a systematic prior-art review beyond the sources above. Research Pass 0 therefore advances definitions, comparison tests, and negative results—not a novelty or security claim.

## 6. Primary sources

- Stuart Haber and W. Scott Stornetta, [“How to Time-Stamp a Digital Document”](https://doi.org/10.1007/BF00196791), *Journal of Cryptology* 3 (1991).
- Scott A. Crosby and Dan S. Wallach, [“Efficient Data Structures for Tamper-Evident Logging”](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident), USENIX Security 2009.
- IETF, [RFC 9162: Certificate Transparency Version 2.0](https://www.rfc-editor.org/rfc/rfc9162.html), especially Sections 2.1.3–2.1.4, 8.2–8.3, and 11.3.
- Git, [“Git Objects”](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects), [`gitrepository-layout`](https://git-scm.com/docs/gitrepository-layout), and [`git-gc`](https://git-scm.com/docs/git-gc).
- SWHID Working Group, [SWHID specification v1.2](https://www.swhid.org/specification/v1.2/); Roberto Di Cosmo, Morane Gruenpeter, and Stefano Zacchiroli, [“Identifiers for Digital Objects: the Case of Software Source Code Preservation”](https://hal.science/hal-01865790), iPRES 2018.
- Satoshi Nakamoto, [“Bitcoin: A Peer-to-Peer Electronic Cash System”](https://bitcoin.org/bitcoin.pdf); Bitcoin Developer Reference, [“Block Chain”](https://developer.bitcoin.org/reference/block_chain.html).
- Ordinal Theory Handbook, [overview](https://docs.ordinals.com/overview.html) and [inscriptions](https://docs.ordinals.com/inscriptions.html).
