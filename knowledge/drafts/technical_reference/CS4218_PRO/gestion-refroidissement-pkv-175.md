---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Commande du refroidissement par le PKV-175"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/refroidisseur.JPG"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300001 - CS00300349 (SAUF CS00300197).pdf"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300350 --.pdf"
  - "sources/inbox/CS 4218 PRO/Manuels utilisateurs/Manuel utilisateur CS 4218 PRO 12.10.2023.pdf"
keywords:
  - "PKV-175"
  - "ventilateur"
  - "refroidissement"
  - "température d'huile"
  - "NTC10"
---

# Sujet

Fonctionnement et diagnostic du refroidissement d'huile commandé par le module PKV-175.

## Objectif

Contrôler la commande progressive du ventilateur, le cycle de nettoyage et les états de défaut à partir de la température d'huile et du voyant du module.

## Composants concernés

- capteur de température NTC10, filetage M22 × 1,5 ;
- contrôleur intelligent de ventilateur PKV-175 ;
- ventilateur et refroidisseur d'huile ;
- fusible de ventilateur 20 A ;
- alimentation directe depuis la batterie du tracteur.

## Principe de fonctionnement

Le PKV-175 adapte en continu la vitesse du ventilateur à la température mesurée par le NTC10. Le démarrage progressif limite le courant de démarrage.

- Entre 35 et 55 °C, la vitesse varie avec la température.
- Au-dessus de 55 °C, le ventilateur fonctionne à sa vitesse maximale.
- Après au moins 10 minutes de fonctionnement, lorsque l'huile redescend sous 35 °C, le ventilateur inverse son sens pendant 30 secondes pour nettoyer le refroidisseur.

## Signalisation du PKV-175

| Voyant | État | Action de contrôle |
| --- | --- | --- |
| Vert, impulsion brève toutes les 3 s | Veille ; module alimenté | Aucun contrôle si l'huile est froide |
| Vert, clignotement toutes les 0,5 s | Régulation continue entre 35 et 55 °C | Vérifier que la vitesse évolue avec la température |
| Vert fixe | Température supérieure à 55 °C ; vitesse maximale | Contrôler le débit d'air et la propreté du refroidisseur |
| Orange fixe | Cycle de nettoyage par inversion pendant 30 s | État normal après refroidissement sous 35 °C et au moins 10 min de fonctionnement |
| Orange, clignotement toutes les 0,1 s | Tension au PKV-175 inférieure à 10,3 V | Contrôler l'alimentation et les chutes de tension |
| Rouge, clignotement toutes les 1 s | NTC10 débranché ; ventilateur arrêté | Contrôler le capteur, son connecteur et son câblage |
| Rouge fixe avec impulsion brève toutes les 3 s | Température d'huile supérieure à 80 °C | Arrêter le travail et rechercher la cause de surchauffe |
| Rouge fixe | Tension inférieure à 9,5 V ; ventilateur arrêté | Rétablir une alimentation correcte avant tout nouvel essai |

## Contrôle de l'alimentation

1. Contrôler le fusible 20 A du ventilateur.
2. Contrôler l'alimentation directe depuis la batterie et l'état des connexions.
3. Vérifier que la section du câble entre batterie et prise est au moins égale à 6 mm².
4. Mesurer la tension au module. Pour le fonctionnement de la machine, elle ne doit pas descendre sous 12,5 V.
5. Si le voyant orange clignote rapidement, rechercher la chute conduisant sous 10,3 V.
6. Si le voyant reste rouge fixe, la tension est sous 9,5 V et le ventilateur est désactivé.

## Références de remplacement

| Plage de numéros de série | Contrôleur de refroidissement |
| --- | --- |
| CS00300001 à CS00300349, sauf CS00300197 | 200005532 |
| CS00300350 et suivants | 200011968 |

La référence doit être choisie à partir du numéro de série réel de la machine.

## Points d'attention

Un ventilateur arrêté par sous-tension ou par déconnexion du NTC10 ne peut plus refroidir l'huile. Corriger le défaut électrique avant de conclure à une défaillance hydraulique ou mécanique du ventilateur.

## Documents liés

- [Signalisation de la LED du panneau de commande](interpretation-clignotement-rapide-led.md)
- [Alimentation électrique, contrôleurs DGM et bus CAN](alimentation-controleurs-et-bus-can.md)
- [Plan d'entretien, fluides et filtration](plan-entretien-fluides-et-filtration.md)

## Mots-clés

- PKV-175
- NTC10
- ventilateur
- refroidisseur
- huile hydraulique
- surchauffe
- sous-tension
