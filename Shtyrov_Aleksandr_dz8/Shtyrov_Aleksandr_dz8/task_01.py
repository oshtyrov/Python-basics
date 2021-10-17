class Data:
    constlen_str_date = 10

    def __init__(self, date):
        self._check_str_data(date)
        self._int_date = self._date_int_converter(date)
        self._check_dm_data(self._int_date)

    def _check_str_data(self, date):
        if len(date) != self.constlen_str_date and date.count('-') < 2:
            raise ValueError('Input date is not valid')

    @classmethod
    def _date_int_converter(cls, date):
        date_list = date.split('-')
        _int_date = [int(el) for el in date_list]
        print([type(el) for el in _int_date])
        return _int_date

    @staticmethod
    def _check_dm_data(date_list):
        if 1 < date_list[0] > 31:
            raise ValueError(f'Input day "{date_list[0]}" is not valid.')
        if 1 < date_list[1] > 12:
            raise ValueError(f'Input month "{date_list[1]}" is not valid.')
        if len(date_list[2]) != 4:
            raise ValueError(f'Input year "{date_list[2]}" is not valid.')


try:
    a = Data('32-11-1989')
    # a = Data('11-111-111')
except ValueError as e:
    print(f'ValueError: {e}')
except AttributeError as e:
    print(f'AttributeError: {e}')
except Exception as e:
    print(f'Exception: {e}')
