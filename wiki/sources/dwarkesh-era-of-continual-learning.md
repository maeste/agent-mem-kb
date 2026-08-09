---
type: source
created: 2026-08-08
updated: 2026-08-08
tags: [continual-learning, ai-economics, regulation, moat, alignment, scaling]
source_path: raw/web/dwarkesh-era-of-continual-learning/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Dwarkesh: 8 Predictions for the Era of Continual Learning

**Autore:** Dwarkesh Patel
**Data:** 2026-08-08
**URL:** https://www.dwarkesh.com/p/era-of-continual-learning
**Raw:** [[raw/web/dwarkesh-era-of-continual-learning/index.md]]

## TL;DR

Otto previsioni sull'impatto del continual learning (modelli che si aggiornano dai dati di deployment, non solo da pre-training). Dwarkesh sostiene che cambierà regolazione, alignment, competitività tra lab e dinamica enterprise.

## Punti chiave

### 1. Regolazione: il modello "train then deploy" è obsoleto
Se i pesi si aggiornano quotidianamente dalle sessioni di lavoro, le safety eval pre-deployment perdono senso. Meglio ispezioni periodiche (mensili/trimestrali) su base continua.

### 2. Alignment: tecniche attuali non valgono
L'alignment è calibrato su pesi congelati. Con weight updates continui e cross-user, servono tecniche nuove: come prevenire jailbreak emergenti, persona drift, backdoor iniettate dagli utenti. Più vicino all'educazione umana che al safety engineering.

### 3. Diversità delle menti AI
Oggi <5 modelli prominenti, simili (stessi dati). Con continual learning, esperienze diverse producono AI effettivamente diverse.

### 4. Ritorni accelerati al leader
Il modello migliore attracta più utenti → più feedback → modello ancora migliore. Data flywheel che si auto-rafforza.

### 5. Pressione a deployare prima
Anthropic ha usato Mythos internamente da febbraio, publicato a giugno. In regime continual, 4 mesi di gap = 4 mesi di deployment learning persi. Il competitor che shippa prima parte peggiore ma migliora più veloce.

### 6. Switching cost = moat
Oggi zero switching cost tra AI (inizi con Codex, finisci con Claude Code). Con continual learning, cambiare modello = licenziare un dipendente con mesi di contesto e riaddestrarne uno nuovo. Lock-in reale, margini alti.

### 7. Carrot and stick enterprise
Lab sussidiano chi permette training sulle proprie sessioni (specialmente lavoro economicamente rilevante). Chi rifiuta non accede ai modelli migliori. Google-search economics.

### 8. Economies of scale in inference
Batch size ottimale per sparse model (DeepSeek V3) >2.400 sequenze concorrenti. Company con molto traffico serve efficientemente la propria weight fork; utente singolo a batch size 1 → 100x+ penalty. Le personalized weights favoriscono le big org.

## Connessioni nel vault

- **harness-design**: il continual learning è correlato al filone self-improving harness (Prime Agent `/refine`, Muse Code co-training). Dwarkesh lo framea a livello di modello, non di harness
- **memory-skills-co-evolution**: la domanda "cosa sopravvive tra le esecuzioni" ora si estende dal livello session/app al livello dei pesi stessi
- Il punto 5 (Anthropic Mythos febbraio→giugno) è dato concreto sul gap internal/external
