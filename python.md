# Notes Python

# POO en Python

## POO : Les classes

### Introduction

Une classe contient un état et un comportement :
- l'**état** fait référence à des données ou des variables
- le **comportement** désigne une série de chose que la classe peut faire.

En POO il existe trois types d'attributs :
- les attributs d'**instance** : propres aux instances crées
- les attributs de **classe** (propre à la classe et partagés entre les instances)
- les attributes **statiques** : presque indépendants de la classe

### Syntaxe en python

#### Création d'une classe

``` python
class Rectangle
  def __init__(self, length, width, color='red'):
    self.length = length
    self.width = width
    self.color = color

  def calculateArea(self):
    return self.width * self.height

```

Les méthodes d'instance incluent toujours "self" en 1er paramètre.

La méthode `__init__` est une méthode magique en python. Elle est nommé constructeur.
Lors de la création, l'instanciation, de la classe il faudra founir les attributs attendu par le constructeur. 

Il faudra fournir `length` et `width` en respectant l'ordre tandis que ``color`` est facultatif car une valeur par début à été défini à ``red``

- Les **attributs d'instance** sont donc des variables définies à l'aide de ``self``. Elles sont relatives à l'instance, et ne peuvent être accédées dans instanciations. Les méthodes de classe sont des méthodes classiques sui possèdent ``self`` en **premier paramètre**.
- Les **attributs de classe** sont donc des variables définies directement **dans le corps de la classe**. Elles peuvent être accédées par la classe sans passer par l'instanciations. Les attributs de classe peuvent **se référencer entre eux** mais ne peuvent pas accéder aux attributs d'instance. Les méthodes de classe sont précédées par`` @classmethod``, et leur premier paramètre sera ``cls`` à la place de ``self``. Les attributs de classe sont souvent utilisés pour créer des données ou des actions gloables à la classe, qui **ne dépendent pas** d'une instance. Les instances peuvent cependant y accéder. Modifier un attribut de classe dans une instance le modifiera **dans toutes les autres**.
- Les attributs statiques sont des attributs qui n'ont pratiquement aucun lien avec la classe. Seules les méthodes peuvent être statique. Pour les créer il suffit de les faire précéder par ``@staticmethod``.

``` python
class Bird:
    """Un oiseau. 🐦"""

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
    
    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )


# On peut accéder aux variables de classe sans instanciation.
Bird.names
Bird.positions
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird = Bird("mouette")

# On le retrouve avec la méthode find_bird.
print(Bird.find_bird((1, 2)))
# méthode statique
print(Bird.get_definition())
```

Il est recommander de privilégier les attributs d'instance qui permettenbt d'utiliser la POO à son plein potentiel. Les attributs de classe peuvent être très utiles, mais sont plus rares. Les attributs statiques sont à l'opposé du paradigme orienté objet, il faut éviter de les utiliser, quitte à utiliser un attribut de classe à la place.

#### Instanciation d'une classe

``` python
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 2, "blue")
rect3 = Rectangle(3, 1, color="pink")
rect4 = Rectangle(length=2, width=3, color="white")
```

#### Accès et Modification d'un objet

``` python
print(rectangle.length)
rectangle.color = "yellow"
area = rectangle.calculate_area()
print(area)
```

### L'héritage en python

#### L'héritage

L'héritage permet de créer une **classe enfant** à partir d'une **classe parent**, qui contient les attributs du **parent** ainsi que d'autres attributs spécifiques à l'**enfant**. Cela permet de réutiliser le code sans avoir à le dupliquer.

Pour définir une classe **enfant**, il suffit de mettre le nom de la classe enfant **entre parenthèse** après le nom de classe : ``class Enfant(Parent)``.

#### La surcharge

La **surcharge** désigne le concept selon lequel une classe enfant crée un **nouvelle implémentation** d'une **méthode héritée** : lorsqu'un méthode dans une classe enfant est créée avec le **même nom** et la **même signature** qu'une méthode dans la classe parent, la méthode enfant l'**emporte**.

``` python
from abc import ABC   # permet de définir des classes de base

class Shape(ABC):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return length * length
```
Dans ce cas **ABC**, signifie **Abstract Base Class**. C'est le mécanisme python pour implémenter une **classe abstraite**. C'est une classe qui ne peut pas être **instanciée**. Une classe abstraite peut aussi insister pour qu'une méthode soit implémentée par ses enfants, pour cela on utilise le décorateur ``@abstractmethod``.

#### L'héritage multiple

L'héritage multiple est aussi possible en mettant entre parenthèses les différentes classes parents séparées par des virgules : ``class Enfant(ParentUn,ParentDeux, ...)``. L'héritage multiple est à utiliser avec précaution. Il existe généralement des design plus simples et plus faciles.

Si deux classes parentes implémentent la même méthode, python choisira celle qui est présente dans la classe la plus à gauche.


#### super()

L'**héritage** permet de récupérer les méthodes de la classe Parent. La **surcharge** permet de modifier entièrement les méthodes héritées. **super()** va permettre de récupérer le code des classes Parents depuis les classes Enfants.

``` python
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
```

Dans cette exemple ``Coffee`` est une sous-classe de ``Drink``, elle possède ses propres tarifs qu'elle passe au constructeur de ``Drink`` pour initialiser le bon prix.



``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```
``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```





``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```