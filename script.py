from abc import ABC
03 20 18 86 79 / 03 20 18 86 08
class Rectangle:
    """Classe définissant un rectangle caractérisé par sa longueur et sa largeur"""
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
    
    # methode area
    def area(self):
        """Calcule l'aire du rectangle"""
        return self.length * self.width

class Bird:
    """Un oiseau."""

    # ici on utilise deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """Les attributs définis ici sont des attributs d'instance."""
        self.position = 1, 2
        self.name = name
        
        # On accède à l'attribut de classe "positions" avec self (c'est possible).
        self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé..."

class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]

 

class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size
    
    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()
    
    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color
    
    def paint(self, color):
        """Paint le marteau."""
        self.color = color
    
    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()
    
    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis."""
     
    MAX_TIGHTNESS = 5
    
    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0
    
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
          self.tightness -= 1
    
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
          self.tightness += 1
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""
    
    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
          self.in_wall = True
    
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
          self.in_wall = False
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."

print("Hello World !")
# Instancier une boite, un tournevis et un marteau
toolbox = ToolBox()
screwdriver = Screwdriver()
hammer = Hammer()

# Mettre le tournevis et le marteau dans la boite
toolbox.add_tool(screwdriver)
toolbox.add_tool(hammer)

# Instancier une vis
screw = Screw()
print(screw)
# Serrer la vis avec le tournevis
screwdriver.tighten(screw)
print(screw)

# Instancier un clou
nail = Nail()
print(nail)
# Enfoncer le clou avec le marteau
hammer.hammer_in(nail)
print(nail)

# Héritage

"""Définit les classes propres à notre forum. ;)"""


class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.name}'.")


class ImageFile(File):
    """Fichier image.
    Pas plus à ajouter pour l'instant !
    """
    def display(self):
        """Affiche le fichier."""
        print(f"Fichier image '{self.name}'.")

# classe ImageGIF héritant de ImageFile
class ImageGIF(ImageFile):
    """Fichier GIF."""
    def display(self):
        """Affiche le fichier."""
        super().display()
        print("Fichier image de type GIF")

class ImagePNG(ImageFile):
    """Fichier GIF."""
    def display(self):
        """Affiche le fichier."""
        super().display()
        print("Fichier image de type PNG")


class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    """Message."""

    def __init__(self, user, time_posted, content):
        """Initialise l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.content)


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)


user = User("Jean", "azerty")
moderator = Moderator("Modo", "qwerty")

fil = user.make_thread("Premier fil", "Ceci est le premier fil de discussion.")
fil.display()

post1 = moderator.post(fil, "Ceci est un message de modérateur.")
fil.display()

post2 = user.post(fil, "Ceci est une réponse hors sujet.")
post3 = moderator.post(fil, "Je suis modérateur, ce message est hors sujet.")
fil.display()

moderator.delete(fil, post3)
moderator.delete(fil, post2)
fil.display()

post4 = user.post(fil, "Ceci est une réponse au premier message.", file=ImageGIF("mon_image.gif", 1234))
moderator.post(fil, "superbe image")
fil.display()




class Drink:
    """Une boisson."""

    def __init__(self, price):
        """Initialise un prix."""
        self.price = price

    def drink(self):
        """Boire la boisson."""
        print("Je ne sais pas ce que c'est, mais je le bois.")


class Coffee(Drink):
    """Café."""
    
    prices = {"simple": 1, "serré": 1, "allongé": 1.5}

    def __init__(self, type):
        """Initialise le type du café."""
        self.type = type
        super().__init__(price=self.prices.get(type, 1))


    def drink(self):
      """Boire le café."""
      print("Un bon café pour me réveiller !")