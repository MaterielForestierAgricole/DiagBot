---
machine: WENGLOR I12H012
brand: WENGLOR
category: technical_reference
language: fr
title: "Brochage et test du capteur inductif"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(40).md"
keywords:
  - "capteur inductif"
  - "M12"
  - "PNP"
  - "sortie NC"
  - "sortie NO"
---

# Sujet

Brochage et contrôle électrique du capteur inductif Wenglor I12H012, décrit comme un capteur PNP quatre fils alimenté en 10 à 30 V DC.

## Objectif

Contrôler les deux sorties complémentaires sans dépasser le courant maximal de sortie.

## Brochage

| Broche | Couleur | Fonction |
| --- | --- | --- |
| 1 | marron | alimentation positive, 10 à 30 V DC |
| 2 | blanc | sortie complémentaire PNP, normalement fermée |
| 3 | bleu | 0 V, masse |
| 4 | noir | sortie principale PNP, normalement ouverte |

## Principe

- Sortie normalement ouverte, broche 4 : 0 V sans cible métallique ; tension d'alimentation lorsque la cible est détectée.
- Sortie normalement fermée, broche 2 : tension d'alimentation sans cible métallique ; 0 V lorsque la cible est détectée.
- Courant maximal indiqué pour une sortie : 150 mA.

## Procédure au multimètre

1. Alimenter la broche 1 avec une tension continue comprise entre 10 et 30 V.
2. Relier la broche 3 au 0 V.
3. Mesurer la tension entre la broche 4 et le 0 V, sans puis avec une cible métallique.
4. Mesurer la tension entre la broche 2 et le 0 V dans les mêmes conditions.

## Résultat attendu

- Broche 4 : passage de 0 V à la tension d'alimentation lors de la détection.
- Broche 2 : passage de la tension d'alimentation à 0 V lors de la détection.

## Test avec une charge

Ne pas brancher directement une lampe de 12 V et 30 W. Elle consomme 2,5 A, soit plus de seize fois le courant maximal indiqué de 150 mA.

Utiliser une LED 12 V avec résistance intégrée ou une charge dont le courant reste inférieur à 150 mA. Pour commander une charge de 30 W, piloter un relais adapté avec la sortie du capteur et alimenter la charge par le circuit de puissance du relais.

## À confirmer

Le modèle, le brochage et le courant maximal n'ont pas été confrontés à une fiche constructeur disponible dans le dépôt. Les confirmer sur l'étiquette et la documentation Wenglor avant câblage.

## Mots-clés

- capteur inductif
- M12
- PNP
- sortie NC
- sortie NO
