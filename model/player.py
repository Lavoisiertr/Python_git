class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_helth(self):
        return self.health
    
    def get_attack(self):
        return self.attack
        
    def bienvenue(self):
        print(f"Bienvenue au joueur {self.pseudo}, tu as {self.health} points de vie et {self.attack} points d'attaque")
    
    def damage(self, damage):
        self.health -= damage
        #print(f"Aie... vous venez de subi {damage} dégâts.")
        
    def attack_player(self, target_player):
        #target_player.damage(self.attack)
        damage = self.attack
        if self.has_weapon(): # Si le joueur a une arme
            damage+=self.weapon.get_damage_amount() # Ajoute les dégâts de l'arme au point d'attaque du joueur
        target_player.damage(damage)
    
    def set_weapon(self, weapon): # Méthode pour changer l'arme du joueur
        self.weapon = weapon
        
    def has_weapon(self): # Méthode pour vérifier si le joueur a une arme
        return self.weapon is not None 
        
         