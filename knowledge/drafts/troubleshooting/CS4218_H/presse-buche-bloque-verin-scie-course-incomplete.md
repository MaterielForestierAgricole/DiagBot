---
machine: CS4218
variant: H
brand: KRPAN
product_family: CS
category: troubleshooting
language: fr
title: "Le presse-bûche reste en bas après le cycle de sciage"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(15).md"
---

# Problème

Le presse-bûche reste bloqué en position basse à la fin du cycle de sciage.

## Symptômes

- Le presse-bûche ne remonte pas après le sciage.
- Le capteur de position haute de la lame ne s'allume pas lorsque la lame remonte.

## Conditions d'apparition

Le défaut apparaît en fin de cycle de sciage, lorsque la lame doit revenir à sa position haute maximale.

## Observations et diagnostic

- La lame n'atteignait pas sa butée mécanique haute contre le châssis.
- Le vérin de scie ne rentrait pas entièrement.
- Le piston du vérin était en train de se dévisser de la tige.

## Contrôles de confirmation

- Présenter un objet métallique devant le capteur de position haute permet de vérifier son fonctionnement.
- Dans le cas observé, le capteur s'allumait pendant ce test et le presse-bûche remontait.
- Lorsque la lame remontait, le capteur restait éteint parce que la lame n'atteignait pas sa butée mécanique haute.

## Cause probable

Course de rentrée incomplète du vérin de scie, provoquée par le dévissage du piston sur la tige. La lame n'atteint alors pas sa position haute et le capteur ne déclenche pas la remontée du presse-bûche.

## Solution

Refixer le piston sur la tige ou remplacer le vérin de scie. Après remontage :

1. Vérifier la rentrée complète du vérin.
2. Vérifier que la lame atteint la butée mécanique haute contre le châssis.
3. Vérifier que le capteur de position haute s'allume.
4. Vérifier que le presse-bûche remonte.

## Pièces concernées

- Vérin de scie.
- Capteur de position haute de lame.
- Presse-bûche.

## Mots-clés

- CS4218 H
- capteur de position haute
- course incomplète
- fin de cycle
- lame
- presse-bûche
- vérin de scie
