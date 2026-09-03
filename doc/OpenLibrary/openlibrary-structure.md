# Structure de la base OpenLibrary — Synthèse

> Objectif : comprendre comment sont structurées les données de OpenLibrary
> et ce qui est disponible pour pouvoir décider ce qu'on
> garde dans notre propre base de données.

## 1. Comment interroger OpenLibrary

OpenLibrary expose ses données via une **API web** (pas un accès direct à une
base SQL). On l'interroge en tapant des URLs qui renvoient du JSON.

| Besoin | URL type | Exemple |
|---|---|---|
| Rechercher des livres | `search.json?q=...` | `openlibrary.org/search.json?q=le+petit+prince` |
| Voir une œuvre précise | `/works/{id}.json` | `openlibrary.org/works/OL10263W.json` |
| Voir une édition précise | `/books/{id}.json` | `openlibrary.org/books/OL7366018M.json` |
| Voir un auteur précis | `/authors/{id}.json` | `openlibrary.org/authors/OL31901A.json` |
| Voir la définition officielle d'un type | `/type/{nom}` | `openlibrary.org/type/work` |

**Remarques**
- `search.json` renvoie une version **résumée** de chaque livre. 
- Les fiches `/works/...`, `/books/...`, `/authors/...` renvoient l'objet **complet**.

## 2. Les 3 objets métier principaux

OpenLibrary structure ses données autour de 3 types principaux ("regular"),
reliés entre eux :

```
Author (auteur)
   │  a écrit (via author_role : auteur + son rôle)
   ▼
Work (œuvre — l'idée du livre)
   │  a plusieurs
   ▼
Edition (édition — une publication précise et matérielle)
```

**Règle pour savoir où vit une info** : est-ce que cette info change si je
prends un autre exemplaire du même livre (autre traduction, autre format) ?
- Oui → elle vit dans l'**Edition**
- Non → elle vit dans le **Work**

On dispose d'autres types principaux **scan_record** par exemple qui trace le processus de numérisation d'une édition physique. C'est probablement le type d'info que nous pourrons écarter.

On trouve aussi des types secondaires ("embeddable"):

On trouve **author_role** qui identifie si un auteur est "l'auteur" d'un livre ou bien un traducteur par exemple.

### Exemple vérifié : Le Petit Prince

| | Work (`OL10263W`) | Edition (`OL7366018M`) |
|---|---|---|
| Ce que c'est | L'œuvre en général | Une publication précise (Harcourt, 1971) |
| Combien y en a-t-il | 1 seul Work | 688 éditions différentes |
| Année | `first_publish_date`: 1943 (1ère parution, tous éditeurs confondus) | `publish_date`: 1971 (cette édition-là) |
| ISBN | absent (n'a pas de sens à ce niveau) | `9780156503006` |
| Nombre de pages | absent | 113 |
| Thèmes/genres | `subjects`: 67 valeurs (adventure, fantasy, friendship...) | possible mais rarement rempli en pratique |

## 3. Dictionnaire des variables

### 3.1 — Type `Work`

| Champ | Description | Observé sur l'exemple ? |
|---|---|---|
| `title` | Titre de l'œuvre | ✓ "Le petit prince" |
| `subtitle` | Sous-titre | — |
| `authors[]` | Auteur(s) + leur rôle (via `author_role`) | ✓ |
| `subjects[]` | Thèmes/genres (peu normalisés) | ✓ 67 valeurs, très hétérogènes |
| `subject_places[]` | Lieux liés à l'œuvre | ✓ "Sahara Desert" |
| `subject_times[]` | Époques liées à l'œuvre | — |
| `subject_people[]` | Personnes liées à l'œuvre | — |
| `description` | Résumé/description | ✓ |
| `dewey_number[]` | Classification Dewey (bibliothéconomie) | ✓ |
| `first_sentence` | Première phrase de l'œuvre | — |
| `original_languages[]` | Langue(s) d'origine | — |
| `first_publish_date` | Date de toute première publication | ✓ "1971" (⚠ à vérifier : incohérent avec 1943 vu ailleurs) |
| `cover_edition` | Édition choisie pour la couverture affichée | ✓ |
| `covers[]` | Identifiants d'images de couverture | ✓ 61 couvertures |
| `genres[]` | Tags de classification (système différent de `subjects`) | ✓ 3 tags |
| `identifiers` | Liens vers bases externes (Wikidata, Goodreads...) | ✓ |

### 3.2 — Type `Edition`

| Champ | Description | Observé sur l'exemple ? |
|---|---|---|
| `title` | Titre de cette édition | ✓ |
| `authors[]` | Auteur(s) (référence directe, pas de rôle ici) | ✓ |
| `isbn_10` / `isbn_13` | Identifiant international, propre à cette édition | ✓ |
| `number_of_pages` | Nombre de pages de cette édition précise | ✓ 113 |
| `publishers[]` | Éditeur(s) | ✓ "Harcourt Childrens Books" |
| `publish_date` | Date de CETTE publication | ✓ "1971" |
| `physical_format` | Format (poche, relié, cartonné...) | — (à vérifier sur d'autres exemples) |
| `languages[]` | Langue de cette édition/traduction | ✓ |
| `works[]` | Lien retour vers le Work parent | ✓ |
| `subjects[]` / `genres[]` | Existent officiellement mais rarement remplis à ce niveau | — |
| `series[]` | Appartenance à une saga/collection | — |
| `translation_of` | Indique si c'est une traduction | — |
| `source_records[]` | Traçabilité des sources ayant alimenté la fiche | ✓ |

### 3.3 — Type `Author`

| Champ | Description | Observé sur l'exemple ? |
|---|---|---|
| `name` / `personal_name` | Nom de l'auteur | ✓ |
| `title` | Attention : ici ce n'est PAS un titre de livre, mais le nom sous forme "Nom, Prénom" (tri alphabétique) | ✓ |
| `alternate_names[]` | Variantes/orthographes du nom rencontrées dans les sources | ✓ 97 valeurs |
| `bio` | Biographie | ✓ |
| `birth_date` / `death_date` | Dates de naissance/mort | ✓ |
| `photos[]` | Identifiants de photos | ✓ |
| `remote_ids` | Liens vers bases externes (VIAF, Wikidata, ISNI) | ✓ |
| `location` | Lieu associé à l'auteur | — |
| `wikipedia` | Lien Wikipedia | — |

## 4. Points de vigilance sur la qualité des données

- **`subjects` très hétérogènes** : mélange de vrais genres ("Children's
  fiction") et de simples mots-clés thématiques ("love", "loss"). C'est
  précisément le problème que soulève la fonctionnalité F5C (normalisation
  des genres).
- **Doublons/incohérences possibles** : une "version abrégée" d'un livre
  peut être fusionnée dans le même Work que l'original, ou au contraire
  exister comme Work séparé — pas de règle garantie, à vérifier au cas par
  cas selon les livres qui vous intéressent.
- **Champs parfois vides** : beaucoup de champs "officiellement possibles"
  (vu dans `/type/...`) ne sont pas toujours remplis en pratique.
- **Deux systèmes de classification qui coexistent** : `subjects[]` (texte
  libre) et `genres[]` (tags avec identifiant, `/tags/OL...T`) — à ne pas
  confondre.

## 5. Ce qu'on peut écarter d'emblée

D'autres types existent dans OpenLibrary mais sont **hors périmètre** pour
Ex-Libris (plomberie interne à OpenLibrary/Internet Archive) :

| Type | Rôle | Pourquoi on l'ignore |
|---|---|---|
| `scan_record` | Suivi du processus de numérisation d'un exemplaire | Concerne la gestion interne des scans, pas la donnée bibliographique |
| `scan_location` | Localisation physique d'un exemplaire scanné | Idem |
| `user` | Compte utilisateur OpenLibrary | Concerne leurs propres utilisateurs, pas les nôtres |
| `author_role` | Structure "embeddable" (auteur + rôle), n'existe pas seule | Utile à comprendre, mais pas un objet à répliquer tel quel |

## 6. Questions ouvertes pour la suite (à trancher en phase de conception)

- Une entrée "livre" dans notre base Ex-Libris correspond-elle à un **Work**
  OpenLibrary, une **Edition**, ou un mix (Work pour les infos générales +
  ISBN d'une édition de référence) ?
- Que fait-on du couple `subjects` / `genres` ? Les deux sont-ils utiles, ou
  se limite-t-on à un seul système, normalisé (cf. F5C) ?
- Est-ce qu'on gère les traductions comme des Works séparés ou comme de
  simples Editions de l'œuvre originale ?
- Quelles données doit-on **dupliquer/stocker localement** vs. requêter à la
  volée sur l'API OpenLibrary à chaque fois ?
