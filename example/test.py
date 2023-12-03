from pycord_ext_i18n import I18n

i18n = I18n()
i18n.load('./locale')
print(i18n.get_text("commands.test.name", "zh-TW", None))
