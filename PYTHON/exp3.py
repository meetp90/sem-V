from typing import Union, Sequence

class Employee:
    _id: int = 0
    name: str = ""
    designation: str = ""

    def __init__(self, **kwargs):
        self._id = kwargs["_id"]
        self.name = kwargs["name"]
        self.designation = kwargs["designation"]

    def __str__(self):
        return f"Id: {self._id}, Name: {self.name}, Designation: {self.designation}\n"

class Developer(Employee):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Tester(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

Worker = Union[Developer, Tester]

class Manager(Employee):
    _developers: Sequence[Worker] = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_worker(self, worker: Worker):
        self._developers.append(worker)

    def remove_worker(self, worker_id: int) -> bool:
        for worker in self._developers:
            if worker._id == worker_id:
                self._developers.remove(worker)
                return True
        return False

    def __str__(self):
        details = f"Manager: {super().__str__()}"
        for worker in self._developers:
            details += f"Worker: {worker.__str__()}"
        return details

def main():
    manager = Manager(_id=0, name="Bru", designation="Manager")
    worker1 = Developer(_id=1, name="Lol", designation="Developer")
    worker2 = Tester(_id=2, name="Man", designation="Tester")
    manager.add_worker(worker1)
    manager.add_worker(worker2)
    print(manager)
    manager.remove_worker(worker1._id)
    manager.remove_worker(worker2._id)
    print(manager)

if __name__ == "__main__":
    main()