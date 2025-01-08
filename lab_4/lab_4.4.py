#Создание пакета состоящий из нескольких модулей созданых мной.Импорт модулей из пакета
x = 0
while x == 0:
    try:
        import pocket.file_commander

        print(
            "1-читать символ(ы)\n2-читать строку(и)\n3-читать файл\n4-редактировать содержание файл(ы)\n5-поиск файла")
        action = int(input("Что вы хотите сделать? "))
        if action == 1:
            pocket.file_commander.symbol()
            break
        if action == 2:
            pocket.file_commander.lines()
            break
        if action == 3:
            pocket.file_commander.all()
            break
        if action == 4:
            pocket.file_commander.write()
            break
        if action == 5:
            pocket.file_commander.search()
            break
    except ValueError:
        print("Выберите  действие корректно.")