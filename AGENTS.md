# MFA TECHNICAL KNOWLEDGE EXTRACTION RULES

This section overrides any generic documentation rule when generating troubleshooting documents.

---

# PROJECT GOAL

This repository is the technical knowledge base used by the MFA internal RAG chatbot.

Its purpose is to retrieve a precise, self-contained answer to a technician's
practical question and to help technicians diagnose and repair machines.

It is NOT a conversation archive.

It is NOT a workshop manual or a general documentation repository.

It is NOT a documentation generator.

It is NOT a conversation summarizer.

Only validated technical knowledge may feed the generated RAG base.

A reader must be able to understand and use any knowledge document without ever seeing the original conversation. Every document shall therefore read like an official service manual page, not like a summary of a chat.

---

# KNOWLEDGE CATEGORIES

DiagBot contains two types of knowledge documents.

## Troubleshooting

Use this category when the source describes a specific technical failure with:

- identifiable symptoms;
- diagnostic observations;
- a confirmed cause or an explicitly supported corrective action.

One troubleshooting document answers one primary diagnostic question only.

## Technical reference

Use this category when the source contains reusable technical knowledge that is
not tied to one resolved failure. This includes measurement and test methods,
operating principles, adjustment procedures, specifications, expected values,
electrical, hydraulic or mechanical calculations, component functions and
general diagnostic checks.

One document shall answer one primary technical question.

A technician should be able to obtain the complete answer to a single practical question by reading only one document.

If a document naturally answers several unrelated questions, split it.

If several documents are always required together to answer one question, merge them.

A technical reference is not a place to reproduce a complete manual chapter.

---

# EXTRACTION DECISION

For every source or coherent source set:

1. Determine whether it contains one or more valid troubleshooting cases.
2. Extract each valid troubleshooting case separately.
3. Determine whether it also contains reusable technical knowledge.
4. Extract each reusable technical subject separately.
5. Skip only content that is incomplete, personal, administrative, unsupported
   or not reusable.

The same source set may produce both categories when the evidence supports both
outputs.

---

# EVIDENCE RULES FOR TECHNICAL REFERENCES

A technical reference may be created from an explicit and reusable procedure,
measurement point, value, calculation, operating principle, adjustment,
interpretation method or diagnostic sequence. A completed repair is not
required.

Do not create a technical reference from unresolved guesses, unsupported
recommendations, incomplete instructions that would be unsafe or misleading, a
simple question without a usable answer, or administrative and customer-service
wording.

Preserve units exactly. Distinguish measured values, manufacturer specifications
and deductions. Never transform an unconfirmed hypothesis into a technical rule.

---

# ONE DOCUMENT = ONE PRIMARY TECHNICAL QUESTION

Each Markdown file answers ONE primary practical question.

Examples of suitable questions include:

- how to measure pressure at MP2;
- why the saw does not descend;
- how to test sensor B1.1;
- what five LED flashes mean;
- how to adjust chain tension.

Broad subjects such as “hydraulic system”, “electrical system”, “machine
operation” or “maintenance” are not acceptable primary questions unless the
source proves that the complete subject forms one indivisible procedure.

Prefer documents of approximately 500 to 1,500 words. This is a retrieval
target, not a reason to split a procedure that naturally belongs together or to
pad a short complete answer.

Never mix unrelated questions or failures inside the same file. If one source
contains several independent questions, create one file per question.

---

# WHAT DEFINES A TECHNICAL PROBLEM

A troubleshooting document is created when all observations, tests and repairs belong to the same root cause.

Do NOT split a diagnostic process into several documents.

Do NOT create one document per repair attempt.

Create one document only if:

- all symptoms describe the same failure;
- all observations belong to the same investigation;
- all diagnostic attempts target the same root cause;
- one final repair solved the issue.

If two independent failures are repaired during the same conversation:

Create two documents.

---

# MACHINE ORGANIZATION

One folder per machine.

Example:

knowledge/drafts/troubleshooting/

    CS4218_H/

    CS4218_PRO/

    CS4218_H_HARVESTER/

    CS4218_PRO_HARVESTER/

    CSKZ/

    TREUILS/

    PALMS/

    TEHNOS/

Each document belongs to exactly one machine/model/variant scope. The
`machine` metadata identifies the model or machine. The `variant` metadata
narrows that scope when the source establishes a variant.

Do not use a list or a generic multi-machine value in either field.

---

# MULTIPLE MACHINES

If exactly the same problem applies to several machines or variants:

Create one independent Markdown file for EACH applicable machine.

Duplicate the technical content.

Only adapt:

- machine
- variant
- output folder

Never create one generic document covering several machines.

If applicability is uncertain:

Generate ONLY the machine explicitly supported by the conversations.

Documents intentionally copied into different machine/model/variant folders
are not duplicates. Duplicate detection applies only when two documents inside
the same scope compete to answer the same primary question.

Cross-references shall remain inside the same machine/model/variant scope. A
document may link to a related document, but it must remain understandable and
operational without opening that link.

---

# NEVER INVENT

Never invent.

Never extrapolate.

Never assume.

Never use external knowledge as technical evidence.

Everything must come from preserved sources in the repository.

---

# KEEP ONLY TECHNICAL INFORMATION

Remove:

- greetings
- signatures
- customer names
- dealer names
- emails
- phone numbers
- URLs
- commercial discussions

Keep only technical information.

---

# REQUIRED STRUCTURE

Every new document starts with `# Résumé`. The summary shall answer the primary
question immediately in no more than 5 to 10 concise lines.

A technical reference may then use these sections when supported:

- `## Objectif`;
- `## Principe de fonctionnement`;
- `## Procédure`;
- `## Valeurs attendues`;
- `## Interprétation`;
- `## Composants concernés`;
- `## Documents liés`;
- `## Limites`.

A troubleshooting document shall then use:

- `## Symptômes`;
- `## Conditions` when established;
- `## Observations`;
- `## Cause probable`;
- `## Contrôles de confirmation` when established;
- `## Action corrective`;
- `## Composants concernés` when established;
- `## Documents liés` when useful;
- `## Limites` when evidence is incomplete or contradictory.

Omit unsupported sections. Never retain an empty heading. Keywords belong in
metadata and need not be repeated in the body.

---

# CORRECTIVE ACTION

The corrective action MUST be the repair that actually solved the problem or
an action explicitly supported by confirmed technical evidence.

Never use an unsuccessful attempt as the final solution.

---

# WRONG DIAGNOSTICS

If the conversation contains incorrect diagnostic attempts:

Do not delete them.

Store them under:

Rejected causes / Wrong diagnostics

---

# PROBABLE CAUSE

Never convert a hypothesis into a confirmed cause.

Only keep the final probable cause supported by the conversation.

---

# SERIAL NUMBERS

Never invent serial number ranges.

Never extend applicability.

---

# STATISTICS

Never write:

- common
- frequent
- recurring
- known issue
- often

unless explicitly stated in the source.

---

# SELF-CONTAINED DOCUMENTS

Every knowledge document must be fully self-contained.

Assume the original conversation will never be available to the reader.

Never write:

- "the conversation"
- "the discussion"
- "the customer says"
- "the user reports"
- "according to the chat"
- "the attached photo"
- "see above"
- "as mentioned previously"
- "in this exchange"

Instead, rewrite every fact as objective technical documentation.

Do not refer to manual page numbers, emails, attached files, photographs or
previous discussions. Traceability belongs in metadata. Technical content
from diagrams or photographs shall be integrated as an explanation of the
system, component, location, measurement or adjustment, never as a description
of the source artifact.

Bad:
"The conversation indicates that the voltage was 12.4 V."

Good:
"A measured supply voltage of 12.4 V was reported."

Bad:
"The customer measured 230 bar."

Good:
"A pressure measurement of 230 bar was obtained during the diagnostic."

Bad:
"The photo shows a cracked weld."

Good:
"The weld exhibited a visible crack."

Bad:
"The discussion recommends..."

Good:
"The recommended diagnostic procedure is..."

---

# RAG METADATA

Keep the existing metadata and use the following optional fields when they
improve retrieval:

- `confidence`: one of `manufacturer`, `field_verified` or `preliminary`;
- `search_intents`: realistic technician questions or query formulations;
- `components`: important component names and identifiers;
- `measurements`: measurement points such as MP2, PS or GND;
- `symptoms`: troubleshooting documents only; observable symptom formulations.

All list values shall be non-empty, unique strings. Do not add a metadata field
with an empty or null value. Metadata should improve query matching and
filtering; it shall not become a second copy of the document body.

Confidence meanings:

- `manufacturer`: established by applicable manufacturer documentation;
- `field_verified`: established by a completed field diagnosis or repair;
- `preliminary`: useful but still awaiting technical confirmation.

Titles shall resemble the question or phrase a technician would search for.
Prefer “Mesurer la pression à MP2”, “Tester le capteur B1.1” or “Cinq
clignotements de LED” over broad labels such as “Architecture hydraulique”.

# SOURCES

Every document shall list the exact preserved source files in its `sources`
metadata. Sources may be conversations, manufacturer documents, technical
drawings, parts catalogues or photographs with real technical value.

Every technical statement must be traceable. Spare-parts catalogues contribute
only terminology, compatibility, serial applicability or information useful to
diagnosis and maintenance. Do not turn them into catalogue documents.

---

# DRAFT IMMUTABILITY

Previously generated troubleshooting documents are considered project artifacts.

Never delete, rewrite, rename or move an existing troubleshooting document unless the user explicitly requests it.

If an existing document no longer satisfies updated extraction rules:

- keep the document unchanged;
- report the inconsistency;
- never delete it automatically.

New executions may only create additional documents.

Knowledge documents are living artifacts only through an explicitly authorized
revision. During such a revision, preserve validated information unless new
evidence establishes that it is incorrect or out of scope. Prefer enriching the
existing answer to creating a competing answer in the same scope.

---


# LANGUAGE

Markdown documents:

French

Metadata:

English

---

# STYLE

Use short sentences.

Use factual wording.

Avoid storytelling.

Avoid speculation.

Avoid unnecessary explanations.

The objective is fast retrieval by a RAG engine.

Use a concise, factual manufacturer-service style. Do not write workshop notes,
chronological investigation reports or AI explanations. Keep terminology and
units consistent within the document and with the applicable source.

---

# QUALITY CHECK BEFORE SAVING

Before saving a document verify:

✔ One primary technical question only

✔ Correct machine

✔ Correct variant

✔ No invented information

✔ No personal information

✔ Final solution only

✔ Wrong diagnostics separated

✔ Self-contained document

✔ Source referenced

✔ Summary answers the question in 5 to 10 lines maximum

✔ Retrieval-oriented title and search intents

✔ Metadata lists contain no empty, null or duplicate value

✔ Cross-references resolve inside the same machine/model/variant scope

✔ Terminology and units are consistent

If one point fails:

Do not generate the document.

Flag it for manual review.

# EXISTING DRAFT PROTECTION

Existing troubleshooting documents are project artifacts.

Never delete, overwrite, rename or move an existing troubleshooting document unless the user explicitly requests it.

If an existing document appears inconsistent with current rules:

- keep it unchanged;
- report the inconsistency;
- do not modify or delete it automatically.

New extraction runs may create additional documents only.

This immutable-artifact rule applies to troubleshooting and technical reference
documents in every knowledge state. Never delete, overwrite, rename or move an
existing knowledge document unless the user explicitly requests it. The only
exception is the one-time structural migration explicitly requested to create
the category directories.
