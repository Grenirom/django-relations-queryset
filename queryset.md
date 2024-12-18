**Что такое QuerySet**
-
QuerySet - это объект, который представляет собой запрос к базе данных. При помощи queryset мы можем считывать, создавать, изменять,  фильтровать и удалять данные из модели

Каждый queryset связан с определенной моделью, из которой берутся данные, и представляют собой коллекций (набор) объектов этой модели

**Как формируется QuerySet**
-
<Model>.objects.<method_name>
Например: Product.objects.all() - вытащит все данные из таблицы Product


**django shell**
-
это оболочка, в которой можно работать с моделями, и писать код
**Команда для входа в django shell**
./manage.py shell

**Основные методы QuerySet**
-
1) .all() - возвращает все объекты из таблицы в БД
Product.objects.all()
2) .filter() - метод, который филтрует данные по определенному условию
Product.objects.filter()
3) .exclude() - метод, который исключает объекты которые подходят по условию 
Product.objects.exclude()
4) .create() - метод, который создает новый объект от модели
Product.objects.create()
5) .get() - метод, который вытаскивает один объект подходящий по условию, если объектов много, то выводится ошибка
Product.objects.get(условие)
6) .count() - метод, который считает количество записей, в таблице
Product.objects.count()
7) .first()/.last() - методы, которые возвращают первый/последний объект в таблице
8) .exists() - метод, который возвращает True/False, и проверяет существует ли товар по заданному условию, используется только после filter
9) .update() - метод, который отвечает за обновление записи в таблице
10) .delete() - метод, который отвечает за удаление записи в таблице
11) .get_or_create() - метод, который либо получит товар, либо его создаст
12) .order_by() - метод, который отвечает за сортировку объектов по какому условию, чтобы сортировать по убыванию, нужно перед условием поставить -

**Look_up fields**
-
Лукап поля (lookup fields) - это специальные условия для фильтрации данных, они используются в методах filter(), exclude(), get()
**Основные lookup fields**
<Model>.objects.<method>(<field>__<lookup>)

1) lt(less than) - меньше чем
2) gt(greater than) - больше чем
3) exact - лукап который означает точное совпадение
4) iexact - то же самое что exact, только не чувствительный к регистр
5) contains - проверяет, содержит ли подстроку, чувстителен к регистру
6) icontains - то же самое что contains, только не чувствительный к регистру

**горячая клавиша для выхода из shell**
-
ctrl + d
