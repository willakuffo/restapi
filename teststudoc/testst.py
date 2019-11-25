import os
class IM:
    def __init__(self,image,width = '200px',height = '100px',align = 'center',alt = 'alternate text'):
        ''' '''
        self.image = image
        self.width = width
        self.align = align
        self.height = height
        self.alt = alt

        #as image
        self.im = '.. image:: '+self.image+'\n\
        :width: '+self.width+'\n\
        :align: '+self.align+'\n\
        :height: '+self.height+'\n\
        :alt: '+self.alt+'\n'
        #as figure
        self.fig = '.. figure:: '+self.image+'\n\
        :width: '+self.width+'\n\
        :align: '+self.align+'\n\
        :height: '+self.width+'\n\
        :alt: '+self.width+'\n\
        :figclass: align-center\n' #by default...care to change in later versions

    #accessors
    
    def get_width(self):
        return self.width
    
    def get_align(self):
        return self.align
    
    def get_height(self):
        return self.height
    
    def get_alt(self):
        return self.alt
    
    def get_image(self):
        return self.image
    
    #mutators
    '''def set_width(self,width):
        self.width = width
    
    def set_align(self,align):
        self.width = align
    
    def set_height(self,height):
        self.height = height
    
    def set_alt(self,alt):
        self.width = alt
    
    def set_image(self,image):
        self.image = image'''
    

    # dir is the directory of the rst file
    def view(self,dir = 'source\index.rst'):
        '''view typed editted rst in shell, for debugging purposes'''
        with open(dir,'r') as file:
            for line in file:
                print(line)  

    def edit(self,editor,dir  ='source\index.rst' ):
        '''append rst feature. editor is a markdown syntax command recognized'''
        file =  open(dir,'a')
        file.write(editor)
   
    def edit_as_im(self,dir = 'source\index.rst'):
        '''append rst feature. editot is a markdown syntax command recognized'''
        file =  open(dir,'a')
        editor = self.im
        file.write(editor)
    
    def edit_as_fig(self,comment,dir = 'source\index.rst'):
        '''append rst feature. editot is a markdown syntax command recognized'''
        file =  open(dir,'a')
        editor = self.fig
        file.write(editor+'\n        '+comment)
    
    def add_table(self,header = 'header',**kwargs):
        self.rst_table = '\n.. csv-table:: **a title**\n\
        :header: "name", "firstname", "age"\n'
 
        for row in kwargs.values():
            self.rst_table = self.rst_table+'\n        '+row
        #print(self.rst_table)
        self.edit(self.rst_table)
        return self.rst_table


        
    


    



im = IM('11.jpg',align = 'left')
#im.edit('TEST TITLE\n==========\n','source\index.rst')
#im.edit_as_im() #will use default pars
#im.edit_as_fig('this is the figure')
im.view('source\index.rst')
os.system('make html')
os.startfile('build\html/index.html')
print(im.get_height())
im.add_table(row1 = '"Smith", "John", 40',row2 = '"Smith", "John", 40')