---
name: Diagram Style Preferences
description: Style patterns validated from first diagram request — subgraphs, color coding, pass-through arrows for dual-use data
type: feedback
---

Use subgraphs to group pipeline stages by responsibility (e.g. Embedding, Retrieval, Augmentation, Generation). This improves readability for multi-stage flows.

**Why:** User requested a "clear, well-labeled" flowchart — grouping by stage achieves this naturally.

**How to apply:** For any pipeline or multi-phase flow diagram, wrap related nodes in labeled subgraphs rather than using a flat node list.

---

Use `classDef` color coding to visually distinguish node roles: terminators (user endpoints), data stores, models, data artifacts, and builders.

**Why:** Color separation makes it immediately clear what type of component each node represents without reading every label.

**How to apply:** Define at minimum: terminator, process/data, store, and model classes for any system architecture diagram.

---

When data is used in multiple downstream steps (e.g. original query used for both embedding AND prompt building), draw explicit pass-through arrows to both consumers.

**Why:** Avoids the common misconception that only one path exists; makes the real data flow accurate.

**How to apply:** Audit diagrams for nodes whose output feeds more than one downstream step and ensure all edges are drawn.
