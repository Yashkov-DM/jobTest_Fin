# Тестовое задание

1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и,
   в т.ч. Flask).
2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры 
   запросов (будет плюсом наличие файлов-схем запросов, например JSON Schema).
3. Данное API должно поддерживать CRUD операции.
4. Тематика данного API связана с продажами машин автодилерами. Модель данных
   (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую,
   на ваше усмотрение, но соответствующую условиям выше.

## Стэк технологий REST API

- PostgreSQL - в качестве базы данных;
- Python 3.6 - язык разработки;
- Django - фрейморк, модели данных;
- Django Rest Framework - фреймворк, отвечающий за представление REST API.
- Docker - для инициализации базы данных PostgreSQL

## Описание endpoints

### GET api/v1/stores
 
Возвращает всех созданных "Авто-дилеров" и содержащиеся в них "Машины"   

**Responses**:

**_status 200_**

```
{
    "id": int,
    "title": str,
    "cars": []
}
```
### POST api/v1/stores

Добавляет новых "Авто-дилеров" 

**Request**:

принимает json следующей структуры:

```
{
    "title": str
}
```

**Responses**:

**_status 201_**

```
{
    "id": int,
    "title": str,
    "cars": []
}
```

### PUT api/v1/stores/{id}/

Обновление данных "Авто-дилеров" по id

**Request**:

принимает json следующей структуры:

```
{
    "title": str
}
```

**Responses**:

**_status 200_**

```
{
    "id": int,
    "title": str,
    "cars": []
}
```

### DELETE api/v1/stores/{id}/

Удаление "Авто-дилеров" и содержащиеся в них "Машины" по id

**Responses**:

В случае выполнения 

**_status 204_**

В случае не выполнения

**_status 404_**

```
{
   "detail": "Not found."
}
```

### GET api/v1/cars
 
Возвращает все созданные "Машины" 

**Responses**:

**_status 200_**

```
{
   "id": 1,
   "title": "KIA RIO IV 2020, 1.6л,  123л.с.",
   "available": true,
   "store": 1
}
```
### POST api/v1/cars

Добавляет новые "Машины" 

**Request**:

принимает json следующей структуры:

```
{
   "title": "KIA RIO IV 2020, 1.6л,  123л.с.",
   "available": true,
   "store": 1
}
```

**Responses**:

**_status 201_**

```
{
   "id": 6,
   "title": "KIA RIO IV 2020, 1.6л,  123л.с.",
   "available": true,
   "store": 1
}
```

### PUT api/v1/cars/{id}/

Обновление данных "Машин" по id

**Request**:

принимает json следующей структуры:

```
{
   "title": "Ford Mustang VI, 2017, 2.3л,  317л.с.",
   "available": true,
   "store": 2
}
```

**Responses**:

**_status 200_**

```
{
   "id": 7,
   "title": "Ford Mustang VI, 2017, 2.3л,  317л.с.",
   "available": true,
   "store": 2
}
```

### DELETE api/v1/stores/{id}/

Удаление "Машин" по id

**Responses**:

В случае выполнения 

**_status 204_**

В случае не выполнения

**_status 404_**

```
{
   "detail": "Not found."
}
```

---



