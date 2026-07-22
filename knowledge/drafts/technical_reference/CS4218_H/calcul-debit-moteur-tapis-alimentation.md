---
machine: CS4218
variant: H
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Calcul du débit du moteur du tapis d'alimentation"
sources:
  - "sources/processed/2026-07-21/chat-export-2026-07-21(7).md"
keywords:
  - "débit hydraulique"
  - "moteur hydraulique"
  - "pompe hydraulique"
  - "prise de force"
  - "tapis d'alimentation"
---

# Sujet

Calcul du débit théorique nécessaire au moteur hydraulique du tapis d'alimentation et du débit théorique fourni par la pompe.

## Objectif

Déterminer le débit requis pour la vitesse standard du tapis et vérifier que le débit théorique de la pompe couvre ce besoin.

## Composants concernés

- moteur hydraulique BG S de 80 cm³/tr, référence 300013556 ;
- pignon de chaîne, référence 300004071 ;
- transmission du tapis par chaîne ;
- régulateur-diviseur de débit du bloc hydraulique ;
- pompe de 6,2 cm³/tr entraînée par un multiplicateur de rapport 1:3,2.

## Données d'entrée

- cylindrée du moteur : 80 cm³/tr ;
- vitesse standard du moteur : environ 30 tr/min ;
- cylindrée de la pompe : 6,2 cm³/tr ;
- rapport du multiplicateur : 1:3,2 ;
- régime de prise de force : 430 à 480 tr/min ;
- pression maximale indiquée : 230 bar.

## Calculs

Le débit nécessaire au moteur est calculé par :

`débit = cylindrée × vitesse`

À 30 tr/min :

`80 cm³/tr × 30 tr/min = 2 400 cm³/min = 2,4 L/min`

Le débit théorique de la pompe est calculé après application du rapport du multiplicateur :

- à 430 tr/min : `430 × 3,2 × 6,2 = 8 531 cm³/min`, soit environ 8,5 L/min ;
- à 480 tr/min : `480 × 3,2 × 6,2 = 9 523 cm³/min`, soit environ 9,5 L/min.

## Résultats attendus

- débit théorique requis pour environ 30 tr/min : 2,4 L/min ;
- débit théorique maximal disponible : environ 8,5 à 9,5 L/min selon le régime de prise de force.

Le régulateur-diviseur de débit ajuste le débit disponible afin d'obtenir la vitesse souhaitée du tapis.

## Points d'attention

Ces résultats sont théoriques. Ils ne tiennent pas compte du rendement volumétrique, des fuites internes, des pertes de charge ni du rapport réel de la transmission par chaîne.

## À confirmer

Les caractéristiques d'entrée et la pression maximale n'ont pas été confrontées à une fiche constructeur disponible dans le dépôt. Confirmer ces valeurs avant tout dimensionnement ou réglage.

## Mots-clés

- débit hydraulique
- moteur hydraulique
- pompe hydraulique
- prise de force
- tapis d'alimentation
