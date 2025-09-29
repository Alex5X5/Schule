from abc import abstractmethod


class IAufgabe:


    @abstractmethod
    def run(self):
        pass

    def __call__(self):
        self.run()