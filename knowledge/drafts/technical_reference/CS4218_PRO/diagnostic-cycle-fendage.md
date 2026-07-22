---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: technical_reference
language: fr
title: "Diagnostic du cycle de fendage"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Guide de diagnostic CS 4218 Pro.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/belier_a.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Photos/capteur fendeur_a.JPG"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schéma électrique CS4218PRO.055.001.01 (del.hod) -final (servis).pdf"
keywords:
  - "fendage"
  - "vérin"
  - "B6.2"
  - "B7.2"
  - "Y17.2"
  - "Y18.2"
---

# Sujet

Diagnostic ordonné d'un cycle de fendage qui ne démarre pas, ne revient pas ou manque de puissance sur la KRPAN CS4218 PRO.

## Objectif

Séparer un défaut d'autorisation ou de capteur d'un défaut d'électrovanne, de distributeur, de pompe, de pression ou de régime de prise de force.

## Conditions préalables

1. Contrôler une tension de 13,5 à 14,5 V à la machine dans les conditions de travail.
2. Contrôler le régime de prise de force et confirmer la plage applicable à la machine ; deux plages incompatibles restent ouvertes à validation.
3. Relever la signalisation de la LED du panneau. Quatre clignotements indiquent que le vérin n'est pas reconnu en position arrière.
4. Vérifier que le protecteur droit est fermé et que l'arrêt d'urgence est libéré.

## Le vérin ne sort pas

1. Vérifier que B6.2 reconnaît la position entièrement rentrée.
2. Contrôler l'alimentation et la magnétisation de l'électrovanne de sortie Y17.2.
3. Si elle n'est pas commandée, contrôler son câblage, l'entrée liée au cycle et la sortie du contrôleur.
4. Si elle est commandée mais que le vérin reste immobile, contrôler le bloc Y17.2/Y18.2.
5. Contrôler le débit en sortie de la pompe 1. Si le débit est absent ou insuffisant, contrôler puis remplacer la pompe seulement après confirmation.

## Le vérin ne revient pas

1. À l'arrivée en fin de course avant, vérifier que B7.2 s'allume.
2. Contrôler l'alimentation et la magnétisation de l'électrovanne de retour Y18.2.
3. Si la commande ne parvient pas à l'électrovanne, contrôler B7.2 et le câblage jusqu'au contrôleur.
4. Si la commande est présente sans retour, contrôler le bloc Y17.2/Y18.2.
5. Une fois le vérin rentré, vérifier le changement d'état de B6.2. Un mauvais réglage de B6.2 peut empêcher l'arrêt ou le cycle suivant.

## Vitesse ou puissance insuffisante

1. Vérifier que le vérin rentre entièrement et que le régime de prise de force reste dans la plage requise.
2. Mesurer la pression à MP1 : débrancher B7.2, commander le fendage vers l'avant jusqu'en fin de course et maintenir seulement le temps nécessaire à la lecture.
3. La pression maximale attendue est de 235 bar.
4. Si la pression est insuffisante, mesurer simultanément le débit de la pompe 1 avec un débitmètre.
5. Débit insuffisant : contrôler la pompe 1.
6. Débit conforme mais pression insuffisante : contrôler le limiteur de pression et le bloc distributeur.
7. Vitesse rapide absente mais pression finale correcte : contrôler la valve double vitesse d'approche.
8. Retour lent : contrôler la soupape de retour rapide.

## Interprétation des résultats

- Pas de départ avec B6.2 incohérent : régler ou remplacer B6.2 avant d'intervenir sur l'hydraulique.
- Commande électrique absente : rechercher le défaut dans les capteurs, le faisceau et le contrôleur.
- Commande et débit présents sans mouvement : contrôler le distributeur et le vérin.
- Débit pompe insuffisant : la pompe 1 est en cause après exclusion de l'entraînement et des restrictions.
- Débit conforme mais pression inférieure à 235 bar : contrôler le limiteur de pression.

## Points d'attention

Le contrôle de pression place le vérin en butée et crée une pression élevée. Rester hors de la zone de mouvement, limiter la durée de maintien et rebrancher B7.2 avant remise en service.

## À confirmer

Les repères des deux électrovannes sont contradictoires. L'attribution « sortie Y17.2, retour Y18.2 » coexiste avec l'attribution inverse. Cette contradiction doit être résolue sur la version et le numéro de série réels avant toute intervention fondée uniquement sur le repère de sortie du contrôleur.

Deux plages de prise de force sont spécifiées : 430 à 480 tr/min et 450 à 480 tr/min. Cette divergence doit être validée avant d'attribuer un défaut de fendage à un régime compris entre 430 et 449 tr/min.

## Documents liés

- [Architecture hydraulique et points de contrôle de pression](architecture-hydraulique-et-points-de-pression.md)
- [Capteurs et interverrouillages de cycle](capteurs-et-interverrouillages.md)
- [Alimentation électrique, contrôleurs DGM et bus CAN](alimentation-controleurs-et-bus-can.md)

## Mots-clés

- pompe 1
- MP1
- limiteur de pression
- valve double vitesse
- retour rapide
- vérin de fendage
