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

\nprint("REDSHIFT custom dashboard cards, account bar, adaptive icon and branding applied.")
