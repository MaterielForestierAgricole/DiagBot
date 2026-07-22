# DiagBot — base de connaissances SAV MFA

DiagBot est la base de connaissances du service après-vente de MFA (Matériel
Forestier Agricole). Il transforme, après revue humaine, des sources techniques
en réponses fiables, traçables et récupérables par un système RAG.

DiagBot n'est ni un manuel d'atelier généraliste ni un dépôt documentaire. Sa
structure vise une utilisation précise : retrouver la meilleure réponse à une
question pratique de technicien.

## Principes non négociables

1. Une conversation est une source, jamais une vérité validée.
2. Aucune donnée technique ne peut être inventée, complétée par intuition ou
   déduite silencieusement.
3. Toute affirmation publiée doit pointer vers une source conservée et vers
   un passage précis de cette source.
4. Une réponse d'assistant, même convaincante, reste non validée tant qu'un
   référent habilité ne l'a pas approuvée.
5. Les sources brutes sont immuables. Une correction produit un nouvel export
   conservé séparément, jamais une réécriture de l'original.
6. Seul le contenu de `knowledge/validated/` alimente la base générée.
7. Les données personnelles, liens temporaires et pièces jointes sont traités
   comme des éléments sensibles.

## Arborescence

```text
.
├── AGENTS.md                    # règles exhaustives pour humains et agents
├── README.md                    # point d'entrée
├── Makefile                     # commandes usuelles
├── sources/
│   ├── inbox/                   # conversations brutes à traiter
│   ├── processed/               # conversations déjà traitées, toujours immuables
│   └── attachments/             # pièces jointes conservées séparément
├── knowledge/
│   ├── drafts/
│   │   ├── troubleshooting/     # pannes et actions correctives en brouillon
│   │   └── technical_reference/ # méthodes et valeurs réutilisables en brouillon
│   └── validated/
│       ├── troubleshooting/     # dépannages approuvés manuellement
│       └── technical_reference/ # références approuvées manuellement
├── templates/
│   ├── troubleshooting.md
│   └── technical_reference.md
├── scripts/                     # inventaire, validation et génération
└── tests/                       # contrôles de régression
```

Les 42 exports initiaux ont été traités et sont conservés, sans modification de
contenu, dans `sources/processed/2026-07-21/`. Deux paires sont des doublons
exacts ; l'outillage les signale mais ne les supprime pas.

## Flux de travail

```text
sources/inbox
      │ audit + décision d'extraction
      ├──► knowledge/drafts/troubleshooting
      └──► knowledge/drafts/technical_reference
                  │ revue et validation humaines
                  ▼
          knowledge/validated ──► build/knowledge-base
```

Une conversation reste une preuve brute dans `inbox/` ou `processed/`. Son
contenu ne doit jamais être corrigé en place. Après traitement, elle peut être
déplacée vers `processed/` sans changer son identité SHA-256.

Le cycle documentaire est volontairement court : extraction en brouillon,
revue humaine du contenu et des preuves, validation dans `knowledge/validated/`,
puis construction de l'index RAG. Une information nouvelle enrichit un document
existant seulement dans le cadre d'une révision explicitement autorisée ; elle
doit ensuite repasser par la validation humaine. Aucun agent ne déclare seul une
fiche validée.

Un dépannage répond à une question de diagnostic précise et conserve le
symptôme, les contrôles, la cause soutenue et l'action corrective. Une référence
technique répond à une question pratique portant sur une méthode, une mesure,
un réglage, une valeur ou un principe de fonctionnement.

Chaque document est autonome et placé dans la catégorie puis dans le dossier de
machine le plus précis, par exemple
`knowledge/drafts/troubleshooting/CS4218_H/`. Il suit le modèle correspondant,
référence les sources exactes et ne contient aucune donnée personnelle inutile.
Seul un document approuvé manuellement est déplacé sous
`knowledge/validated/` dans la même catégorie.

## Conception pour le RAG

La règle centrale est : **un document répond à une question technique
principale**. Le titre et les intentions de recherche doivent se rapprocher des
formulations qu'un technicien saisirait, par exemple « Mesurer la pression à
MP2 » ou « Pourquoi la scie ne descend pas ? ».

Viser environ 500 à 1 500 mots. Cette plage guide la granularité sans imposer de
couper une procédure cohérente ni d'allonger artificiellement une réponse.

- Scinder un document s'il répond à plusieurs questions indépendantes.
- Fusionner des documents si une même question exige toujours leur lecture
  conjointe.
- Ne jamais fusionner des sujets uniquement pour réduire le nombre de fichiers.
- Conserver une copie indépendante par machine/modèle/variante lorsque la même
  connaissance s'applique à plusieurs périmètres.
- Limiter les liens aux documents du même périmètre ; chaque réponse reste
  compréhensible sans suivre ces liens.

Tout nouveau document commence par un résumé de 5 à 10 lignes maximum qui
répond immédiatement à la question principale. Les sections suivantes apportent
la procédure, les valeurs, l'interprétation et les limites effectivement
soutenues par les sources.

## Métadonnées de recherche

Les métadonnées existantes restent utilisées. Les champs facultatifs suivants
améliorent le classement et la récupération :

- `confidence` : `manufacturer`, `field_verified` ou `preliminary` ;
- `search_intents` : formulations réalistes de questions de technicien ;
- `components` : composants et repères importants ;
- `measurements` : points de mesure tels que MP2, PS ou GND ;
- `symptoms` : symptômes observables, uniquement pour les dépannages.

Ne jamais écrire un champ vide ou `null`. Ces listes servent à la recherche et
ne doivent pas recopier inutilement le corps du document.

## Démarrage

Prérequis : Python 3.11 ou ultérieur. Aucun paquet tiers n'est nécessaire pour
les contrôles de base.

```bash
make audit
make catalog
make test
make validate
make build
```

- `make audit` lit tous les exports, calcule leurs empreintes, détecte les
  doublons et vérifie que les fichiers sont lisibles.
- `make catalog` écrit le catalogue reproductible dans
  `build/catalog/sources.json`.
- `make validate` contrôle l'arborescence, les métadonnées Markdown, les
  sections, les sources, les liens, le périmètre des références croisées et les
  règles déterministes de rédaction RAG.
- `make test` exécute les contrôles de régression.
- `make build` copie les documents validés et génère leur index RAG.
- `make clean` vide uniquement le contenu généré de `build/`.

Pour préparer la structure vide d'un brouillon autorisé :

```bash
python3 scripts/create_troubleshooting.py \
  --machine CS4218 \
  --variant H \
  --slug symptome-cause-confirmee \
  --title "Cinq clignotements de LED" \
  --confidence field_verified \
  --search-intent "pourquoi la LED clignote cinq fois" \
  --symptom "cinq clignotements de LED" \
  --source sources/processed/AAAA-MM-JJ/conversation.md
```

Pour préparer une référence technique :

```bash
python3 scripts/create_technical_reference.py \
  --folder CS4218_H \
  --machine CS4218 \
  --variant H \
  --slug mesure-tension-entre-ps-et-gnd \
  --title "Mesurer la tension entre PS et GND" \
  --confidence manufacturer \
  --search-intent "comment mesurer la tension entre PS et GND" \
  --measurement PS \
  --measurement GND \
  --keyword tension \
  --source sources/processed/AAAA-MM-JJ/conversation.md
```

La commande refuse une source inconnue et n'invente aucun contenu technique.
L'extraction et les critères de qualité sont définis dans `AGENTS.md`.

## Identifiants et traçabilité

Une conversation reçoit dans le catalogue l'identifiant
`conv-<sha256 complet>`. L'identifiant dépend des octets du fichier, pas de son
nom ni de son emplacement. Deux exports strictement identiques partagent donc
le même identifiant et restent tous deux répertoriés comme occurrences.

Les références inscrites dans un document de connaissance doivent viser les
fichiers sources exacts : conversation, documentation constructeur, schéma,
catalogue de pièces ou photographie technique utile. Lors de la revue, toute affirmation opérationnelle
doit pouvoir être retrouvée dans un passage précis de ces sources. Un doublon
exact ne constitue pas une confirmation indépendante.

## Sécurité et confidentialité

Les conversations peuvent contenir des noms, adresses électroniques, photos,
identifiants de fichiers et URL signées. Ne pas les recopier dans une fiche sauf
nécessité documentée. Ne jamais exposer `sources/` dans un site public. La
sortie générée doit être relue avant toute diffusion externe.

## Contribution

Lire d'abord [AGENTS.md](AGENTS.md). Ne jamais transformer une hypothèse en
fait, élargir un périmètre de machine sans preuve ou valider au nom d'un
référent technique. Toute modification d'outil doit conserver l'intégrité des
sources et réussir les tests proportionnés.

## État initial audité

L'audit de départ a observé 42 fichiers Markdown, 233 036 octets, 133 messages
utilisateur, 115 messages assistant, 69 références de pièces jointes et deux
groupes de doublons exacts. Les exports n'ont pas de métadonnées structurées.
Ces nombres décrivent l'import initial ; `make audit` reste la référence pour
l'état courant.
