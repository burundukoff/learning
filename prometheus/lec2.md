Процесс сбора данных для Prom это exposition , сбор идет по http протоколу в формате plaintext в кодировке UTF-8
для коментариев используется # , кроме случаев если пишем HELP и TYPE /
В случае HELP ожидается как минимум название метрики
Общий вид метрик 
Метрики, в общем, имеют следующий формат:

metric_name{label_name="label_value",label_name="label_value"} value timestamp

Обычно метрики собираются exporters это сторонние приложения которые собирают метрики и отдают prom уже в нужном ему виде
Можно писать свои експортеры, еть готовые библиотеки
Можно встраивать уже выдачу метрик напрямую в свои библиотеки, там тоже есть уже готовые библиотеки
------------------------
самый первый это node exporter, для win wmiexporter
используется для считывания данных о железе и может о состоянии systemd сервисов
запускается как бинарник под root из командной строки , вся настройка с помощью парамтеров из командной тсроки
но т.к. таким образом это не наш метод, то лучше сделать systemd сервис и запускать его

Все ключи и параметры лучше вынести в отдельный файл, чтобы не перечитывать systemd файл

2.  Создадим файл со списком ключей для запуска Node Exporter.

Node Exporter не имеет конфигурационного файла и настраивается дополнительными ключами. Для того, чтобы каждый раз не перечитывать настройки systemd, список ключей вынесен в файл: /etc/sysconfig/node_exporter.

cat <<EOF > /etc/sysconfig/node_exporter
OPTIONS=""
EOF

3. Создаем systemd сервис.

cat <<EOF > /usr/lib/systemd/system/node_exporter.service 
[Unit]
Description=Prometheus Node exporter for machine metrics
Documentation=https://github.com/prometheus/node_exporter

[Service]
Restart=always
User=root
EnvironmentFile=/etc/sysconfig/node_exporter
ExecStart=/usr/local/bin/node_exporter \$OPTIONS
ExecReload=/bin/kill -HUP \$MAINPID
TimeoutStopSec=20s
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
EOF

С помощью директивы: EnvironmentFile все переменные из файла, указанного в этой директиве, добавляются в env, это позволяет нам передавать список ключей для Node Exporter через переменную $OPTIONS без изменения службы.

NB! Обратите внимание, Node Exporter требует root привилегий.

4. Обновляем список служб systemd, запускаем Node exporter и добавляем в автозапуск.

systemctl daemon-reload
systemctl start node_exporter
systemctl enable node_exporter

5. Проверяем работу.

По умолчанию, Node Exporter слушает порт 9100.

curl -I http://localhost:9100

Ответ должен быть примерно таким:

HTTP/1.1 200 OK
Date: Fri, 08 Nov 2019 14:01:07 GMT
Content-Length: 150
Content-Type: text/html; charset=utf-8