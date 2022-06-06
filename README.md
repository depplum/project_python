Доброго времени суток!
-------------------------------------
Если вы посетили мой репозиторий, значит, вы - сисадмин, который нуждается в помощи, либо мой преподаватель, охотно желающий проверить мой проект (почему-то я склоняюсь больше ко 2 варианту)...
-------------------------------------------------
Мой скрипт имеет огромную ценность, ведь он выполняет жизненно важную функцию !!! вывод последних n файлов в директории по времени изменения или доступа. Скрипт получает путь к директории, режим - изменение или доступ, количество файлов, которое нужно вывести. А еще реализовывает обработки всех типов ошибок при вводе данных.
-----------------------------------------------------
Звучит круто, а на деле все еще интереснее.

Я реализовала скрипт на двух яп: Python и Bash.
----------------------------------------------------------
Для запуска кода на баше следует:
1) Загрузить файл 
2) Разрешить доступ командой chmod +x название_файла
3) Запустить код командой ./название_файла

Для запуска на питоне следует:
1)Загрузить файл
2)Запустить код командой python3 название_файла -d [path/to/dir] -a [access or change] -c [the first n]

------------------------------------------------------------------
Немного о баше и  питоне:
Bash — усовершенствованная и модернизированная вариация командной оболочки Bourne shell. Одна из наиболее популярных современных разновидностей командной оболочки UNIX. Особенно популярна в среде Linux, где она часто используется в качестве предустановленной командной оболочки. 
+ Универсальность и доступность
+ Не требуется установка дополнительных пакетов
+ Средство автоматизации работы с файлами и утилитами

Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.
+ Скорость разработки
+ Синтаксис
+ Разнообразие библиотек

-----------------------------------------------------------------------------
Вывод: все языки программирования важны и нужны, но честно говоря, я выбираю питон. ТК на нем код было писать явно проще, понятнее (я же его дольше изучала), а баш можно сравнить с пальмой, которую увидел впервые житель сибири. А если перейти к серьезным разговорам, то по сути реализация скрипта не была сильно легче ни на питоне, ни на баше. В питоновском скрипте более сложная логика, а в баше более сложные выражения. Объем примерно одинаковый. В реализации на python были использованы библиотеки: sys, argparse - для аргументов командной строки и os для получения информации о файлах и получения самих файлов при момощи os.walk. В обеих реализациях удалась обработка ошибок.
------------------------------------------------------------------------------------------
[photo_2022-06-06_05-57-20](https://user-images.githubusercontent.com/89969340/172087033-f9114d9a-34e2-424b-8599-7268919f58e5.jpg)

PS: Альберт Андреевич, зная вашу любовь к тщательному анализу кода и всех его свойств, я сделала приятный бонус )))) коммент к каждой строчке :)
