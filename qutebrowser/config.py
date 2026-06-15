config.load_autoconfig(False)

# ==========================================================================
# Configuración Base y Optimización
# ==========================================================================

# Quitar barra superior y otros elementos visuales
c.window.hide_decoration = True
c.scrolling.bar = 'never'

# pestañas
c.tabs.show = 'switching'
c.tabs.position = 'top'
config.bind('<Tab>', 'config-cycle tabs.show always never')

# Optimizacion de memoria
c.session.lazy_restore = True
c.content.blocking.method = 'both'
c.content.blocking.enabled = True
c.content.autoplay = False
c.qt.args = [
    'renderer-process-limit=2',
    'disable-gpu-memory-buffer-video-frames',
    'enable-low-res-tiling',
    'disable-features=RendererCodeIntegrity',
    'disable-logging',
]

# ==========================================================================
# Configuración del Motor Web (Modo Oscuro Nativo)
# ==========================================================================

# Forzar modo oscuro nativo
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.contrast = -0.1
c.colors.webpage.darkmode.threshold.foreground = 150
c.colors.webpage.darkmode.threshold.background = 150
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = "#E6DED5"

# ==========================================================================
# Tema BlueInk (Interfaz de Navegador)
# ==========================================================================

# Definición de paleta
palette = {
    "paper_base": "#E6DED5",
    "paper_shadow": "#D4C9BC",
    "paper_crust": "#C2B6A7",
    "ink_washed": "#516491",
    "ink_base": "#022164",
    "ink_mid": "#1C3773",
    "ink_heavy": "#010B22",
}

# completion {{{
c.colors.completion.category.bg = palette["ink_heavy"]
c.colors.completion.category.border.bottom = palette["ink_heavy"]
c.colors.completion.category.border.top = palette["ink_heavy"]
c.colors.completion.category.fg = palette["paper_base"]
c.colors.completion.even.bg = palette["paper_base"]
c.colors.completion.odd.bg = palette["paper_base"]
c.colors.completion.fg = palette["ink_base"]

c.colors.completion.item.selected.bg = palette["paper_shadow"]
c.colors.completion.item.selected.border.bottom = palette["paper_shadow"]
c.colors.completion.item.selected.border.top = palette["paper_shadow"]
c.colors.completion.item.selected.fg = palette["ink_heavy"]
c.colors.completion.item.selected.match.fg = palette["ink_heavy"]
c.colors.completion.match.fg = palette["ink_mid"]
c.colors.completion.scrollbar.bg = palette["paper_crust"]
c.colors.completion.scrollbar.fg = palette["ink_washed"]
# }}}

# downloads {{{
c.colors.downloads.bar.bg = palette["paper_base"]
c.colors.downloads.error.bg = palette["ink_heavy"]
c.colors.downloads.start.bg = palette["paper_shadow"]
c.colors.downloads.stop.bg = palette["paper_base"]
c.colors.downloads.error.fg = palette["paper_base"]
c.colors.downloads.start.fg = palette["ink_base"]
c.colors.downloads.stop.fg = palette["ink_mid"]
# }}}

# hints {{{
c.colors.hints.bg = palette["ink_heavy"]
c.colors.hints.fg = palette["paper_base"]
c.hints.border = "1px solid " + palette["ink_heavy"]
c.colors.hints.match.fg = palette["ink_washed"]
# }}}

# messages {{{
c.colors.messages.error.bg = palette["ink_heavy"]
c.colors.messages.info.bg = palette["paper_shadow"]
c.colors.messages.warning.bg = palette["ink_mid"]
c.colors.messages.error.border = palette["ink_heavy"]
c.colors.messages.info.border = palette["paper_shadow"]
c.colors.messages.warning.border = palette["ink_mid"]
c.colors.messages.error.fg = palette["paper_base"]
c.colors.messages.info.fg = palette["ink_heavy"]
c.colors.messages.warning.fg = palette["paper_base"]
# }}}

# prompts {{{
c.colors.prompts.bg = palette["paper_base"]
c.colors.prompts.border = "1px solid " + palette["paper_shadow"]
c.colors.prompts.fg = palette["ink_base"]
c.colors.prompts.selected.bg = palette["paper_shadow"]
c.colors.prompts.selected.fg = palette["ink_heavy"]
# }}}

# statusbar {{{
c.colors.statusbar.normal.bg = palette["paper_base"]
c.colors.statusbar.normal.fg = palette["ink_mid"]
c.colors.statusbar.insert.bg = palette["ink_mid"]
c.colors.statusbar.insert.fg = palette["paper_base"]
c.colors.statusbar.command.bg = palette["paper_shadow"]
c.colors.statusbar.command.fg = palette["ink_heavy"]
c.colors.statusbar.passthrough.bg = palette["ink_washed"]
c.colors.statusbar.passthrough.fg = palette["paper_base"]
c.colors.statusbar.caret.bg = palette["ink_mid"]
c.colors.statusbar.caret.fg = palette["paper_base"]
c.colors.statusbar.caret.selection.bg = palette["ink_heavy"]
c.colors.statusbar.caret.selection.fg = palette["paper_base"]
c.colors.statusbar.progress.bg = palette["ink_mid"]
c.colors.statusbar.url.error.fg = palette["ink_heavy"]
c.colors.statusbar.url.fg = palette["ink_base"]
c.colors.statusbar.url.hover.fg = palette["ink_mid"]
c.colors.statusbar.url.success.http.fg = palette["ink_base"]
c.colors.statusbar.url.success.https.fg = palette["ink_base"]
c.colors.statusbar.url.warn.fg = palette["ink_mid"]
# }}}

# tabs {{{
c.colors.tabs.bar.bg = palette["paper_shadow"]
c.colors.tabs.even.bg = palette["paper_shadow"]
c.colors.tabs.odd.bg = palette["paper_shadow"]
c.colors.tabs.even.fg = palette["ink_washed"]
c.colors.tabs.odd.fg = palette["ink_washed"]
c.colors.tabs.indicator.error = palette["ink_heavy"]
c.colors.tabs.indicator.system = "none"
c.colors.tabs.selected.even.bg = palette["paper_base"]
c.colors.tabs.selected.odd.bg = palette["paper_base"]
c.colors.tabs.selected.even.fg = palette["ink_heavy"]
c.colors.tabs.selected.odd.fg = palette["ink_heavy"]
# }}}

# context menus {{{
c.colors.contextmenu.menu.bg = palette["paper_base"]
c.colors.contextmenu.menu.fg = palette["ink_base"]
c.colors.contextmenu.disabled.bg = palette["paper_shadow"]
c.colors.contextmenu.disabled.fg = palette["ink_washed"]
c.colors.contextmenu.selected.bg = palette["paper_shadow"]
c.colors.contextmenu.selected.fg = palette["ink_heavy"]
# }}}
