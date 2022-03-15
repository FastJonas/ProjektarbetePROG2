class Room:
    def __init__(self,lista):
        self.__plats=int(lista[0])
        self.__w=int(lista[1])
        self.__n=int(lista[2])
        self.__e=int(lista[3])
        self.__s=int(lista[4])
        self.__info=(lista[5])
        self.__object=(lista[6])
        self.__wname=(lista[7])
        self.__nname=(lista[8])
        self.__ename=(lista[9])
        self.__sname=(lista[10])
        self.__getplatsname=(lista[11])
        
    def get_info(self):
        return self.__info
    
    def get_object(self):
        return self.__object
    
    def get_w(self):
        return self.__w
    
    def get_n(self):
        return self.__n
    
    def get_e(self):
        return self.__e
    
    def get_s(self):
        return self.__s
    
    def get_plats(self):
        return self.__plats

    def get_wname(self):
        return self.__wname

    def get_nname(self):
        return self.__nname

    def get_ename(self):
        return self.__ename

    def get_sname(self):
        return self.__sname

    def get_platsname(self):
        return self.__getplatsname

    
    def set_info(self,new):
        self.__info=new
    
    def set_object(self,new):
        self.__object=new
    
    def set_w(self,new):
        self.__w=new
    
    def set_n(self,new):
        self.__n=new
    
    def set_e(self,new):
        self.__e=new
    
    def set_s(self,new):
        self.__s=new
   
    def set_plats(self,new):
        self.__plats=new
    
    
    def set_wname(self,new):
        self.__wname=new

    def set_nname(self,new):
        self.__nname=new

    def set_ename(self,new):
        self.__ename=new

    def set_sname(self,new):
        self.__sname=new

    def set_getplatsname(self,new):
        self.__getplatsname=new
