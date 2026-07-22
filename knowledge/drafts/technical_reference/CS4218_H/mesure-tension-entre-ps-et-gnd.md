---
machine: CS4218
variant: H
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Mesure de la tension entre PS et GND"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(4).md"
  - "sources/processed/2026-07-21/chat-export-2026-07-21(10).md"
  - "sources/processed/2026-07-21/chat-export-2026-07-21(16).md"
keywords:
  - "alimentation électrique"
  - "GND"
  - "multimètre"
  - "PS"
  - "tension continue"
---

# Sujet

Mesure de la tension d'alimentation générale d'une KRPAN CS4218 H entre les bornes PS et GND.

## Objectif

Vérifier que l'alimentation reste suffisante pendant les phases de travail les plus exigeantes.

## Point de mesure

Effectuer la mesure dans le coffret de fusibles gris situé près du distributeur hydraulique principal :

- borne PS : alimentation positive ;
- borne GND : masse électrique.

Ce point est plus accessible que les bornes du contrôleur DGM.

## Procédure

1. Régler le multimètre sur la mesure de tension continue.
2. Placer la pointe rouge sur PS et la pointe noire sur GND.
3. Relever la tension à vide.
4. Amener la machine à sa température de travail.
5. Faire fonctionner le ventilateur à sa vitesse maximale.
6. Relever la tension minimale pendant un cycle de sciage et de fendage.

## Valeurs attendues

- tension à vide : au moins 13,5 V ;
- tension en charge : au moins 12,5 V.

## Interprétation des résultats

- Au moins 13,5 V à vide et au moins 12,5 V en charge : alimentation conforme aux valeurs établies.
- Moins de 12,5 V en charge : alimentation insuffisante ; contrôler la batterie, les connexions, la prise 3 pôles, le câble, les fusibles et la masse.

## À confirmer

Un seuil inférieur à 10,5 V associé à un clignotement rapide de 0,1 s est également cité, mais le document constructeur qui l'établit n'est pas disponible dans le dépôt. Confirmer ce seuil dans le manuel applicable avant validation.

## Documents liés

- [Contrôle du circuit d'alimentation électrique](../CS4218_H/controle-circuit-alimentation-electrique.md)
- [Contrôle initial de la LED lorsque la machine ne coupe pas](../CS4218_H/controle-led-machine-ne-coupe-pas.md)

## Mots-clés

- alimentation électrique
- GND
- multimètre
- PS
- tension continue
