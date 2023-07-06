class AnimalFactory:
    def create_animal(self, animal_class, **kwargs):
        return animal_class(**kwargs)