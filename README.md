# Назначение скрипта

Скрипт предназначен для работы с базой данных "Электронного дневника школы", находящегося на репозитории https://github.com/devmanorg/e-diary/tree/master

# Назначение фукций

Функция `create_commendation(child_name,Subject_name)` находит последнюю дату урока для ученика c ФИО (параметр - child_name) и предмету (параметр Subject_name) и созадет похвалу.

Функция `fix_marks(schoolkid)` находит по ученику (параметр schoolkid) все оцеки 2 и 3 и заменяет их на 5.

Функция `remove_chastisements(schoolkid)` находит по ученику (параметр schoolkid) все замечания и удаляет их.