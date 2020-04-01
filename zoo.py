class animal: 
    def _init_(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    def set_nombre(self,nombre): 
        self.nombre = nombre
          
    def get_nombre(self):
        print(self.nombre)
        self.get_miprueba()
        
                  
        
def main():
    
    nanimales = int(input("¿Cuántos animales son?: "))
    lanimales = [nanimales]
    for x in range(0,nanimales):
        anombre = input("¿Cuál es su nombre?")
        atipo = input("¿Qué tipo es?")
        if x<(nanimales - 1):
            lanimales[x] = animal(anombre,atipo)

        
    
if __name__ == "__main__":
	main()