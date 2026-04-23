# Лабораторная работа: GitHub + Travis CI + SonarCloud

Проект подготовлен на Java 17 и Maven с автоматическим запуском:
- сборки и тестов;
- отчета покрытия JaCoCo;
- анализа SonarCloud через SonarScanner for Maven.

## Что уже настроено в проекте

- `.travis.yml` для Travis CI;
- `pom.xml` с Java 17, JUnit 5, JaCoCo и SonarScanner;
- пример исходного кода и тестов.

## Шаги выполнения задания

### 1.1 Подготовка репозитория GitHub

1. Создайте новый репозиторий на GitHub.
2. Выполните в локальной папке:

```bash
git init
git add .
git commit -m "Initial commit: Java 17 + Travis + SonarCloud"
git branch -M main
git remote add origin <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
git push -u origin main
```

### 1.2 Настройка проекта в SonarCloud

1. Войдите в SonarCloud через GitHub.
2. Создайте проект из репозитория.
3. Сгенерируйте токен доступа и сохраните значения:
- `SONAR_TOKEN`
- `SONAR_ORGANIZATION`
- `SONAR_PROJECT_KEY`

### 1.3 Подключение репозитория в Travis CI и переменные окружения

1. Активируйте репозиторий в Travis CI.
2. В настройках репозитория добавьте переменные:
- `SONAR_TOKEN`
- `SONAR_ORGANIZATION`
- `SONAR_PROJECT_KEY`

### 1.4 Конфигурационные файлы и исходный код проекта

Проект использует:
- Java 17;
- Maven;
- JaCoCo для покрытия;
- SonarScanner for Maven для анализа.

Файл конфигурации Travis CI: `.travis.yml`.

### 1.5 Результаты выполнения сборки и анализа

После коммита в GitHub Travis CI:
1. выполняет `mvn clean verify` (сборка + тесты + отчет JaCoCo);
2. запускает `mvn sonar:sonar` для SonarCloud.

Результаты качества, ошибки и покрытие тестами отображаются в интерфейсе SonarCloud.

