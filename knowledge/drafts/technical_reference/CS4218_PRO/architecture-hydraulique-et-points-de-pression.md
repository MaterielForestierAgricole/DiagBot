---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Architecture hydraulique et points de contrôle de pression"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/Ancien doc/Légende schéma hydro.xlsx"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Ancien doc/Schéma hydraulique CS4218PRO.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/A partir de CS00300203/Bloc de sciage.jpg"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/A partir de CS00300203/Bloc principal.jpg"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/pompes_a.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schema hydraulique 4218 Pro.jpg"
keywords:
  - "hydraulique"
  - "pression"
  - "MP1"
  - "MP2"
  - "MP3"
  - "MP4"
---

# Sujet

Répartition des fonctions hydrauliques et contrôle des pressions sur la KRPAN CS4218 PRO.

## Objectif

Identifier le circuit à contrôler en fonction de la fonction défaillante, raccorder le manomètre au point adapté et comparer la pression mesurée à la valeur attendue.

## Architecture des circuits

Le groupe comporte quatre pompes entraînées par un multiplicateur de rapport 1:3,5 lubrifié avec une huile ISO 150.

| Pompe | Fonctions alimentées | Point de contrôle | Pression maximale |
| --- | --- | --- | --- |
| 1 | Vérin de fendage | MP1 | 235 bar |
| 2 | Scie et tapis d'entrée | MP2 | 230 bar |
| 3 | Moteur et télescope du tapis d'évacuation | MP3 pour le télescope | 170 bar ± 2 pour le vérin de télescope |
| 4, circuit auxiliaire | Montée et descente de la table élévatrice par raccords rapides | MP4.1 | 170 bar ± 2 |
| 4, distributeur principal | Orientation du tapis, coin, table d'appui, guide et presse-bûche | MP4.2 | 140 bar ± 2 |
| 4, descente du guide | Pression réduite du guide | M4.5 | 17,5 bar avec guide 3/8 ; 14,5 bar avec guide Harvester |

Le distributeur principal commande l'orientation gauche/droite du tapis télescopique, la table élévatrice, le coin de fendage, la table d'appui, le guide de coupe et le presse-bûche. Le distributeur de scie commande la chaîne et le tapis d'entrée. Le distributeur du fendeur intègre une approche rapide, le passage en vitesse lente à pression maximale et un retour rapide.

## Procédures de mesure

Les mesures hydrauliques mettent la machine sous pression. Elles sont réservées à une personne compétente. Couper l'entraînement et l'alimentation électrique avant de brancher ou de débrancher un manomètre ou un capteur.

### Circuit auxiliaire MP4.1

1. Brancher un manomètre adapté sur MP4.1.
2. Débrancher les raccords rapides de la table élévatrice.
3. Commander la montée ou la descente de la table.
4. La pression maximale attendue est de 170 bar ± 2.

### Distributeur principal MP4.2

1. Brancher le manomètre sur MP4.2.
2. Orienter le tapis en butée à gauche ou à droite.
3. Maintenir brièvement la commande.
4. La pression maximale attendue est de 140 bar ± 2.

### Pression de descente du guide M4.5

1. Retirer la chaîne de coupe.
2. Déconnecter le capteur B4.1.
3. Placer une pièce de bois transversalement sous le guide.
4. Commander la descente du guide.
5. Comparer la mesure à 17,5 bar pour un guide 3/8 ou 14,5 bar pour un guide Harvester.

### Circuit scie et tapis d'entrée MP2

1. Brancher le manomètre sur MP2.
2. Retirer la boucle des prises auxiliaires III et IV.
3. Actionner le tapis d'entrée.
4. La pression maximale attendue est de 230 bar.

### Circuit de fendage MP1

1. Brancher le manomètre sur MP1.
2. Débrancher le capteur B7.2.
3. Commander le fendage vers l'avant jusqu'en fin de course.
4. Maintenir seulement le temps nécessaire à la lecture.
5. La pression maximale attendue est de 235 bar.

## Filtration

- Les circuits des pompes 1 et 2 utilisent des éléments de filtre haute pression de référence 765200005127.
- Les circuits des pompes 3 et 4 utilisent des éléments intégrés aux distributeurs de référence 765200009061.
- Le kit complet comprenant filtre de retour et joints porte la référence 765FILTRATION4218PRO.
- Lorsque l'indicateur de colmatage du filtre de retour atteint la zone rouge, remplacer l'élément filtrant.

## Points d'attention

- Ne pas rester en butée au-delà du temps nécessaire à la mesure.
- Ne pas effectuer le contrôle MP1 à proximité de la zone de déplacement du vérin de fendage.
- Rétablir les capteurs et les raccordements déposés avant la remise en service.
- Sur le moteur du tapis d'évacuation, conserver un jeu de 2 à 3 mm aux écrous de montage. Le faux-rond observé en fonctionnement est prévu ; le serrage complet des écrous risque d'endommager le moteur.

## Limites

Deux plages de régime de prise de force sont spécifiées : 430 à 480 tr/min et 450 à 480 tr/min. Confirmer la plage applicable avant d'interpréter une pression dépendante du régime.

## Documents liés

- [Diagnostic du cycle de sciage](diagnostic-cycle-sciage.md)
- [Diagnostic du cycle de fendage](diagnostic-cycle-fendage.md)
- [Plan d'entretien, fluides et filtration](plan-entretien-fluides-et-filtration.md)

## Mots-clés

- pompe hydraulique
- distributeur
- manomètre
- limiteur de pression
- MP1
- MP2
- MP3
- MP4.1
- MP4.2
- M4.5
