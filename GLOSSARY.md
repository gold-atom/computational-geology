# Provisional Glossary

**Status:** Research Pass 0 vocabulary. These terms are hypotheses for comparison, not a frozen specification or a claim that software systems literally behave like physical geology.

Where a geological word carries more intuition than the technical definition can support, the technical definition controls and the word should be replaced.

## Core terms

### Assay

A deterministic procedure that evaluates a candidate and witness against a specific formation descriptor and ore definition. Equal-input agreement is reproducibility; independent verification additionally requires source/view evidence obtainable without trusting the discoverer. An assay does not assign ownership or prove that the underlying history was honestly produced.

### Candidate

A canonical structure extracted from formation material before the ore predicate is applied. Multiple serializations, proofs, or overlapping descriptions may represent one candidate; a predeclared candidate schema, not a later ore predicate, states the equivalence rule for strong prior-existence claims.

### Candidate schema

A versioned occurrence grammar fixing extraction, canonicalization, equivalence, ore-independent identity, and execution semantics. If a formation template fixes the schema before closure, later ores can classify an already-fixed occurrence universe. A later classifier that supplies the schema instead performs weak retrospective typing.

### Claim

An assertion by an actor about an object—for example priority, discovery, custody, or a requested right. A claim is a later record and is not evidence that the object began to exist when claimed.

### Classification

Application or publication of an ore definition that partitions or labels historical structures. Classification can occur after the source history. Unrestricted classifier choice can manufacture arbitrary apparent rarity, so a class's selection process and degrees of freedom are part of its evidence.

### Closure

A family of separately stated conditions: a fixed and reached boundary; no later valid extension/removal; settlement under a quantified reversal bound and horizon; pinned semantics; and evidence binding a view to bytes. A commitment may give evidentiary closure without proving source completeness. Availability is separate. Closure is always relative to a declared source, view, adversary, probability, and time horizon.

### Commitment

A binding digest or authenticated data structure associated with historical material. A commitment can make later alteration detectable under cryptographic assumptions. By itself it does not prove completeness, availability, honest timestamps, uniqueness of the publisher's view, or manufacture resistance.

### Computational geological primitive

A complete history-derived object construction satisfying G1–G8 in [`THEORY.md`](THEORY.md), including source-causal separability and a nontrivial historical manufacture bound. G1–G7 describe only a geological candidate; G1–G6 may be ordinary retrospective indexing. Component interfaces such as an assay, stratum record, or fault marker have only their separately stated guarantees. Research Pass 0 admits no complete construction under this definition.

### Custody

Control of a witness, archive, credential, key, or physical storage medium associated with an object. Custody may enable proof or transfer but does not imply existence, discovery priority, or ownership.

### Discovery

An observer-relative epistemic event in which an observer obtains a candidate and enough evidence for an assay to accept it. Discovery may remain private; its actual first time is generally unverifiable. It changes knowledge, not the underlying object set.

### Existence

Membership in `Objects(F,Q,O,H*)` for a fixed formation, candidate schema, ore definition, and admissible history view. Two readings must be distinguished when classification is introduced later:

- **substrate existence:** the historical occurrence predates classification;
- **ore-relative existence:** after the ore definition is fixed, the occurrence's membership is determined entirely by the older substrate.

The second does not prove that the category itself was fixed before classification.

### Formation

A bounded or named body of historical material derived by applying a formation template to an admissible source view. Its identity-bearing core excludes evolving signatures, closure/settlement observations, archive locations, and availability evidence. For a public canonical source, its realization should be derivable whether or not anyone publishes it; a publisher-chosen private archive remains self-attested. A formation may satisfy some closure conditions and fail others.

### Formation template

A rule fixed before source realization that selects a source, coordinate domain, boundary, canonical view, semantics, candidate-schema registry, and availability policy. The identity-bearing realization adds source coordinates and a content commitment; evolving closure and availability evidence refers to that ID separately. Post-hoc template or boundary selection is an adversarial choice.

### Fossil

A candidate historical occurrence that satisfies a specified ore definition and has a stable occurrence identity. “Fossil” is useful only if the occurrence predates its discovery and cannot be multiplied by alternate encodings or claims; the label alone does not establish G7 source-causal separability or G8 manufacture resistance.

### Geological integrity

The conjunction of the exact properties a candidate claims—never a synonym for hash rarity. At minimum, reports should separately state closure, view convergence, availability, discovery non-creation, identity stability, locality, and measured manufacture resistance.

### Historical coordinate

A canonical reference into a source history under pinned semantics. Examples might include a block height plus transaction index or a ship, desk, and Clay commit identity. A participant-selected timestamp is not sufficient on its own.

### History source

A system that produces ordered or partially ordered records under explicit validity, view-selection, availability, and interpretation rules. “History” does not imply global consensus or permanence.

### Inventory

The cardinality or complete membership of the object set for one fixed `(formation, candidate schema, ore, view)` tuple. Unknown cardinality, unknown member identities, and an incomplete public discovery catalog are distinct claims. Inventories belonging to different schemas or ore definitions must not be added without an explicit aggregation rule.

### Locality

Authenticated historical coordinates and relations that exist under source semantics independently of the geological overlay and materially constrain admission, causation, observation, participant control, or availability. Locality should usually be time-indexed. A freely copied label—even one made validity-relevant only by an assay—is not locality.

### Non-mintable

Reserved here for a primitive with discovery non-creation, source-causal separability, and a nontrivial pre-closure manufacture threshold or scaling law under a stated actor, capability, budget, security parameter, probability, information, and horizon model. Use **discovery-independent** or **post-closure invariant** for the weaker fact that discovery, publication, and claims do not alter a fixed object set.

### Object

A stable identifier assigned to an equivalence class of qualifying historical occurrences under a fixed ore definition. The object is distinct from every witness, discovery record, title, token, or physical copy of its data.

### Occurrence identity

An identifier for canonical source material independent of whether it qualifies as ore or which overlapping formation includes it. Keeping occurrence identity separate from formation membership and ore-qualified object identity prevents wrappers and later classifiers from multiplying or rewriting provenance.

### Ore

A provisional name for a deterministic class over a fixed candidate schema: predicate, parameters, optional grade rule, assay procedure, runtime/version, resource rule, and test vectors. Selection, commitment/reveal, authorship, and trial history are separate provenance records so identical semantics retain one ore ID. Ore does not define base occurrence equivalence or identity in a strong prior-existence model. It is a classification rule, not the object, its witness, or its economic value.

### Ownership

A right recognized by some external rule system. Ownership requires naming that system and its transition rules. It does not arise automatically from existence, finding, knowledge, custody, or a cryptographic signature.

### Provenance

Evidence about origin, historical coordinates, classification, discovery, publication, claims, custody, and transformations. Provenance is structured evidence, not one undifferentiated chain. Each relation should be typed and independently checkable.

### Prospecting

Searching already-fixed formation material for candidates satisfying a fixed ore definition. If the searcher alternates varying admissible source material with evaluating the predicate until it passes, the activity is production, mining, or grinding rather than prospecting regardless of iteration cost.

### Permissionless prospectability

The property that, during a declared availability interval, a fresh unprivileged party can obtain query-sufficient formation material and search any admitted ore without approval or secrets from the publisher, prior discoverers, claimants, or a privileged witness service. It is stronger than permissionless verification of one supplied witness and must state access costs, rate limits, and erosion behavior.

### Publication

Communication of a formation, ore, discovery report, claim, or witness at an authenticated coordinate. A discovery report proves publication under its registry assumptions, not first private discovery, existence, ownership, or complete public inventory.

### Stable identity

The property that all equivalent valid witnesses for one historical occurrence resolve to one object identifier across honest verifiers under the same pinned candidate schema, ore, and semantics version. Version changes use explicit alias, migration, or branch relations; they never silently inherit identity.

### Stratum

A deterministic commitment to a historical interval or state, together with enough metadata to interpret and locate its material. A digest without a source boundary, semantics version, and availability story is not yet a useful stratum.

### Transfer

A rule-system event that changes recognized ownership, control, or custody. Transfer affects a relation to an object, not the object's historical existence.

### Witness

The data required by an assay to demonstrate that a candidate is in the object set. A witness may include source material, inclusion and consistency proofs, signatures, or commitments. Losing a witness can make an object unassayable without making a claim of continued existence independently useful.

## Source-model terms

### Endogenous geology

Formation material derived from activity controlled in material part by participants who may benefit from discoveries. The default threat is manufactured rarity.

### Exogenous geology

Formation material derived from an external history whose manipulation is outside an application participant's affordable capability under stated assumptions. Exogeneity is never absolute: an application participant may also be an external block producer, operator, or censor.

### Composite geology

Formation material defined from both local/network history and an external consensus or commitment source. The construction inherits the assumptions and attacks of every component plus the binding between them.

## Geological analogies under investigation

### Erosion

Loss of underlying historical material while commitments, summaries, current state, or discovery records survive. Erosion may preserve evidence that *some* bytes once existed without preserving enough data to assay new or old objects.

### Fault

A documented discontinuity or divergence between otherwise related historical sequences or views. A fault descriptor must identify both sides and the evidence for divergence; it is not a license to hide an ambiguous canonical history.

### Intrusion

An externally sourced record or commitment incorporated into a local formation. A Bitcoin anchor in an Urbit-derived formation is a possible intrusion. It imports ordering or cost assumptions, not automatic truth about the local preimage.

### Metamorphism

A later classification that reveals a deterministic property of older material without changing that material. Metamorphism is legitimate as retrospective analysis, but it cannot by itself establish that a category or rarity claim was fixed earlier.

### Unconformity

A boundary at which expected history is missing, pruned, reset, or not comparable under the same semantics. Treating absence as an unconformity requires positive evidence of the boundary; otherwise it may be ordinary data loss or selective omission.

## Terms to avoid without qualification

| Term | Required qualification |
|---|---|
| immutable | state the fork, rewrite, key-compromise, governance, and semantics assumptions |
| permanent | distinguish current-state persistence from retention of original events and witnesses |
| global | distinguish a global namespace from globally replicated data or globally agreed history |
| scarce | identify whether scarcity concerns occurrences, object IDs, discoveries, claims, or rights |
| unknown supply | name the ore, formation, observer, time, information set, and resource bound |
| random | identify the source and every party able to select, withhold, or bias it |
| region | state the authenticated membership rule and time coordinate |
| provenance | enumerate the specific typed evidence actually retained |

## Prohibited conflations

```text
rare digest        ≠ costly-to-manufacture history
committed root     ≠ complete or available archive
deterministic node ≠ shared canonical view
current state      ≠ retained event history
address prefix     ≠ current sponsor set
sponsor set        ≠ actual routing or update path
discovery record   ≠ object creation record
first publication  ≠ ownership
key control        ≠ historical authorship
closed formation   ≠ unknown inventory
```
