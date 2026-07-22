---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Signalisation de la LED du panneau de commande"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Manuels utilisateurs/Manuel utilisateur CS 4218 PRO 12.10.2023.pdf"
  - "sources/processed/2026-07-21/chat-export-2026-07-21(24).md"
keywords:
  - "LED blanche"
  - "panneau de commande"
  - "code défaut"
  - "sous-tension"
  - "sécurité"
---

# Sujet

Interprétation de la LED blanche placée sur le panneau de commande de la KRPAN CS4218 PRO.

## Objectif

Identifier l'état de la machine ou le circuit à contrôler à partir de l'allumage fixe, de la cadence ou du nombre de clignotements de la LED.

## Interprétation

| Signal | État indiqué | Contrôle prioritaire |
| --- | --- | --- |
| LED allumée en continu | Panneau sous tension et prêt à fonctionner | Aucun contrôle si les fonctions sont disponibles |
| Clignotement continu toutes les 0,5 s | Protecteur droit ouvert ou arrêt d'urgence enfoncé | Fermer le protecteur et libérer l'arrêt d'urgence |
| Deux clignotements suivis d'une pause | Sciage inhibé parce que la lame n'est pas en position supérieure | Contrôler la position haute du guide et le capteur B3.1 |
| Trois clignotements suivis d'une pause | Sciage inhibé parce que le presse-bûche n'est pas en position supérieure | Contrôler la remontée du presse-bûche et le capteur B5.1 |
| Quatre clignotements suivis d'une pause | Fendage inhibé parce que le vérin de fendage n'est pas revenu en position arrière | Contrôler le retour du vérin et le capteur B6.2 |
| Cinq clignotements suivis d'une pause | Ventilateur déconnecté ou température d'huile supérieure à 70 °C | Contrôler le raccordement du ventilateur puis la température et le refroidissement de l'huile |
| Clignotement rapide toutes les 0,1 s | Tension du panneau de commande inférieure à 10,5 V | Mesurer l'alimentation au panneau et rechercher une chute de tension |

Lorsque l'arrêt est dû à une température d'huile excessive, la reprise n'est autorisée qu'après retour de l'huile sous 50 °C.

## Contrôle d'une sous-tension

1. Alimenter la machine directement depuis la batterie du tracteur avec le câble prévu.
2. Faire fonctionner le tracteur à chaud, machine en coupe et ventilateur à sa vitesse maximale.
3. Mesurer la tension disponible : elle doit rester entre 13,5 et 14,5 V dans ces conditions.
4. Contrôler l'état de la batterie, la capacité de l'alternateur, le serrage et l'oxydation des connexions.
5. Vérifier que le câble entre la batterie et la prise de la machine a une section minimale de 6 mm².

L'alternateur du tracteur doit fournir au minimum 40 A. Une tension inférieure à 13,5 V dans les conditions de contrôle impose de corriger l'alimentation avant de poursuivre le diagnostic fonctionnel.

## Points d'attention

Le signal de cinq clignotements doit d'abord être traité selon les deux causes définies par la signalisation constructeur. Un cas de terrain distinct a toutefois associé ce même symptôme à une perte de communication CAN provoquée par un joystick défectueux ; ce cas est documenté séparément et ne doit être recherché qu'après contrôle du ventilateur et de la température d'huile.

## Documents liés

- [Diagnostic d'une LED blanche à cinq clignotements](../../troubleshooting/CS4218_PRO/led-cinq-clignotements-joystick-defectueux.md)
- [Commande du refroidissement par le PKV-175](gestion-refroidissement-pkv-175.md)
- [Alimentation électrique, contrôleurs DGM et bus CAN](alimentation-controleurs-et-bus-can.md)
- [Capteurs et interverrouillages de cycle](capteurs-et-interverrouillages.md)

## Mots-clés

- CS4218 PRO
- LED blanche
- code défaut
- panneau de commande
- sous-tension
- température d'huile
