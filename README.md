# silvatorTextureGenerator
Generateur de textures pour le datapack silva-laser

Vidéo youtube: [ici](https://www.youtube.com/watch?v=S3YaT7lix4w)

Lien de téléchargement: [ici](https://www.planetminecraft.com/data-pack/silva-laser/)

Mais surtout, ne clicker pas [ici](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Bon ben voila quoi, ce datapack est **génial** mais il n'est pas parfaitement complet: il manque *la pluspart* des textures de block minecraft 😭.

J'ai donc décidé de faire un programme pour les ajouter ! 😱

## Le fonctionnement
C'est some toutes assez simple: 
1. vous mettez le datapack et le ressourcepack dans le même dossier que le programme
2. vous mettez les blocks que vous voulez dans le fichier `blocklist.txt`
3. vous lancez le programme `blockGenerator.py` (il faut python d'intallé)
4. vous déplacez ensuite le resource pack et le datapack générés dans leur dossier comme d'habitude
5. vous pofitez de ce merveilleux datapack 😁

## changer l'emplacement du dosser datapack ou du dossier ressource pack
Bon, la il y en a qui vont raller parceque ils ne peuvent pas mettre le dossier la ou ils veulent et qu'ils doivent tout déplacer a chaque fois pour avoir la version modifiée.

Je vous anonce d'ors et déjà que c'est possible:
- Avec l'argument `--datapack` vous pouvez préciser ou se situe le datapack
- Avec l'argument `--resourcepack` vous pouvez préciser ou se situe le resourcepack

## Aide pour python
### instalation
Il faut que vous ayez python sur votre machine pour lancer le programme

Sur linux il est sans dout déjà installé sinon, installez le

Sur windows, vous pouvez suivre un tuto [ici](https://docs.python.org/fr/3/using/windows.html) par exemple

### lancement de la commande
Soit vous êtes sous windows et vous avez mis le datapack et le ressourcepack dans le même dossier que le programme et dans ce cas vous pouvez simplement lancer le programme en double clickant dessu.

Soit vous êtes sous linux ou vous voulez avoir le ressourcepack ou le datapack dans un autre dossier et dans ce cas, vous devez ouvrir une console, vous déplacer dans le dossier du programme puis le lancer avec la commande suivante:
```sh
python ./blockGenerator.py [--datapack DATAPACK] [--resourcepack RESOURCEPACK]
```
Les arguments sont entre crochets car ils sont optionels vous pouvez préciser soit l'un soit l'autre soit les deux soit aucun.