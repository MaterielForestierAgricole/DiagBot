---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Diagnostic du cycle de sciage"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Guide de diagnostic CS 4218 Pro.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/A partir de CS00300203/Bloc de sciage.jpg"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/courroie.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/moteur coupe.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schéma électrique CS4218PRO.055.001.01 (del.hod) -final (servis).pdf"
  - "sources/inbox/CS 4218 PRO/Manuels utilisateurs/Manuel utilisateur CS 4218 PRO 12.10.2023.pdf"
keywords:
  - "sciage"
  - "guide de coupe"
  - "chaîne"
  - "presse-bûche"
  - "diagnostic"
---

# Sujet

Diagnostic ordonné d'un cycle de sciage incomplet ou d'une coupe incorrecte sur la KRPAN CS4218 PRO.

## Objectif

Localiser la défaillance dans l'autorisation électrique, le serrage du bois, la descente du guide, l'entraînement de chaîne, la remontée ou la qualité de coupe.

## Conditions préalables

1. Contrôler l'alimentation directement à la machine, tracteur chaud, machine en coupe et ventilateur à vitesse maximale. La tension attendue est de 13,5 à 14,5 V.
2. Contrôler le régime de prise de force et confirmer la plage applicable à la machine ; deux plages incompatibles restent ouvertes à validation.
3. Relever la signalisation de la LED du panneau avant toute activation manuelle.
4. Vérifier que le protecteur droit est fermé et que l'arrêt d'urgence est libéré.

## Diagnostic du presse-bûche

1. Maintenir la commande de démarrage du cycle.
2. Vérifier si la table d'appui et l'orientation du tapis fonctionnent. Si aucune de ces fonctions ne répond, contrôler l'alimentation de DGM1, l'électrovanne de sécurité Y9.1, le débit d'alimentation du distributeur principal et la pompe 4.
3. Si Y9.1 n'est pas alimentée, contrôler son câblage jusqu'au contrôleur. Si elle est alimentée mais ne commute pas, contrôler ou remplacer Y9.1.
4. Si le presse-bûche ne descend pas, vérifier l'alimentation et la magnétisation de Y8.1.
5. Si Y8.1 n'est pas commandée, contrôler son câblage et la sortie du contrôleur. Si elle est commandée sans mouvement, contrôler ou remplacer l'électrovanne.
6. Lorsque le presse-bûche descend, vérifier que B5.1 s'éteint. Le tapis d'entrée doit alors être inhibé et le sciage autorisé.

## Diagnostic de la descente du guide

1. Vérifier que la molette de vitesse de descente est ouverte.
2. Machine arrêtée, vérifier la liberté mécanique de la butée de longueur, du mécanisme de guide et de la pompe de lubrification. Un robinet fermé, un piston de pompe grippé ou de la sciure derrière la tôle graduée peuvent bloquer la descente.
3. Contrôler l'alimentation et la magnétisation de Y12.1.
4. Si Y12.1 est commandée sans mouvement, contrôler son tiroir pour encrassement ou grippage.
5. Contrôler la présence de débit en sortie P4.5 du distributeur principal.
6. Si le débit est présent mais insuffisant, contrôler le diviseur de réglage de descente et la pression réduite : 17,5 bar pour un guide 3/8 ou 14,5 bar pour un guide Harvester.

## Diagnostic de l'entraînement de chaîne

1. Vérifier que B3.1 s'éteint lorsque le guide quitte la position haute.
2. Contrôler l'alimentation et la magnétisation de Y1.1.
3. Si Y1.1 n'est pas commandée, contrôler le câblage jusqu'au contrôleur.
4. Si l'activation manuelle de Y1.1 ne fait pas tourner la chaîne, contrôler le bloc Y1.1/Y2.1.
5. Mesurer la pression à MP2 en commandant le tapis après retrait de la boucle des prises auxiliaires. La pression maximale attendue est de 230 bar.
6. Si la pression ne peut pas être obtenue, contrôler le limiteur puis le débit de la pompe 2.
7. Si le débit atteint le moteur mais que celui-ci ne tourne pas, contrôler ou remplacer le moteur hydraulique.
8. Si le moteur tourne sans entraîner correctement la chaîne, contrôler l'état et la tension de la courroie.

## Diagnostic de la remontée et de l'arrêt

1. En position basse, vérifier que B4.1 s'allume.
2. Contrôler l'alimentation et la magnétisation de Y13.1.
3. Si la commande électrique est conforme mais que le guide ne remonte pas, contrôler le bloc Y12.1/Y13.1 et les ressorts de rappel.
4. En position haute, vérifier que B3.1 s'allume et que la chaîne s'arrête.
5. Si la chaîne s'arrête mais que le moteur hydraulique continue à tourner, contrôler la courroie et sa transmission.

## Coupe incorrecte

Lorsque le cycle est complet mais que la coupe reste mauvaise :

1. contrôler l'état et l'affûtage de la chaîne ;
2. contrôler l'usure, les bavures et la rectitude du guide et de son support ;
3. effectuer un essai avec un guide neuf et une chaîne neuve lorsque l'état reste douteux ;
4. vérifier que l'huile arrive sur la partie supérieure de la chaîne pendant le sciage ;
5. adapter la vitesse de descente au bois ;
6. contrôler la pression de descente du guide.

## Interprétation des résultats

- Aucun mouvement hydraulique auxiliaire : rechercher d'abord l'alimentation, Y9.1 et la pompe 4.
- Presse-bûche actif mais guide immobile : concentrer le contrôle sur B5.1, Y12.1, le réglage de débit et la mécanique du guide.
- Guide mobile mais chaîne arrêtée : concentrer le contrôle sur B3.1, Y1.1, MP2, la pompe 2, le moteur et la courroie.
- Cycle complet mais mauvaise coupe : traiter l'ensemble chaîne-guide-lubrification-vitesse-pression.

## Limites

Deux plages de prise de force sont spécifiées : 430 à 480 tr/min et 450 à 480 tr/min. Cette divergence doit être validée avant d'attribuer un défaut de coupe à un régime compris entre 430 et 449 tr/min.

## Documents liés

- [Architecture hydraulique et points de contrôle de pression](architecture-hydraulique-et-points-de-pression.md)
- [Capteurs et interverrouillages de cycle](capteurs-et-interverrouillages.md)
- [Entretien de la chaîne, du guide et de l'entraînement de scie](entretien-chaine-guide-et-entrainement-scie.md)

## Mots-clés

- Y1.1
- Y8.1
- Y9.1
- Y12.1
- Y13.1
- B3.1
- B4.1
- B5.1
- MP2
