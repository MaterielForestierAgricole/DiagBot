---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Capteurs et interverrouillages de cycle"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Guide de diagnostic CS 4218 Pro.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/capot.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/capteur fendeur_a.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schéma électrique CS4218PRO.055.001.01 (del.hod) -final (servis).pdf"
  - "sources/inbox/CS 4218 PRO/Manuels utilisateurs/Manuel utilisateur CS 4218 PRO 12.10.2023.pdf"
keywords:
  - "capteur"
  - "interverrouillage"
  - "B3.1"
  - "B4.1"
  - "B5.1"
  - "S2"
---

# Sujet

Fonction des capteurs de position et des interverrouillages qui autorisent les cycles de la KRPAN CS4218 PRO.

## Objectif

Identifier le capteur qui bloque une fonction et vérifier que son état correspond à la position mécanique réelle avant d'intervenir sur les électrovannes ou les contrôleurs.

## Capteurs de cycle

| Repère | Position surveillée | État et effet fonctionnel |
| --- | --- | --- |
| B3.1 | Guide en position haute | Le démarrage de la chaîne intervient lorsque le guide quitte ce capteur pendant la descente. Une lame non reconnue en position haute inhibe le sciage et produit deux clignotements de la LED du panneau. |
| B4.1 | Guide en position basse | Déclenche la remontée du guide. |
| B5.1 | Presse-bûche en position haute | Capteur actif : tapis d'entrée autorisé et sciage interdit. Capteur libéré pendant la descente : tapis interdit et sciage autorisé. |
| B6.2 | Vérin de fendage en position arrière | Autorise le départ d'un nouveau cycle de fendage. L'absence de retour reconnu produit quatre clignotements de la LED. |
| B7.2 | Vérin de fendage en position sortie | Désactive le réglage de hauteur du coin lorsque la position avant est atteinte. |
| B1.1 | Table d'appui en position sortie | Allumé lorsque la table est rentrée ou en transit ; éteint lorsqu'elle est entièrement sortie. |
| B2.1 | Table d'appui en position rentrée | Allumé uniquement lorsque la table est rentrée. |
| S2 | Protecteur droit fermé | Protecteur ouvert : aucun composant ne fonctionne et la LED du panneau clignote toutes les 0,5 s. |

L'arrêt d'urgence enfoncé produit la même cadence de 0,5 s que l'ouverture du protecteur droit.

## Méthode de contrôle

1. Relever le code de la LED du panneau avant de déplacer un organe.
2. Contrôler la position mécanique réelle de l'organe concerné.
3. Observer le voyant du capteur, lorsqu'il est présent, pendant le passage devant la cible.
4. Vérifier le réglage, la fixation, l'entrefer, le connecteur et le faisceau.
5. Contrôler l'entrée correspondante au DGM uniquement après avoir établi que le capteur est correctement alimenté et commute.
6. Rétablir tous les protecteurs et capteurs avant un essai de cycle.

## Interprétation des blocages

- Tapis d'entrée inactif alors que le presse-bûche est haut : vérifier que B5.1 est actif.
- Chaîne qui ne démarre pas à la descente : vérifier que B5.1 se libère et que B3.1 change d'état lorsque le guide quitte la position haute.
- Guide qui ne remonte pas : vérifier B4.1 et la position basse réelle.
- Nouveau fendage impossible : vérifier que B6.2 reconnaît le vérin entièrement rentré.
- Réglage de coin indisponible : vérifier si B7.2 signale à tort la position avant du vérin.
- Toutes les fonctions indisponibles : contrôler d'abord S2 et l'arrêt d'urgence, puis l'alimentation des contrôleurs.

## Points d'attention

Ne pas neutraliser un capteur de protecteur pour exploiter la machine. Le débranchement temporaire de B4.1 ou B7.2 n'est utilisé que dans les procédures de mesure hydraulique prévues, par une personne compétente, puis le capteur doit être rebranché avant remise en service.

## Documents liés

- [Signalisation de la LED du panneau de commande](interpretation-clignotement-rapide-led.md)
- [Diagnostic du cycle de sciage](diagnostic-cycle-sciage.md)
- [Diagnostic du cycle de fendage](diagnostic-cycle-fendage.md)
- [Alimentation électrique, contrôleurs DGM et bus CAN](alimentation-controleurs-et-bus-can.md)

## Mots-clés

- capteur inductif
- capteur magnétique
- guide de coupe
- presse-bûche
- vérin de fendage
- table d'appui
- protecteur
