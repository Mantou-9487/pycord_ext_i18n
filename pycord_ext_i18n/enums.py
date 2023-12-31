from enum import Enum
#reference: https://discord.com/developers/docs/reference#locales
class Locale(Enum):
    bg = "bg"
    "Bulgarian | български"  # noqa: RUF001
    cs = "cs"
    "Czech | Čeština"
    da = "da"
    "Danish | Dansk"
    de = "de"
    "German | Deutsch"
    el = "el"
    "Greek | Ελληνικά"  # noqa: RUF001
    en_GB = "en-GB"
    "English, UK | English, UK"
    en_US = "en-US"
    "English, US | English, US"
    es_ES = "es-ES"
    "Spanish | Español"
    fi = "fi"
    "Finnish | Suomi"
    fr = "fr"
    "French | Français"
    hi = "hi"
    "Hindi | हिन्दी"
    hr = "hr"
    "Croatian | Hrvatski"
    hu = "hu"
    "Hungarian | Magyar"
    id = "id"
    "Indonesian | Bahasa Indonesia"
    it = "it"
    "Italian | Italiano"
    ja = "ja"
    "Japanese | 日本語"
    ko = "ko"
    "Korean | 한국어"
    lt = "lt"
    "Lithuanian | Lietuviškai"
    nl = "nl"
    "Dutch | Nederlands"
    no = "no"
    "Norwegian | Norsk"
    pl = "pl"
    "Polish | Polski"
    pt_BR = "pt-BR"
    "Portuguese, Brazilian | Português do Brasil"
    ro = "ro"
    "Romanian, Romania | Română"
    ru = "ru"
    "Russian | Pусский"  # noqa: RUF001
    sv_SE = "sv-SE"
    "Swedish | Svenska"
    th = "th"
    "Thai | ไทย"
    tr = "tr"
    "Turkish | Türkçe"
    uk = "uk"
    "Ukrainian | Українська"  # noqa: RUF001
    vi = "vi"
    "Vietnamese | Tiếng Việt"
    zh_CN = "zh-CN"
    "Chinese, China | 中文"
    zh_TW = "zh-TW"
    "Chinese, Taiwan | 繁體中文"

    def __str__(self) -> str:
        return self.value