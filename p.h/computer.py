class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage


def print_specs(self):
    print("Display Size:", self.size)
    print("Storage size:", self.storage)


low_spec = Computer('12', '256GB')
high_spec = Computer('27', '1TB')

print('Low Spec Computer:')
low_spec.print_specs()

print('High Spec Computer:')
high_spec.print_specs()



