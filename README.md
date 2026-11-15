# 🔴 REDSHIFT Launcher

<p align="center">
  <strong>Быстрый и настраиваемый Minecraft: Java Edition на Android</strong><br>
  <sub>Свобода сборок. Контроль производительности. Твой Minecraft — твои правила.</sub>
</p>

<p align="center">
  <a href="https://github.com/bs9973866-png/redshiftmobile/actions/workflows/android.yml"><img src="https://github.com/bs9973866-png/redshiftmobile/actions/workflows/android.yml/badge.svg" alt="Android APK build"></a>
  <img src="https://img.shields.io/github/downloads/bs9973866-png/redshiftmobile/total?label=downloads&color=red" alt="GitHub downloads">
  <img src="https://hits.sh/github.com/bs9973866-png/redshiftmobile.svg?style=flat-square&label=views&color=8b0000" alt="Repository page views">
  <img src="https://img.shields.io/github/stars/bs9973866-png/redshiftmobile?style=flat&label=stars" alt="GitHub stars">
  <img src="https://img.shields.io/github/last-commit/bs9973866-png/redshiftmobile?label=last%20update" alt="Last update">
</p>

<p align="center">
  <a href="https://github.com/bs9973866-png/redshiftmobile/actions">Скачать тестовую сборку</a> ·
  <a href="https://github.com/bs9973866-png/redshiftmobile/issues">Сообщить об ошибке</a> ·
  <a href="https://github.com/bs9973866-png/redshiftmobile/releases">Релизы</a>
</p>

---

## ✨ О проекте

**REDSHIFT Launcher** — независимый Android-лаунчер для Minecraft: Java Edition. Цель проекта — объединить удобное управление аккаунтами, скинами, версиями, модами и настройками производительности в одном мобильном приложении.

Проект находится в разработке. Текущая техническая основа — Android Java launcher на базе проекта [minelauncher](https://github.com/BoreKKst/minelauncher), который использует наработки Amethyst/PojavLauncher. Сторонние лицензии, уведомления об авторстве и обязательные файлы лицензий должны сохраняться.

## 📊 Статистика репозитория

| Показатель | Что показывает |
|---|---|
| **Просмотры** | Счётчик посещений README/страницы репозитория через внешний badge-сервис Hits. Это не официальная статистика GitHub Traffic и может учитывать повторные открытия. |
| **Скачивания** | Суммарные загрузки файлов из опубликованных GitHub Releases. Загрузки Actions Artifacts сюда не входят. |
| **Звёзды** | Количество GitHub Stars. |
| **Сборка** | Текущий статус последнего workflow Android APK. |

> Счётчики обновляются внешними сервисами с задержкой. Для точных просмотров GitHub используй **Insights → Traffic** (доступ зависит от прав на репозиторий).

## 🚀 Возможности и план разработки

### Аккаунты и скины
- [ ] Ely.by: авторизация и получение скинов.
- [ ] Microsoft: официальный вход для владельцев Minecraft: Java Edition.
- [ ] Offline: локальный профиль с ником.
- [ ] Управление скином из лаунчера и 3D-предпросмотр.
- [ ] Поддержка Classic/Slim и PNG-скинов.

### Сборки и контент
- [ ] Создание отдельных игровых профилей.
- [ ] Выбор версии Minecraft и загрузчика модов.
- [ ] Установка модов из Modrinth и CurseForge.
- [ ] Установка ресурспаков и шейдеров из каталогов.
- [ ] Проверка совместимости версий и загрузчиков перед установкой.

### Производительность
- [ ] Автоматический подбор совместимых оптимизационных модов при создании сборки.
- [ ] Профили настроек для слабых, средних и мощных устройств.
- [ ] Управление выделением RAM и графическими параметрами.
- [ ] Настройки дальности прорисовки, частиц и эффектов.
- [ ] Возможность отключить тяжёлые эффекты ради стабильного FPS.

### Интерфейс
- [ ] Фирменная тёмная тема REDSHIFT с красными неоновыми акцентами.
- [ ] Адаптация интерфейса под телефоны и планшеты.
- [ ] Экран загрузок с прогрессом, скоростью и понятными ошибками.

Отмеченные пункты — план работ, а не заявление о готовности функций. Галочки будут ставиться после реализации и проверки.

## 📦 Как получить APK

1. Открой [GitHub Actions](https://github.com/bs9973866-png/redshiftmobile/actions).
2. Выбери **REDSHIFT Android APK**.
3. Открой последний успешный запуск со статусом зелёной галочки.
4. Внизу страницы скачай artifact **redshift-debug-apk**.
5. Распакуй ZIP и установи APK на Android.

Если workflow ещё выполняется, дождись завершения. Если он завершился ошибкой, открой run и посмотри лог шага **Build APK**.

**Важно:** Actions Artifacts временные и не увеличивают счётчик GitHub Releases downloads. Для публичного постоянного APK потребуется отдельный GitHub Release.

## 🛠️ Сборка из исходников

Сборка выполняется GitHub Actions на Ubuntu. Workflow получает исходники лаунчера с submodules, применяет REDSHIFT branding и запускает Gradle task:

```bash
./gradlew :app_pojavlauncher:assembleDebug --no-daemon
```

Готовый APK публикуется как artifact `redshift-debug-apk`. Для локальной сборки потребуются JDK и Android SDK, совместимые с upstream-проектом.

## 🔐 Безопасность и аккаунты

- Не отправляй пароли, коды 2FA, access tokens и файлы ключей в Issues или Pull Requests.
- Используй только собственные аккаунты.
- Microsoft-вход предназначен для пользователей, у которых есть лицензия Minecraft: Java Edition.
- Offline-профиль не предоставляет доступ к серверам, требующим лицензионную авторизацию.

## ⚖️ Правовой статус и благодарности

REDSHIFT Launcher — независимый проект, не связанный с Mojang Studios, Microsoft или Ely.by. Minecraft является товарным знаком соответствующих правообладателей.

Техническая основа и её компоненты распространяются по собственным лицензиям. Перед распространением производной сборки необходимо сохранять upstream LICENSE/NOTICE, соблюдать условия используемых библиотек и не удалять атрибуцию авторов.

---

<p align="center">
  <sub>REDSHIFT Launcher · Android · Minecraft Java Edition</sub>
</p>
