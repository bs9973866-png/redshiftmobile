from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("app_pojavlauncher/src/main")
RES = ROOT / "res"

def replace_text(path, replacements):
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

# Keep the existing authentication, Java runtime, profile, loader and mod APIs.
# This patch changes presentation and localization without replacing their logic.
replace_text(RES / "values/strings.xml", {
    '<string name="app_name" translatable="false">minelauncher</string>':
        '<string name="app_name" translatable="false">REDSHIFT</string>',
    'minelauncher has unexpectedly crashed': 'REDSHIFT has unexpectedly crashed',
})

replace_text(RES / "values/colors.xml", {
    "#181818": "#10090D",
    "#464646": "#39202A",
    "#242424": "#1B0D14",
    "#232323": "#170B11",
    "#9649b8": "#FF334F",
    "#4CC4C4C4": "#66FF334F",
})

styles = RES / "values/styles.xml"
replace_text(styles, {
    '<item name="android:windowContentOverlay">@null</item>':
        '<item name="android:windowContentOverlay">@null</item>\n'
        '        <item name="android:windowLightStatusBar">false</item>',
})

# REDSHIFT brand mark: vector asset, scales cleanly on every Android density.
(RES / "drawable/ic_redshift_mark.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="64dp" android:height="64dp" android:viewportWidth="64" android:viewportHeight="64">
    <path android:fillColor="#FF334F" android:pathData="M32,2 C15.4,2 2,15.4 2,32 C2,48.6 15.4,62 32,62 C48.6,62 62,48.6 62,32 C62,15.4 48.6,2 32,2 Z"/>
    <path android:fillColor="#16090E" android:pathData="M18,14 L43,14 C51,14 55,18 55,25 C55,31 52,35 46,37 L55,50 L42,50 L33,37 L29,37 L29,50 L18,50 Z M29,24 L29,29 L42,29 C44,29 45,28 45,26.5 C45,25 44,24 42,24 Z"/>
</vector>
""", encoding="utf-8")

(RES / "drawable/bg_redshift_hero.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="18dp"/>
    <gradient android:angle="0" android:startColor="#281018" android:centerColor="#1B0D14" android:endColor="#130A12"/>
    <stroke android:width="1dp" android:color="#66FF334F"/>
</shape>
""", encoding="utf-8")

# A compact branded dashboard header, inserted without changing existing controls.
layout = RES / "layout/fragment_launcher.xml"
xml = layout.read_text(encoding="utf-8")
anchor = '<com.kdt.mcgui.LauncherMenuButton\n\t\t\t\tandroid:id="@+id/custom_control_button"'
if anchor in xml and 'redshift_hero' not in xml:
    hero = """<LinearLayout
                android:id="@+id/redshift_hero"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginStart="16dp"
                android:layout_marginTop="14dp"
                android:layout_marginEnd="16dp"
                android:layout_marginBottom="10dp"
                android:background="@drawable/bg_redshift_hero"
                android:gravity="center_vertical"
                android:minHeight="104dp"
                android:orientation="horizontal"
                android:padding="16dp"
                app:layout_constraintTop_toTopOf="parent">
                <ImageView
                    android:layout_width="54dp"
                    android:layout_height="54dp"
                    android:contentDescription="REDSHIFT"
                    android:src="@drawable/ic_redshift_mark" />
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_marginStart="14dp"
                    android:layout_weight="1"
                    android:orientation="vertical">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="REDSHIFT"
                        android:textColor="#FFFFF5F7"
                        android:textSize="22sp"
                        android:textStyle="bold"
                        android:letterSpacing="0.08" />
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="4dp"
                        android:text="MINECRAFT JAVA EDITION"
                        android:textColor="#FFFF7185"
                        android:textSize="10sp"
                        android:letterSpacing="0.12" />
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="5dp"
                        android:text="Твой мир. Твои правила."
                        android:textColor="#FFBDAAB0"
                        android:textSize="12sp" />
                </LinearLayout>
            </LinearLayout>
            """
    xml = xml.replace(anchor, hero + anchor)
    xml = xml.replace('app:layout_constraintTop_toTopOf="parent" />',
                      'app:layout_constraintTop_toBottomOf="@id/redshift_hero" />', 1)
    layout.write_text(xml, encoding="utf-8")

# Russian labels for the primary launcher and authentication surfaces.
ru = RES / "values-ru"
ru.mkdir(parents=True, exist_ok=True)
(ru / "strings.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">REDSHIFT</string>
    <string name="app_short_name">REDSHIFT</string>
    <string name="main_play">ИГРАТЬ</string>
    <string name="mcl_option_customcontrol">Управление</string>
    <string name="main_install_jar_file">Установить JAR-файл</string>
    <string name="main_share_logs">Поделиться логами</string>
    <string name="mcl_button_open_directory">Открыть папку игры</string>
    <string name="login_elyby_account">Аккаунт Ely.by</string>
    <string name="login_elyby_username_hint">Логин или почта Ely.by</string>
    <string name="login_elyby_password_hint">Пароль</string>
    <string name="login_elyby_totp_hint">Код 2FA (необязательно)</string>
    <string name="login_elyby_register">Создать аккаунт Ely.by</string>
    <string name="login_microsoft">Войти через Microsoft</string>
    <string name="login_online_login_label">Войти</string>
    <string name="login_online_username_hint">Имя пользователя</string>
    <string name="global_save">Сохранить</string>
    <string name="global_cancel">Отмена</string>
    <string name="global_retry">Повторить</string>
    <string name="global_error">Ошибка</string>
    <string name="mcl_setting_title_javaargs">Аргументы JVM</string>
    <string name="mcl_setting_title_resolution_scaler">Масштаб разрешения</string>
    <string name="mcl_setting_title_renderer_settings">Настройки рендерера</string>
    <string name="mcl_setting_category_renderer">Рендерер</string>
    <string name="mcl_setting_renderer_gles2_4">GL4ES — быстрый режим</string>
    <string name="mcl_setting_renderer_vulkan_zink">Zink (Vulkan)</string>
    <string name="mcl_setting_renderer_mobileglues">MobileGlues (OpenGL ES)</string>
    <string name="mcl_setting_veroption_release">Релизы</string>
    <string name="mcl_setting_veroption_snapshot">Снапшоты</string>
    <string name="mcl_setting_veroption_oldalpha">Старые Alpha</string>
    <string name="mcl_setting_veroption_oldbeta">Старые Beta</string>
</resources>
""", encoding="utf-8")


# Adaptive launcher icon for Android 8+ (the manifest already references these names).
adaptive = RES / "mipmap-anydpi-v26"
adaptive.mkdir(parents=True, exist_ok=True)
foreground = RES / "drawable/ic_redshift_launcher_foreground.xml"
foreground.write_text("""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FF334F"
        android:pathData="M54,8 C28.6,8 8,28.6 8,54 C8,79.4 28.6,100 54,100 C79.4,100 100,79.4 100,54 C100,28.6 79.4,8 54,8 Z"/>
    <path android:fillColor="#16090E"
        android:pathData="M31,30 L67,30 C78,30 84,36 84,47 C84,55 80,61 71,64 L85,82 L67,82 L54,65 L48,65 L48,82 L31,82 Z M48,44 L48,52 L66,52 C69,52 71,51 71,48 C71,45 69,44 66,44 Z"/>
</vector>
""", encoding="utf-8")
icon_xml = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/redshift_icon_background"/>
    <foreground android:drawable="@drawable/ic_redshift_launcher_foreground"/>
</adaptive-icon>
"""
(adaptive / "ic_launcher.xml").write_text(icon_xml, encoding="utf-8")
(adaptive / "ic_launcher_round.xml").write_text(icon_xml, encoding="utf-8")
(RES / "values/redshift_icon.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<resources><color name="redshift_icon_background">#10090D</color></resources>
""", encoding="utf-8")

# Apply the same compact brand header to the landscape launcher layout.
land_layout = RES / "layout-land/fragment_launcher.xml"
if land_layout.exists():
    land_xml = land_layout.read_text(encoding="utf-8")
    land_anchor = '<com.kdt.mcgui.LauncherMenuButton'
    if 'redshift_hero' not in land_xml and land_anchor in land_xml:
        first_button = land_xml.find(land_anchor)
        # Keep the banner inside the existing scroll content, before its first menu item.
        hero_land = """<LinearLayout
                android:id="@+id/redshift_hero"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_margin="10dp"
                android:background="@drawable/bg_redshift_hero"
                android:gravity="center_vertical"
                android:minHeight="78dp"
                android:orientation="horizontal"
                android:padding="12dp">
                <ImageView
                    android:layout_width="44dp"
                    android:layout_height="44dp"
                    android:contentDescription="REDSHIFT"
                    android:src="@drawable/ic_redshift_mark" />
                <LinearLayout
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginStart="12dp"
                    android:orientation="vertical">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="REDSHIFT"
                        android:textColor="#FFFFF5F7"
                        android:textSize="20sp"
                        android:textStyle="bold" />
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="MINECRAFT JAVA EDITION"
                        android:textColor="#FFFF7185"
                        android:textSize="10sp" />
                </LinearLayout>
            </LinearLayout>
            """
        land_xml = land_xml[:first_button] + hero_land + land_xml[first_button:]
        land_xml = land_xml.replace('app:layout_constraintTop_toTopOf="parent"/>',
                                    'app:layout_constraintTop_toBottomOf="@id/redshift_hero"/>', 1)
        land_xml = land_xml.replace('app:layout_constraintTop_toTopOf="parent" />',
                                    'app:layout_constraintTop_toBottomOf="@id/redshift_hero" />', 1)
        land_layout.write_text(land_xml, encoding="utf-8")



# Replace the inherited flat menu rows with a compact, card-based REDSHIFT dashboard.
(RES / "drawable/bg_redshift_action.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#33FF4964">
    <item>
        <shape android:shape="rectangle">
            <corners android:radius="15dp"/>
            <solid android:color="#1B1018"/>
            <stroke android:width="1dp" android:color="#38212D"/>
        </shape>
    </item>
</ripple>
""", encoding="utf-8")
(RES / "drawable/bg_redshift_play.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#55FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <corners android:radius="18dp"/>
            <gradient android:angle="0" android:startColor="#FF526B" android:endColor="#D91E43"/>
            <stroke android:width="1dp" android:color="#FFFF8797"/>
        </shape>
    </item>
</ripple>
""", encoding="utf-8")
(RES / "drawable/bg_redshift_surface.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="18dp"/>
    <solid android:color="#160D14"/>
    <stroke android:width="1dp" android:color="#38212D"/>
</shape>
""", encoding="utf-8")

# Turn the stock button stack into spaced action cards, without changing IDs/listeners.
menu_style = RES / "values/styles.xml"
style_text = menu_style.read_text(encoding="utf-8")
style_text = style_text.replace(
    '<style name="LauncherMenuButton.Universal" parent="LauncherMenuButton">\n'
    '        <item name="android:layout_height">@dimen/_66sdp</item>\n'
    '    </style>',
    '<style name="LauncherMenuButton.Universal" parent="LauncherMenuButton">\n'
    '        <item name="android:layout_height">58dp</item>\n'
    '        <item name="android:layout_marginStart">14dp</item>\n'
    '        <item name="android:layout_marginEnd">14dp</item>\n'
    '        <item name="android:layout_marginTop">7dp</item>\n'
    '        <item name="android:layout_marginBottom">7dp</item>\n'
    '        <item name="android:background">@drawable/bg_redshift_action</item>\n'
    '        <item name="android:textColor">#FFF5F7</item>\n'
    '        <item name="android:textAllCaps">false</item>\n'
    '        <item name="android:textSize">14sp</item>\n'
    '        <item name="android:paddingStart">18dp</item>\n'
    '        <item name="android:paddingEnd">16dp</item>\n'
    '        <item name="android:drawableTint">#FFFF7185</item>\n'
    '        <item name="android:elevation">2dp</item>\n'
    '    </style>'
)
menu_style.write_text(style_text, encoding="utf-8")

# Improve vertical dashboard spacing and give the version selector a clear surface.
portrait = RES / "layout/fragment_launcher.xml"
p = portrait.read_text(encoding="utf-8")
p = p.replace('<ScrollView\n\t\tandroid:layout_width="match_parent"', '<ScrollView\n\t\tandroid:clipToPadding="false"\n\t\tandroid:fillViewport="false"\n\t\tandroid:layout_width="match_parent"')
p = p.replace('android:layout_height="wrap_content">\n\t\t\t<com.kdt.mcgui.LauncherMenuButton',
              'android:layout_height="wrap_content"\n            android:paddingTop="8dp"\n            android:paddingBottom="10dp">\n\t\t\t<com.kdt.mcgui.LauncherMenuButton', 1)
p = p.replace('android:background="@android:color/transparent"\n\t\tandroid:drawableEnd="@drawable/spinner_arrow"',
              'android:background="@drawable/bg_redshift_surface"\n        android:paddingStart="12dp"\n        android:paddingEnd="12dp"\n        android:drawableEnd="@drawable/spinner_arrow"')
p = p.replace('android:layout_marginHorizontal="@dimen/_17sdp"\n\t\tandroid:layout_marginBottom="@dimen/_15sdp"',
              'android:layout_marginHorizontal="16dp"\n        android:layout_marginBottom="14dp"\n        android:background="@drawable/bg_redshift_play"\n        android:textColor="#FFFFFFFF"\n        android:textSize="17sp"\n        android:textStyle="bold"\n        android:elevation="5dp"')
portrait.write_text(p, encoding="utf-8")

# Landscape dashboard gets the same action-card language and a more deliberate bottom dock.
land = RES / "layout-land/fragment_launcher.xml"
if land.exists():
    x = land.read_text(encoding="utf-8")
    x = x.replace('android:background="@android:color/transparent"\n        android:drawableEnd="@drawable/spinner_arrow"',
                  'android:background="@drawable/bg_redshift_surface"\n        android:paddingStart="10dp"\n        android:paddingEnd="10dp"\n        android:drawableEnd="@drawable/spinner_arrow"')
    x = x.replace('android:textAllCaps="true"\n        app:layout_constraintBottom_toBottomOf="@+id/mc_version_spinner"',
                  'android:textAllCaps="true"\n        android:background="@drawable/bg_redshift_play"\n        android:textColor="#FFFFFFFF"\n        android:textStyle="bold"\n        android:elevation="4dp"\n        app:layout_constraintBottom_toBottomOf="@+id/mc_version_spinner"')
    land.write_text(x, encoding="utf-8")

# Restyle the account selector and settings control so the app chrome no longer resembles Pojav.
activity = RES / "layout/activity_pojav_launcher.xml"
a = activity.read_text(encoding="utf-8")
a = a.replace('android:layout_height="@dimen/_52sdp"\n\n        android:dropDownWidth',
              'android:layout_height="@dimen/_48sdp"\n        android:layout_marginStart="14dp"\n        android:layout_marginTop="10dp"\n        android:layout_marginEnd="68dp"\n        android:background="@drawable/bg_redshift_surface"\n        android:paddingStart="12dp"\n        android:paddingEnd="12dp"\n\n        android:dropDownWidth')
a = a.replace('android:layout_width="@dimen/_52sdp"\n        android:layout_height="@dimen/_52sdp"\n        android:background="?attr/selectableItemBackground"',
              'android:layout_width="48dp"\n        android:layout_height="48dp"\n        android:layout_marginTop="10dp"\n        android:layout_marginEnd="14dp"\n        android:background="@drawable/bg_redshift_action"')
a = a.replace('android:paddingVertical="@dimen/_8sdp"\n\n        app:layout_constraintEnd', 'android:padding="12dp"\n        android:tint="#FFFF7185"\n\n        app:layout_constraintEnd')
a = a.replace('app:layout_constraintTop_toBottomOf="@+id/account_spinner" />',
              'app:layout_constraintTop_toBottomOf="@+id/account_spinner"\n        android:layout_marginTop="8dp" />')
activity.write_text(a, encoding="utf-8")

print("REDSHIFT custom dashboard cards, account bar, adaptive icon and branding applied.")


# === REDSHIFT 2.0: rebuild the screen hierarchy, not just its colors ===
# The original Pojav-style menu list is replaced by a launcher dashboard.
# Keep the view IDs consumed by MainMenuFragment so existing actions still work.

portrait_layout = r"""<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/fragment_menu_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background_app">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:clipToPadding="false"
        android:fillViewport="true"
        android:overScrollMode="never">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingStart="20dp"
            android:paddingTop="18dp"
            android:paddingEnd="20dp"
            android:paddingBottom="24dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="REDSHIFT  /  GAME CENTER"
                android:textColor="#FFFF637C"
                android:textSize="11sp"
                android:textStyle="bold"
                android:letterSpacing="0.16" />

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:text="Твой мир.\nТвой следующий шаг."
                android:textColor="#FFFFF5F7"
                android:textSize="30sp"
                android:lineSpacingExtra="1dp"
                android:fontFamily="sans"
                android:textStyle="bold" />

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="8dp"
                android:text="Управляй сборками и запускай Minecraft в один тап."
                android:textColor="#FFB9AAB0"
                android:textSize="13sp" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="22dp"
                android:background="@drawable/bg_redshift_hero"
                android:orientation="vertical"
                android:padding="18dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">

                    <TextView
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:text="LAUNCH CONTROL"
                        android:textColor="#FFFF7185"
                        android:textSize="10sp"
                        android:textStyle="bold"
                        android:letterSpacing="0.15" />

                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:background="@drawable/bg_redshift_action"
                        android:paddingStart="10dp"
                        android:paddingTop="5dp"
                        android:paddingEnd="10dp"
                        android:paddingBottom="5dp"
                        android:text="READY"
                        android:textColor="#FFFFB8C2"
                        android:textSize="9sp"
                        android:textStyle="bold"
                        android:letterSpacing="0.1" />
                </LinearLayout>

                <TextView
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="18dp"
                    android:text="ВЫБРАННАЯ СБОРКА"
                    android:textColor="#FFB9AAB0"
                    android:textSize="10sp"
                    android:textStyle="bold"
                    android:letterSpacing="0.12" />

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="8dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">

                    <com.kdt.mcgui.mcVersionSpinner
                        android:id="@+id/mc_version_spinner"
                        android:layout_width="0dp"
                        android:layout_height="54dp"
                        android:layout_weight="1"
                        android:background="@drawable/bg_redshift_surface"
                        android:paddingStart="12dp"
                        android:paddingEnd="10dp"
                        android:drawableEnd="@drawable/spinner_arrow"
                        app:drawableEndPadding="6dp"
                        app:drawableEndSize="16dp"
                        app:drawableStartIntegerScaling="true"
                        app:drawableStartSize="34dp" />

                    <ImageButton
                        android:id="@+id/edit_profile_button"
                        android:layout_width="54dp"
                        android:layout_height="54dp"
                        android:layout_marginStart="8dp"
                        android:background="@drawable/bg_redshift_action"
                        android:contentDescription="Настроить сборку"
                        android:padding="14dp"
                        android:scaleType="fitCenter"
                        android:src="@drawable/ic_edit_profile"
                        android:tint="#FFFF7185" />
                </LinearLayout>

                <TextView
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="10dp"
                    android:text="Версия, профиль и параметры запуска — здесь."
                    android:textColor="#FFB9AAB0"
                    android:textSize="11sp" />

                <com.kdt.mcgui.MineButton
                    android:id="@+id/play_button"
                    android:layout_width="match_parent"
                    android:layout_height="64dp"
                    android:layout_marginTop="18dp"
                    android:background="@drawable/bg_redshift_play"
                    android:elevation="4dp"
                    android:text="@string/main_play"
                    android:textAllCaps="true"
                    android:textColor="#FFFFFFFF"
                    android:textSize="17sp"
                    android:textStyle="bold" />
            </LinearLayout>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="26dp"
                android:text="БЫСТРЫЕ ДЕЙСТВИЯ"
                android:textColor="#FFFFF5F7"
                android:textSize="12sp"
                android:textStyle="bold"
                android:letterSpacing="0.12" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="12dp"
                android:orientation="horizontal">

                <com.kdt.mcgui.LauncherMenuButton
                    android:id="@+id/custom_control_button"
                    style="@style/LauncherMenuButton.Universal"
                    android:layout_width="0dp"
                    android:layout_height="82dp"
                    android:layout_weight="1"
                    android:layout_margin="5dp"
                    android:background="@drawable/bg_redshift_action"
                    android:drawableStart="@drawable/ic_menu_custom_controls"
                    android:drawableTint="#FFFF7185"
                    android:gravity="center_vertical"
                    android:paddingStart="12dp"
                    android:text="@string/mcl_option_customcontrol"
                    android:textAllCaps="false"
                    android:textColor="#FFFFF5F7"
                    android:textSize="12sp" />

                <com.kdt.mcgui.LauncherMenuButton
                    android:id="@+id/install_jar_button"
                    style="@style/LauncherMenuButton.Universal"
                    android:layout_width="0dp"
                    android:layout_height="82dp"
                    android:layout_weight="1"
                    android:layout_margin="5dp"
                    android:background="@drawable/bg_redshift_action"
                    android:drawableStart="@drawable/ic_menu_install_jar"
                    android:drawableTint="#FFFF7185"
                    android:gravity="center_vertical"
                    android:paddingStart="12dp"
                    android:text="@string/main_install_jar_file"
                    android:textAllCaps="false"
                    android:textColor="#FFFFF5F7"
                    android:textSize="12sp" />
            </LinearLayout>

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="horizontal">

                <com.kdt.mcgui.LauncherMenuButton
                    android:id="@+id/language_button"
                    style="@style/LauncherMenuButton.Universal"
                    android:layout_width="0dp"
                    android:layout_height="82dp"
                    android:layout_weight="1"
                    android:layout_margin="5dp"
                    android:background="@drawable/bg_redshift_action"
                    android:drawableStart="@drawable/ic_language"
                    android:drawableTint="#FFFF7185"
                    android:gravity="center_vertical"
                    android:paddingStart="12dp"
                    android:text="@string/force_minecraft_language"
                    android:textAllCaps="false"
                    android:textColor="#FFFFF5F7"
                    android:textSize="12sp" />

                <com.kdt.mcgui.LauncherMenuButton
                    android:id="@+id/open_files_button"
                    style="@style/LauncherMenuButton.Universal"
                    android:layout_width="0dp"
                    android:layout_height="82dp"
                    android:layout_weight="1"
                    android:layout_margin="5dp"
                    android:background="@drawable/bg_redshift_action"
                    android:drawableStart="@drawable/ic_folder"
                    android:drawableTint="#FFFF7185"
                    android:gravity="center_vertical"
                    android:paddingStart="12dp"
                    android:text="@string/mcl_button_open_directory"
                    android:textAllCaps="false"
                    android:textColor="#FFFFF5F7"
                    android:textSize="12sp" />
            </LinearLayout>

            <com.kdt.mcgui.LauncherMenuButton
                android:id="@+id/share_logs_button"
                style="@style/LauncherMenuButton.Universal"
                android:layout_width="match_parent"
                android:layout_height="62dp"
                android:layout_margin="5dp"
                android:background="@drawable/bg_redshift_action"
                android:drawableStart="@android:drawable/ic_menu_share"
                android:drawableTint="#FFFF7185"
                android:gravity="center_vertical"
                android:paddingStart="16dp"
                android:text="@string/main_share_logs"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="13sp" />
        </LinearLayout>
    </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
"""

landscape_layout = r"""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/fragment_menu_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background_app"
    android:orientation="horizontal"
    android:padding="18dp">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="match_parent"
        android:layout_weight="1.08"
        android:orientation="vertical"
        android:paddingEnd="18dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="REDSHIFT  /  GAME CENTER"
            android:textColor="#FFFF637C"
            android:textSize="10sp"
            android:textStyle="bold"
            android:letterSpacing="0.15" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="9dp"
            android:text="Твой мир.\nТвой следующий шаг."
            android:textColor="#FFFFF5F7"
            android:textSize="26sp"
            android:textStyle="bold" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="7dp"
            android:text="Всё нужное для Minecraft — под рукой."
            android:textColor="#FFB9AAB0"
            android:textSize="12sp" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="24dp"
            android:text="БЫСТРЫЕ ДЕЙСТВИЯ"
            android:textColor="#FFFFF5F7"
            android:textSize="11sp"
            android:textStyle="bold"
            android:letterSpacing="0.12" />

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="8dp"
            android:orientation="horizontal">

            <com.kdt.mcgui.LauncherMenuButton
                android:id="@+id/custom_control_button"
                style="@style/LauncherMenuButton.Universal"
                android:layout_width="0dp"
                android:layout_height="76dp"
                android:layout_weight="1"
                android:layout_margin="4dp"
                android:background="@drawable/bg_redshift_action"
                android:drawableStart="@drawable/ic_menu_custom_controls"
                android:drawableTint="#FFFF7185"
                android:paddingStart="10dp"
                android:text="@string/mcl_option_customcontrol"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="11sp" />

            <com.kdt.mcgui.LauncherMenuButton
                android:id="@+id/install_jar_button"
                style="@style/LauncherMenuButton.Universal"
                android:layout_width="0dp"
                android:layout_height="76dp"
                android:layout_weight="1"
                android:layout_margin="4dp"
                android:background="@drawable/bg_redshift_action"
                android:drawableStart="@drawable/ic_menu_install_jar"
                android:drawableTint="#FFFF7185"
                android:paddingStart="10dp"
                android:text="@string/main_install_jar_file"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="11sp" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal">

            <com.kdt.mcgui.LauncherMenuButton
                android:id="@+id/language_button"
                style="@style/LauncherMenuButton.Universal"
                android:layout_width="0dp"
                android:layout_height="76dp"
                android:layout_weight="1"
                android:layout_margin="4dp"
                android:background="@drawable/bg_redshift_action"
                android:drawableStart="@drawable/ic_language"
                android:drawableTint="#FFFF7185"
                android:paddingStart="10dp"
                android:text="@string/force_minecraft_language"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="11sp" />

            <com.kdt.mcgui.LauncherMenuButton
                android:id="@+id/open_files_button"
                style="@style/LauncherMenuButton.Universal"
                android:layout_width="0dp"
                android:layout_height="76dp"
                android:layout_weight="1"
                android:layout_margin="4dp"
                android:background="@drawable/bg_redshift_action"
                android:drawableStart="@drawable/ic_folder"
                android:drawableTint="#FFFF7185"
                android:paddingStart="10dp"
                android:text="@string/mcl_button_open_directory"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="11sp" />
        </LinearLayout>

        <com.kdt.mcgui.LauncherMenuButton
            android:id="@+id/share_logs_button"
            style="@style/LauncherMenuButton.Universal"
            android:layout_width="match_parent"
            android:layout_height="58dp"
            android:layout_margin="4dp"
            android:background="@drawable/bg_redshift_action"
            android:drawableStart="@android:drawable/ic_menu_share"
            android:drawableTint="#FFFF7185"
            android:paddingStart="12dp"
            android:text="@string/main_share_logs"
            android:textAllCaps="false"
            android:textColor="#FFFFF5F7"
            android:textSize="12sp" />
    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="match_parent"
        android:layout_weight="0.92"
        android:background="@drawable/bg_redshift_hero"
        android:gravity="center_vertical"
        android:orientation="vertical"
        android:padding="20dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="LAUNCH CONTROL"
            android:textColor="#FFFF7185"
            android:textSize="10sp"
            android:textStyle="bold"
            android:letterSpacing="0.15" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="18dp"
            android:text="ВЫБРАННАЯ СБОРКА"
            android:textColor="#FFB9AAB0"
            android:textSize="10sp"
            android:textStyle="bold"
            android:letterSpacing="0.12" />

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="8dp"
            android:gravity="center_vertical"
            android:orientation="horizontal">

            <com.kdt.mcgui.mcVersionSpinner
                android:id="@+id/mc_version_spinner"
                android:layout_width="0dp"
                android:layout_height="52dp"
                android:layout_weight="1"
                android:background="@drawable/bg_redshift_surface"
                android:paddingStart="10dp"
                android:paddingEnd="8dp"
                android:drawableEnd="@drawable/spinner_arrow"
                app:drawableEndPadding="5dp"
                app:drawableEndSize="14dp"
                app:drawableStartIntegerScaling="true"
                app:drawableStartSize="30dp" />

            <ImageButton
                android:id="@+id/edit_profile_button"
                android:layout_width="52dp"
                android:layout_height="52dp"
                android:layout_marginStart="7dp"
                android:background="@drawable/bg_redshift_action"
                android:contentDescription="Настроить сборку"
                android:padding="13dp"
                android:src="@drawable/ic_edit_profile"
                android:tint="#FFFF7185" />
        </LinearLayout>

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="10dp"
            android:text="Выбери профиль, проверь версию и запускай игру."
            android:textColor="#FFB9AAB0"
            android:textSize="11sp" />

        <com.kdt.mcgui.MineButton
            android:id="@+id/play_button"
            android:layout_width="match_parent"
            android:layout_height="66dp"
            android:layout_marginTop="22dp"
            android:background="@drawable/bg_redshift_play"
            android:elevation="4dp"
            android:text="@string/main_play"
            android:textAllCaps="true"
            android:textColor="#FFFFFFFF"
            android:textSize="17sp"
            android:textStyle="bold" />
    </LinearLayout>
</LinearLayout>
"""

activity_layout = r"""<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background_app">

    <LinearLayout
        android:id="@+id/redshift_top_area"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#10090D"
        android:orientation="vertical"
        android:paddingStart="18dp"
        android:paddingTop="10dp"
        android:paddingEnd="18dp"
        android:paddingBottom="12dp"
        app:layout_constraintTop_toTopOf="parent">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="48dp"
            android:gravity="center_vertical"
            android:orientation="horizontal">

            <ImageView
                android:layout_width="38dp"
                android:layout_height="38dp"
                android:contentDescription="REDSHIFT"
                android:src="@drawable/ic_redshift_mark" />

            <LinearLayout
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_marginStart="11dp"
                android:layout_weight="1"
                android:orientation="vertical">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="REDSHIFT"
                    android:textColor="#FFFFF5F7"
                    android:textSize="17sp"
                    android:textStyle="bold"
                    android:letterSpacing="0.12" />

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="MINECRAFT JAVA LAUNCHER"
                    android:textColor="#FFFF7185"
                    android:textSize="8sp"
                    android:letterSpacing="0.13" />
            </LinearLayout>

            <ImageButton
                android:id="@+id/setting_button"
                android:layout_width="44dp"
                android:layout_height="44dp"
                android:background="@drawable/bg_redshift_action"
                android:contentDescription="Настройки"
                android:padding="11dp"
                android:scaleType="fitCenter"
                android:src="@drawable/ic_menu_settings"
                android:tint="#FFFF9BAA" />
        </LinearLayout>

        <com.kdt.mcgui.mcAccountSpinner
            android:id="@+id/account_spinner"
            android:layout_width="match_parent"
            android:layout_height="48dp"
            android:layout_marginTop="10dp"
            android:background="@drawable/bg_redshift_surface"
            android:dropDownWidth="280dp"
            android:dropDownVerticalOffset="48dp"
            android:paddingStart="12dp"
            android:paddingEnd="12dp" />
    </LinearLayout>

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/container_fragment"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        app:layout_constraintTop_toBottomOf="@id/redshift_top_area"
        app:layout_constraintBottom_toTopOf="@id/progress_layout" />

    <com.kdt.mcgui.ProgressLayout
        android:id="@+id/progress_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:layout_constraintBottom_toBottomOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
"""

(RES / "layout/fragment_launcher.xml").write_text(portrait_layout, encoding="utf-8")
(RES / "layout-land/fragment_launcher.xml").write_text(landscape_layout, encoding="utf-8")
(RES / "layout/activity_pojav_launcher.xml").write_text(activity_layout, encoding="utf-8")

print("REDSHIFT 2.0 dashboard hierarchy replaced: new account header, launch control panel, action grid and landscape split layout.")


# === REDSHIFT identity flows: account provider and mod-loader selection ===
# Preserve all IDs so upstream fragment click handlers continue to own navigation.

auth_selector = r"""<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background_app"
    android:fillViewport="true"
    android:overScrollMode="never">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center_horizontal"
        android:orientation="vertical"
        android:paddingStart="22dp"
        android:paddingTop="28dp"
        android:paddingEnd="22dp"
        android:paddingBottom="28dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="REDSHIFT IDENTITY"
            android:textColor="#FFFF637C"
            android:textSize="10sp"
            android:textStyle="bold"
            android:letterSpacing="0.18" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="12dp"
            android:gravity="center"
            android:text="Выбери способ входа"
            android:textColor="#FFFFF5F7"
            android:textSize="25sp"
            android:textStyle="bold" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="7dp"
            android:gravity="center"
            android:text="Подключи аккаунт или продолжи без авторизации."
            android:textColor="#FFB9AAB0"
            android:textSize="13sp" />

        <LinearLayout
            android:id="@+id/login_menu"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="28dp"
            android:background="@drawable/bg_redshift_hero"
            android:orientation="vertical"
            android:padding="14dp">

            <com.kdt.mcgui.MineButton
                android:id="@+id/button_microsoft_authentication"
                android:layout_width="match_parent"
                android:layout_height="64dp"
                android:layout_marginBottom="10dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="18dp"
                android:text="Microsoft Account"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="15sp" />

            <com.kdt.mcgui.MineButton
                android:id="@+id/button_elyby_authentication"
                android:layout_width="match_parent"
                android:layout_height="64dp"
                android:layout_marginBottom="10dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="18dp"
                android:text="@string/login_elyby_account"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="15sp" />

            <com.kdt.mcgui.MineButton
                android:id="@+id/button_local_authentication"
                android:layout_width="match_parent"
                android:layout_height="64dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="18dp"
                android:text="Offline — никнейм"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="15sp" />
        </LinearLayout>

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="14dp"
            android:gravity="center"
            android:text="REDSHIFT • ACCOUNT CENTER"
            android:textColor="#FF76656D"
            android:textSize="9sp"
            android:letterSpacing="0.14" />
    </LinearLayout>
</ScrollView>
"""

modloader_selector = r"""<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background_app"
    android:fillViewport="true"
    android:overScrollMode="never">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:paddingStart="20dp"
        android:paddingTop="24dp"
        android:paddingEnd="20dp"
        android:paddingBottom="24dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="INSTANCE BUILDER"
            android:textColor="#FFFF637C"
            android:textSize="10sp"
            android:textStyle="bold"
            android:letterSpacing="0.16" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="10dp"
            android:text="Выбери загрузчик"
            android:textColor="#FFFFF5F7"
            android:textSize="26sp"
            android:textStyle="bold" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="7dp"
            android:text="Загрузчик определяет совместимость модов и сборки."
            android:textColor="#FFB9AAB0"
            android:textSize="13sp" />

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="22dp"
            android:background="@drawable/bg_redshift_hero"
            android:orientation="vertical"
            android:padding="14dp">

            <com.kdt.mcgui.MineButton
                android:id="@+id/btn_loader_fabric"
                android:layout_width="match_parent"
                android:layout_height="62dp"
                android:layout_marginBottom="9dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="16dp"
                android:text="FABRIC  •  Лёгкий и быстрый"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="14sp" />

            <com.kdt.mcgui.MineButton
                android:id="@+id/btn_loader_forge"
                android:layout_width="match_parent"
                android:layout_height="62dp"
                android:layout_marginBottom="9dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="16dp"
                android:text="FORGE  •  Большая библиотека модов"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="14sp" />

            <com.kdt.mcgui.MineButton
                android:id="@+id/btn_loader_neoforge"
                android:layout_width="match_parent"
                android:layout_height="62dp"
                android:layout_marginBottom="9dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="16dp"
                android:text="NEOFORGE  •  Современные сборки"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="14sp" />

            <com.kdt.mcgui.MineButton
                android:id="@+id/btn_loader_quilt"
                android:layout_width="match_parent"
                android:layout_height="62dp"
                android:background="@drawable/bg_redshift_action"
                android:gravity="center_vertical"
                android:paddingStart="16dp"
                android:text="QUILT  •  Альтернатива Fabric"
                android:textAllCaps="false"
                android:textColor="#FFFFF5F7"
                android:textSize="14sp" />
        </LinearLayout>

        <com.kdt.mcgui.MineButton
            android:id="@+id/btn_loader_back"
            android:layout_width="match_parent"
            android:layout_height="54dp"
            android:layout_marginTop="16dp"
            android:background="@drawable/bg_redshift_surface"
            android:text="@string/modloader_select_back"
            android:textAllCaps="false"
            android:textColor="#FFFF9BAA"
            android:textSize="13sp" />
    </LinearLayout>
</ScrollView>
"""

(RES / "layout/fragment_select_auth_method.xml").write_text(auth_selector, encoding="utf-8")
(RES / "layout/fragment_modloader_select.xml").write_text(modloader_selector, encoding="utf-8")

print("REDSHIFT identity and mod-loader selection screens redesigned with preserved upstream action IDs.")


# === REDSHIFT profile workshop: rebuild profile editor into grouped instance settings ===
profile_editor = r"""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="@color/background_app">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:clipToPadding="false"
        android:fillViewport="false"
        android:overScrollMode="never">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingStart="18dp"
            android:paddingTop="20dp"
            android:paddingEnd="18dp"
            android:paddingBottom="20dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="INSTANCE WORKSHOP"
                android:textColor="#FFFF637C"
                android:textSize="10sp"
                android:textStyle="bold"
                android:letterSpacing="0.17" />

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="8dp"
                android:text="Настройка сборки"
                android:textColor="#FFFFF5F7"
                android:textSize="25sp"
                android:textStyle="bold" />

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="5dp"
                android:text="Профиль, среда запуска и параметры Minecraft в одном месте."
                android:textColor="#FFB9AAB0"
                android:textSize="12sp" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:background="@drawable/bg_redshift_hero"
                android:orientation="vertical"
                android:padding="16dp">

                <ImageView
                    android:id="@+id/vprof_editor_profile_icon"
                    android:layout_width="58dp"
                    android:layout_height="58dp"
                    android:layout_gravity="center_horizontal"
                    android:contentDescription="Иконка профиля"
                    android:src="@drawable/ic_redshift_mark" />

                <TextView
                    android:id="@+id/vprof_editor_profile_name_sub"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="14dp"
                    android:text="@string/profiles_profile_name"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />

                <EditText
                    android:id="@+id/vprof_editor_profile_name"
                    android:layout_width="match_parent"
                    android:layout_height="48dp"
                    android:layout_marginTop="5dp"
                    android:background="@drawable/bg_redshift_surface"
                    android:hint="@string/unnamed"
                    android:inputType="textPersonName"
                    android:paddingHorizontal="13dp"
                    android:textColor="#FFFFF5F7"
                    android:textColorHint="#FF76656D"
                    android:textSize="14sp" />
            </LinearLayout>

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:text="ИГРОВАЯ СБОРКА"
                android:textColor="#FFFF637C"
                android:textSize="10sp"
                android:textStyle="bold"
                android:letterSpacing="0.14" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="9dp"
                android:background="@drawable/bg_redshift_surface"
                android:orientation="vertical"
                android:padding="13dp">

                <TextView
                    android:id="@+id/textView4"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="@string/profiles_profile_version"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="48dp"
                    android:layout_marginTop="4dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">
                    <TextView
                        android:id="@+id/vprof_editor_version_spinner"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:background="@drawable/bg_redshift_hero"
                        android:gravity="center_vertical"
                        android:hint="@string/version_select_hint"
                        android:paddingHorizontal="12dp"
                        android:textColor="#FFFFF5F7"
                        android:textSize="13sp" />
                    <Button
                        android:id="@+id/vprof_editor_version_button"
                        android:layout_width="wrap_content"
                        android:layout_height="match_parent"
                        android:layout_marginStart="8dp"
                        android:text="@string/global_select" />
                </LinearLayout>

                <TextView
                    android:id="@+id/textView7"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="14dp"
                    android:text="@string/default_control"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="48dp"
                    android:layout_marginTop="4dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">
                    <TextView
                        android:id="@+id/vprof_editor_ctrl_spinner"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:background="@drawable/bg_redshift_hero"
                        android:gravity="center_vertical"
                        android:hint="@string/use_global_default"
                        android:paddingHorizontal="12dp"
                        android:textColor="#FFFFF5F7"
                        android:textSize="13sp" />
                    <Button
                        android:id="@+id/vprof_editor_ctrl_button"
                        android:layout_width="wrap_content"
                        android:layout_height="match_parent"
                        android:layout_marginStart="8dp"
                        android:text="@string/global_select" />
                </LinearLayout>

                <TextView
                    android:id="@+id/vprof_editor_beginPathView"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="14dp"
                    android:text="Папка игры"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">
                    <TextView
                        android:id="@+id/vprof_editor_path"
                        android:layout_width="0dp"
                        android:layout_height="48dp"
                        android:layout_weight="1"
                        android:background="@drawable/bg_redshift_hero"
                        android:ellipsize="end"
                        android:gravity="center_vertical"
                        android:hint=".minecraft"
                        android:maxLines="2"
                        android:paddingHorizontal="12dp"
                        android:textColor="#FFFFF5F7"
                        android:textSize="12sp" />
                    <Button
                        android:id="@+id/vprof_editor_path_button"
                        android:layout_width="wrap_content"
                        android:layout_height="48dp"
                        android:layout_marginStart="8dp"
                        android:text="@string/global_select" />
                </LinearLayout>
            </LinearLayout>

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:text="СРЕДА ЗАПУСКА"
                android:textColor="#FFFF637C"
                android:textSize="10sp"
                android:textStyle="bold"
                android:letterSpacing="0.14" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="9dp"
                android:background="@drawable/bg_redshift_surface"
                android:orientation="vertical"
                android:padding="13dp">

                <TextView
                    android:id="@+id/textView2"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="@string/pedit_java_runtime"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />
                <Spinner
                    android:id="@+id/vprof_editor_spinner_runtime"
                    android:layout_width="match_parent"
                    android:layout_height="48dp"
                    android:layout_marginTop="4dp"
                    android:background="@drawable/bg_redshift_hero"
                    android:paddingHorizontal="10dp" />

                <TextView
                    android:id="@+id/textView3"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="14dp"
                    android:text="@string/pedit_renderer"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />
                <Spinner
                    android:id="@+id/vprof_editor_profile_renderer"
                    android:layout_width="match_parent"
                    android:layout_height="48dp"
                    android:layout_marginTop="4dp"
                    android:background="@drawable/bg_redshift_hero"
                    android:paddingHorizontal="10dp" />

                <TextView
                    android:id="@+id/textView6"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="14dp"
                    android:text="@string/pvc_jvmArgs"
                    android:textColor="#FFFF9BAA"
                    android:textSize="11sp" />
                <EditText
                    android:id="@+id/vprof_editor_jre_args"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:background="@drawable/bg_redshift_hero"
                    android:hint="@string/use_global_default"
                    android:inputType="text"
                    android:minHeight="48dp"
                    android:padding="12dp"
                    android:textColor="#FFFFF5F7"
                    android:textColorHint="#FF76656D"
                    android:textSize="12sp" />
            </LinearLayout>

            <com.kdt.mcgui.MineButton
                android:id="@+id/vprof_editor_shortcut_button"
                android:layout_width="match_parent"
                android:layout_height="54dp"
                android:layout_marginTop="14dp"
                android:background="@drawable/bg_redshift_action"
                android:text="@string/create_shortcut"
                android:textAllCaps="false"
                android:textColor="#FFFF9BAA" />
        </LinearLayout>
    </ScrollView>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:paddingHorizontal="18dp"
        android:paddingVertical="10dp">
        <com.kdt.mcgui.MineButton
            android:id="@+id/vprof_editor_save_button"
            android:layout_width="0dp"
            android:layout_height="54dp"
            android:layout_weight="1"
            android:layout_marginEnd="6dp"
            android:background="@drawable/bg_redshift_play"
            android:text="@string/global_save"
            android:textColor="#FFFFFFFF" />
        <com.kdt.mcgui.MineButton
            android:id="@+id/vprof_editor_delete_button"
            android:layout_width="0dp"
            android:layout_height="54dp"
            android:layout_weight="1"
            android:layout_marginStart="6dp"
            android:background="@drawable/bg_redshift_action"
            android:text="@string/global_delete"
            android:textColor="#FFFF9BAA" />
    </LinearLayout>
</LinearLayout>
"""
(RES / "layout/fragment_profile_editor.xml").write_text(profile_editor, encoding="utf-8")
print("REDSHIFT profile editor rebuilt as grouped Instance Workshop.")


# Bundle the version-aware optimization catalog into the APK.
# Runtime installation is implemented separately; this resource is the single
# source of truth for project candidates, loader constraints and conflict rules.
catalog_source = Path("../patches/performance_catalog.json")
if catalog_source.exists():
    raw_dir = RES / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "redshift_performance_catalog.json").write_text(
        catalog_source.read_text(encoding="utf-8"), encoding="utf-8"
    )
else:
    raise FileNotFoundError("REDSHIFT performance catalog is missing")


# === REDSHIFT Performance Engine: real Modrinth resolution + profile-scoped install ===
engine_java = r"""package net.kdt.pojavlaunch.performance;

import android.content.Context;
import android.widget.Toast;
import android.widget.EditText;
import android.widget.LinearLayout;

import androidx.appcompat.app.AlertDialog;

import net.kdt.pojavlaunch.Tools;
import net.kdt.pojavlaunch.modloaders.modpacks.api.ModDependencyResolver;
import net.kdt.pojavlaunch.modloaders.modpacks.api.ResolveResult;
import net.kdt.pojavlaunch.modloaders.modpacks.api.SingleModInstaller;
import net.kdt.pojavlaunch.modloaders.modpacks.models.ModItem;
import net.kdt.pojavlaunch.value.launcherprofiles.LauncherProfiles;
import net.kdt.pojavlaunch.value.launcherprofiles.MinecraftProfile;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public final class RedshiftPerformanceEngine {
    private RedshiftPerformanceEngine() {}

    public static void show(Context context, String profileId) {
        String[] modes = {"Lite — максимум FPS", "Balanced — баланс", "Quality — больше визуальных улучшений"};
        new AlertDialog.Builder(context)
            .setTitle("REDSHIFT Performance Engine")
            .setMessage("Подберём моды именно под выбранную версию Minecraft и загрузчик. Несовместимые проекты будут пропущены.")
            .setSingleChoiceItems(modes, 1, (dialog, which) -> {
                dialog.dismiss();
                install(context, profileId, which);
            })
            .setNeutralButton("Настройки графики", (dialog, which) -> showGraphicsEditor(context, profileId))
            .setPositiveButton("Мои моды", (dialog, which) -> showModManager(context, profileId))
            .setNegativeButton("Отмена", null)
            .show();
    }


    private static void showGraphicsEditor(Context context, String profileId) {
        try {
            LauncherProfiles.load();
            MinecraftProfile profile = LauncherProfiles.mainProfileJson.profiles.get(profileId);
            if (profile == null) throw new IOException("Профиль не найден");
            File options = new File(Tools.getGameDirPath(profile), "options.txt");
            Map<String, String> current = new LinkedHashMap<>();
            if (options.isFile()) {
                try (BufferedReader reader = new BufferedReader(new FileReader(options))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        int colon = line.indexOf(':');
                        if (colon > 0) current.put(line.substring(0, colon), line.substring(colon + 1));
                    }
                }
            }
            LinearLayout panel = new LinearLayout(context);
            panel.setOrientation(LinearLayout.VERTICAL);
            int pad = (int) (18 * context.getResources().getDisplayMetrics().density);
            panel.setPadding(pad, pad, pad, 0);
            EditText render = new EditText(context);
            render.setSingleLine(true);
            render.setInputType(2);
            render.setHint("Дальность прорисовки (2–32)");
            render.setText(current.getOrDefault("renderDistance", "8"));
            panel.addView(render);
            EditText simulation = new EditText(context);
            simulation.setSingleLine(true);
            simulation.setInputType(2);
            simulation.setHint("Дальность симуляции (5–32)");
            simulation.setText(current.getOrDefault("simulationDistance", "6"));
            panel.addView(simulation);
            EditText particles = new EditText(context);
            particles.setSingleLine(true);
            particles.setInputType(2);
            particles.setHint("Частицы: 0 — минимум, 1 — снижено, 2 — все");
            particles.setText(current.getOrDefault("particles", "1"));
            panel.addView(particles);
            new AlertDialog.Builder(context)
                .setTitle("Графика Minecraft")
                .setMessage("Настройки сохраняются в options.txt выбранного профиля. Перед изменением создаётся резервная копия.")
                .setView(panel)
                .setPositiveButton("Применить", (dialog, which) -> {
                    try {
                        int r = Integer.parseInt(render.getText().toString().trim());
                        int sim = Integer.parseInt(simulation.getText().toString().trim());
                        int p = Integer.parseInt(particles.getText().toString().trim());
                        if (r < 2 || r > 32 || sim < 5 || sim > 32 || p < 0 || p > 2) {
                            throw new IllegalArgumentException("Проверь диапазоны: прорисовка 2–32, симуляция 5–32, частицы 0–2");
                        }
                        File gameDir = Tools.getGameDirPath(profile);
                        if (!gameDir.isDirectory() && !gameDir.mkdirs()) throw new IOException("Не удалось открыть папку игры");
                        if (options.isFile()) {
                            File backup = new File(new File(new File(gameDir, ".redshift-backups"), "graphics-" + System.currentTimeMillis()), "options.txt");
                            copyFile(options, backup);
                        }
                        current.put("renderDistance", String.valueOf(r));
                        current.put("simulationDistance", String.valueOf(sim));
                        current.put("particles", String.valueOf(p));
                        StringBuilder output = new StringBuilder();
                        for (Map.Entry<String, String> entry : current.entrySet()) {
                            output.append(entry.getKey()).append(':').append(entry.getValue()).append('\\n');
                        }
                        try (FileOutputStream stream = new FileOutputStream(options)) {
                            stream.write(output.toString().getBytes(StandardCharsets.UTF_8));
                        }
                        Toast.makeText(context, "Настройки графики сохранены", Toast.LENGTH_LONG).show();
                    } catch (Exception error) {
                        Toast.makeText(context, "Не удалось применить: " + error.getMessage(), Toast.LENGTH_LONG).show();
                    }
                })
                .setNegativeButton("Отмена", null)
                .show();
        } catch (Exception e) {
            Toast.makeText(context, "Ошибка редактора графики: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private static void showBackups(Context context, String profileId) {
        try {
            LauncherProfiles.load();
            MinecraftProfile profile = LauncherProfiles.mainProfileJson.profiles.get(profileId);
            if (profile == null) throw new IOException("Профиль не найден");
            File root = new File(Tools.getGameDirPath(profile), ".redshift-backups");
            File[] backups = root.listFiles(File::isDirectory);
            if (backups == null || backups.length == 0) {
                Toast.makeText(context, "Резервных копий пока нет", Toast.LENGTH_LONG).show();
                return;
            }
            java.util.Arrays.sort(backups, (a, b) -> Long.compare(b.lastModified(), a.lastModified()));
            String[] labels = new String[backups.length];
            for (int i = 0; i < backups.length; i++) labels[i] = backups[i].getName();
            new AlertDialog.Builder(context).setTitle("Резервные копии REDSHIFT")
                .setItems(labels, (dialog, which) -> new AlertDialog.Builder(context)
                    .setTitle("Восстановить " + labels[which] + "?")
                    .setMessage("Существующие файлы модов не будут перезаписаны. Сохранённый options.txt будет восстановлен вместо текущего.")
                    .setPositiveButton("Восстановить", (d, w) -> restoreBackup(context, profile, backups[which]))
                    .setNegativeButton("Отмена", null).show())
                .setNegativeButton("Закрыть", null).show();
        } catch (Exception e) {
            Toast.makeText(context, "Ошибка списка копий: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private static void restoreBackup(Context context, MinecraftProfile profile, File backupDir) {
        try {
            File gameDir = Tools.getGameDirPath(profile);
            File modsBackup = new File(backupDir, "mods");
            File modsDir = new File(gameDir, "mods");
            int restored = 0;
            File[] jars = modsBackup.listFiles();
            if (jars != null) {
                if (!modsDir.exists() && !modsDir.mkdirs()) throw new IOException("Не удалось создать папку mods");
                for (File jar : jars) {
                    if (jar.isFile() && jar.getName().endsWith(".jar")) {
                        File target = new File(modsDir, jar.getName());
                        if (!target.exists()) { copyFile(jar, target); restored++; }
                    }
                }
            }
            File savedOptions = new File(backupDir, "options.txt");
            if (savedOptions.isFile()) copyFile(savedOptions, new File(gameDir, "options.txt"));
            Toast.makeText(context, "Восстановлено модов: " + restored + ". Конфликтующие файлы пропущены.", Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(context, "Не удалось восстановить: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }


    private static void showModManager(Context context, String profileId) {
        try {
            LauncherProfiles.load();
            MinecraftProfile profile = LauncherProfiles.mainProfileJson.profiles.get(profileId);
            if (profile == null) throw new IOException("Профиль не найден");
            File modsDir = new File(Tools.getGameDirPath(profile), "mods");
            File[] jars = modsDir.listFiles((dir, name) -> name.toLowerCase(java.util.Locale.ROOT).endsWith(".jar"));
            if (jars == null || jars.length == 0) {
                Toast.makeText(context, "В этой сборке пока нет JAR-модов", Toast.LENGTH_LONG).show();
                return;
            }
            java.util.Arrays.sort(jars, (a, b) -> a.getName().compareToIgnoreCase(b.getName()));
            String[] labels = new String[jars.length];
            for (int i = 0; i < jars.length; i++) labels[i] = jars[i].getName();
            new AlertDialog.Builder(context)
                .setTitle("Моды сборки • " + jars.length)
                .setItems(labels, (dialog, which) -> new AlertDialog.Builder(context)
                    .setTitle("Удалить мод?")
                    .setMessage(labels[which] + "\\n\\nПеред удалением файл будет сохранён в резервную копию REDSHIFT.")
                    .setPositiveButton("Сохранить и удалить", (confirm, action) -> removeMod(context, profile, jars[which]))
                    .setNegativeButton("Отмена", null)
                    .show())
                .setNegativeButton("Закрыть", null)
                .show();
        } catch (Exception e) {
            Toast.makeText(context, "Не удалось открыть список модов: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private static void removeMod(Context context, MinecraftProfile profile, File modFile) {
        try {
            if (!modFile.isFile() || !modFile.getName().toLowerCase(java.util.Locale.ROOT).endsWith(".jar")) {
                throw new IOException("Файл мода больше не существует");
            }
            File backupRoot = new File(new File(Tools.getGameDirPath(profile), ".redshift-backups"),
                "manual-" + System.currentTimeMillis());
            File savedMod = new File(new File(backupRoot, "mods"), modFile.getName());
            copyFile(modFile, savedMod);
            if (!modFile.delete()) throw new IOException("Резервная копия создана, но удалить исходный файл не удалось");
            Toast.makeText(context, "Мод удалён. Копия сохранена: " + savedMod.getName(), Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(context, "Ошибка удаления мода: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private static void install(Context context, String profileId, int mode) {
        Toast.makeText(context, "Проверяем совместимость модов…", Toast.LENGTH_SHORT).show();
        new Thread(() -> {
            try {
                LauncherProfiles.load();
                MinecraftProfile profile = LauncherProfiles.mainProfileJson.profiles.get(profileId);
                if (profile == null) throw new Exception("Профиль Minecraft не найден");
                String mcVersion = profile.lastVersionId;
                String loader = profile.modLoader;
                if (mcVersion == null || mcVersion.trim().isEmpty()) throw new Exception("Сначала выбери версию Minecraft");
                if (loader == null || loader.trim().isEmpty()) loader = "fabric";
                loader = loader.toLowerCase(java.util.Locale.ROOT);
                if (!loader.equals("fabric") && !loader.equals("forge") &&
                    !loader.equals("neoforge") && !loader.equals("quilt")) {
                    throw new Exception("Для загрузчика " + loader + " пока нет набора автооптимизации");
                }

                List<String> projects = projectsFor(loader, mode);
                ResolveResult combined = new ResolveResult();
                Set<String> planned = new HashSet<>();
                List<String> skipped = new ArrayList<>();
                ModDependencyResolver resolver = new ModDependencyResolver();

                for (String projectId : projects) {
                    ResolveResult one = resolver.resolve(projectId, profile, mcVersion, loader);
                    if (!one.success) {
                        skipped.add(projectId);
                        continue;
                    }
                    addUnique(combined.modsToInstall, one.modsToInstall, planned);
                    addUnique(combined.dependenciesToInstall, one.dependenciesToInstall, planned);
                }

                if (combined.modsToInstall.isEmpty() && combined.dependenciesToInstall.isEmpty()) {
                    throw new Exception("Не найдено совместимых оптимизационных модов для " + mcVersion + " / " + loader);
                }

                combined.success = true;
                final int installCount = combined.modsToInstall.size() + combined.dependenciesToInstall.size();
                final int skippedCount = skipped.size();
                if (installCount == 0) throw new Exception("Нет новых модов для установки");
                File modsDir = new File(Tools.getGameDirPath(profile), "mods");
                if (modsDir.isDirectory()) {
                    for (ModItem plannedMod : combined.modsToInstall) ensureNoFilenameCollision(modsDir, plannedMod);
                    for (ModItem plannedMod : combined.dependenciesToInstall) ensureNoFilenameCollision(modsDir, plannedMod);
                }
                File backupDir = backupMods(profile, profileId, mcVersion, loader, mode);
                SingleModInstaller.installModWithDependencies(combined, profileId,
                    () -> {
                        try { tuneOptions(profile, backupDir, mode); } catch (Exception ignored) { ignored.printStackTrace(); }
                        Tools.runOnUiThread(() -> Toast.makeText(context,
                            "Готово: установлено " + installCount + " модов. Настройки графики применены." +
                            (skippedCount > 0 ? ", пропущено несовместимых: " + skippedCount : ""),
                            Toast.LENGTH_LONG).show());
                    },
                    () -> Tools.runOnUiThread(() -> Toast.makeText(context,
                        "Не удалось установить набор оптимизации", Toast.LENGTH_LONG).show())
                );
            } catch (Exception e) {
                final String message = e.getMessage() == null ? "Неизвестная ошибка" : e.getMessage();
                Tools.runOnUiThread(() -> Toast.makeText(context, message, Toast.LENGTH_LONG).show());
            }
        }).start();
    }

    private static void tuneOptions(MinecraftProfile profile, File backupDir, int mode) throws IOException {
        File gameDir = Tools.getGameDirPath(profile);
        File options = new File(gameDir, "options.txt");
        if (!options.exists()) return;
        File backup = new File(backupDir, "options.txt");
        copyFile(options, backup);
        Map<String, String> values = new LinkedHashMap<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(options))) {
            String line;
            while ((line = reader.readLine()) != null) {
                int colon = line.indexOf(':');
                if (colon > 0) values.put(line.substring(0, colon), line.substring(colon + 1));
            }
        }
        if (mode == 0) {
            values.put("graphics", "fast");
            values.put("renderDistance", "6");
            values.put("simulationDistance", "4");
            values.put("particles", "0");
            values.put("cloudStatus", "0");
            values.put("entityDistanceScaling", "0.5");
            values.put("biomeBlendRadius", "0");
        } else if (mode == 1) {
            values.put("graphics", "fast");
            values.put("renderDistance", "10");
            values.put("simulationDistance", "6");
            values.put("particles", "1");
            values.put("cloudStatus", "1");
            values.put("entityDistanceScaling", "0.75");
            values.put("biomeBlendRadius", "2");
        } else {
            values.put("graphics", "fancy");
            values.put("renderDistance", "14");
            values.put("simulationDistance", "8");
            values.put("particles", "2");
            values.put("cloudStatus", "2");
            values.put("entityDistanceScaling", "1.0");
            values.put("biomeBlendRadius", "4");
        }
        StringBuilder output = new StringBuilder();
        for (Map.Entry<String, String> entry : values.entrySet()) {
            output.append(entry.getKey()).append(':').append(entry.getValue()).append('\n');
        }
        try (FileOutputStream stream = new FileOutputStream(options)) {
            stream.write(output.toString().getBytes(StandardCharsets.UTF_8));
        }
    }

    private static void ensureNoFilenameCollision(File modsDir, ModItem mod) throws IOException {
        if (mod.fileName == null || mod.fileName.trim().isEmpty()) throw new IOException("У мода отсутствует имя файла");
        File existing = new File(modsDir, mod.fileName);
        if (existing.exists()) {
            throw new IOException("Файл уже существует: " + mod.fileName + ". Ничего не перезаписано — проверь моды вручную.");
        }
    }

    private static File backupMods(MinecraftProfile profile, String profileId, String mcVersion, String loader, int mode) throws IOException {
        File gameDir = Tools.getGameDirPath(profile);
        File modsDir = new File(gameDir, "mods");
        File backupDir = new File(new File(gameDir, ".redshift-backups"), "performance-" + System.currentTimeMillis());
        if (!backupDir.mkdirs() && !backupDir.isDirectory()) throw new IOException("Не удалось создать папку резервной копии");
        File backupMods = new File(backupDir, "mods");
        if (modsDir.isDirectory()) {
            File[] files = modsDir.listFiles();
            if (files != null) {
                for (File file : files) {
                    if (file.isFile() && file.getName().toLowerCase(java.util.Locale.ROOT).endsWith(".jar")) {
                        copyFile(file, new File(backupMods, file.getName()));
                    }
                }
            }
        }
        File manifest = new File(backupDir, "REDSHIFT-backup.txt");
        try (FileOutputStream output = new FileOutputStream(manifest)) {
            String data = "REDSHIFT Performance Engine backup\nProfile: " + profileId +
                "\nMinecraft: " + mcVersion + "\nLoader: " + loader +
                "\nMode: " + mode + "\nCreated: " + new java.util.Date() +
                "\\nRestore: copy files from mods/ back into the profile mods directory.";
            output.write(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        }
        return backupDir;
    }

    private static void copyFile(File source, File destination) throws IOException {
        File parent = destination.getParentFile();
        if (parent != null && !parent.exists() && !parent.mkdirs()) throw new IOException("Не удалось создать папку резервной копии");
        try (FileInputStream input = new FileInputStream(source);
             FileOutputStream output = new FileOutputStream(destination)) {
            byte[] buffer = new byte[8192];
            int count;
            while ((count = input.read(buffer)) != -1) output.write(buffer, 0, count);
        }
    }

    private static List<String> projectsFor(String loader, int mode) {
        List<String> ids = new ArrayList<>();
        if (loader.equals("fabric") || loader.equals("quilt")) {
            ids.add("sodium");
            ids.add("lithium");
            ids.add("ferrite-core");
            ids.add("immediatelyfast");
            ids.add("entityculling");
            if (mode >= 1) ids.add("dynamic-fps");
            if (mode >= 2) ids.add("badoptimizations");
        } else {
            ids.add("embeddium");
            ids.add("ferrite-core");
            ids.add("immediatelyfast");
            ids.add("entityculling");
            ids.add("modernfix");
            if (mode >= 1) ids.add("memoryleakfix");
            if (mode >= 2) ids.add("badoptimizations");
        }
        return ids;
    }

    private static void addUnique(List<ModItem> target, List<ModItem> incoming, Set<String> planned) {
        for (ModItem mod : incoming) {
            String key = mod.projectId == null ? mod.id : mod.projectId;
            if (key != null && planned.add(key)) target.add(mod);
        }
    }
}
"""
perf_dir = ROOT / "java/net/kdt/pojavlaunch/performance"
perf_dir.mkdir(parents=True, exist_ok=True)
(perf_dir / "RedshiftPerformanceEngine.java").write_text(engine_java, encoding="utf-8")

# Add a genuine dashboard action and connect it to the selected instance.
portrait_path = RES / "layout/fragment_launcher.xml"
portrait_xml = portrait_path.read_text(encoding="utf-8")
if 'performance_engine_button' not in portrait_xml:
    tile = """<com.kdt.mcgui.LauncherMenuButton
                    android:id="@+id/performance_engine_button"
                    style="@style/LauncherMenuButton.Universal"
                    android:layout_width="match_parent"
                    android:layout_height="58dp"
                    android:layout_marginTop="8dp"
                    android:background="@drawable/bg_redshift_action"
                    android:drawableStart="@drawable/ic_redshift_mark"
                    android:drawableTint="#FFFF7185"
                    android:gravity="center_vertical"
                    android:paddingStart="14dp"
                    android:text="PERFORMANCE ENGINE  •  Автооптимизация"
                    android:textAllCaps="false"
                    android:textColor="#FFFFF5F7"
                    android:textSize="13sp" />"""
    anchor = '<com.kdt.mcgui.LauncherMenuButton\n                    android:id="@+id/open_files_button"'
    if anchor in portrait_xml:
        # place the engine card immediately before the open-folder action
        portrait_xml = portrait_xml.replace(anchor, tile + "\n\n                " + anchor, 1)
    else:
        raise RuntimeError("Could not locate REDSHIFT dashboard action section")
    portrait_path.write_text(portrait_xml, encoding="utf-8")

main_menu = ROOT / "java/net/kdt/pojavlaunch/fragments/MainMenuFragment.java"
main_source = main_menu.read_text(encoding="utf-8")
if "RedshiftPerformanceEngine.show" not in main_source:
    marker = "        mOpenDirectoryButton.setOnClickListener((v)-> openPath(v.getContext(), getCurrentProfileDirectory(), false));"
    handler = marker + """

        View performanceButton = view.findViewById(R.id.performance_engine_button);
        if (performanceButton != null) {
            performanceButton.setOnClickListener(v -> {
                String selectedProfile = LauncherPreferences.DEFAULT_PREF.getString(
                    LauncherPreferences.PREF_KEY_CURRENT_PROFILE, null);
                if (!Tools.isValidString(selectedProfile)) {
                    Toast.makeText(requireContext(), "Сначала выбери профиль Minecraft", Toast.LENGTH_LONG).show();
                } else {
                    net.kdt.pojavlaunch.performance.RedshiftPerformanceEngine.show(requireContext(), selectedProfile);
                }
            });
        }"""
    if marker not in main_source:
        raise RuntimeError("Could not attach Performance Engine click handler")
    main_menu.write_text(main_source.replace(marker, handler, 1), encoding="utf-8")

print("REDSHIFT Performance Engine wired to dashboard: exact-version Modrinth resolver and profile-specific installer.")
