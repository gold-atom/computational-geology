# Computational Geology and Sedimentary Media
## From historical specimens to creative works

*Concept paper. The historical-specimen tools are experimental; the media architecture described here is proposed. Neither implies demonstrated monetary scarcity or manufacture-resistant digital resources.*

## 1. History as material

Computational geology begins with a distinction between making something and finding something.

An ordinary production system creates an object through an authorized operation: a file is uploaded, a token is issued, a work is generated. Computational geology asks whether a sufficiently fixed computational history can contain identifiable structures whose discovery does not bring them into existence.

The historical material might be a software revision graph, a sequence of Bitcoin headers, or an authenticated event log. A specimen might be a return to an earlier state, an exceptional relationship between observations, or a causal formation spanning several records. The individual records may have been deliberately produced. The question is whether the particular structure being studied exists independently of the later system that discovers, classifies, and reports it.

This is the research program’s central distinction:

**History → formation → search → discovery**, rather than **intention → production → newly created object**.[^theory]

The analogy is not that hashes resemble stones. It is that a history might behave as material with properties that exceed its producers’ immediate intentions.

The new media proposal starts one step later. Once a specimen has been identified and assayed, it can become the basis of a creative work: a film, sound piece, image, text, performance, or executable environment. The work does not create the parent occurrence. It interprets it, takes constraints from it, or establishes a verifiable association with it.

Call this proposed practice **sedimentary media**:

> Creative works made in a declared relationship to identifiable formations in computational history.

Its simplest architecture is:

```text
COMPUTATIONAL HISTORY
        ↓
SPECIMEN DISCOVERY
        ↓
INDEPENDENT ASSAY
        ↓
CREATIVE ENVELOPE
        ↓
HUMAN / PROCEDURAL / GENERATIVE PRODUCTION
        ↓
MEDIA + EVIDENCE OF THE RELATIONSHIP
```

The historical source, the creative procedure, and the resulting artwork remain distinct objects.

## 2. What the geological claim requires

A finite dataset can always be searched for patterns. That alone is not a new kind of geology.

The project therefore distinguishes a historical pattern from a retrospective object, and both from a stronger manufacture-bounded geological primitive. The stronger claim requires evidence that source participants could not materially increase or target the qualifying object set under a stated adversary and resource model. Permissionless prospecting and genuinely uncertain inventory impose additional requirements.[^theory]

The existing Git prototype supplies a deliberately modest control. It searches one file’s first-parent history for three consecutive content runs of the form **A → B → A**. It assigns deterministic specimen identities, checks evidence against a local repository, and renders a catalogue. Missing evidence and contradicted evidence are different outcomes. Its documentation does not claim that a Git user is unable to manufacture the pattern deliberately.[^readme]

This distinction should carry into the media layer. A film derived from that Git specimen can have a reproducible historical relationship without inheriting manufacture resistance the specimen never established. A compelling artwork cannot upgrade the scientific classification of its source.

There is also a temporal distinction. A relationship in old material can predate its classification, but a classifier invented today was not necessarily part of yesterday’s world. Strong claims about ore-relative prior existence require the relevant schema and classifier to have been fixed beforehand; later classification must be identified as retrospective.[^theory]

Finally, unenumerated is not the same as unknowable. When a public formation has a manageable candidate space and cheap tests, its inventory can be counted. Sedimentary media does not need to conceal that fact. **A completely catalogued formation can still support indefinitely many interpretations.**

## 3. “21e8, but inverted”

One concrete historical 21e8 implementation describes publishing proof-of-work jobs that identify arbitrary material through its SHA-256 digest and specify a mining puzzle. In that construction, material is designated and computational work is requested in relation to it.[^21e8]

That gives a useful comparison, without pretending that one implementation exhausts every ambition associated with 21e8:

```text
Content-linked PoW:
content → work job → computational proof

Specimen-first media:
historical occurrence → assay → creative constraints → content
```

The inversion concerns **what precedes and conditions the artwork**.

Instead of beginning with an image and commissioning computation around it, the creator begins with an assayed occurrence and makes an image in response. The historical material becomes an input to production rather than a certificate attached only afterward.

This is not cryptographic reversal: the artist is not decoding a hidden movie from Bitcoin. The movie did not exist inside an old hash. It is made now. What predates it is a particular historical occurrence, and perhaps a previously specified rule for translating that occurrence into constraints.

Nor is the benefit necessarily scarcity. The more interesting benefit may be a creative starting point that the artist encounters rather than invents from nothing.

**The specimen is not the artwork’s price. It is part of the artwork’s situation.**

## 4. From specimen to score

The central media component is a **creative envelope**: a versioned procedure that translates an assayed specimen into a set of production constraints.

An envelope could specify temporal proportions, recurrence, framing, color relationships, sound events, spatial connectivity, or permitted transformations. It should normally leave substantial decisions to the artist.

Conceptually:

\[
E_v(o)=f_v\bigl(\operatorname{Core}(o),\operatorname{Features}(o)\bigr)
\]

Here, \(o\) is the specimen, \(v\) identifies the envelope recipe, and the features are independently checked historical properties. An artwork is then produced from the envelope and additional artistic decisions:

\[
M=g(E_v(o),A).
\]

The recipe is designed. History does not decree a frame rate or musical scale. What can be non-discretionary is the application of a published recipe to a specified specimen. The creator must distinguish historical measurements from the authored mapping applied to them.

Two modes are possible.

**Identifier-seeded work** uses a stable specimen identity to derive pseudorandom parameters. This provides a reproducible association, but its historical content may be thin: the ID functions chiefly as a seed.

**Structurally derived work** uses properties of the occurrence itself. Recurrence becomes repetition; causal branching becomes a branching score; intervals between authenticated coordinates become temporal proportions; shared ancestry becomes a shared motif.

The second mode is the more distinctive research direction because replacing the specimen with an arbitrary seed would remove information the work actually uses.

The envelope must depend on stable identity-bearing material and explicitly fixed features—not on a discoverer’s signature, archive URL, current verification tip, or interchangeable proof packaging. Obtaining better evidence should not accidentally change a film’s score.

Choosing the specimen and recipe remains an artistic act. Searching thousands of specimens for a preferred envelope is legitimate curation, but it is not evidence that the artist had no choice over the constraints. Any stronger non-selection claim needs its own procedure and evidence.

## 5. One specimen, three works

Consider a content-return specimen with three occurrence coordinates: A, B, then A again. A published recipe extracts the return structure and two intervals between those coordinates. It maps them to a fifteen-second score with an opening passage, an interruption, and a return.

Fifteen seconds is the recipe designer’s choice. The historical intervals determine proportions under a stated normalization rule. An illustrative output might be three seconds, nine seconds, and three seconds; those numbers are not a claim about the existing demo specimen.

A filmmaker makes the opening passage a fixed shot across an empty indoor swimming pool. During the interruption, the same compositional space becomes an auditorium: rows of seats occupy the pool’s depth, while the lighting remains inexplicably unchanged. The final passage reuses the opening image sequence exactly.

The image returns. The soundtrack does not. A tone introduced during the interruption continues decaying over the restored pool.

The computational structure supplies repetition and temporal proportion. It does not prescribe the swimming pool, the auditorium, or the relationship between visual return and audible persistence. Those are the artist’s decisions. The viewer can experience the piece without reading a hash; the evidence remains available to someone who wants to inspect the rule.

A musician uses the same envelope differently. A stable texture is interrupted and returns, but an additional layer retains traces of the interruption. The shared history becomes a compositional problem rather than an identical sonic surface.

A visual artist produces a triptych with identical outer panels and an altered center. Its panel proportions and recurrence follow the same score, but its imagery need not resemble the film.

These are not three editions of a scarce object. They are three works associated with one occurrence through one declared structural interpretation.

The specimen remains one specimen. The artworks remain distinct works.

**What they share is not an appearance. It is a history translated into form.**

## 6. Locality without a fake map

A mature system could organize works by historical locality rather than only by creator, genre, or publication date. The catalogue might let a visitor follow shared ancestors, overlapping occurrences, neighboring source coordinates, or common causal events.

However, proximity must be defined. Hash-derived seeds alone do not supply a meaningful neighborhood relation. Two adjacent source events need not generate similar palettes merely because their identifiers are fed into the same function.

A locality-preserving recipe would explicitly separate shared features from specimen-specific features. A common historical formation might supply a rhythmic grammar, while individual occurrences determine variations. Where relatedness is asserted, the evidence must establish the historical relation independently of the visualization.[^theory]

This could support a different kind of exhibition. A room might contain films and sound works derived from related historical formations, with the family resemblance arising partly from a common score. Another artist could use a different recipe and produce an incompatible reading of the same material.

The atlas need not declare one interpretation canonical.

That opens a useful distinction: **historical locality can be shared while aesthetic interpretation remains contested**. A regional school of sedimentary media would be an artistic possibility, not a consensus rule.

## 7. What the system can actually verify

A credible media layer needs more than a single green “authentic” badge. At least four different claims should be distinguished:

| Claim | Appropriate evidence | What it does not establish |
|---|---|---|
| Historical membership | Specimen assay, source evidence, declared view assumptions | Manufacture resistance or completeness beyond the stated scope |
| Media association | A binding between a media digest, specimen identity, and recipe | That the media was actually produced using that recipe |
| Constraint compliance | Independent checks of explicitly testable output properties | The full historical production process or artistic quality |
| Reproducible derivation | A pinned procedure that regenerates the specified output under declared conditions | That no other procedure could produce the same output |

For example, a validator may establish that the opening and closing image sequences are identical, that the durations match the envelope, and that a media file has not changed since its digest was recorded. It cannot infer from those facts alone that a named AI model was used or that an artist did not attach the manifest after finishing the work.

A genuine prior-commitment claim requires separate chronology evidence. A claimed generation history requires its own trusted instrumentation, attestation, or independently checkable execution evidence. It must not be inferred from a hash binding.

This is compatible with existing provenance work. C2PA defines signed assertions and bindings between provenance manifests and media; its documentation also warns that valid provenance does not make depicted content true.[^c2pa][^c2pa-harms]

Reproducibility also needs a precise scope. A seed and prompt do not automatically specify a bit-identical generative output across environments. PyTorch’s documentation explicitly warns about differences across releases and platforms, including CPU/GPU differences with identical seeds.[^pytorch]

A first implementation should therefore make the envelope exactly reproducible and reserve bitwise output claims for a pinned, tested renderer. Generative-film outputs can be preserved as particular renders, with the independently testable parts of their relationship stated separately.

If a source is later unavailable or its canonical status changes, the media does not vanish. Its file integrity may remain checkable while its geological-parent claim becomes insufficiently evidenced or contradicted. That change belongs in an appended status record, not a silent rewrite of the work’s history.

## 8. Synthetic cinema with a historical dependency

The artistic proposition is not to make synthetic images resemble documentary evidence. It is to give a work a particular historical dependency without falsely claiming that the depicted scene happened.

A generated pool containing an auditorium is not a photograph of a real occurrence. Yet its recurrence structure and temporal score can derive from authenticated computational events.

The work can say:

> This scene was invented. This part of its construction was inherited.

That suggests a procedural form of truth-of-envelope: source, recipe, declared choices, outputs, and limits are available for examination. The historical relation can be genuine while the depicted world is entirely fictional.

This can be more interesting than using provenance only as an authenticity sticker. The evidence may become a second surface of the artwork: a score, an annotated source graph, an alternate performance instruction, or a small printed catalogue accompanying the film.

The viewer does not need to understand the protocol to watch. But the work has an inspectable answer to a specific question: **why this structure rather than another?**

Not every decision needs that answer. The framework should preserve ambiguity, intuition, bad judgment, deliberate contradiction, and artistic refusal. It is a means of organizing constraints, not a machine for certifying taste.

## 9. When media becomes sediment

The longer-term proposal is recursive.

An assayed specimen contributes to a work. The work, its revisions, and its publication records become part of a later preserved history. A future researcher identifies a new formation in that history, and another creator works from it:

```text
history → specimen → artwork → recorded history → new specimen → new artwork
```

The first artist does not have to know what the later classifier will notice. A relationship between abandoned versions, a pattern of returns, or a collaboration’s branching structure may become material for a future work.

But two safeguards are essential.

First, publishing descendants must not change the parent specimen’s object set. New media belongs to a later, separately declared formation; it cannot retroactively revise the closed source on which the parent assay depended.

Second, intentionally producing material that later yields specimens does not automatically produce manufacture-resistant geology. Creators could coordinate revisions or generate fake histories to satisfy a known classifier. That is an adversarial issue to measure, not a feature to hide beneath sedimentary language.

The recursive system could still be valuable as a cultural archive without passing the stronger geological criteria. It would preserve interpretations, derivations, failures, and disagreements. It becomes geological in the stronger technical sense only where its causal and manufacture claims survive independent testing.

## 10. Abundance, rights, and optional work

The media layer should not turn every specimen into a scarce permission slip.

A finite set of parent occurrences can support an open-ended number of films, performances, remixes, and critical editions. Multiple creators may legitimately use the same specimen. Discovering it first does not, under this proposal, establish exclusive ownership of the underlying historical event or of later works.

The following remain separate:

**Specimen identity, artwork identity, edition identity, publication record, work certificate, and ownership claim.**

Any rights system would be an additional arrangement. A catalogue entry should not silently imply that such a system exists.

Likewise, the distinction between a historical occurrence’s uniqueness and economic scarcity must remain visible. A block or commit can be unique without making its associated media scarce, desirable, or valuable. The cultural hypothesis is that meaningful source relationships, craft, and interpretation might matter to audiences. It is not a price theorem.

Optional proof of work could be added after creation. A versioned work job could bind a specimen identity, an envelope digest, and a media digest. A successful result would be a separately assayable computational certificate for that combination—not additional historical ore.

Such a layer would reconnect the proposal with content-linked PoW, but without making it foundational. Hardware compatibility, encoding, target interpretation, and domain separation would need separate testing. A certificate must not claim to store a measured quantity of electricity or prove artistic merit.

The essential causal order remains:

**Prospect history. Create media. Optionally perform new work.**

## 11. What is inherited, and what is being proposed

This project does not begin outside existing scholarship and infrastructure.

W3C PROV already supplies models for entities, activities, derivation, and provenance exchange. Software Heritage provides intrinsic identifiers and contextual references for preserved software artifacts. Sedimentary media should build on those distinctions rather than rebrand content hashes as a new discovery.[^prov][^swh]

There is also an existing geological vocabulary in media theory. Jussi Parikka’s *A Geology of Media* examines the Earth materials, energy, and waste underlying media technologies. The proposal here has a different immediate object—verifiable formations within computational histories—but it should not use digital strata to make those physical conditions disappear.[^parikka]

The proposed contribution is narrower:

> A reusable connection between assayed historical occurrences, explicit creative scores, plural artistic works, and independently checkable evidence of their relationship.

No individual component needs to be unprecedented for the composition to deserve testing. But novelty should be established through actual constructions and comparisons, not by the geological vocabulary alone.

## 12. The first demonstration

The first release should be an instrument, not a marketplace.

Use one specimen already supported by the verification tool. Preserve its current classification; a synthetic Git control is sufficient to test the media plumbing, but must remain labeled as such. Do not wait for a monetary theorem, and do not imply that the control proves manufacture resistance.

Implement one versioned envelope recipe. Render a simple reference image, sound sequence, and short animation from it using a pinned local procedure. Display them on a plain specimen page alongside the source coordinates, envelope, media digests, and assay results.

Then invite two people to make different works from the same envelope.

The engineering tests should establish that repeated discovery preserves specimen identity, changing artwork does not create a new parent occurrence, changing the recipe is recorded as a different derivation, and missing source evidence is not silently accepted. A dishonest manifest, a substituted specimen, and a noncompliant render should each fail the particular claim they falsify.

The artistic test is different: **does the shared historical constraint produce a meaningful relationship between works without dictating their imagery or flattening their differences?**

A successful result could remain small: one specimen, three media forms, several interpretations, and enough evidence for a stranger to examine the connection.

That would demonstrate something concrete without promising digital gold.

## Conclusion

Computational geology asks whether historical computation can function as terrain: identifiable structures encountered after their formation, with discovery separated from creation and stronger manufacture claims subjected to attack.

Sedimentary media asks what culture might do with such terrain—or, initially, with honestly labeled retrospective specimens that fall short of the stronger geological definition.

Its ambition is not to prove that artworks were waiting inside hashes. It is to let works inherit constraints from particular histories while remaining unmistakably new creations.

The media can be abundant. The interpretations can conflict. The evidence can be inspected. None of those freedoms needs to erase the historical relationship.

**History is the material. The specimen is the encounter. The envelope is the score. The artwork is what someone makes of it.**

---

## Sources and scope

Project sources were read for this concept paper on 25 September 2026. They describe experimental software and provisional theory, not production guarantees. The creative-envelope and sedimentary-media architecture in this paper is a proposal; this document does not report a completed implementation or independent security audit of that architecture.

[^theory]: *Theory of Computational Geology*, `gold-atom/computational-geology`, `THEORY.md`. Retrieved file blob: `e4721ef6af665987c802b7a40baa4dfd3d8eb5ba`. https://github.com/gold-atom/computational-geology/blob/main/THEORY.md

[^readme]: *Computational Geology*, repository README. Retrieved file blob: `424b565fc2b09e82f40e62203aed67f89cc54b88`. https://github.com/gold-atom/computational-geology/blob/main/README.md

[^21e8]: Dean Little, `21e8miner`, README, especially “Publish 21e8 jobs.” Used as a concrete implementation-level precedent, not a comprehensive definition of 21e8. https://github.com/deanmlittle/21e8miner

[^c2pa]: C2PA, *Content Credentials: C2PA Technical Specification*, version 2.3. https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html

[^c2pa-harms]: C2PA, *Harms Modelling*, version 2.0, section 6.2. https://c2pa.org/specifications/specifications/2.0/security/Harms_Modelling.html

[^pytorch]: PyTorch, *Reproducibility*, official documentation source. https://github.com/pytorch/docs/blob/site/main/notes/randomness.md

[^prov]: W3C, *PROV-Overview: An Overview of the PROV Family of Documents*. https://www.w3.org/TR/prov-overview/

[^swh]: Software Heritage, *SoftWare Hash persistent IDentifiers*. https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html

[^parikka]: Jussi Parikka, *A Geology of Media*, University of Minnesota Press, 2015; publisher description. https://www.upress.umn.edu/9780816695522/a-geology-of-media/