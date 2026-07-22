### User

tu as une image pour la mesure de tensuion d'alimentation?

### Assistant

Oui, mais il n'y a pas de photo réelle dans la documentation.

En revanche, il y a tout ce qu'il faut pour réaliser un schéma pédagogique beaucoup plus parlant que le plan électrique.

Je ferais quelque chose comme ceci dans le manuel :
```
            Mesure de la tension d'alimentation

             Multimètre en Volts DC

                 +──────────────+
      Rouge  ───►│      V       │
      Noir   ───►│              │
                 +──────────────+

                 Coffret électrique

          ┌───────────────────────────┐
          │                           │
          │  PS (+12 V)      ●◄── Rouge
          │                   │
          │                   │
          │  GND (0 V)   ●◄── Noir
          │                           │
          └───────────────────────────┘

Conditions de mesure :
✓ Tracteur chaud
✓ Ventilateur à vitesse maximale
✓ Pendant une phase de coupe
```

À côté du dessin, on peut rappeler les valeurs :

- ✅**13,5 à 14,5 V**: alimentation correcte.
- ⚠️**12,5 à 13,5 V**: alimentation limite, à surveiller.
- ❌**< 12,5 V**: alimentation insuffisante, le diagnostic de la machine devient non fiable.

Ces valeurs sont celles indiquées dans le guide technique et reprises également dans le guide de diagnostic.
CS 4218 H Guide technique v0824

Guide de diagnostic CS 4218 H

Le schéma électrique confirme également que les deux points de mesure sont les bornes**PS (+12 V)**et**0V/GND**sur l'alimentation du coffret électrique.
Schéma Electrique CS4218H

Pour ton guide de mise en route, je peux aller plus loin et réaliser une**illustration 3D "type manuel constructeur"**avec :

- un vrai coffret électrique CS4218H dessiné,
- les pointes de touche rouge et noire,
- les bornes**PS**et**GND**clairement repérées,
- un encadré vert**« Tension correcte : 13,5 à 14,5 V »**,
- un style homogène avec le reste du document.

C'est beaucoup plus professionnel qu'un extrait du schéma électrique.

