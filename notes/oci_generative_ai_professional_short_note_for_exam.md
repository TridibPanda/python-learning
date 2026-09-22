# OCI GENERATIVE AI PROFESSIONAL — EXAM CHEAT SHEET (1Z0-1127-25)

> Oracle Cloud Infrastructure 2025 Generative AI Professional

## MODULE 1 ▸ INTRODUCTION TO LARGE LANGUAGE MODELS

### LANGUAGE MODEL BASICS

- LM = probabilistic model of text: given a prefix → prob distribution
	over vocabulary for the next word  
- LLM = same as LM; "Large" = large # of parameters (no fixed threshold)
- 2 ways to affect distribution: PROMPTING (no param change) or
	TRAINING (changes params)  
- Decoding = generating text from LLM (one token at a time)

---

### ARCHITECTURES

All built on: TRANSFORMER ("Attention Is All You Need", 2017)  

| Architecture | Purpose | Use Cases / Notes |
| --- | --- | --- |
| ENCODER<br>(e.g., BERT) | EMBED text<br>→ vectors | Semantic/vector search,<br>classification, regression |
| DECODER<br>(GPT-4, Llama,<br>Cohere Cmd) | GENERATE text<br>1 token/call | Chat, Q&A, dialogue<br>NOT for embedding<br>Computationally expensive |
| ENCODER-DECODER | Seq-to-seq | Translation; hybrid architecture |

Model size = # trainable parameters. Decoders >> Encoders in size.  

---

### PROMPTING & PROMPT ENGINEERING

Prompting = altering model input to change output (NO param changes)  
Prompt Engineering = iteratively refining input to get desired output  

#### K-SHOT PROMPTING:
Zero-shot  = no examples; One-shot = 1 example; Few-shot = K examples  
In-Context Learning (ICL) = providing demos in prompt; NO param change  

#### ADVANCED STRATEGIES:
Chain-of-Thought (CoT)  → Show intermediate reasoning steps in prompt  
Zero-Shot CoT           → Append "Let's think step by step."  
Least-to-Most           → Solve easy sub-problems first; build up  
First Principles        → State relevant equations/concepts first  

⚠ Small changes (even whitespace) can cause LARGE unpredictable effects  

---

### PROMPT INJECTION ATTACKS

| Attack Type | What Happens |
| --- | --- |
| Prompt Injection | Attacker hijacks model behavior via crafted<br>input; ignores developer instructions |
| Leaked Prompt | Developer's system prompt is revealed to user |
| Private Data Leak | Model reveals sensitive training data via query |

- Analogous to SQL injection attacks
- Off-the-shelf LLMs have NO default protection → must add guardrails

---

### TRAINING APPROACHES

| Approach | Cost | Labeled<br>Data? | Key Detail |
| --- | --- | --- | --- |
| Fine-Tuning | HIGH | YES | ALL params<br>updated |
| PEFT / LoRA<br>(Low Rank Adaptation) | LOW | YES | ~0.01% params<br>updated; orig<br>model frozen |
| Soft Prompting | LOW | YES | Learnable<br>prompt tokens<br>(randomly init) |
| Continual Pre-Training | HIGH | NO | ALL params;<br>next-word pred |

Cost order (most → least): Pre-Training > Fine-Tuning > PEFT > Inference  

---

### DECODING

Decoding = turning prob distribution into text; one token at a time  

| Method | Description |
| --- | --- |
| Greedy Decoding | Always pick HIGHEST prob token; DETERMINISTIC;<br>same input → same output; typical/predictable |
| Random Sampling | Pick randomly from distribution; NON-DETERMIN.;<br>creative/varied output |
| Nucleus Sampling | Random sampling with Top-P/Top-K constraints;<br>prevents sampling very unlikely words |
| Beam Search | Generate MULTIPLE sequences simultaneously;<br>prune low-prob paths; higher joint probability<br>than greedy; more compute |


#### TEMPERATURE:
Low  → peaks distribution → approaches greedy → typical output  
High → flattens distribution → rare words more likely → creative  
Rule: Temperature NEVER changes the ORDER of word probabilities!  
Temp = 0 → fully deterministic (always highest prob word)  

Top K = restrict candidate tokens to top K by count  
Top P = restrict to tokens whose cumulative prob sums to P  

---

### HALLUCINATION

Definition: Text generated NOT grounded in training data OR input data;  
includes factually incorrect / nonsensical statements  

Key insight: LLMs are trained to SOUND like human text — NOT to be true  
"All LLM output is hallucinated; generations just happen to be correct  
most of the time" (widely cited)  

Fluency ≠ Accuracy — text can sound perfect but be factually wrong  
Subtle hallucinations (1 wrong word) are MORE dangerous than obvious  

NO known method eliminates hallucination 100%  

#### MITIGATIONS:
RAG             → grounds output in real documents → less hallucination  
NLI (TRUE model)→ checks if output is entailed by supporting source  
Grounded QA     → answers come with cited sources  
Attribution     → attributes each claim to a source  

---

### LLM APPLICATIONS SUMMARY

| Application | Key Facts |
| --- | --- |
| RAG | Retrieve docs → ground LLM answer; non-parametric<br>improvement (add docs, no retraining needed) |
| Code Models<br>(Copilot, Codex) | Trained on code; great at completion & boilerplate<br>Bug patching: best models < 15% success rate |
| Multi-Modal<br>(Diffusion) | Text + images + audio; diffusion models generate<br>images by refining ALL pixels simultaneously<br>(joint decoding, not sequential like text) |
| Language Agents<br>(ReAct Framework) | Sequential decision-making; action-observe loop;<br>emit THOUGHTS (goal+progress+next steps); tool use |

Diffusion vs Text: images = fixed size + continuous pixels (refineable)  
Text = unknown length + discrete tokens (hard to do joint decoding)  

---

## MODULE 2 ▸ OCI GENERATIVE AI SERVICE

### SERVICE OVERVIEW

- Fully MANAGED, SERVERLESS service — no infrastructure to manage
- Single API; switch models with minimal code changes
- 3 Pillars: Pre-trained Models | Fine-Tuning (T-Few) | Dedicated Clusters
- Regions: available in selected OCI regions only

#### TWO ACCESS MODES:
ON-DEMAND   → Call pre-trained models directly via API/Console/CLI;  
pay-per-use; no cluster setup needed; fastest to start  
DEDICATED   → GPU cluster reserved for you; used for fine-tuning and  
AI CLUSTER    hosting custom models; single-tenant; consistent perf  

#### MODEL TYPES SUPPORTED:
Chat | Embeddings | Rerank | OpenAI-compatible APIs  

---

### CHAT MODELS

| Model | Provider | Context | Notes |
| --- | --- | --- | --- |
| Command R+ | Cohere | 128K in<br>4K out | Powerful; complex<br>use cases; expensive |
| Command R (16K) | Cohere | 16K in<br>4K out | Affordable; fast;<br>standard tasks |
| Llama 3.1 70B Instruct | Meta | 128K in<br>128K out | Open-source based;<br>enterprise-grade |
| Llama 3.1 400B | Meta | 128K in<br>128K out | LARGEST publicly<br>available model |

- Chat models are INSTRUCTION-TUNED (fine-tuned + RLHF aligned)
- RLHF: human annotators rank outputs → reward model → aligns LLM
- Llama 2 example: 2T token base; fine-tuned on ~28K pairs;
aligned with 1.4M+ examples via RLHF  

---

### TOKENS

Token = unit LLMs process (not chars, not always full words)  
Token types: part-of-word | whole word | punctuation mark  
Simple text ≈ 1 token/word; Complex text ≈ 2–3 tokens/word  
Example: "indivisible" → 2 tokens ("indiv" + "isible")  

---

### CHAT MODEL PARAMETERS

| Parameter | What It Controls |
| --- | --- |
| Max Output Tokens | Length of response; controls cost/speed |
| Preamble Override | Replace default system prompt; sets tone/<br>style/behavior (e.g., "Answer as a pirate.") |
| Temperature | Randomness; Temp=0 = deterministic;<br>High = creative; never changes prob ORDER |
| Top K | Restrict pool to top K tokens by COUNT |
| Top P | Restrict pool to tokens summing to prob P<br>(nucleus sampling); can combine with Top K |
| Frequency Penalty | Penalise repeated tokens scaled by frequency |
| Presence Penalty | Penalise ANY previously used token (flat);<br>encourages broader vocabulary |

---

### EMBEDDING MODELS

Embedding = text → vector of numbers; captures semantic meaning  
Semantically similar text → NUMERICALLY similar vectors  
Similarity measures: Cosine Similarity | Dot Product  

| Model | Dims | MaxTok | MaxInput | Lang |
| --- | --- | --- | --- | --- |
| cohere.embed-english-v3 | 1,024 | 512 | 96 | EN |
| cohere.embed-english-light-v3 | 384 | 512 | 96 | EN |
| cohere.embed-multilingual-v3 | 1,024 | 512 | 96 | 100+ |
| cohere.embed-multilingual-light-v3 | 384 | 512 | 96 | 100+ |

v3 improvement: evaluates query-document match quality +  
content quality → ranks best docs at top → better RAG  
Use v3 wherever possible; multilingual supports cross-language search  

---

### RERANK MODELS

Purpose: ORDER documents by RELEVANCE to a query  
Use case: Post-retrieval step in RAG — re-rank retrieved chunks before  
feeding to LLM; improves precision of final answer  

| Model | Notes |
| --- | --- |
| cohere.rerank-v3.5 | Latest production rerank model |
| cohere.rerank-v4.0 | Newer generation rerank model |


#### HOW RERANK WORKS IN A RAG PIPELINE:
Retrieve Top K chunks (vector search)  
↓  
Rerank model scores each chunk against query (relevance score)  
↓  
Re-ordered Top N chunks (most relevant first)  
↓  
Feed re-ordered chunks to LLM → more accurate grounded response  

Key: Rerank uses a CROSS-ENCODER (query + doc together) vs embedding  
models which use BI-ENCODER (query and doc separately encoded)  
Cross-encoder = more accurate relevance scoring; bi-encoder = faster  

---

### CUSTOMIZING LLMs — 3 APPROACHES

Training from scratch: ~$1M for 10B params; 2T tokens; deep expertise  
- → IMPRACTICAL for most; use one of the 3 approaches below

| Approach | When To Use | Key Trade-offs |
| --- | --- | --- |
| Few-Shot Prompting | Model already<br>knows domain;<br>simple tasks | ✓ No training cost<br>✗ Adds latency per request<br>✗ Limited by context window |
| Fine-Tuning | Model underper-<br>forms; large<br>training data | ✓ Better perf; no inference<br>latency<br>✗ Needs labeled data;<br>complex to set up |
| RAG | Rapidly changing<br>data; private<br>knowledge base | ✓ Always fresh; grounded<br>✓ No fine-tuning needed<br>✗ More complex to set up |

These are ADDITIVE — can combine all three; best: fine-tune a RAG model  
Framework: Prompt → Few-shot → Identify bottleneck:  
Context problem → RAG | Behaviour problem → Fine-Tuning  

---

### FINE-TUNING & INFERENCE IN OCI

Fine-Tuning = additional training with custom data  
Inference  = model generates output text from new input  
Custom Model = pre-trained base + fine-tuned with your dataset  

#### WORKFLOW:
Fine-Tuning: Create FT cluster → Gather training data →  
Run fine-tuning → Custom model ready  
Inference:   Create Hosting cluster → Create Endpoint → Serve traffic  

#### TWO CLUSTER TYPES:
Fine-Tuning Cluster  → for TRAINING  
Hosting Cluster      → for INFERENCE; 1 base + up to N custom models  
(all serve CONCURRENTLY)  

#### DEDICATED AI CLUSTERS:
- SINGLE-TENANT GPU deployment (not shared with other customers)
- Endpoint can be DEACTIVATED / REACTIVATED as needed

T-FEW vs VANILLA:  
T-Few: inserts new layers; updates only ~0.01% of model size  
Vanilla: updates all/most layers (more expensive, slower)  

PARAMETER SHARING (T-Few benefit):  
Base model loaded into GPU once; only tiny delta (~0.01%) per  
custom model swapped → minimal GPU memory; minimal switch overhead  

---

### DEDICATED AI CLUSTERS — SIZING & PRICING

⚠ ALL cluster unit quotas are ZEROED OUT by default — must request  
service limit increase before use!  

| Unit Type (SKU) | Supports | Models |
| --- | --- | --- |
| Large Cohere<br>(unit-large-cohere) | Fine-Tune + Hosting | Command R+ family |
| Small Cohere<br>(unit-small-cohere) | Fine-Tune + Hosting | Command R family |
| Embed Cohere<br>(unit-embed-cohere) | Hosting ONLY<br>(NO fine-tuning) | Embed English &<br>Multilingual |
| Large Meta<br>(unit-large-meta) | Fine-Tune + Hosting | Llama 3.x models |


#### UNITS REQUIRED PER MODEL:
| Model | Fine-Tuning Units | Hosting Units |
| --- | --- | --- |
| Command R+ 08-2024 | NOT supported | 2 × Large Cohere |
| Command R 08-2024 | 8 × Small Cohere | 1 × Small Cohere |
| Meta Llama 70B/405B/Vis | 4 × Large Meta | 1 × Large Meta |
| Cohere Embed (any) | NOT supported | 1 × Embed Cohere |


#### BILLING:
Fine-Tuning: min 1 hour; billed per actual duration (rounded up)  
Hosting:     min FULL MONTH (744 unit-hours); no partial hosting  

EXAMPLE (Command R 08-2024, FT weekly 4×/month, 5hr each + hosting):  
FT: 8 units × 5hrs × 4 weeks = 160 unit-hrs/month  
Hosting: 1 unit × 744 hrs = 744 unit-hrs/month  
Total: 904 unit-hrs × $6.50 ≈ $5,900/month  
Service limit needed: dedicated-unit-small-cohere-count = 9  

---

### FINE-TUNING CONFIG — PEFT METHODS

PEFT = Parameter Efficient Fine-Tuning (adjust without full retraining)  

| Method | Used With | What Changes |
| --- | --- | --- |
| T-Few | Cohere Command R / R+ | New T-Few layers added<br>(~0.01% of model size) |
| LoRA<br>(Low Rank<br>Adaptation) | Meta Llama models | New low-rank update<br>matrices (frozen base) |

---

### HYPERPARAMETERS — OCI DEFAULT VALUES (Source: Oracle Docs 2025-09-29)


T-FEW (Cohere Command R / R 08-2024):  
| Parameter | Valid Range | Default |
| --- | --- | --- |
| Total training epochs | 1–10 (int) | 1 |
| Learning rate | 0.000005 – 0.1 | 0.01 |
| Training batch size | 8–32 (int) | 16 |
| Early stopping patience | 0 or 1–16 | 10 |
| Early stopping threshold | 0.001 – 0.1 | 0.001 |
| Log model metrics interval | Fixed (can't tune) | 1 |


LoRA (Meta Llama 3.3-70B / 3.1-70B):  
| Parameter | Valid Range | Default |
| --- | --- | --- |
| Total training epochs | ≥ 1 (int) | 3 |
| Learning rate | 0 – 1.0 | 0.0002 |
| Training batch size | 8–16 (int) | 8 |
| Early stopping patience | 0 or ≥ 1 | 15 |
| Early stopping threshold | 0 or > 0 | 0.0001 |
| Log model metrics interval | Preset to 10 | 10 |
| LoRA r (rank) | 1–64 (int) | 8 |
| LoRA alpha (scaling) | 1–128 (int) | 8 |
| LoRA dropout | decimal < 1 | 0.1 (= 10%) |


totalTrainingSteps = (epochs × dataset_size) / batch_size  

#### KEY HYPERPARAMETER DEFINITIONS:
Epochs         → # full passes through dataset; more = more study  
Batch size     → samples per weight update; larger = faster; smaller  
= more granular updates  
Learning rate  → speed of weight adjustments; too high = unstable;  
too low = slow convergence  
Early stop threshold → min loss improvement to keep training  
Early stop patience → grace periods after threshold trigger;  
0 = disable early stopping  
LoRA r         → rank of update matrices; lower = smaller params  
LoRA alpha     → scaling factor; weights scaled by alpha/r  
LoRA dropout   → % neurons randomly dropped; prevents overfitting  

---

### EVALUATION METRICS: ACCURACY vs LOSS

| Metric | Accuracy | Loss |
| --- | --- | --- |
| Measures | % tokens matching<br>annotated tokens | HOW WRONG outputs are<br>(prob distribution diff.) |
| Best value | 100% | 0 |
| As model improves | INCREASES | DECREASES |
| Context-aware? | NO — diff words =<br>wrong even if same<br>meaning | YES — considers semantic<br>distance between outputs |
| Preferred for<br>Gen AI? | NO | YES ✓ |

"slept" vs "sat": accuracy = 0 (wrong word); loss = LOW (close meaning)  
Start with default hyperparameters → monitor accuracy + loss → iterate  

---

### OCI GENERATIVE AI SECURITY

Security = ESSENTIAL DESIGN PRINCIPLE (not afterthought)  

#### 3 LAYERS:
| Layer | Detail |
| --- | --- |
| Layer 1: GPU/Network<br>Isolation | Dedicated GPU pool + dedicated RDMA<br>network per customer; GPUs NEVER<br>shared across customers |
| Layer 2: Model/Data<br>Isolation | Cluster handles ONLY that customer's<br>models; data restricted within<br>customer's OCI TENANCY |
| Layer 3: OCI Security<br>Services | IAM (auth/authz) + Key Management<br>(encrypt model weights) + Object<br>Storage (store weights, encrypted) |


- App can ONLY access models within its OWN tenancy (cross-tenancy ✗)
- OCI IAM: who can access WHAT (e.g., App X → Custom Model X only)
- OCI Key Management: encrypts model weights (base + custom)
- OCI Object Storage: stores fine-tuned model weights; ENCRYPTED by def
- Security isolation maintained at the GPU LEVEL

---

## MODULE 3 ▸ RAG USING GENERATIVE AI SERVICE AND ORACLE 23AI VECTOR SEARCH

### LANGCHAIN OVERVIEW

Definition: Open-source framework for building context-aware,  
LLM-powered applications  
Components are EASILY EXCHANGEABLE (swap LLMs with minimal code change)  

#### KEY COMPONENTS:
LLMs / Chat Models | Prompts | Memory | Chains  
Vector Stores | Document Loaders | Text Splitters  

| Type | LLM (completion) | Chat Model |
| --- | --- | --- |
| Input | String prompt | List of chat messages |
| Output | String completion | AI message |


#### PROMPT TYPES:
PromptTemplate    → fixed text + placeholders; for completion models  
ChatPromptTemplate→ list of messages (role + content); for chat models  

CHAINS (compose operations in sequence):  
LCEL (preferred/declarative) or Python classes (e.g., LLMChain)  
Flow: User query → Prompt → LLM → Response  

MEMORY: Stores conversation history; chain reads history → passes to  
LLM → writes new query+answer back; types: full / summary / entities  

ORACLE 23ai INTEGRATION METHODS:  
DB UTILs + REST APIs → embeddings generated OUTSIDE the DB  
SELECT AI           → natural language → SQL query on Oracle DB data  
LangChain classes   → Python integration with OCI Gen AI  
Python SDK          → build apps using OCI Gen AI + Oracle 23ai  

---

### RAG PIPELINE — 3 PHASES

#### WHY RAG:
- ✓ Up-to-date info at query time (not stale training data)
- ✓ Mitigates training data bias/errors (diverse external sources)
- ✓ Overcomes context limits (only Top K chunks fed, not whole doc)
- ✓ Broader query range without exponentially larger training data

> PHASE 1: INGESTION (offline / one-time)  
> Documents → Chunk → Embed → Index in Vector DB  
>
> PHASE 2: RETRIEVAL (per user query)  
> User Query → Encode as vector → Similarity search → Top K chunks  
>
> PHASE 3: GENERATION (per user query)  
> Top K chunks + User Query → LLM → Grounded response  

---

### INGESTION: DOCUMENT LOADING & CHUNKING

LOADING: Supported formats: PDF, CSV, HTML, JSON, and more  
LangChain provides loader classes per format;  
Can load single file OR entire directory  

CHUNKING — 3 KEY CONSIDERATIONS:  
| Consideration | Detail |
| --- | --- |
| Chunk Size | Max = LLM context window; too small = not useful;<br>too large = not specific; find balanced size |
| Chunk Overlap | Include portion of preceding chunk at start of<br>each new chunk → preserves context continuity |
| Split Strategy | Semantic separators in priority order:<br>1st: Paragraph → 2nd: Sentence → 3rd: Word |


#### CODE:
```text
PDFReader → extract_text() →
TextSplitter(chunk_size=X, chunk_overlap=Y) → split_text(text)
```

---

### INGESTION: EMBEDDINGS + ORACLE 23AI VECTOR STORE

Embeddings = numerical (vector) representations; similar text =  
close vectors in multidimensional space  

EMBEDDING GENERATION OPTIONS in Oracle 23ai:  
OUTSIDE DB → use OCI Gen AI or other third-party embedding models  
INSIDE DB  → import ONNX-format model into Oracle 23ai directly  
ONNX = Open Neural Network Exchange (portable model format)  

ORACLE 23ai VECTOR DATA TYPE:  
New native VECTOR column type to store embeddings  
Can coexist with regular columns (text, number, date)  
Standard INSERT/UPDATE SQL statements work with VECTOR columns  
Table example: id | text | embedding(VECTOR)  

#### CODE STEPS:
```text
1. DB connection (OracleDB.connect)
2. chunks → Document objects (page_content + metadata)
chunks_to_docs() → Document(page_content, metadata{id,link,page})
3. OCIGenAIEmbeddings(model_name, service_endpoint, compartment_id,
auth_type)
4. OracleVS.from_documents(docs, embed_model, connection,
table_name, distance_strategy)
distance_strategy: COSINE | DOT_PRODUCT
```

---

### RETRIEVAL: VECTOR SEARCH, INDEXES & GENERATION

#### RETRIEVAL STEPS:
1. Encode query using SAME embedding model as ingestion (essential!)  
2. Similarity search in vector DB  
3. Return Top K most similar chunks  
4. Top K chunks + original query → LLM → grounded response  

#### SIMILARITY MEASURES:
|  | Dot Product | Cosine Similarity |
| --- | --- | --- |
| Considers magnitude? | YES (magnitude + angle) | NO (angle only) |
| NLP interpretation | Higher mag ≈ richer<br>content | Smaller angle ≈<br>more similar |


VECTOR INDEXES (needed for large-scale; brute-force too slow):  
| Index | Description |
| --- | --- |
| HNSW | Hierarchical Navigable Small-World Graph;<br>IN-MEMORY graph-based; very efficient approximate search |
| IVF | Inverted File Flat; partition-based; narrows search<br>space using neighbor partitions/clusters |

Both = approximate similarity search (not exact) at scale  

#### RETRIEVAL CHAIN CODE (LangChain + Oracle 23ai):
```text
OracleVS(embed, connection, table, distance_strategy)
.as_retriever(search_type="similarity", search_kwargs={"k": 3})
ChatOCIGenAI(model_id, endpoint, compartment_id, auth)
RetrievalQA.from_chain_type(llm, retriever,
return_source_documents=True)
chain.invoke({"query": "..."}) → answer + source docs
```

---

## MODULE 4 ▸ CHATBOT USING GENERATIVE AI AGENT SERVICE

### OCI GENERATIVE AI AGENTS — OVERVIEW

Definition: Fully managed service combining LLMs + intelligent retrieval  
to create contextually relevant answers from a knowledge base  

WHAT AN AGENT DOES (example: "Book me a flight to Vegas + Hilton"):  
Step 1: Understand and interpret the query  
Step 2: Determine next steps / plan of action  
Step 3: Retrieve data from data stores  
Step 4: Give a response OR execute an action ("Your travel is booked")  

#### CAPABILITIES:
- → Packaged, validated LLM applications ready to use
- → Scalable, enterprise-efficient; can perform complex tasks autonomously
- → Can mimic chain-of-thought; can automate use cases
- → Users interact via chat interface or API

---

### AGENT KEY FEATURES (from Oracle Docs)

| Feature | Detail |
| --- | --- |
| Simple agent setup | Fully managed; few-step setup process<br>to create and deploy agents |
| Tools orchestration | Orchestrate several tools and services<br>to address complex workflows |
| Multi-turn chat | Dynamic multi-turn dialogues with<br>more human-like interactions |
| Context retention | Ask follow-up questions; agent<br>remembers conversation context across<br>turns for consistent interactions |
| Custom instructions | Guide agent behavior with added<br>instructions (system prompt / preamble) |
| Guardrails | Content moderation + Prompt Injection<br>(PI) protection + PII protection at<br>endpoints |
| Human-in-the-loop | Optional; real-time monitoring and<br>human intervention capability |
| Scalability and security | OCI's inherent secure, scalable infra |

---

### AGENT ARCHITECTURE

INTERFACE (chatbot, web app, voice, API)  
↓  
LLM — 4 CORE OPERATIONS:  
| Operation | Description |
| --- | --- |
| REASONING | Analyze input; provide logical response |
| ACTING | Determine actions (query DB, call APIs, etc.) |
| PERSONA | Maintain consistent tone/style for brand/use case |
| PLANNING | Organize multi-step workflows strategically |

↓  
RESPONSE → FEEDBACK LOOP → SHORT-TERM MEMORY  

LLM INPUTS: Memory (short/long-term) | Tools (APIs, DBs) | Prompt (query)  

---

### DATA HIERARCHY & CORE CONCEPTS

| Concept | Definition |
| --- | --- |
| Data Store | Repository where data RESIDES<br>(e.g., Object Storage bucket, database) |
| Data Source | Provides CONNECTION DETAILS to the data store;<br>enables agent to access and retrieve data |
| Knowledge Base | VECTOR STORAGE SYSTEM; ingests data from source;<br>organizes for efficient retrieval |
| Answerability | Model generates RELEVANT responses to user queries |
| Groundedness | Responses are TRACEABLE to data sources |
| Session | Interactive conversation; maintains context |
| Agent Endpoint | Access point enabling agent to talk to<br>external systems/services |
| Trace | History of chat (prompts + responses); for<br>monitoring, transparency, decision visibility |
| Citation | Source of info used in response; includes title,<br>external path, doc ID, page numbers |
| Content<br>Moderation | Detects/filters harmful content from prompts<br>and/or responses; harm types: hate, harassment,<br>self-harm, ideological harm, exploitation<br>Applies to: prompt only \| response only \| BOTH |
| Guardrails<br>(at endpoints) | Broader safety umbrella at endpoints:<br>1. Content Moderation (harm types above)<br>2. Prompt Injection (PI) protection<br>3. PII (Personally Identifiable Info) protection<br>All three applied at agent endpoint level |

---

### AGENT TOOLS — 5 TYPES

Each agent can be empowered with one or more TOOLS (up to 20 or 5  
depending on region — see Resource Limits)  

| Tool Type | What It Does |
| --- | --- |
| 1. RAG Tool<br>(Retrieval-Augmented Gen) | READY-TO-USE: Retrieves information<br>from one or more KNOWLEDGE BASES;<br>responds with relevant, context-aware<br>info in natural language |
| 2. SQL Tool<br>(NL to SQL) | READY-TO-USE: Converts natural<br>language queries into SQL statements;<br>CAN RUN the SQL against a connected<br>database to generate responses |
| 3. Agent as a Tool<br>(Agent orchestration) | READY-TO-USE: Orchestrate a NETWORK<br>of specialized agents that<br>collaborate to accomplish a task |
| 4. Function Calling Tool<br>(Custom) | CUSTOM: Call functions YOU define;<br>expand features agent covers;<br>agent runs related function and<br>responds based on function output |
| 5. API Endpoint Calling Tool<br>(Custom) | CUSTOM: Integrate and call OCI APIs<br>and your own REST APIs |


Types 1–3 = READY-TO-USE (managed by OCI)  
Types 4–5 = CUSTOM (you define/configure the function or endpoint)  

---

### THREE DATA SOURCE OPTIONS

| Option | Detail |
| --- | --- |
| 1. Object Storage | Upload files to OCI bucket; service<br>AUTOMATICALLY ingests (service-managed) |
| 2. OpenSearch | Bring your own ingested + indexed data<br>from OCI Search with OpenSearch (BYOD) |
| 3. Oracle 23ai<br>Vector Store | Bring your own vector embeddings from<br>Oracle Base DB 23ai or Autonomous DB 23ai |

---

### OBJECT STORAGE DATA SOURCE — RULES

- Supported formats: PDF and TXT only
- Max file size: 100 MB per file
- Each data source → ONE bucket only
- PDFs CAN include images, charts, reference tables
- → Images/charts in PDFs: max 8 MB
- → Charts must be 2D with labeled axes
- → Model can interpret charts and answer questions about them
- → Reference tables (multi-row/col) are supported
- All hyperlinks in PDFs extracted as CLICKABLE LINKS in chat responses
- Can create an EMPTY FOLDER for the data source → populate data later

---

### ORACLE 23AI VECTOR STORE — SETUP REQUIREMENTS

Gen AI Agents does NOT manage the DB — you must set it up yourself  

#### REQUIRED TABLE FIELDS:
DOCID       → document identifier           (REQUIRED)  
body        → text chunks of the data       (REQUIRED)  
text_vec    → vector embedding of body      (REQUIRED)  
CHUNKID     → chunk identifier              (optional)  
URL         → source URL                    (optional)  
title       → document title               (optional)  
page_number → page reference               (optional)  

REQUIRED RETRIEVAL FUNCTION (e.g., retrieval_func_ai):  
Parameters: p_query (user query text), top_k (# results to return)  
Returns: SYS_REFCURSOR with DOCID, body, score  
(score = similarity distance: cosine / Euclidean)  
Returns top_k rows sorted by similarity score (descending)  

⚠ CRITICAL: Embedding model used in function (for p_query) MUST MATCH  
the model used to generate text_vec in the table!  

---

### AGENT CREATION WORKFLOW

Step 1: Create KNOWLEDGE BASE  
- → Choose data store type (Object Storage / Oracle 23ai)
- → Object Storage: specify bucket + optional hybrid search
- → Oracle 23ai: set up DB tool connection + vector search func
- → Start ingestion job

Step 2: Create AGENT  
- → Name, compartment, welcome message, RAG instructions
- → Assign knowledge base(s) to agent

Step 3: Create ENDPOINT  
- → Access point for the agent
- → Configure session, moderation, trace, citation settings

Step 4: CHAT  
- → Chat with agent via endpoint
- → View citations (source grounding) + traces (decision history)

---

### RESOURCE LIMITS (Source: Oracle Docs, updated 2026-02-06)


INCREASABLE LIMITS (can submit service limit increase request):  
| Resource | Default |
| --- | --- |
| Agents per tenancy | 2 |
| Knowledge bases per tenancy | 3 |
| Endpoints per agent | 3 |
| Files per data source (ingestion) | 10,000 |
| Sessions per agent endpoint | 1,000 |


PRESET LIMITS (CANNOT be changed):  
| Resource | Limit |
| --- | --- |
| Tools per agent (Frankfurt/London/<br>Chicago) | 20 |
| Tools per agent (Ashburn/Sao Paulo/<br>Osaka) | 5 |
| Data sources per knowledge base | 1 |
| Max file size per data source | 100 MB |
| Active ingestion jobs per DS | 1 |
| Knowledge bases per agent | 2 |
| Session idle timeout | Max 7 days; default/min = 1hr |

---

## QUICK-REFERENCE: KEY NUMBERS & FACTS FOR EXAM

### NUMBERS TO REMEMBER

#### MODELS & CONTEXT:
Command R+         → 128K token input; 4K output  
Command R (16K)    → 16K token input;  4K output  
Llama 3.1 70B/400B → 128K token in; 128K token out  
Embedding models   → 1,024 dims (v3); 384 dims (light-v3)  
- → max 512 tokens/input; max 96 inputs/run

#### TRAINING COST REFERENCE:
~$1M to train a 10B parameter model from scratch  
Meta Llama 2 base: 2 trillion tokens for pre-training  
Llama 2 Chat fine-tuning: ~28,000 prompt-response pairs  
Llama 2 RLHF alignment: 1.4M+ examples  
T-Few: ~0.01% of model size (tiny delta)  
Code models: bug patching < 15% success rate  

#### CLUSTER SIZING:
Command R+ hosting       → 2 × Large Cohere units  
Command R hosting        → 1 × Small Cohere unit  
Command R fine-tuning    → 8 × Small Cohere units  
Llama FT                 → 4 × Large Meta units  
Llama hosting            → 1 × Large Meta unit  
Embed hosting            → 1 × Embed Cohere unit  
Full month hosting       → 744 unit-hours; FT minimum → 1 hour  
To FT + host Command R   → need 9 Small Cohere units (8+1)  

#### AGENT LIMITS:
2 agents; 3 KBs; 3 endpoints/agent; 10K files/DS; 1K sessions/agent  
Tools: 20 (Frankfurt/London/Chicago); 5 (Ashburn/SaoPaulo/Osaka)  
1 data source per KB; 2 KBs per agent; 100 MB max file  
Session idle timeout: max 7 days; default/min = 1 hour  
Object Storage: PDF/TXT only; 100 MB/file; 8 MB images in PDFs  

---

### AGENT TOOLS QUICK-REFERENCE

1. RAG Tool          → retrieve from knowledge base (ready-to-use)  
2. SQL Tool          → NL → SQL → run against DB (ready-to-use)  
3. Agent as a Tool   → orchestrate multiple agents (ready-to-use)  
4. Function Calling  → call your custom-defined functions (custom)  
5. API Endpoint      → call OCI or REST APIs (custom)  
Ready-to-use = 1,2,3 | Custom = 4,5  
Human-in-the-loop: optional real-time monitoring + human intervention  

---

### KEY DEFINITIONS TO KNOW

RAG       = Retrieve docs at query time; ground LLM output in real docs  
PEFT/LoRA = Parameter Efficient Fine-Tuning; trains small subset only  
T-Few     = PEFT for Cohere models; ~0.01% new layer weights trained  
RLHF      = Reinforcement Learning from Human Feedback; aligns LLMs  
CoT       = Chain-of-Thought; show reasoning steps in prompt  
Zero-Shot CoT = "Let's think step by step." triggers CoT without demos  
ICL       = In-Context Learning = providing demos in prompt (no params)  
HNSW      = Hierarchical Navigable Small-World Graph (vector index)  
IVF       = Inverted File Flat (partition-based vector index)  
ONNX      = Open Neural Network Exchange (portable model format)  
NLI       = Natural Language Inference (used for groundedness scoring)  
Greedy    = Always pick highest-prob token; DETERMINISTIC  
Beam Search = Multiple sequences simultaneously; better than greedy  
Encoder   = Embed text → vectors (BERT); NOT for generation  
Decoder   = Generate text 1 token/call (GPT, Llama, Cohere Command)  
Embedding = Text → vector; semantically similar = numerically close  
Inference = Model generates output from new input (not just prediction)  

---

### WHAT TO USE WHEN — DECISION RULES

Embedding tasks         → Encoder (NOT decoder)  
Text generation         → Decoder  
Translation             → Encoder-Decoder  
Facts / precise answers → Low temperature / Greedy decoding  
Creative writing        → High temperature  
Repetition reduction    → Frequency/Presence Penalty  
Data changes rapidly    → RAG (not fine-tuning)  
Model underperforms     → Fine-Tuning  
Not enough examples     → Few-shot prompting / RAG  
Multi-step complex task → Chain-of-Thought prompting  
No examples available   → Zero-Shot CoT ("Let's think step by step.")  
Cohere model FT         → T-Few method  
Meta Llama model FT     → LoRA method  
Embedding model FT      → NOT SUPPORTED in OCI  
Command R+ FT           → NOT SUPPORTED in OCI  
Large dataset embedding → Use v3 models (quality ranking feature)  
Re-order docs by relevance → Rerank model (cross-encoder; post-  
retrieval step in RAG pipeline)  
Agent needs structured DB → SQL Tool (NL → SQL → run query)  
Agent needs external API  → API Endpoint Calling Tool  
Agent needs custom logic  → Function Calling Tool  
Multiple agents together  → Agent as a Tool (orchestration)  
Quick model testing       → On-demand access (no cluster needed)  
Custom model inference    → Dedicated AI Cluster (hosting cluster)  

---

### ARCHITECTURE / SECURITY QUICK-FIRE

Who can access a model? → Only apps within the SAME tenancy  
What encrypts model weights? → OCI Key Management Service  
Where are fine-tuned weights stored? → OCI Object Storage (encrypted)  
Cluster sharing? → SINGLE-TENANT; GPUs NEVER shared across customers  
RDMA → high-speed low-latency GPU interconnect in dedicated cluster  
T-Few memory benefit → base model loaded ONCE; only ~0.01% delta swap  
Cohere vs Meta → use same cluster type (don't mix)  
Default cluster quota → ZERO; must request service limit increase  
Oracle 23ai vector field must match embedding model → same model used  
to create text_vec AND to embed p_query in retrieval_func_ai  
Agent Tools by region: 20 (EU/US-Chicago) vs 5 (US-East/SaoPaulo/JP)  
Agent Guardrails = 3 things: Content Moderation + PI + PII protection  
Agent Tool types: RAG(1), SQL(2), Agent-as-Tool(3) = ready-to-use;  
Function Calling(4), API Endpoint(5) = custom  
Rerank = cross-encoder scoring; use AFTER vector retrieval in RAG  
On-demand = no cluster; pay-per-use; pre-trained models only  
Dedicated = cluster required; fine-tuning + hosting custom models  

---

> **END OF CHEAT SHEET — Good Luck on 1Z0-1127-25!**