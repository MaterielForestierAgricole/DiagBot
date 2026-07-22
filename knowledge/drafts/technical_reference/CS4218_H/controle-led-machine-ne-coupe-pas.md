---
machine: CS4218
variant: H
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Contrôle initial de la LED lorsque la machine ne coupe pas"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(14).md"
keywords:
  - "diagnostic initial"
  - "LED blanche"
  - "machine ne coupe pas"
  - "PKV-175"
---

# Sujet

Observation initiale de la LED blanche du boîtier PKV-175 lorsqu'une KRPAN CS4218 H ne lance pas le cycle de coupe.

## Objectif

Orienter le premier contrôle à partir de l'état de la LED de commande.

## Procédure

1. Mettre la machine dans les conditions normales de préparation au travail.
2. Observer la LED blanche du boîtier PKV-175 au moment de la demande de coupe.
3. Identifier son état : allumée fixe, clignotante ou éteinte.
4. Si elle clignote, compter précisément les clignotements successifs.

## Résultat attendu

La LED reste allumée de manière fixe lorsque la machine est prête.

## Interprétation des résultats

- LED fixe : l'état « prêt » est établi ; poursuivre le diagnostic sur la fonction de coupe.
- LED clignotante : relever le nombre de clignotements avant de rechercher la signification du code.
- LED éteinte : contrôler en priorité l'alimentation électrique générale.

## Limites

L'état de la LED oriente le contrôle suivant mais n'établit pas à lui seul la cause de la panne. La signification des différents nombres de clignotements n'est pas établie par cette source.

## Documents liés

- [Contrôle du circuit d'alimentation électrique](../CS4218_H/controle-circuit-alimentation-electrique.md)
- [Mesure de la tension entre PS et GND](../CS4218_H/mesure-tension-entre-ps-et-gnd.md)

## Mots-clés

- diagnostic initial
- LED blanche
- machine ne coupe pas
- PKV-175
