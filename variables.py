number_of_complited_homework = 12
number_of_hour_spent = 1.5
course_name = 'Python'
time_for_one_task = (number_of_hour_spent / number_of_complited_homework)
print('Курс: ' + course_name + ', всего задач: ' + str(number_of_complited_homework) + ', затрачено часов: ' + str(number_of_hour_spent) + ', среднее время выполнения ' + str(time_for_one_task))
# я использовала оператор сложения в линии 5 вместо перечисления через запятую т.к.
# если использовать перечисление, то те строки, которые у меня начинаются с запятой
# в терминале отделяются еще одним пробелом перед запятой и итоговый текст выглядит не грамотно
# собственно, поэтому была необходимость перевести int и float в тип str
# надеюсь, это не ошибка :)