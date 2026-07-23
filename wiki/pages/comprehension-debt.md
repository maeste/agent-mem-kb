---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [comprehension-debt, dark-factory, verification, agentic, concept]
---

# Comprehension Debt

Il divario crescente tra quante codice esiste e quanto ne capisce un essere umano. Più codice viene generato da agenti senza supervisione, più questo debito si accumula. I test restano verdi mentre la comprensione del sistema eroso silenziosamente.

## Origine

Definito da Osmani in [[wiki/sources/addy-osmani-software-factories]]. La **dark factory** (agenti che shippano codice senza che nessuno lo legga) non paga il debito: lo contrae alla massima velocità possibile, mantenendo i test verdi lungo tutto il percorso. La resa dei conti non è drammatica: è silenziosa e tardiva.

## Back Pressure

La regola cardine: puoi delegare a un loop solo tanta autonomia quanta ne puoi verificare in modo economico e affidabile. La generazione è illimitata; la verifica è il collo di bottia. Senza verifica, si genera un surplus di PR cattivi. Vedi [[wiki/pages/harness-design|harness design]] per come i gate di verifica strutturano l'autonomia.

## Remediation

La **lit factory** mantiene le luci accese dove serve giudizio umano. Non aggiunge review alla fine: sposta il giudizio a monte, su design e architettura, prima che l'agente inizi a generare. Il prezzo è banale: un'ora di design upfront risparmia ore di review su migliaia di righe generate.

## Loop che meritano il dark

Un loop può essere automatizzato completamente solo se: la verifica è economica, gira ad alta frequenza, e non può essere ingannata (green/red oracle, type gate, property test). Loop corti (3-10 step) sono più facili da verificare; oltre i 20 step l'agente perde il filo.
