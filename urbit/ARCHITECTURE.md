# Urbit Architecture Relevant to Computational Geology

**Research date:** 2026-09-04
**Status:** Factual source review plus explicitly labeled inferences. No claim that Urbit currently implements geological primitives.

## 1. Evidence labels

- **Existing:** behavior or data structure documented or implemented in the cited Urbit/Azimuth source.
- **Inference:** consequence derived from existing behavior; it should be tested against a running pinned release.
- **Proposed:** new machinery that does not currently exist as an Urbit guarantee.

This distinction matters because Urbit has suggestive words—ships, desks, continuity, sponsorship, global namespace—whose actual security meanings are narrower than the metaphors.

## 2. Urbit ID and Azimuth

### 2.1 Point coordinate, activation, and rank

**Existing.** Azimuth represents galaxies, stars, and planets as 32-bit points with rank/prefix functions. The contract's numeric ranges imply 256 galaxies, 65,280 star-rank points, and 4,294,901,760 planet-rank points; some higher-level documentation rounds these to `2^8`, `2^16`, and `2^32`. See the pinned [`Azimuth.sol` rank and prefix functions](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Azimuth.sol#L682-L705) and the official [Azimuth Hoon School explanation](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/hoon-school/C-azimuth.md#L55-L97).

**Existing.** A possible numeric coordinate is not the same as an allocated or active identity. Ecliptic's spawn paths check authority and unused state. Direct spawn records, activates, and assigns the point; indirect spawn records the child and holder/transfer-proxy relation while leaving activation for a later operation. Both are intentional allocation/creation paths under this project's distinction, not retrospective discovery. See pinned [`Ecliptic.sol` spawning logic](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Ecliptic.sol#L360-L460).

### 2.2 Four relations that must remain separate

| Relation | Existing representation | Stability |
|---|---|---|
| Numeric point/prefix | deterministic `uint32` and rank/prefix functions | stable as syntax under pinned rules |
| Ownership and proxies | Azimuth `Deed` fields | intentionally transferable/mutable |
| Effective sponsorship | point state plus escape/adopt/detach and L2 interpretation | mutable and time-indexed |
| Ship state/history | local pier, Arvo state/event log, Clay/Gall data | locally operated; not committed by Azimuth |

[`Azimuth.sol`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Azimuth.sol#L112-L210) stores networking keys, spawned children, activity/sponsorship fields, `life`, and `rift` in `Point`, while `Deed` separately stores owner and management, spawn, voting, and transfer proxies. It contains no commitment to a ship's Clay, Gall, or complete Arvo history.

**Inference.** Transferring a star does not transfer independently owned descendants or their piers. On-chain ownership, control of current network keys, custody of a pier, and authorship of old events are different provenance facts.

### 2.3 Sponsorship and software source

**Existing.** Activation begins with a default sponsor derived from a prefix, but escape/adopt and detach operations change sponsorship. See [`Azimuth.sol`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Azimuth.sol#L543-L555) and [`Ecliptic.sol`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Ecliptic.sol#L586-L680).

**Existing.** Changing sponsor does not itself force the same OTA source; the user manual instructs a separate `|ota` operation after a sponsor change. See [Using Bridge](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/id/using-bridge.md#L77-L96).

**Inference.** “Under star S” could mean numeric prefix, original spawning parent, current sponsor, or current software source. These sets need not match.

### 2.4 Life, rift, transfer, and reset

**Existing.** `life` counts networking-key revisions and `rift` counts personal continuity breaches; a breach may increase `rift` without changing keys. See [Life and Rift](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/life-and-rift.md#L16-L42).

**Existing.** A transfer can preserve continuity or include a reset, depending on the operation. See [`Ecliptic.sol`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Ecliptic.sol#L464-L582).

**Existing.** The factory-reset guide describes reset as clearing the ship's event log and asking peers to discard networking sequence state. It requires a new pier and loss/reconstruction of application subscriptions. See [Guide to Factory Resets](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/id/guide-to-resets.md#L16-L59).

**Inference.** A persistent `@p` is not a continuous immutable history. At minimum, historical coordinates should include `rift`; key-sensitive evidence should also include `life`.

**Inference.** A valid signature authenticates a message/key relation, not its claimed historical time. A current or compromised retired key can sign a past-looking envelope. Historical provenance therefore also needs authorization-at-coordinate evidence plus an independently constrained publication coordinate or a forward-secure construction; `@p` and a valid signature alone are insufficient.

### 2.5 Literal Azimuth claims

**Existing.** Azimuth's separate Claims contract lets point managers add, update, and remove claims; it recommends removing identity claims before transfer, and Ecliptic may clear them. See [`Claims.sol`](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Claims.sol#L8-L21) and its [mutation functions](https://github.com/urbit/azimuth/blob/bcf1d7bcf64cd73a3688434feb786be39a116819/contracts/Claims.sol#L70-L145).

**Inference.** Even Urbit's literal claim primitive is controller-authored mutable metadata. It must not be used as geological existence.

### 2.6 Layer 1 and naive-rollup Layer 2

**Existing.** Layer-1 Azimuth state is executed by Ethereum contracts. The official [L2 overview](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/l2/README.md#L32-L58) describes signed transactions collected into batches and published to Ethereum, with resulting state transitions calculated by Urbit's `naive.hoon`. The same documentation states that effective L2-aware sponsorship state used by a ship can differ permanently from the L1 Azimuth contract view ([state distinctions](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/l2/README.md#L90-L117)).

**Existing.** The `%azimuth` Gall agent maintains locally derived PKI state and known logs from a configured Ethereum source; `%eth-watcher` collects Ethereum event logs. See [Azimuth data flow](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/flow.md#L24-L89).

**Existing.** Ecliptic business logic is upgradeable through galaxy voting. See [Ecliptic reference](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-id/ecliptic.md#L16-L24).

**Open verification requirement.** A production historical descriptor would need exact Ethereum block endpoints, contract/code versions, batch data, `naive.hoon` semantics, disavow/reorganization behavior, and a proof that a new independent observer can reconstruct the same historical effective state. The documentation is not itself that proof.

## 3. Arvo, Vere, and the pier

### 3.1 Deterministic local state

**Existing.** Arvo is modeled as a deterministic transition function; its current state is a pure function of its event history. The pinned [Arvo architecture](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/README.md#L52-L71) gives both `(State, Input) → (State, Output)` and `History → State` formulations. Pinned [Clay architecture](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/architecture.md#L20-L22) states that effects are emitted only after the event has been persisted.

This is highly relevant: a retained, pinned event sequence can in principle be replayed deterministically.

It is not global consensus. Each ship runs its own state machine over its own admitted inputs.

**Existing.** In the inspected Vere implementation, an ordinary disk event record contains a jammed event plus a 31-bit `mug`; replay recomputes state and compares the stored `mug` ([event serialization](https://github.com/urbit/vere/blob/44cf01074a09facb0b89d8ac046c582be7318768/pkg/vere/disk.c#L118-L157), [replay check](https://github.com/urbit/vere/blob/44cf01074a09facb0b89d8ac046c582be7318768/pkg/vere/mars.c#L975-L1010)). A [`mug`](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/hoon/stdlib/2e.md#L18-L50) is a non-cryptographic 31-bit Murmur-derived hash. This format supports local replay/divergence detection; no cryptographic previous-record chain or portable author signature was found in that serialization. Other integrity layers require separate audit before making a system-wide claim.

### 3.2 State persistence versus historical retention

**Existing.** The Vere manual calls a ship event log a totally ordered list of that ship's Arvo events and says state can be rebuilt by replay. It also documents event-log epochs and the `chop` command, which deletes all but the two newest epochs, after which replay from the beginning is impossible. See pinned [Vere: Truncate event log](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/running/vere.md#L139-L182).

**Existing.** Arvo documentation likewise says runtimes may snapshot current state and delete earlier event history because logs grow linearly. See pinned [Arvo: Event log](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/arvo/README.md#L86-L96).

**Inference.** Urbit's strong current-state persistence does not provide permanent query-sufficient history for future classifiers. A state snapshot may preserve a derived fact while erasing the event-level terrain from which a new ore would be computed.

### 3.3 Host time is not consensus time

**Existing.** For a poke, the inspected Vere source obtains time from host `gettimeofday()` ([`_mars_work`](https://github.com/urbit/vere/blob/44cf01074a09facb0b89d8ac046c582be7318768/pkg/vere/mars.c#L563-L605)). Arvo's monotonic-time assertion is commented out with the explanation that Vere timestamps are unreliable ([Arvo `poke`](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/arvo.hoon#L1887-L1902)). Clay passes this `now` into local commit construction ([Clay `park`](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L1870-L1888)).

**Inference.** A Clay date is operator-influenceable host time, not a global clock, monotonic sequence guarantee, or closure certificate. A date-bounded formation requires independent witnessing or an external settlement coordinate.

## 4. Clay

### 4.1 Existing revision semantics

**Existing.** Each ship holds independently revision-controlled desks. A Clay `$yaki` contains parents, a path-to-page-hash namespace, self-reference, and date; page IDs use SHA-256, while commit construction hashes parents, namespace, and date into the `$tako` ([types](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/lull.hoon#L2621-L2643), [hash construction](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/lull.hoon#L2727-L2757)). The commit identity binds those fields, but not ship, desk, local revision/aeon, continuity era, author, publication event, or signature. The revision-to-commit map is stored separately in the desk state ([Clay data types](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/data-types.md#L469-L497)).

**Existing.** Clay's `$beam = [ship desk case path]` omits `life` and `rift` ([`$beam`](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/data-types.md#L319-L339)). Because a reset starts a fresh pier under the same `@p`, the same `(ship, desk, revision)` syntax can be rebound across continuity. A geological coordinate needs a separately witnessed association among continuity, desk/revision, and commit hash.

**Existing.** Merge `%init` and some `%fine` paths can reuse a source commit object and map it to the destination desk's next local aeon ([merge behavior](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L2376-L2473), [`park`](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L1877-L1888)). Thus one commit can appear at multiple ship/desk/revision contexts; copying does not prove origin or locality.

**Source-grounded inference requiring a runtime test.** A hard `|new-desk` over an existing desk passes no parent commit, creates an empty-parent commit, and advances the desk revision ([command documentation](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/os/dojo-tools.md#L2242-L2295), [generator](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/gen/hood/clay/new-desk.hoon#L11-L27), [helper](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/zuse.hoon#L4451-L4459)). A numbered interval therefore cannot assume uninterrupted ancestry; graph validation must detect disconnected roots.

**Existing.** Tombstoning can remove an old page body while its hash reference survives; reading then fails. `%seek` requests missing pages from a reachable source and recomputes page hashes, but cannot recover a preimage from its hash ([tomb implementation](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L6374-L6444), [documented effect](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/user-manual/os/dojo-tools.md#L2299-L2380), [backfill](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L3485-L3517)). Commit structure may therefore survive erosion while prospectable content does not.

Desks and branches remain user-controlled revision structures, not consensus chains. A retained corpus can support independent recomputation of page/commit hashes, but Clay alone does not prove source completeness, exclusive publication history, intrinsic ship/desk origin, or permanent availability.

### 4.2 “Global” namespace does not mean global ledger

Clay documentation calls the namespace global because paths can name another ship and its desk/revision. Its own data types describe foreign desks as data about a neighbor cached on the local pier.

**Existing.** If remote material is absent locally, Clay asks the source ship; success depends on that source and permissions ([Using Clay](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/clay/using.md#L18-L28)). On a peer breach notification, Clay cancels subscriptions and deletes that peer's foreign-desk state ([breach handling](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/clay.hoon#L6252-L6280)).

**Inference.** Remote addressability and synchronization do not imply:

- universal replication;
- one globally selected commit per desk;
- permanent serving by the source ship;
- proof that a published branch was the only private branch; or
- completeness of all historical application events.

Any geological use needs a canonical export and archive policy independent of the phrase “global filesystem.”

## 5. Gall agents

**Existing.** Gall is Arvo's application framework. Agent state lives within the local persistent Arvo state rather than normally being serialized into Clay. The pinned [App School Arvo overview](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/app-school/1-arvo.md#L63-L71) notes that most application data live in Gall/vanes, while Clay primarily holds source and related files.

**Existing.** Gall agents handle event-driven transitions and may exchange pokes/subscriptions across ships. During a code upgrade, `+on-save` exports state and the new `+on-load` imports or migrates it into the new agent version. See pinned [Gall agent lifecycle](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/app-school/4-lifecycle.md#L20-L32). Current Gall `%nuke` handling replaces a running agent with a placeholder and discards its state; see pinned [Gall source](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/gall.hoon#L913-L947).

**Inference.** Gall is a plausible implementation environment for a formation publisher, indexer, or assay agent. Gall state is not automatically public, globally replicated, historically queryable, or immune to owner-generated inputs. Upgrade migration can transform state, so a historical assay must pin code and state semantics rather than merely an agent name.

## 6. Ames and directed messaging

### 6.1 Legacy Ames properties

**Existing.** Ames maps Urbit identities to an overlay over physical network lanes. Its documented guarantees include encryption for permanent ships, deduplication/only-once delivery to a destination vane, and total message order **within a flow**. Order across flows is unspecified. On breach, Ames discards peer messaging state and does not maintain its guarantees across the boundary. See pinned [Ames technical overview](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/urbit-os/kernel/ames/README.md#L24-L60) and pinned [Ames source](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/ames.hoon#L1-L77).

**Existing.** Peer discovery and packet relay use learned/direct routes and fallback infrastructure; route, flow, peer, and quality data are local state. Pinned code shows route selection and fallback behavior ([route logic](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/ames.hoon#L4600-L4755), [peer/route maintenance](https://github.com/urbit/urbit/blob/08026c84b29e9ba47b1764d109f5a646e1db7ff2/pkg/arvo/sys/vane/ames.hoon#L5370-L5536)). Physical IP/port and NAT mappings are mutable operational state, not durable historical coordinates.

**Inference.** Ames supplies bilateral delivery semantics to applications, not a global network event order or public message archive. Relay participation does not imply retention of packet contents or durable evidence available to third parties.

### 6.2 Current protocol heterogeneity

**Existing release evidence.** [`408k`](https://github.com/urbit/urbit/releases/tag/408k) incorporated the Directed Messaging/Mesa machinery from [PR #7208](https://github.com/urbit/urbit/pull/7208), but its release note described a staged rollout: manual activation and continued migration by pre-release peers first, with automatic activation promised for `408k-1`. The actual [`408k-1`](https://github.com/urbit/urbit/releases/tag/408k-1) note says it does nothing for ships already on 408, while current [`408k-2`](https://github.com/urbit/urbit/releases/tag/408k-2) notes further Mesa fixes without establishing the network-wide rollout state.

**Inference.** A formation must pin and observe the transport semantics actually used; it cannot infer a homogeneous 2026 network from a release tag. Mesa route/liveness state remains observer-local, and exact deployed authentication, replay, migration, and fallback behavior require separate audit.

## 7. Desks and application distribution

**Existing.** Apps are distributed as Clay desks containing source, marks/types, configuration, and optionally Gall agents. The pinned [software distribution overview](https://github.com/urbit/docs.urbit.org/blob/f6bfd25b0ab738930f799f77de93d8b1f7979b09/content/build-on-urbit/userspace/dist/README.md#L16-L63) describes self-contained desks and distribution, while app front ends may be obtained over Ames or HTTP.

**Inference.** A desk can distribute an ore definition or assay implementation, but installation does not make its publisher's data canonical. A reproducible ore manifest should commit to code, dependencies, kernel/kelvin compatibility, runtime semantics, and test vectors independently of a mutable distribution pointer.

## 8. Durability and reconstructability matrix

| Material | Exists today? | Normal authority/control | Independently reconstructable? | Geological limitation |
|---|---:|---|---|---|
| Azimuth L1 point/deed history | yes, via Ethereum history | authorized keys + Ethereum consensus | under Ethereum archival/view assumptions | identity control history, not ship event history |
| Azimuth L2 effective state | yes, locally derived from published batches | signed actors, rollers, interpretation code | **requires independent verification** | L1 state alone can differ from effective state |
| Current Arvo state/snapshot | yes, per pier | ship operator + admitted inputs | only with snapshot or sufficient event history | not globally shared; snapshot hides old event terrain |
| Full Arvo event history | possible locally | ship operator/runtime | if all epochs, boot inputs, and semantics retained | ordinary record check is a 31-bit `mug`; old epochs can be chopped; reset clears continuity |
| Clay desk history | yes, per ship/cache | desk publisher and merge operations | content/ancestry for a complete retained and independently rehashed corpus | commit omits ship/desk/revision/author; source analysis suggests hard overwrite can disconnect roots (runtime test pending); page bodies can be tombstoned |
| Gall application state | yes, inside Arvo | agent code, operator, incoming events | with adequate state/history and pinned migrations | not automatically public or revision-queryable |
| Ames flow/delivery state | yes, local operational state | communicating ships/network conditions | not as a global historical record | only per-flow order; breach ends guarantees |
| Route/IP/port/hop data | yes, transient/local | NAT, runtime, intermediaries | generally no durable common view | mutable and observer-dependent |
| App/desk distribution lineage | partially | publisher, installer, OTA choices | if commits/blobs/source relations retained | sponsor, OTA source, and installed code may diverge |

## 9. Can star subtrees be regions?

At least five different region functions are possible:

1. **Prefix region:** all numeric planet coordinates with a star prefix. Stable and deterministic, but mostly a syntactic, fully enumerable potential address range.
2. **Spawn-provenance region:** points historically spawned by a star. Authenticated through Azimuth history but intentionally created by the controller.
3. **Sponsor region at state `t`:** points effectively sponsored by a star in a pinned L1/L2 state. Meaningful and time-indexed, but mutable and strategic.
4. **Operational routing/update region:** ships actually using a star/galaxy for relaying, discovery, or software. Dynamic, observer-dependent, and not equivalent to sponsorship.
5. **Shared-history region:** ships contributing to one committed formation. This would be **proposed**; Urbit does not supply it automatically.

**Pass 0 conclusion:** a “star region” without a chosen relation and historical state is ambiguous. The safest current use is a syntactic prefix coordinate or a time-indexed effective-sponsorship relation, neither of which proves shared history or manufacture-resistant locality.

## 10. Factual conclusions

1. Urbit provides unusually rich **local** deterministic histories and durable identity/control coordinates.
2. Azimuth is a point/control/sponsorship graph, not a commitment to complete ship history.
3. Arvo persistence preserves current state strongly, while ordinary maintenance and resets can remove the event material needed for future prospecting.
4. Clay provides content/ancestry integrity for retained material, but a commit does not intrinsically prove ship/desk locality or publication; source analysis indicates a hard overwrite may introduce an ancestry break (runtime confirmation pending), and referenced page bodies can be deleted.
5. Gall can host new research applications; it is not itself an independent consensus or archive.
6. Documented legacy Ames provides authenticated, scoped peer communication and per-flow ordering; current Mesa deployment, authentication, and replay behavior require verification, and neither supplies a total network history.
7. Star/planet hierarchy does not yield one unambiguous, durable region relation.
8. Urbit therefore supplies components for **proposed** composite geological primitives, not a ready-made global geology.

## 11. Items requiring independent verification

- current Vere `chop`, snapshot, garbage-collection, and replay behavior across supported releases;
- exact retention of old Clay commit nodes/blobs after normal cleanup and remote publisher disappearance;
- runtime confirmation of hard desk overwrite producing an empty-parent root at the next aeon;
- adversarial validation of incoming foreign commit self-references;
- every Vere at-rest integrity layer beyond the inspected ordinary event-record serialization;
- full reconstruction of L2-aware Azimuth history from Ethereum plus public batch data;
- current live Ecliptic contract/code versions versus older public repositories;
- exact `naive.hoon` version binding and reorg/disavow semantics;
- Mesa's current wire authentication, replay, ordering, and breach behavior;
- whether raw network inputs or only admitted Arvo events remain in logs; and
- app-state behavior across uninstall/reinstall and incompatible migration code.

These are empirical tasks, not details to fill with analogy.

## 12. Primary-source pins

- Urbit documentation repository at [`f6bfd25b0ab738930f799f77de93d8b1f7979b09`](https://github.com/urbit/docs.urbit.org/tree/f6bfd25b0ab738930f799f77de93d8b1f7979b09).
- Azimuth contracts at [`bcf1d7bcf64cd73a3688434feb786be39a116819`](https://github.com/urbit/azimuth/tree/bcf1d7bcf64cd73a3688434feb786be39a116819).
- Urbit/Arvo source excerpts at [`08026c84b29e9ba47b1764d109f5a646e1db7ff2`](https://github.com/urbit/urbit/tree/08026c84b29e9ba47b1764d109f5a646e1db7ff2).
- Vere source excerpts at [`44cf01074a09facb0b89d8ac046c582be7318768`](https://github.com/urbit/vere/tree/44cf01074a09facb0b89d8ac046c582be7318768).
