# Bitcoin Header-Field Return Profile v1

**Status:** executable prototype profile for an offline, read-only Bitcoin header adapter.

This profile recognizes an **exact field-value return** within one explicitly declared contiguous Bitcoin block-header stream.

## Declared scope

Inputs:

- one offline file containing concatenated raw 80-byte Bitcoin block headers;
- one declared network label;
- one declared starting height for the first header in the file; and
- one selected header field projection.

Traversal and coverage:

- headers are read in file order;
- each header must parse as one 80-byte Bitcoin block header;
- each header after the first must point to the immediately preceding header's block hash;
- the profile currently supports the `version`, `timestamp`, `bits`, `nonce`, `previous_block_hash`, and `merkle_root` projections; and
- no claim is made about proof-of-work validity, active-chain selection, burial, or transaction contents.

## Formation rule

For each header in the declared scope, read the projected field value.

Compress successive identical projected values into runs.

A specimen exists exactly when three **consecutive** runs have labels:

```text
A -> B -> A
```

with `A != B`.

The occurrence references are the **first height** and **first block hash** of each of the three runs.

This profile recognizes that the selected field returned within the declared offline header scope. It does **not** prove that a real Bitcoin active chain is complete in the local file, that the declared height range is independently authenticated when the file starts above genesis, or that the observed return has any rarity or manufacture-resistance significance.

## Deterministic specimen identity

The specimen identifier is the SHA-256 digest of a domain-separated canonical payload binding:

- the versioned formation rule identifier (`bitcoin-header-field-return/v1`);
- the declared network label;
- the selected field name;
- the three occurrence start heights;
- the three occurrence start block hashes; and
- the three projected field values.

The identifier does **not** bind the local filesystem path of the header file, a mainnet retrieval method, a random nonce, or any later catalogue entry.
