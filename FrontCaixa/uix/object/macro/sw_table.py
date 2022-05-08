from functools import partial
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.button import MDIconButton
from kivy.properties import ListProperty, BooleanProperty, ColorProperty, DictProperty, NumericProperty, ObjectProperty
from kivy.metrics import dp


from FrontCaixa.uix.object.micro.sw_chacked_button import SWCheckedButton


class SWRowTable(MDBoxLayout):
    check = BooleanProperty(None)
    columns = ListProperty([])
    sizes = ListProperty([])
    table_color = ColorProperty([1, 1, 1, 1])
    line_color = ColorProperty([0, 0, 0, 1])
    index = NumericProperty()
    update_data = ObjectProperty()

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.md_bg_color = self.line_color

    def on_columns(self, obj, data):
        self.clear_widgets()
        self.spacing = dp(1)
        for index, text in enumerate(self.columns):
            if self.check != None and index == 0:
                self.button = SWCheckedButton(
                    self.check,
                    md_bg_color=self.table_color,
                    width=dp(30),
                    pos_hint={'center_y': 0.5, 'center_x': 0.5})
                self.button.bind(on_release=lambda *args: self.update_data())
                self.add_widget(self.button)

            self.add_widget(MDLabel(
                text=text,
                size_hint=[None, None],
                size=self.sizes[index],
                halign='center',
                pos_hint={'center_y': 0.5, 'center_x': 0.5},
                md_bg_color=self.table_color
            ))


class SWTable(MDBoxLayout):
    header = ListProperty([])
    data = ListProperty([])
    sizes = ListProperty([])
    lines_color = ColorProperty([1, 0, 0, 1])
    head_color = ColorProperty([0, 0, 1, 0])
    data_values = DictProperty()

    def on_data(self, obj, data):
        self.ids.table.data = data
        data_values = {}

        for row in data:
            for index, column in enumerate(row['columns']):
                try:
                    valor = float(column)
                    check = False if self.header[0] == None else True
                    if check:
                        if data_values.get(self.header[index+1]):
                            data_values[self.header[index+1]] += valor
                        else:
                            data_values[self.header[index+1]] = valor
                    else:
                        if data_values.get(self.header[index]):
                            data_values[self.header[index]] += valor
                        else:
                            data_values[self.header[index]] = valor

                except:
                    ...
        self.data_values = data_values

    def on_header(self, onj, header):
        self.ids.header.clear_widgets()

        self.head = SWRowTable()
        self.head.update_data = self.update_checked_row_all
        self.head.md_bg_color = 0, 1, 1, 1  # self.head_color
        self.head.radius = [self.radius[0], self.radius[1], dp(0), dp(0)]
        self.head.sizes = self.sizes
        self.head.size_hint_y = None
        self.head.height = self.sizes[0][1]
        self.head.table_color = [0, 0, 0, 0]
        self.head.line_color = 1, 0, 1, 1  # self.head_color
        if header[0] in (True, False):
            self.ids.table.width = sum(x for x, y in self.sizes)+dp(30)
            self.head.check = False
            self.head.columns = header[1:]
        else:
            self.ids.table.width = sum(x for x, y in self.sizes)
            self.head.columns = header

        self.ids.header.add_widget(self.head)

    def update_checked_row(self, index):
        self.data[index]['check'] = not self.data[index]['check']

    def update_checked_row_all(self):
        self.head.check = not self.head.check
        for row in self.data:
            row['check'] = self.head.check
        data = self.data.copy()
        self.data = []
        self.data = data

    def set_data(self):
        self.data = list(
            {
                'check': True,
                'sizes': self.sizes,
                'index': i,
                'update_data': partial(self.update_checked_row, i),
                'columns': [str(i), '#08', 'Coca Cola', '5.30', '2', str(5.30*2)],
            } for i in range(2))
