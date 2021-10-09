#! /bin/python3
# BTW I use Arch Linux ;)

datapack = "./silva-laser-datapack-e2751"
ressourcepack = "./silva-laser-resourcepack"


def loadTemplate(name):
	with open(f"./templates/{name}","r") as f:
		return f.read()

templatesToLoad = [
	"dropTemplate",
	"functionTemplate",
	"textureTemplate",
	"ghastSpawnEggOverrideTemplate",
	"ghastSpawnEggTemplate",
	"selectTemplate"
]

dropFile = ("kill @e[type=armor_stand,tag=s_new_laser,distance=..1]\n" +
		    "execute if entity @s[tag=s_style_normal] run summon item ~-.2 ~ ~-.3 {Motion:[0.04d,0.22d,0.06d],Item:{id:\"ghast_spawn_egg\",Count:1b,tag:{silva:laser,CustomModelData:6661,display:{Name:'[{\"text\":\"Trigger Laser\",\"italic\":false}]'},EntityTag:{id:\"minecraft: armor_stand\",Invisible:1b,Invulnerable:1b,Marker:1b,ArmorItems:[{},{},{},{id:\"minecraft: ghast_spawn_egg\",Count:1b,tag:{CustomModelData:6661}}],Tags:[\"s_new_laser\",\"s_laser\",\"s_style_normal\"]}}}}")

ghastSpawnEggFile = ""

selectFile = "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n#                                                                                 #\n#       Code by Silvathor                                                         #\n#                                                                                 #\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # "

print("Recherche des textures ...... ",end="\r")
textures = []
with open("blockList.txt", "r") as f:
	textures = f.read().splitlines()

print("Recherche des textures ...... OK")
print(f"{len(textures)} textures trouvées")

print("Recuperation des template ...... ",end="\r")

templates = dict()
for t in templatesToLoad:
	templates[t] = loadTemplate(t)


print("Recuperation des template ...... Ok")


print("Creation des fichiers textures et des commandes ")
baseModelData = 6662
for i,t in enumerate(textures):
	print(f"Création des fichiers pour le block {t} ...... ", end="\r")
	# création de la texture
	with open(f"{ressourcepack}/assets/slaser/models/{t}.json","w") as f:
		f.write(templates["textureTemplate"].replace("{{BLOCK}}", t))
	
	# creation de la commande
	with open(f"{datapack}/data/slaser/functions/craft/add_block/{t}.mcfunction", "w") as f:
		f.write(templates["functionTemplate"]
                    .replace("{{MODELDATA}}", str(baseModelData + i))
					.replace("{{BLOCK}}",t)
				)
	
	dropFile += (templates["dropTemplate"].replace("{{MODELDATA}}", str(baseModelData + i))
										  .replace("{{BLOCK}}", t))
	
	ghastSpawnEggFile += (templates["ghastSpawnEggOverrideTemplate"].replace("{{MODELDATA}}", str(baseModelData + i))
             							   			   			    .replace("{{BLOCK}}", t))

	selectFile += templates["selectTemplate"].replace("{{BLOCK}}", t)

	print(f"Création des fichiers pour le block {t} ...... Ok")

print("Création des fichiers généraux ...... ", end="\r")

with open(f"{datapack}/data/slaser/functions/place/drop.mcfunction","w") as f:
	f.write(dropFile)

with open(f"{datapack}/data/slaser/functions/craft/add_block/select.mcfunction", "w") as f:
	f.write(selectFile)

with open(f"{ressourcepack}/assets/minecraft/models/item/ghast_spawn_egg.json", "w") as f:
	f.write(templates["ghastSpawnEggTemplate"].replace("{{OVERRIDE}}", ghastSpawnEggFile))

print("Création des fichiers généraux ...... Ok")
