---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Alimentation électrique, contrôleurs DGM et bus CAN"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/Fusibles.jpg"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/elec_a.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schéma électrique CS4218PRO.055.001.01 (del.hod) -final (servis).pdf"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300001 - CS00300349 (SAUF CS00300197).pdf"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300350 --.pdf"
keywords:
  - "DGM1"
  - "DGM2"
  - "CAN-H"
  - "CAN-L"
  - "alimentation"
---

# Sujet

Alimentation des contrôleurs DGM1 et DGM2, état de fonctionnement et liaisons du bus CAN de la KRPAN CS4218 PRO.

## Objectif

Séparer un défaut d'alimentation d'un défaut de contrôleur, de faisceau ou de communication avec le joystick.

## Alimentation de la machine

La machine doit être raccordée directement à la batterie du tracteur avec le faisceau fourni.

- Fil 1 : positif, borne 15/30.
- Fil 2 : négatif, borne 31.
- Section minimale du câble entre batterie et prise : 6 mm².
- Tension attendue, tracteur chaud, machine en coupe et ventilateur à vitesse maximale : 13,5 à 14,5 V.
- Capacité minimale de l'alternateur : 40 A.

Une tension inférieure à 13,5 V dans ces conditions impose le contrôle de la batterie, de l'alternateur, des connexions, de l'oxydation et des chutes de tension avant tout remplacement de contrôleur.

## Contrôleurs DGM

Chaque contrôleur comporte un voyant de fonctionnement qui doit clignoter en service normal. Si le voyant ne clignote pas, contrôler en premier le fusible 15 A, l'alimentation et la masse du contrôleur.

| Contrôleur | Connecteur | Alimentation | Masses | CAN-H | CAN-L |
| --- | --- | --- | --- | --- | --- |
| DGM1 | X1 | C1.1, Ub | A8.1 et B8.1 | C2.1 | C3.1 |
| DGM2 | X3 | C1.1, Ub | A8.1 et B8.1 | C2.1 | C3.1 |

## Bus CAN et joystick

Le joystick, référence 200003725, communique sur les lignes CAN-H et CAN-L communes à DGM1 et DGM2. Lorsqu'une perte de communication est suspectée :

1. Vérifier que les deux DGM sont alimentés et que leurs voyants clignotent.
2. Contrôler les masses aux bornes indiquées.
3. Machine hors tension, contrôler la continuité de CAN-H puis de CAN-L entre le joystick, DGM1 et DGM2.
4. Inspecter les connecteurs et rechercher un court-circuit entre CAN-H, CAN-L, le positif ou la masse.
5. Isoler l'organe défectueux avant remplacement. Un remplacement sans modification du symptôme écarte l'organe remplacé mais ne valide pas automatiquement le suivant.

## Références et configuration

La référence du joystick 200003725 est commune aux deux plages de numéros de série documentées.

La configuration à course de fendage variable utilise DGM1 référence 200009702 et DGM2 référence 200009951. La configuration à course standard utilise d'autres références :

| Plage de numéros de série | Configuration | Contrôleurs répertoriés |
| --- | --- | --- |
| CS00300001 à CS00300349, sauf CS00300197 | Course standard | 200009952 et 200009953 |
| CS00300001 à CS00300349, sauf CS00300197 | Course variable | 200009702 et 200009951 |
| CS00300350 et suivants | Course standard | 200011688 et 200011689 |
| CS00300350 et suivants | Course variable | 200009702 et 200009951 |

Avant remplacement, identifier le numéro de série et la configuration de course de fendage de la machine. L'affectation individuelle DGM1/DGM2 des paires de la configuration standard reste à confirmer.

## Interprétation des résultats

- Aucun voyant DGM : rechercher une perte commune d'alimentation ou de masse.
- Un seul voyant DGM éteint : contrôler le fusible, l'alimentation et la masse de ce contrôleur.
- Deux DGM actifs mais commandes absentes : poursuivre par le bus CAN, le joystick, les entrées de sécurité et les capteurs concernés.
- Alimentation conforme à vide mais défaut en coupe : répéter la mesure sous charge, ventilateur au maximum.

## Documents liés

- [Signalisation de la LED du panneau de commande](interpretation-clignotement-rapide-led.md)
- [Capteurs et interverrouillages de cycle](capteurs-et-interverrouillages.md)
- [Diagnostic d'une LED blanche à cinq clignotements](../../troubleshooting/CS4218_PRO/led-cinq-clignotements-joystick-defectueux.md)

## Mots-clés

- alimentation 12 V
- DGM ES211
- fusible 15 A
- bus CAN
- joystick
- connecteur X1
- connecteur X3
