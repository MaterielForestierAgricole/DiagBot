---
machine: CS4218
variant: PRO
brand: KRPAN
product_family: CS
category: troubleshooting
language: fr
title: "La LED blanche clignote cinq fois"
sources:
  - "sources/inbox/CS 4218 PRO/Documents atelier/CS 4218 Pro Guide technique v1123.pdf"
  - "sources/inbox/CS 4218 PRO/Documents atelier/Schéma électrique CS4218PRO.055.001.01 (del.hod) -final (servis).pdf"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300001 - CS00300349 (SAUF CS00300197).pdf"
  - "sources/inbox/CS 4218 PRO/Listes de pièces/Liste de pièces CS4218 PRO CS00300350 --.pdf"
  - "sources/inbox/CS 4218 PRO/Manuels utilisateurs/Manuel utilisateur CS 4218 PRO 12.10.2023.pdf"
  - "sources/processed/2026-07-21/chat-export-2026-07-21(28).md"
---

# Problème

La LED blanche du panneau de commande émet cinq clignotements suivis d'une pause.

## Symptômes

- La LED blanche clignote cinq fois de manière répétitive.
- Certaines fonctions peuvent rester indisponibles.
- Dans un cas de terrain, le défaut est resté présent après remplacement du contrôleur DGM1 et du boîtier PKV-175.

## Observations et diagnostic

Le code constructeur associe en premier lieu cinq clignotements à un ventilateur déconnecté ou à une température d'huile supérieure à 70 °C.

1. Contrôler le branchement et le fonctionnement du ventilateur.
2. Contrôler la température d'huile. Si elle a dépassé la limite, attendre son retour sous 50 °C avant d'essayer de remettre la machine en service.
3. Si le ventilateur est raccordé, que la température est conforme et que le code persiste, contrôler l'alimentation et la masse des contrôleurs.
4. Contrôler la continuité des conducteurs CAN-H et CAN-L entre le joystick, DGM1 et DGM2, ainsi que l'état des connecteurs.
5. Sur DGM1, le bus CAN arrive sur X1, C2.1 pour CAN-H et C3.1 pour CAN-L. Sur DGM2, il arrive sur X3, C2.1 pour CAN-H et C3.1 pour CAN-L.
6. Ne remplacer un organe qu'après avoir isolé le défaut par ces contrôles.

Dans le cas de terrain documenté, la continuité de masse était conforme. Le remplacement de DGM1 puis du PKV-175 n'a produit aucun changement. Le joystick a ensuite été identifié comme l'organe défectueux interrompant la communication CAN.

## Cause probable

Les causes définies pour ce code sont un ventilateur déconnecté ou une température d'huile supérieure à 70 °C.

Si ces deux causes sont écartées et que les contrôles CAN reproduisent le cas de terrain documenté, la cause peut être un joystick défectueux qui ne communique plus avec DGM1 et DGM2.

## Solution

- Rebrancher ou réparer le circuit du ventilateur lorsqu'il est déconnecté.
- Corriger la cause de surchauffe et attendre que l'huile redescende sous 50 °C avant la reprise.
- Dans le cas où la perte de communication CAN est isolée au joystick, remplacer le joystick par la référence KRPAN 200003725. Cette référence figure dans les deux catalogues couvrant CS00300001 à CS00300349, sauf CS00300197, puis CS00300350 et suivants.

## Diagnostics écartés

Dans le cas de terrain :

- défaut de continuité de masse ;
- défaillance de DGM1 après remplacement sans effet ;
- défaillance du PKV-175 après remplacement sans effet.

## Pièces concernées

- Joystick : référence 200003725 pour les deux plages de numéros de série documentées.
- Contrôleurs DGM1 et DGM2.
- Contrôleur de ventilateur PKV-175 et ventilateur.

## Limites

Le cas de terrain confirme le diagnostic du joystick mais ne contient pas de validation explicite après son remplacement. Le lien entre la perte CAN et le code de cinq clignotements n'apparaît pas dans la table constructeur ; il doit donc être conservé comme branche de diagnostic secondaire et soumis à validation technique.

## Documents liés

- [Signalisation de la LED du panneau de commande](../../technical_reference/CS4218_PRO/interpretation-clignotement-rapide-led.md)
- [Commande du refroidissement par le PKV-175](../../technical_reference/CS4218_PRO/gestion-refroidissement-pkv-175.md)
- [Alimentation électrique, contrôleurs DGM et bus CAN](../../technical_reference/CS4218_PRO/alimentation-controleurs-et-bus-can.md)

## Mots-clés

- CS4218 PRO
- cinq clignotements
- communication CAN
- DGM1
- DGM2
- joystick
- LED blanche
- PKV-175
