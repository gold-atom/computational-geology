# Endogenous, Exogenous, and Composite Geology

**Status:** Comparative models for Research Pass 0. They classify where formation material comes from; they do not certify a construction.

## 1. Comparison

| Dimension | Endogenous | Exogenous | Composite |
|---|---|---|---|
| Formation source | Participant/network activity | External historical system | Local/network material bound to external history |
| Default control concern | Direct input manufacture | Producer bias, withholding, censorship, reorg | All component attacks plus binding failures |
| Natural strength | Rich local causality and semantics | Shared ordering/settlement cost | External cutoff and evidentiary closure for meaningful local material |
| Natural weakness | Grinding, spam, Sybils, private forks | Weak locality to the application; not unbiased | Anchor proves a commitment, not local completeness |
| Unknown-inventory prospect | Rich but easily manufactured candidate surface | Fixed public domains are often enumerable | Potential search space with explicit closure |
| Required evidence | Admission/control/influence law | External consensus and economic assumptions | Local completeness + external finality + source binding |

## 2. Endogenous geology

### Definition

The prospective beneficiaries materially control the events from which formations are derived. In Urbit this might include a ship's app events, Gall state transitions, Clay commits, messages it chooses to send, or identities/relationships it can create or change.

### What it can express

Endogenous material can encode genuine network history:

- causal application transitions;
- bilateral or multi-party interactions;
- software lineages;
- membership trajectories; and
- long-lived local state.

This semantic density is attractive. It also supplies many knobs to attackers.

### Presumption of failure

If a participant can cheaply create more valid events, choose their bytes, split activity across Sybils, privately test branches, or commit only successful results, a rare predicate is a production rule. Hashing the result after the fact does not help.

An endogenous candidate must specify an admission law that constrains event opportunities independently of the beneficiary. Candidate controls include cross-party receipts, rate-limited scarce resources, multi-witness thresholds, or a canonical external schedule. Each adds assumptions and can still leave content grinding.

### Research questions

- Can interaction between independently controlled ships create canonical event opportunities without a trusted global sequencer?
- Can each participant's marginal and cumulative influence be bounded under adaptive withholding?
- Can complete formation material be proven without globally replicating every event?
- Can locality remain meaningful when identities and sponsors move?

No positive answer is assumed.

## 3. Exogenous geology

### Definition

The application derives formation material from a history that its ordinary participants cannot affordably control under a declared threat model.

Bitcoin headers are a candidate source because they have a canonical proof-of-work selection rule and widely replicated history. They remain miner-produced, probabilistically final, and manipulable within consensus-valid choices.

### Potential contribution

- common historical coordinates;
- objective ordering under one chain view;
- a costly rewrite condition;
- public commitments to transaction sets; and
- header-derived inputs not wholly chosen by an ordinary application user; transaction bytes remain submitter-controlled.

### Limits

- miners select and order transactions and choose coinbase data and any transactions they themselves create;
- timestamps are bounded claims, not precise wall-clock truth;
- blocks and transactions can be withheld or censored;
- chain history can reorganize;
- an application participant may also be a miner;
- fixed historical headers are publicly enumerable; and
- chain work is shared security, not exclusive substance belonging to each derived object.

Exogeneity must therefore be expressed as a manipulation-cost or influence bound, never as “participants cannot control it.”

## 4. Composite geology

### Definition

A composite descriptor binds material from at least two source domains, commonly a semantically rich local history and a publicly ordered external anchor.

One schematic example is:

```text
local archive A_i
  → canonical encoding
  → Merkle root r_i
  → descriptor (source, interval, semantics, r_i)
  → external publication at anchor coordinate b
```

After sufficient settlement under the chosen external source's rule, `b` can supply a public chain-relative publication coordinate and an ordering among published descriptors. Any wall-clock or finality interpretation inherits that source's assumptions.

### Properties potentially unavailable from either source alone

1. **Semantically meaningful, externally sealed locality:** local records retain ship/application coordinates while an external history fixes a public commitment coordinate under its own settlement and view rules.
2. **Cross-ship comparison:** independently operated ships can publish commitments into one reference history without making their internal states globally consensual.
3. **Fixed prospecting domain:** a predeclared cutoff, fixed candidate schema, independently constrained selection rule, and retained archive can bound a body of local material for later ore definitions.
4. **Fault evidence:** later inconsistent local roots can be compared with the anchored descriptor.

These are research hypotheses, not established primitives.

### What the anchor cannot prove

An external commitment does not prove that:

- `A_i` contains every relevant local event;
- timestamps or authorship inside `A_i` are truthful;
- the publisher did not grind or fork `A_i` before anchoring;
- every observer received the same preimage;
- the preimage remains available;
- the local semantics were correctly executed; or
- the external producer did not censor or bias the anchor.

### Binding requirements

A serious composite candidate needs:

1. canonical source and archive encodings;
2. unambiguous interval boundaries in both domains;
3. a commitment that binds source identity and semantics version, not only a bare root;
4. inclusion and, where relevant, consistency proofs;
5. an archive replication and challenge policy;
6. reorganization behavior;
7. evidence for cross-party events;
8. explicit handling of late/missing commitments; and
9. a joint adversary model allowing correlated roles.

## 5. Composite constructions to test

| Candidate | Intended gain | Immediate counterexample/status |
|---|---|---|
| Single-ship archive + Bitcoin root | Public cutoff and evidentiary closure for one disclosed local interval | Ship privately forks or omits events before anchoring. Inconclusive as geology; useful as self-attestation. |
| Bilateral event receipts + external root | Stronger evidence that an interaction occurred | Parties may collude; nonparticipants cannot prove completeness; receipt retention required. |
| Star-sponsored regional root | Shared commitment for a time-indexed sponsor set | Sponsor membership is mutable; star can censor/omit; “region” relation must be pinned. |
| Multi-witness threshold root | Reduce single-publisher equivocation | Sybil and witness-selection problems; threshold agreement still does not prove unseen-event absence. |
| Cross-anchor root | Survive one anchor failure | Correlated miners, finality mismatch, last-revealer and availability complexity. More anchors can add attack surface. |
| Commit–challenge archive | Make omitted data challengeable before closure | Requires sampling soundness, response windows, incentives, and a durable challenger set. Not designed here. |

## 6. Model-selection rule

Use the weakest model that accurately describes the source. A local Urbit event log does not become exogenous because its ship has a scarce identity. A Bitcoin commitment to that log makes the result composite, not Bitcoin-native. A multi-party signature set does not create global consensus unless its membership and threshold have a justified trust model.

## 7. Research verdict

- **Endogenous:** richest semantics; strongest default grinding objection.
- **Exogenous:** strongest shared closure candidate; weakest application-specific locality and generally enumerable past.
- **Composite:** most promising way to combine semantic terrain with public closure, but its central unsolved problem is proving that sealed local terrain is complete and not strategically manufactured.
