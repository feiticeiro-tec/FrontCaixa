from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty,BooleanProperty,ColorProperty,DictProperty
from kivymd.uix.label import MDIcon,MDLabel
from kivy.metrics import dp
class SWRowTable(MDBoxLayout):
    check = BooleanProperty(None)
    columns = ListProperty([])
    sizes = ListProperty([])
    table_color = ColorProperty([1,1,1,1])
    line_color = ColorProperty([0,0,0,1])
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        self.md_bg_color = self.line_color

    def on_columns(self,obj,data):
        self.clear_widgets()
        self.spacing = dp(1)
        for index,text in enumerate(self.columns):
            if self.check != None and index == 0:
                self.add_widget(MDIcon(
                    icon='checkbox-intermediate' if self.check else 'checkbox-blank-outline',
                    md_bg_color=self.table_color,
                    size_hint_x=None,
                    width=dp(30),
                    pos_hint={'center_y':0.5,'center_x':0.5}))
            self.add_widget(MDLabel(
                text=text,
                size_hint=[None,None],
                size=self.sizes[index],
                halign='center',
                pos_hint={'center_y':0.5,'center_x':0.5},
                md_bg_color=self.table_color
                ))

class SWTable(MDBoxLayout):
    header = ListProperty([])
    data = ListProperty([])
    sizes = ListProperty([])
    lines_color = ColorProperty([1,0,0,1])
    head_color = ColorProperty([0,0,1,0])
    data_values = DictProperty()
    def on_data(self,obj,data):
        self.ids.table.data = data

    def on_header(self,onj,header):
        self.ids.header.clear_widgets()
        
        head = SWRowTable()
        head.md_bg_color = 0,1,1,1#self.head_color
        head.radius = [self.radius[0],self.radius[1],dp(0),dp(0)]
        head.sizes = self.sizes
        head.size_hint_y = None
        head.height = self.sizes[0][1]
        head.table_color = [0,0,0,0]
        head.line_color = 1,0,1,1#self.head_color
        if header[0] in (True, False):
            self.ids.table.width = sum(x for x,y in self.sizes)+dp(30)
            head.check = False
            head.columns = header[1:]
        else:
            self.ids.table.width = sum(x for x,y in self.sizes)
            head.columns = header
            
        self.ids.header.add_widget(head)


    def set_data(self):
        self.data =list({'check':True,'sizes':self.sizes,'columns':[str(i),'#08','Coca Cola','5.30','2',str(5.30*2)]} for i in range(2))
        data_values = {}
        
        for row in self.data:
            for index,column in enumerate(row['columns']):
                try:
                    valor = float(column)
                    print( self.header[0],data_values.get(self.header[index+1]),self.header[index+1])
                    
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