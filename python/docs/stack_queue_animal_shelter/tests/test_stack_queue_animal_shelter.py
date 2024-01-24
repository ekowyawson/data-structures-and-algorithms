import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat("Felix")
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog("Clifford")
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat("Garfield")
    dog = Dog("Lassie")
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat("Cinderella")
    dog = Dog("Brian")
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat("Tom")
    dog = Dog("Fido")
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual
