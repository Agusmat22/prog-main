#clases

class Persona:

    def __init__(self,entidad,plan,n_af,int,nombre,apellido,tipo_documento,dni) -> None:
        
        self._entidad = entidad
        self._plan = plan
        self._n_af = n_af
        self._int = int
        self._nombre = nombre
        self._apellido = apellido
        self._tipo_documento = tipo_documento
        self._dni = dni


    def __str__(self) -> str:
        return self._nombre + ' ' + self._apellido


    
    #GETTERS
    @property
    def entidad(self):

        return self._entidad
    @property
    def plan(self):

        return self._plan
    @property
    def n_af(self):

        return self._n_af
    @property
    def int(self):

        return self._int
    @property
    def nombre(self):

        return self._nombre
    @property
    def apellido(self):

        return self._apellido
    @property
    def tipo_documento(self):

        return self._tipo_documento
    @property
    def dni(self):

        return self._dni
    
    #SETTERS

    @entidad.setter
    def entidad(self,valor):

        self._entidad = valor


    @plan.setter
    def plan(self,valor):

        self._plan = valor


    @n_af.setter
    def n_af(self,valor):

        self._n_af = valor


    @int.setter
    def int(self,valor):

        self._int = valor


    @nombre.setter
    def nombre(self,valor):

        self._nombre = valor


    @apellido.setter
    def apellido(self,valor):

        self._apellido = valor

    @tipo_documento.setter
    def tipo_documento(self,valor):

        self._tipo_documento = valor


    @dni.setter
    def dni(self,valor):

        self._dni = valor



class AfiliadoPrestador(Persona):

    def __init__(self, entidad, plan, n_af, int, nombre, apellido, tipo_documento, dni) -> None:
        super().__init__(entidad, plan, n_af, int, nombre, apellido, tipo_documento, dni)
    
    

    @property
    def n_af(self):

        return self._n_af

    @n_af.setter
    def n_af(self,valor):

        self._n_af = valor
    


    

