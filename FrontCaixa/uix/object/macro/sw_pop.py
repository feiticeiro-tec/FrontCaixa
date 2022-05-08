from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class SWPop(MDDialog):
    def __init__(self, content, title, _parent=None, auto_dismiss=True, args=[]):
        self._content = content(*args, _parent=self)
        self.__parent = _parent
        self.auto_dismiss = auto_dismiss
        super().__init__(
            type='custom',
            content_cls=self._content,
            title=f'[color=#ffffff]{title}[/color]',
            md_bg_color=self._content.md_bg_color
        )
        self.adaptive_width = True
        self.open()

    def on_dismiss(self):
        if self.auto_dismiss:
            if self._parent:
                self._parent.pop = None
            return super().on_dismiss()
