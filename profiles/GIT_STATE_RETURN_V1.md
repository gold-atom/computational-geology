# Git State-Return Profile v1

**Status:** executable prototype profile for the first computational-geology specimen engine.

This profile recognizes an **exact-content return** in Git history for one explicitly selected repository-relative path.

## Declared scope

Inputs:

- a local Git repository;
- one pinned full commit object ID;
- one explicitly selected repository-relative file path.

Traversal and coverage:

- only the pinned commit's **first-parent** ancestry is inspected;
- commits are ordered **oldest to newest**;
- path matching is **exact** and repository-relative;
- only ordinary file blobs are admitted (`100644` and `100755` Git modes);
- rename heuristics are disabled;
- second parents are never traversed;
- no claim is made about authorship, originality, causation, intent, or wall-clock age.

## Formation rule

For each commit in the declared scope, read the object identity at the selected path.

- If the path is missing, the sequence is broken.
- If the path names a non-file entry or any unsupported object type, the sequence is broken.
- Broken segments are not silently bridged.

Compress successive identical blob identities into runs.

A specimen exists exactly when three **consecutive** runs have labels:

```text
A -> B -> A
```

with `A != B`.

The occurrence references are the **first commit** of each of the three runs.

This profile recognizes that exact content returned within the declared Git history scope. It does **not** prove why the content returned, whether the changes were independent, whether the return was unintentional, or whether someone could intentionally manufacture a similar future history.

## Deterministic specimen identity

The specimen identifier is the SHA-256 digest of a domain-separated canonical payload binding:

- the versioned formation rule identifier (`git-state-return/v1`);
- the Git object-hash algorithm reported by the inspected repository;
- the exact repository-relative file path encoded as UTF-8 hex;
- the three occurrence start-commit IDs;
- the three relevant blob identities.

The identifier does **not** bind discoverer identity, discovery time, local filesystem path, repository hosting URL, a random nonce, or the latest global snapshot hash.

The pinned snapshot belongs to the evidence bundle's declared verification scope, not to specimen identity. Extending history beyond an already-complete occurrence therefore preserves that occurrence's identifier.
