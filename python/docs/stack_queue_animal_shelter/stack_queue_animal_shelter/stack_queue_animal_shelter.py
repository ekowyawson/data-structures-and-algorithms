from stack_queue_animal_shelter.queue import Queue
from stack_queue_animal_shelter.invalid_operation_error import InvalidOperationError

class Dog:
    """Represents a dog in the animal shelter.

    Attributes:
        name (str): The name of the dog.
        species (str): The species of the animal, which is "dog" for this class.
    """
    def __init__(self, name):
        self.name = name
        self.species = "dog"

class Cat:
    """
    Represents a cat in the animal shelter.

    Attributes:
        name (str): The name of the cat.
        species (str): The species of the animal, which is "cat" for this class.
    """
    def __init__(self, name):
        self.name = name
        self.species = "cat"

class AnimalShelter:
    """
    Manages an animal shelter that holds only dogs and cats.

    Attributes:
        dog_queue (Queue): A queue to manage dogs in the shelter.
        cat_queue (Queue): A queue to manage cats in the shelter.
        order (int): A counter to track the arrival order of the animals.
    """
    def __init__(self):
        """
        Initializes the AnimalShelter with separate queues for dogs and cats.
        """
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.order = 0

    def enqueue(self, animal):
        """
        Adds an animal to the shelter.

        Args:
            animal (Dog or Cat): The animal to be added to the shelter.

        Raises:
            ValueError: If the animal is neither a dog nor a cat.
        """
        animal.order = self.order
        self.order += 1

        if animal.species == "dog":
            self.dog_queue.enqueue(animal)
        elif animal.species == "cat":
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("Animal must be either a dog or a cat")

    def dequeue_any(self):
        """
        Dequeues the animal that has been in the shelter the longest.

        Returns:
            Dog or Cat: The animal that has been waiting the longest.

        Raises:
            InvalidOperationError: If the shelter is empty.
        """
        if self.dog_queue.is_empty() and self.cat_queue.is_empty():
            raise InvalidOperationError("No animals in shelter")

        if self.dog_queue.is_empty():
            return self.dequeue_cat()
        if self.cat_queue.is_empty():
            return self.dequeue_dog()

        # Compare the order of the animals in the front of the queues
        if self.dog_queue.peek().order < self.cat_queue.peek().order:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        """
        Dequeues a dog from the shelter.

        Returns:
            Dog: The dog that is at the front of the dog queue.

        Raises:
            InvalidOperationError: If there are no dogs in the shelter.
        """
        if self.dog_queue.is_empty():
            raise InvalidOperationError("No dogs in shelter")
        return self.dog_queue.dequeue()

    def dequeue_cat(self):
        """
        Dequeues a cat from the shelter.

        Returns:
            Cat: The cat that is at the front of the cat queue.

        Raises:
            InvalidOperationError: If there are no cats in the shelter.
        """
        if self.cat_queue.is_empty():
            raise InvalidOperationError("No cats in shelter")
        return self.cat_queue.dequeue()

    def dequeue(self, pref):
        """
        Dequeues an animal based on the given preference.

        Args:
            pref (str): The preferred species to dequeue ("dog", "cat", or "any").

        Returns:
            Dog or Cat: The dequeued animal based on the preference.

        Raises:
            InvalidOperationError: If there is no animal of the preferred type in the shelter.
        """
        if pref == "dog":
            return self.dequeue_dog()
        elif pref == "cat":
            return self.dequeue_cat()
        else:
            return None
