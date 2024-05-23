# PyStructure

`PyStructure` - это инструмент для отображения структуры каталогов проекта на Python или любой другой структуры папок. 

Он позволяет фильтровать отображаемые файлы и директории на основе списка игнорируемых директорий или файла `.gitignore`.

## Установка

1. **Склонируйте репозиторий или загрузите проект:**

    ```sh
    git clone https://github.com/ваш_репозиторий/PyStructure.git
    cd PyStructure
    ```

2. **Убедитесь, что у вас установлен Python 3.6 или выше.**

## Использование

### Запуск из командной строки

Вы можете запустить `PyStructure` из командной строки, указав корневой каталог вашего проекта и опциональные параметры:

### Параметры

- `root_dir` (обязательный): Корневой каталог проекта, для которого нужно отобразить структуру.
- `--ignore FILES [FILES ...]` (опциональный): Список файлов или директорий, которые нужно игнорировать при отображении структуры.
- `--use-gitignore` (опциональный): Флаг, указывающий на использование файла `.gitignore` для определения игнорируемых директорий и файлов.

### Примеры использования

1. **Отобразить структуру каталога без дополнительных фильтров:**

    ```sh
    python main.py /path/to/project
    ```

    Вывод:
    ```
    Structure of '/path/to/project': 
    ├── .gitignore
    ├── .idea
    │   ├── .gitignore
    │   ├── PyStructure.iml
    │   ├── inspectionProfiles
    │   │   ├── Project_Default.xml
    │   │   └── profiles_settings.xml
    │   ├── misc.xml
    │   ├── modules.xml
    │   └── workspace.xml
    ├── README.MD
    └── main.py
    ```

2. **Игнорировать определённые файлы или директории:**

    ```sh
    python main.py /path/to/project --ignore .idea
    ```

    Вывод:
    ```
    Structure of '/path/to/project': 
    ├── .gitignore
    ├── README.MD
    └── main.py
    ```

3. **Использовать правила из файла `.gitignore`:**

    Пример содержимого `.gitignore`:
    ```
    .idea/
    ```

    Команда:
    ```sh
    python main.py /path/to/project --use-gitignore
    ```

    Вывод:
    ```
    Structure of '/path/to/project': 
    ├── README.MD
    └── main.py
    ```

### Использование в вашем коде

Вы также можете использовать `PyStructure` в своем коде. Для этого импортируйте необходимые классы и функции и создайте экземпляр `PyStructure`:

```python
from main import PyStructure, assert_path

# Убедитесь, что путь существует
project_path = "/path/to/project"
assert_path(project_path)

# Создайте экземпляр PyStructure
project = PyStructure(root_dir=project_path, ignores=['.idea', '.gitignore'], use_gitignore=True)

# Отобразите структуру проекта
project.show_structure()
```

Этот код проверяет существование пути, создает экземпляр `PyStructure` с указанными параметрами и выводит структуру проекта.
