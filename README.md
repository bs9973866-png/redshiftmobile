# REDSHIFT Launcher (Android)

**REDSHIFT Launcher** — независимый лаунчер Minecraft: Java Edition для Android. Проект собирается в APK через GitHub Actions, поэтому разработка и получение сборки не требуют ПК со стороны пользователя.

## Основа

Первый этап использует Android Java-launcher codebase с поддержкой Ely.by, Microsoft и offline-профилей, Ely.by skins, Java runtimes и Android native rendering. Базовый upstream и его лицензии/авторства сохраняются; REDSHIFT — отдельный бренд, не официальный продукт Mojang/Microsoft/Ely.by.

## План REDSHIFT

- [x] Создать репозиторий и автоматическую Android APK-сборку.
- [ ] Полный REDSHIFT UI: тёмная графитовая тема, красный неон, адаптация под телефон.
- [ ] Проверить Ely.by / Microsoft / offline login на реальном Android-устройстве.
- [ ] Удобное управление скинами и предпросмотр.
- [ ] Профили/сборки, подбор совместимых оптимизационных модов.
- [ ] Каталог Modrinth и CurseForge: моды, ресурспаки, шейдеры.
- [ ] Пресеты производительности для слабых устройств с настройками под конкретный телефон.

## Получение APK

Открой вкладку **Actions**, выбери workflow **REDSHIFT Android APK** и запусти **Run workflow**. После успешного завершения APK будет прикреплён к run как artifact `redshift-debug-apk`.

> Сейчас это bootstrap-сборка на базе upstream. Она не означает, что все пункты плана уже реализованы или протестированы. Microsoft-вход требует действительного аккаунта с Minecraft: Java Edition. Не публикуй пароли, токены или ключи подписи в репозитории.

## Сборка

Workflow клонирует исходный Android launcher с submodules, применяет только брендирование REDSHIFT и запускает Gradle. APK не содержит игровые файлы Minecraft: они загружаются лаунчером на устройстве по запросу пользователя.

## Лицензии и благодарности

См. upstream LICENSE и NOTICE-файлы в исходном проекте, которые должны оставаться в производных сборках. REDSHIFT не связан с Mojang Studios, Microsoft или Ely.by.
