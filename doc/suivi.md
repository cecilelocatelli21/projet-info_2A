à utiliser avec **https://hackmd.io/**

# :clipboard:  Présentation du sujet

* **Sujet** : Application pour gérer les lectures d'utilisateurs
* **Tuteur / Tutrice** : Elwenn Joubrel ()
* [Dépôt GitHub](https://github.com/ludo2ne/ENSAI-projet-info-2A-template)

# :dart: Échéances

---
Dossier d'Analyse :  :clock1: <iframe src="https://free.timeanddate.com/countdown/i83zdl7u/n1264/cf11/cm0/cu2/ct4/cs0/ca0/co0/cr0/ss0/cac009/cpcf00/pcfff/tcfff/fs100/szw256/szh108/iso2026-09-17T20:00:00" allowtransparency="true" frameborder="0" width="130" height="16"></iframe>

---


```mermaid
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    title       Diagramme de Gantt
     
    section Suivi
    TP1 et Suivi 1               :milestone, 2026-08-28,
    TP2 et Suivi 2               :milestone, 2026-09-04,
    TP3 et Suivi 3               :milestone, 2026-09-11,
    TP4                          :milestone, 2026-09-18,
    TP5 et Suivi 4               :milestone, 2026-09-25,
    Suivi 5                      :milestone, 2026-11-03,
    3j immersion                 :active,    2026-11-03, 3d
    Suivi 6                      :milestone, 2026-11-05,
    
    section Rendu
    Dossier Analyse              :milestone, 2026-09-17,
    Rapport + Code               :milestone, 2026-11-21,
    Soutenance                   :milestone, 2026-12-09,
    
    section Vac
    Toussaint                    :crit,    2026-10-23, 2026-11-02
    
    section Analyse
    analyse sujet                :active,    2026-08-28, 2026-09-07
    modélisation                 :active,    2026-09-05, 2026-09-13
    rédaction                    :active,    2026-09-10, 2026-09-16
    relecture                    :active,    2026-09-16, 2026-09-17
    
    section Code
    coder une v0                 :active,    2026-09-20, 15d
    lister classes à coder       :active,    2026-10-07, 7d
```

# :calendar: Livrables

| Date    | Livrables                                                    |
| ------- | ------------------------------------------------------------ |
| 17 sept. | [Dossier d'Analyse](https://www.overleaf.com/)               |
| 21 nov. | Rapport final + code (:hammer_and_wrench:  [correcteur orthographe et grammaire](https://www.scribens.fr/))|
| 09 déc. | Soutenance                                                   |

# :construction: Todo List

## Dossier Analyse

* [ ] Diagramme de Gantt
* [ ] Diagramme de cas d'utilisation
* [ ] Diagramme de classe
* [ ] Répartition des parties à rédiger

## Code

* [x] Créer dépôt Git commun
  * [ ] vérifier que tout le monde peut **push** et **pull**
* [ ] Version 0 de l'application
  * coder une et une seule fonctionnalité simple de A à Z, et faire tourner l'appli
  * cela permettra à toute l'équipe d'avoir une bonne base de départ
* [ ] Lister classes et méthodes à coder

---

* [ ] appel WS
* [ ] création WS
* [ ] Vue inscription
* [ ] hacher password

---

<style>h1 {
    color: darkblue;
    font-family: "Calibri";
    font-weight: bold;
    background-color: seagreen;
    padding-left: 10px;
}

h2 {
    color: darkblue;
    background-color: darkseagreen;
    margin-right: 10%;
    padding-left: 10px;
}

h3 {
    color: darkblue;
    background-color: lightseagreen;
    margin-right: 20%;
    padding-left: 10px;
}

h4 {
    color: darkblue;
    background-color: aquamarine;
    margin-right: 30%;
    padding-left: 10px;
}

</style>
