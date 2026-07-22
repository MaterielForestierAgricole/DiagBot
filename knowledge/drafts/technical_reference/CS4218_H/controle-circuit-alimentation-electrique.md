---
machine: CS4218
variant: H
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Contrôle du circuit d'alimentation électrique"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(5).md"
  - "sources/processed/2026-07-21/chat-export-2026-07-21(16).md"
keywords:
  - "alimentation électrique"
  - "batterie"
  - "connectique"
  - "fusible"
  - "prise 3 pôles"
---

# Sujet

Contrôle du circuit d'alimentation électrique général d'une KRPAN CS4218 H.

## Objectif

Rechercher une coupure, une résistance de contact ou une chute de tension pouvant interrompre simultanément plusieurs fonctions puis provoquer leur redémarrage.

## Procédure

1. Contrôler l'état et la charge de la batterie du tracteur.
2. Contrôler le serrage, l'oxydation et les traces d'échauffement aux connexions positive et négative de la batterie.
3. Inspecter les broches, le serrage et les traces d'échauffement de la prise d'alimentation 3 pôles entre le tracteur et la machine.
4. Inspecter le câble d'alimentation sur toute sa longueur.
5. Contrôler les fusibles et les porte-fusibles du coffret électrique.
6. Contrôler le câble de masse et son point de fixation.
7. Mesurer la tension entre PS et GND dans le coffret de fusibles gris, près du distributeur hydraulique principal.
8. Relever la tension à vide, puis la tension minimale machine chaude, ventilateur à vitesse maximale, pendant un cycle de sciage et de fendage.

## Valeurs attendues

- à vide : au moins 13,5 V ;
- en charge : ne pas descendre sous 12,5 V.

## Interprétation des résultats

- Une chute sous 12,5 V en charge indique une alimentation insuffisante dans les conditions de mesure définies.
- Une connexion oxydée, desserrée ou échauffée peut provoquer une coupure intermittente même si la tension à vide paraît correcte.
- Une interruption simultanée des fonctions suivie d'un redémarrage justifie le contrôle prioritaire de l'alimentation générale et de ses connexions.

## Documents liés

- [Mesure de la tension entre PS et GND](../CS4218_H/mesure-tension-entre-ps-et-gnd.md)

## Mots-clés

- alimentation électrique
- batterie
- connectique
- fusible
- prise 3 pôles
