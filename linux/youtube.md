lsusb просмотр usb устройств , может не стоять на centos нужно установить usbutils
lspci промотр pci
lshw прсомотр оборудвоания, вроед как устарело
blkid просмотр блочных устройств, можно увидеть id ЖД и прочего, это может понадобится для правки или прсмотра свойств загрузчика



udevadm info -a -p /sys/class/net/tun0  просмотр свойств устройств
udevadm monitor --property --kernel  мониторинг чем занимается устройство
usevadm test /sys/block/sda  проверка устройства

lsmod просмотр загруженных моделей ядра, моули можно смотреть modinfo vmx3 например просмотр модуля сетевухи
rmmod vmx3 прямо в горячую удаляет модуль сетевухи от вмвари
insmod vmx3 вставка модуля назад в жествокм виде, может блокирвоать selinux и пр.
modprobe vmx3 мягкая вставка моделя в ядро, обычно работает


загрузка иедт следующим образом
bios/uefi-grub-kernel-init
при загрузке ели нажать i можно увидеть свойства загрузчика
там в шрафе search выбирается какой диск монтируется
графа floppy это уже то какое ядро загрузится
initrd образ ram диска которое находится в памяти
если прямо тут редактировать то это будет параметры на одну загрузку
ro точно чтение quet показывает всю красоту загрузки  splash показфывет только краивую картинку

после загрузки 
dmesg команда обо всех сообщениях ядра, нужно понимать разницу между dmesg и логом dmesg . в логе dmesg харнится толкьо лог загрузки, далее там информации по работе ядра уже нет
pstree команда показывает все процессы в системе

в паке /boot лежат сами ядра, образы initram дисков, в папке /boot/grub сам загрузчик  grub.cfg основной файл в котором все параметры для згрузки
initrd стандартный диск рам в котром есть куча всего что нужно ядру для корректной загрузки

/etc/init.d папка сс скриптами инициализации , они все тут, тут куча скриптов, которые запускают прееленные службы (демоны)
остановить службу можно тоже скриптами из этой папки  ./network stop  
тоже самое service network start

/etc/rc3.d тут тоже куча скриптов, начинающиеся с K это KILL т.е. убивают процессы начианется с S т.е стартую процессы
цифра после буквы это в какой  последовательности все это стартует и убивается

Команы которые используются при настройке и и нициализации системы
init   настройка иницилаизации
TelInit  управление init  по сути тоже что и верхнее
Wall вывод сообщения всем пользователям системы
Halt выключение, но потом нужно нажатть еще кнопку
reboot перезагрудка
shutdown умеет все в зависмости от ключей


имя файла это хардлинк, в выводе ll можно увидеть сколько их, файл жив пока живо хоятбы одно имя.
у них общая inode. Права у хардлинков тоже общие.
у / inode №2

stat "Имя файла" показывает расширенную информацию о файле, айноды, когда создан, изменен, и пр.

Софт линки имеют права 777, а вот уже далее читаются права куда он указывает
