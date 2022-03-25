import os
class Limpiar:
    def limpiarConsola(self):
        if os.name in ('nt','dos'):
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)