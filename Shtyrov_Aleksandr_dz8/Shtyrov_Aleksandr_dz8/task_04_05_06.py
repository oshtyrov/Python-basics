class Stock:
    pass


class OfficeEquipment(Stock):
    def __init__(
            self, producer, model_name, weight, color,
            length, width, height
    ):
        self._check_int_valid_input(
            weight, length, width, height
        )
        self.producer = producer
        self.model_name = model_name
        self.weight = weight
        self.color = color
        self.sizes = {
            'length': length, 'width': width, 'height': height
        }
        self._items_in_stock = 0

    @classmethod
    def _check_int_valid_input(
            cls, weight, length, width, height
    ):
        check_list = [weight, length, width, height]
        for el in check_list:
            if not isinstance(el, int):
                raise ValueError(
                    f'"{el}" is not int.'
                )

    def get_office_equip(self, new_items):
        if not isinstance(new_items, int):
            raise ValueError(f'{new_items} is not int.')
        self._items_in_stock += new_items

    def transfer_office_equip(self, transf_oe):
        if not isinstance(transf_oe, int):
            raise ValueError(f'"{transf_oe}" is not int.')
        if self._items_in_stock - transf_oe < 0:
            raise ValueError(
                f'Not enough units to transfer equipment, '
                f'{self._items_in_stock}, items in stock'
            )
        self._items_in_stock -= transf_oe

    def __str__(self):
        return f'{self.__class__.__name__}: {self.producer},' \
               f' {self.model_name}, {self.color}, weight = {self.weight} kg,\n' \
               f'sizes = {self.sizes},\nitems in stock {self._items_in_stock}.'


class Printer(OfficeEquipment):
    def __init__(
            self, producer, model_name, weight, color,
            length, width, height, print_per_minute=None
    ):
        super().__init__(
            producer, model_name, weight, color,
            length, width, height
        )
        self.print_per_minute = print_per_minute


class Scanner(OfficeEquipment):
    def __init__(
            self, producer, model_name, weight, color,
            length, width, height, scan_per_minute=None
    ):
        super().__init__(
            producer, model_name, weight, color,
            length, width, height
        )
        self.scan_per_minute = scan_per_minute


class Xerox(OfficeEquipment):
    def __init__(
            self, producer, model_name, weight, color,
            length, width, height, copy_per_minute=None
    ):
        super().__init__(
            producer, model_name, weight, color,
            length, width, height
        )
        self.copy_per_minute = copy_per_minute


try:
    # a = Scanner('HP', 'Nimbus-2000', 2, 'white', 50, 50, 50)
    # print(a)
    # a.get_office_equip(20)
    # print(a)
    # a.transfer_office_equip(10)
    # print(a)
    a = Scanner('HP', 'Nimbus-2000', 'qwerty', 'white', 50, 50, 50)
    # a.transfer_office_equip('qwerty')

except ValueError as e:
    print(f'ValueError: {e}')
except AttributeError as e:
    print(f'AttributeError: {e}')
except Exception as e:
    print(f'Exception: {e}')
