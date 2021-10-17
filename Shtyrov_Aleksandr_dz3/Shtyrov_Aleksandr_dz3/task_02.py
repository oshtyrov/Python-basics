user_data = {
    'name': 'Max',
    'surname': 'Pupkins',
    'yob': '2000',
    'city': 'Stambul',
    'email': 'pupkins@pup.com',
    'tel': '937-99-92'
}


def print_user_values(tel, surname, name, yob,
                      city, email):
    print(f'Данные пользователя: {name} {surname}, {yob} года рождения,'
          f'город проживания: {city}, email: {email}, tel: {tel}')


print_user_values(**user_data)


