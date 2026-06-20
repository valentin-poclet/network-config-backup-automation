config = """
hostname R1

interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0

router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
"""

with open("backups/R1_config.txt", "w") as fichier:
    fichier.write(config)

print("Sauvegarde créée")
