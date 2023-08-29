Общий пример строки 

schema://user:password@app.kit.ru:8000/path/to/document/index.php?arg1=data1&arg2=data2

server {
    listen 80;
    server_name example.com;

    location ^~ /admin/ {
        return 202;
    }

    location ~ \.Html$ {
        return 200;
    }

    location ~ \.htMl {
        return 201;
    }
}


    1. Nginx проверяет все location без regexp (без модификаторов ~ и ~*). ~ то регистрозависимая строка, если ~* то строка далее не регистрозависимая.  \. экранирование точки, иначе она обработается как в регулярке как любой символ
    2. Если встретился location с модификатором = и он совпадает с запросом — то поиск прекращается и обработка переходит внутрь найденного location. чтобы nginx не парсил весь конфиг при обращении к главной странице ставят = /
    Если найден подходящий location с модификатором ^~, то дальше location с regexp проверяться не будут и обработка перейдет в найденный location.
    Если подходящих location с модификаторами = или ^~ не найдено, то nginx запоминает location с самым длинным префиксом (самый конкретный) и продолжает поиск среди location с regexp.
    Nginx просматривает все location с regexp и проверяет строку запроса на соответствие regexp'у. Nginx перебирает все regexp location до первого совпадения — как только совпадение найдено, поиск прекращается и обработка уходит в найденный location.
    Если ни один regexp location не подходит — то будет использован location, найденный в четвертом пункте (самый длинный префикс).

    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name test.ccc7a5d229de9c95055b1053a2475041.kis.im;

        location ^~/admin {
                return 403;
        }

        location /admin/readme.md {
                return 200;
        }

        location ~*\.(jpg|png) {
                return 202;
        }

        location ~\.txt {
                return 404;
        }

        location ~\.TXT {
                return 204;
        }

}

    Все запросы на /admin/ и все вложенные файлы и директории должны возвращать 403 (вне зависимости от следующих условий — то есть txt / jpg / png в /admin/ также возвращают 403).
    Все запросы на /admin/readme.md должны возвращать 200.
    Все запросы на файлы с расширением jpg и png в любом регистре должны возвращать 202.
    Все запросы на файлы с расширением TXT должны возвращать 204 (запросы на файлы txt должны возвращать 404).

