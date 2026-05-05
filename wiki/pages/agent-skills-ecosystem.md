---
type: page
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, agent-skills, ecosystem, registry, governance]
---

# L'ecosistema delle Agent Skills

Le agent skills non sono più solo un meccanismo interno all'agente: la batch di lavori 2026 disegna un *ecosistema* in senso pieno — formato standard, distribuzione, registry, discovery, lifecycle cross-agente, governance. Questa pagina raccoglie il livello di sistema che le pagine su estrazione, riuso e governance toccano solo lateralmente.

## Scala dell'ecosistema (oggi)

- AgentSkillOS riporta oltre 280.000 skill pubblicamente disponibili a inizio 2026, con ecosistemi di scala 200 / 1K / 200K usati come regimi di test [[wiki/sources/arxiv-2603.02176]]
- SkVM analizza un corpus di 118.000 skill da clawhub.ai e skills.sh, due dei principali registry community [[wiki/sources/arxiv-2604.03088]]
- SkillFlow recupera su 36K definizioni minate da GitHub [[wiki/sources/li-2026-skillflow]]; lo standard SKILL.md è aperto da dicembre 2025 e il repo Anthropic ha superato 62K stelle in 4 mesi [[wiki/sources/xu-2026-agent-skills-survey]]

L'ecosistema è quindi grande e in crescita, ma ancora privo della disciplina che software libraries hanno conquistato in trent'anni.

## Registry e distribuzione

Il pattern emergente è "registry community + asset GitHub-backed + protocollo standardizzato":

- Skilldex propone un package manager esplicito per skill (CLI `skillpm`/`spm`, registry Hono/Supabase, server MCP nativo), con conformance score in stile compilatore (0–100) sulla spec SKILL.md, scope gerarchico global/shared/project, e tier di trust seedati dalle skill ufficiali Anthropic — il modello mentale è npm/pip applicato alle skill [[wiki/sources/arxiv-2604.16911]]
- Il mining sistematico di repository agentici open-source [[wiki/sources/arxiv-2603.11808]] tratta GitHub come backend de facto: il framework a tre stadi (analisi strutturale → identificazione semantica → traduzione in SKILL.md) è una via di mezzo tra authoring manuale e scoperta autonoma
- Skilldex introduce inoltre la *skillset abstraction* — bundle di skill correlate con asset condivisi (vocabolari, template, documenti di riferimento) — riconoscendo che la coerenza cross-skill non emerge da skill installate indipendentemente [[wiki/sources/arxiv-2604.16911]]
- L'analisi empirica dell'ecosistema (Ling 2026) conferma che la community adotta il formato in modo eterogeneo, con qualità e sicurezza non uniformi [[wiki/sources/ling-2026-agent-skills-analysis]]

## Discovery decentralizzata e orchestrazione

Trovare la skill giusta in un catalogo da 280K è un problema diverso da trovarla in 36K, ed è diverso ancora se gli agenti sono distribuiti.

- AgentSkillOS costruisce un *capability tree* gerarchico via partizionamento ricorsivo in nodi-categoria, recupera per esplorazione dell'albero, e compone le skill in piani DAG con tre varianti di strategia. Risultato chiave: a parità di skill set ottimale, l'orchestrazione strutturata via DAG batte significativamente l'invocazione piatta — la *composizione*, non la mera disponibilità, è il fattore critico [[wiki/sources/arxiv-2603.02176]]
- Per i sistemi *decentralizzati*, Dazzi et al. studiano il discovery peer-to-peer con doppio churn (host-level e demand-level con stati warm/cold), confrontando overlay structured (Kademlia DHT) e gossip (Cyclon+Vicinity). La regime map è non banale: structured è migliore in regimi stabili o con churn di nodo, gossip può essere più veloce quando domina il readiness degli agenti. Il lavoro è esplicitamente dentro il framework AGNTCY per skill-based agent discovery [[wiki/sources/arxiv-2604.23080]]
- SRA pone il problema retrieval-side: skill come corpus esterno, non come prompt enumeration. SRA-Bench (5.400 task, 636 gold skill in 26.262) mostra che il retrieval funziona, ma l'*incorporation* (capire quando una skill recuperata è effettivamente utile) è il vero collo di bottiglia [[wiki/sources/arxiv-2604.24594]]

## Lifecycle a livello ecosistema

Il SoK di Jiang et al. è il primo tentativo serio di sistematizzare l'intero lifecycle come oggetto di studio in sé, non come dettaglio implementativo dei singoli sistemi:

- Sette stadi: discovery, practice, distillation, storage, composition, evaluation, update — con due tassonomie complementari (sette pattern di sistema, e una orthogonal representation × scope) [[wiki/sources/arxiv-2602.20867]]
- La definizione formale S = (C, π, T, R) — applicability conditions, executable policy, termination criteria, reusable callable interface — fornisce un'astrazione condivisa che distingue le skill da tool atomici, piani one-shot e memoria episodica [[wiki/sources/arxiv-2602.20867]]
- Sul lato evaluation, il SoK riporta che skill curate migliorano sostanzialmente i success rate, mentre skill auto-generate possono *degradare* le performance: la pipeline ha bisogno di gate qualitativi non banali [[wiki/sources/arxiv-2602.20867]]

OneManCompany salta un livello sopra e propone *Talents* — identità di agente portabili che incapsulano skill, tool e configurazioni runtime — orchestrate da un E²R tree search (Explore–Execute–Review) con un Talent Market community-driven per recruitment on-demand: la tesi è che il campo deve passare da "skills" (cosa sa fare un agente) a "organisations" (come strutturare e gestire una forza lavoro di agenti eterogenei). Su PRDBench, OMC ottiene 84.67% di success rate, +15.48 punti rispetto allo stato dell'arte precedente [[wiki/sources/arxiv-2604.22446]].

## Portabilità cross-LLM

Lo stesso file SKILL.md può comportarsi diversamente su modelli diversi, e questo non è un dettaglio di tuning: è un problema strutturale.

- SkVM rileva che abilitare le skill degrada le performance nel 15% dei task (7% per Opus 4.6, 25% per Qwen3-30B) e non aiuta in fino all'87% dei task per almeno un modello: mismatch fondamentale tra spec statica e capacità variabile [[wiki/sources/arxiv-2604.03088]]
- La risposta SkVM è capability-based compilation con 26 dimensioni primitive misurate per coppia modello-harness, JIT code solidification per template ad alta frequenza, e recompilation adattiva: +15.3% completion rate, -40% token, 3.2×–50× speedup [[wiki/sources/arxiv-2604.03088]]
- EvoSkill fornisce evidenza complementare a livello di trasferibilità: una skill evoluta su SealQA migra zero-shot a BrowseComp con +5.3% senza modifiche, suggerendo che l'ottimizzazione *a livello di skill* produce capacità più trasferibili rispetto a prompt- o code-level evolution [[wiki/sources/arxiv-2603.02766]]

## Estrazione dell'ecosistema (memory → skill → registry)

Tre lavori coprono complementarmente la pipeline che riempie il registry:

- Mining strutturale di repo agentici (Bi et al.) come via scalabile tra authoring manuale e open-world discovery, con SKILL.md a tre livelli (metadata 30–100 token / instructions 200–5K / resources unbounded) come target di traduzione [[wiki/sources/arxiv-2603.11808]]
- SkillFoundry come pipeline closed-loop su un domain knowledge tree, con validation a tre livelli (execution / system / synthetic-data testing) e potatura — il 71.1% delle skill prodotte differisce da SkillHub e SkillSMP, indicando che il pool ecosistemico è ancora ben lontano dalla saturazione [[wiki/sources/arxiv-2604.03964]]
- SkillX in chiave knowledge-base auto-costruita con Multi-Level Skills Design + Iterative Refinement + Exploratory Expansion, esplicitamente contro l'apprendimento isolato dei singoli agenti [[wiki/sources/arxiv-2604.04804]]

## Open questions a livello ecosistema

- **Sicurezza non risolta**: il caso ClawHavoc (~1.200 skill malevole infiltrate in un grande marketplace) [[wiki/sources/arxiv-2602.20867]] e il dato del 26.1% di skill community vulnerabili [[wiki/sources/xu-2026-agent-skills-survey]] dicono che il problema è strutturale, non un incidente. Skilldex e SSL forniscono tooling per scoring e ispezione [[wiki/sources/arxiv-2604.16911]] [[wiki/sources/arxiv-2604.24026]], ma non un'autorità di certificazione condivisa.
- **Incorporation vs retrieval**: SRA mostra che gli agenti caricano skill a tassi simili indipendentemente dall'utilità reale [[wiki/sources/arxiv-2604.24594]] — un registry ben popolato non basta, serve giudizio.
- **Composizione vs disponibilità**: AgentSkillOS dimostra che il guadagno viene dall'orchestrazione DAG, non dal mero accesso — l'ecosistema deve standardizzare anche le forme di composizione [[wiki/sources/arxiv-2603.02176]].
- **Capability mismatch cross-LLM**: SkVM rivela che lo stesso skill set produce risultati radicalmente diversi su modelli diversi [[wiki/sources/arxiv-2604.03088]] — la portabilità è un problema attivo, non una proprietà gratuita del formato.
- **Decentralizzazione**: il discovery peer-to-peer non ha una soluzione universale; structured e gossip overlay coprono regimi diversi [[wiki/sources/arxiv-2604.23080]].
- **Layer organizzativo**: passare da skill a *forze lavoro* di agenti (Talents, E²R) [[wiki/sources/arxiv-2604.22446]] sposta il problema di governance dal singolo pacchetto al perimetro dell'organizzazione — un livello di astrazione che la maggior parte degli altri lavori ancora non guarda.

## Domanda aperta

Se l'ecosistema delle skill sta seguendo la traiettoria dei package manager (npm, pip), la lezione storica è che la sicurezza è il debito che nessuno paga finché non esplode. Il dato del 26.1% di vulnerabilità community e ClawHavoc suggeriscono che siamo già nella fase post-esplosione. Skilldex propone scoring e trust tier, SSL propone ispezione strutturale, il SoK propone certificazione: nessuno di questi è ancora un'autorità accettata. La domanda non è se serve un livello di trust condiviso, è chi avrà la legittimità per istituirlo.
