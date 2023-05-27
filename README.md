## Задание

1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

```
 alice@ubserv:~/gb_final_test$ cat >> домашние_животные
 собаки
 кошки
 хомяки
```

![screen of creating the first file.](./screens/0.png "screen of creating the first file.")

```
alice@ubserv:~/gb_final_test$ cat >> вьючные_животные
лошади
верблюды
ослы
```

![screen of creating the second file.](./screens/1.png "screen of creating the second file.")

```
alice@ubserv:~/gb_final_test$ cat домашние_животные вьючные_животные > животные
alice@ubserv:~/gb_final_test$ cat животные
собаки
кошки
хомяки
лошади
верблюды
ослы
alice@ubserv:~/gb_final_test$ mv животные друзья_человека
alice@ubserv:~/gb_final_test$ ls
вьючные_животные  домашние_животные  друзья_человека
alice@ubserv:~/gb_final_test$
```

![screen of uniting and renaming file.](./screens/2.png "screen of uniting and renaming file.")

2. Создать директорию, переместить файл туда.

```
alice@ubserv:~/gb_final_test$ mkdir new_dir
alice@ubserv:~/gb_final_test$ mv друзья_человека new_dir/
alice@ubserv:~/gb_final_test$ ls new_dir
друзья_человека
alice@ubserv:~/gb_final_test$
```

![screen of moving file.](./screens/3.png "screen of moving file.")

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

```
alice@ubserv:~$ sudo add-apt-repository 'deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-8.0'
Repository: 'deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-8.0'
Description:
Archive for codename: bionic components: mysql-8.0
More info: http://repo.mysql.com/apt/ubuntu/
Adding repository.
Press [ENTER] to continue or Ctrl-c to cancel.
```

![screen of adding repository.](./screens/4.png "screen of adding repository.")

```
alice@ubserv:~$  wget -c https://repo.mysql.com/RPM-GPG-KEY-mysql-2022 -O- | sudo apt-key add -
```

![screen of adding repository key.](./screens/5.png "screen of adding repository key.")

```
alice@ubserv:~$ sudo apt update
```

![screen of updating apt.](./screens/6.png "screen of updating apt.")

```
alice@ubserv:~$ sudo apt install mysql-router
```

![screen of installing mysql-router.](./screens/7.png "screen of installing mysql-router.")

4. Установить и удалить deb-пакет с помощью dpkg

```
alice@ubserv:~$ curl -O http://ftp.de.debian.org/debian/pool/main/m/midori/midori_7.0-2.1_amd64.deb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  717k  100  717k    0     0   898k      0 --:--:-- --:--:-- --:--:--  898k
alice@ubserv:~$ sudo dpkg -i midori_7.0-2.1_amd64.deb
[sudo] password for alice:
Sorry, try again.
[sudo] password for alice:
Selecting previously unselected package midori.
(Reading database ... 74589 files and directories currently installed.)
Preparing to unpack midori_7.0-2.1_amd64.deb ...
Unpacking midori (7.0-2.1) ...
```

![screen of installing a package using pdkg.](./screens/8.png "screen of installing a package using pdkg.")

```
alice@ubserv:~$ sudo dpkg -r midori
[sudo] password for alice:
(Reading database ... 74706 files and directories currently installed.)
Removing midori (7.0-2.1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Processing triggers for man-db (2.10.2-1) ...
alice@ubserv:~$
```

![screen of uninstalling a package using pdkg.](./screens/9.png "screen of uninstalling a package using pdkg.")


5. Выложить историю команд в терминале ubuntu

```
alice@ubserv:~$ history
    1  sudo shutdown now
    2  sudo apt update
    3  sudo apt upgrade
    4  sudo reboot now
    5  sudo apt install ca-certificates curl gnupg lsb-release
    6  sudo mkdir -p /etc/apt/keyrings
    7  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    8  echo   "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
```

![screen of commands history.](./screens/10.png "screen of commands history.")

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы).

![diagram of animal classes.](./diagrams/animals.drawio.png "diagram of animal classes.")

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

```
mysql> CREATE DATABASE друзья_человека;
mysql> show databases;
+-------------------------------+
| Database                      |
+-------------------------------+
| information_schema            |
| mysql                         |
| performance_schema            |
| sys                           |
| друзья_человека               |
+-------------------------------+
```

![screen of creating database.](./screens/11.png "screen of creating database.")

8. Создать таблицы с иерархией из диаграммы в БД

```
mysql> CREATE TABLE домашние_животные (   id INT AUTO_INCREMENT PRIMARY KEY,   name VARCHAR(255),   date_of_birth DATE );
Query OK, 0 rows affected (0,03 sec)

mysql> CREATE TABLE вьючные_животные (   id INT AUTO_INCREMENT PRIMARY KEY,   name VARCHAR(255),   date_of_birth DATE );
Query OK, 0 rows affected (0,12 sec)

mysql> show tables;
+-----------------------------------------+
| Tables_in_друзья_человека               |
+-----------------------------------------+
| вьючные_животные                        |
| домашние_животные                       |
+-----------------------------------------+
2 rows in set (0,01 sec)
```

![screen of creating tables.](./screens/12.png "screen of creating tables.")

```
mysql> CREATE TABLE Собаки(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   mass REAL,
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES домашние_животные(id)
    -> );

Query OK, 0 rows affected (0,15 sec)

mysql> CREATE TABLE Кошки(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   breed VARCHAR(255),
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES домашние_животные(id)
    -> );
Query OK, 0 rows affected (0,04 sec)

mysql> CREATE TABLE хомяки(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   furr_color VARCHAR(255),
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES домашние_животные(id)
    -> );
Query OK, 0 rows affected (0,04 sec)

mysql> CREATE TABLE лошади(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   lear VARCHAR(255),
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES вьючные_животные(id)
    -> );
Query OK, 0 rows affected (0,03 sec)

mysql> CREATE TABLE верблюды(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   bend_quantity INT,
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES вьючные_животные(id)
    -> );
Query OK, 0 rows affected (0,41 sec)

mysql> CREATE TABLE Ослы(
    ->   id INT NOT NULL AUTO_INCREMENT,
    ->   parent_id INT NOT NULL,
    ->   capacity REAL,
    ->   PRIMARY KEY (id),
    ->   FOREIGN KEY (parent_id) REFERENCES вьючные_животные(id)
    -> );
Query OK, 0 rows affected (0,12 sec)
```

![screen of creating child tables.](./screens/13.png "screen of creating child tables.")

9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

```
mysql> INSERT INTO домашние_животные(name, date_of_birth) VALUES ('Лайка', '2015-03-12');
Query OK, 1 row affected (0,01 sec)
mysql> INSERT INTO Собаки(parent_id, mass) VALUES (LAST_INSERT_ID(), 9.4);
Query OK, 1 row affected (0,00 sec)

mysql> INSERT INTO домашние_животные(name, date_of_birth) VALUES ('Муся', '2023-001-10');
Query OK, 1 row affected (0,01 sec)
mysql> INSERT INTO Кошки(parent_id, breed) VALUES (LAST_INSERT_ID(), 'Сфинкс');
Query OK, 1 row affected (0,00 sec)

mysql> INSERT INTO домашние_животные(name, date_of_birth) VALUES ('Персик', '2022-03-08');
Query OK, 1 row affected (0,01 sec)
mysql> INSERT INTO хомяки(parent_id, furr_color) VALUES (LAST_INSERT_ID(), 'Розовый');
Query OK, 1 row affected (0,01 sec)

mysql> INSERT INTO вьючные_животные(name, date_of_birth) VALUES ('Ветер', '2018-10-02');
Query OK, 1 row affected (0,01 sec)
mysql> INSERT INTO лошади(parent_id, lear) VALUES (LAST_INSERT_ID(), 'Пегий');
Query OK, 1 row affected (0,01 sec)

mysql> INSERT INTO вьючные_животные(name, date_of_birth) VALUES ('Ветер', '2019-05-10');
Query OK, 1 row affected (0,02 sec)
mysql> INSERT INTO верблюды(parent_id, bend_quantity) VALUES (LAST_INSERT_ID(), 2);
Query OK, 1 row affected (0,01 sec)

mysql> INSERT INTO вьючные_животные(name, date_of_birth) VALUES ('Степан', '2022-11-25');
Query OK, 1 row affected (0,01 sec)
mysql> INSERT INTO Ослы(parent_id, capacity) VALUES (LAST_INSERT_ID(), 24.2);
Query OK, 1 row affected (0,00 sec)
```

![screen of filling up tables.](./screens/14.png "screen of filling up tables.")


