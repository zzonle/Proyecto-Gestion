# main.py
# main.py

from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from models.empleado import Empleado
from models.departamento import Departamento
from models.proyecto import Proyecto


empleado_controller = EmpleadoController()
departamento_controller = DepartamentoController()
proyecto_controller = ProyectoController()

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1.1":
                    # Código para crear empleado
                    rut = input("Ingrese el RUT del empleado: ")
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la dirección del empleado: ")
                    telefono = input("Ingrese el teléfono del empleado: ")
                    email = input("Ingrese el email del empleado: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    salario = float(input("Ingrese el salario del empleado: "))
                    departamento_id = int(input("Ingrese el ID del departamento: "))

                    nuevo_empleado = Empleado(
                        rut=rut, 
                        nombre=nombre, 
                        direccion=direccion, 
                        telefono=telefono, 
                        email=email, 
                        fecha_inicio=fecha_inicio, 
                        salario=salario, 
                        departamento_id=departamento_id
                    )
                    
                    empleado_controller.crear_empleado(nuevo_empleado)
                    print("Empleado creado exitosamente.")

                elif sub_opcion == "1.2":
                    # Código para listar empleados
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                        print(emp)

                elif sub_opcion == "1.3":
                    # Código para buscar empleado por RUT
                    rut = input("Ingrese el RUT del empleado a buscar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.4":
                    # Código para modificar empleado
                    rut = input("Ingrese el RUT del empleado a modificar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        nombre = input("Ingrese el nuevo nombre del empleado: ")
                        direccion = input("Ingrese la nueva dirección del empleado: ")
                        telefono = input("Ingrese el nuevo teléfono del empleado: ")
                        email = input("Ingrese el nuevo email del empleado: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
                        salario = float(input("Ingrese el nuevo salario del empleado: "))
                        departamento_id = int(input("Ingrese el nuevo ID del departamento: "))

                        empleado_modificado = Empleado(
                            id=empleado[0],
                            rut=rut,
                            nombre=nombre,
                            direccion=direccion,
                            telefono=telefono,
                            email=email,
                            fecha_inicio=fecha_inicio,
                            salario=salario,
                            departamento_id=departamento_id
                        )
                        
                        empleado_controller.modificar_empleado(empleado_modificado)
                        print("Empleado modificado exitosamente.")
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.5":
                    # Código para eliminar empleado
                    rut = input("Ingrese el RUT del empleado a eliminar: ")
                    empleado_controller.eliminar_empleado(rut)
                    print("Empleado eliminado exitosamente.")

                elif sub_opcion == "1.6":
                    break

        elif opcion == "2":
            while True:
                menu_departamento()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "2.1":
                    nombre = input("Ingrese el nombre del departamento: ")
                    gerente_id = input("Ingrese el ID del gerente (opcional): ")
                    gerente_id = int(gerente_id) if gerente_id else None

                    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
                    departamento_controller.crear_departamento(nuevo_departamento)
                    print("Departamento creado exitosamente.")

                elif sub_opcion == "2.2":
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(dep)

                elif sub_opcion == "2.3":
                    id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        print(departamento)
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.4":
                    id_dep = int(input("Ingrese el ID del departamento a modificar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        nombre = input("Ingrese el nuevo nombre del departamento: ")
                        gerente_id = input("Ingrese el nuevo ID del gerente (opcional): ")
                        gerente_id = int(gerente_id) if gerente_id else None

                        departamento_modificado = Departamento(id=id_dep, nombre=nombre, gerente_id=gerente_id)
                        departamento_controller.modificar_departamento(departamento_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.5":
                    id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                    departamento_controller.eliminar_departamento(id_dep)
                    print("Departamento eliminado exitosamente.")

                elif sub_opcion == "2.6":
                    break
        elif opcion == "3":
            while True:
                menu_proyecto()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "3.1":
                    nombre = input("Ingrese el nombre del proyecto: ")
                    descripcion = input("Ingrese la descripción del proyecto: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    
                    nuevo_proyecto = Proyecto(
                        nombre = nombre,
                        descripcion= descripcion,
                        fecha_inicio= fecha_inicio
                    )
                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                    print("Proyecto creado exitosamente.")
                elif sub_opcion == "3.2":
                    id = input("Ingrese la ID del proyecto a buscar: ")
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id)
                    if proyecto:
                        print(proyecto)
                    else:
                        print("Proyecto no encontrado.")
                elif sub_opcion == "3.3":
                    id = input("Ingrese la ID del proyecto a modificar: ")
                    nombre = input("Ingrese el nuevo nombre del proyecto: ")
                    descripcion = input("Ingrese la nueva descripción del proyecto: ")
                    
                    proyecto_modificado = Proyecto(
                        id=id,
                        nombre=nombre,
                        descripcion=descripcion
                    ) 
                    
                    proyecto_controller.modificar_proyecto(proyecto_modificado)
                    
                    if (proyecto_modificado):
                        print("Proyecto modificado exitosamente.")
                    else:
                        print("Proyecto no encontrado.")       
                elif sub_opcion == "3.4":
                    id = input("Ingrese la ID del proyecto a eliminar:")
                       
                    proyecto = proyecto_controller.eliminar_proyecto(id)
                    
                    if proyecto:
                        print("Proyecto eliminado exitosamente.")
                    else:
                        print("Proyecto no encontrado.")
                elif sub_opcion == "3.5":
                    empleado_id = input("Ingrese la ID del empleado para agregar al proyecto: ")
                    proyecto_id = input("Ingrese la ID del proyecto: ")
                    
                    proyectoempleado = proyecto_controller.agregar_empleado_proyecto(proyecto_id , empleado_id)
                    
                    if proyectoempleado:
                        print("Empleado o proyecto no encontrados.")
                    else:
                        print("Empleado agregado al proyecto exitosamente.")
                    
                    
                elif sub_opcion == "3.6":     
                    pass
                elif sub_opcion == "3.7":
                    proyecto_id = input("Ingrese la ID del proyecto para buscar los empleados: ")
                    
                    empleados_proyecto = proyecto_controller.listar_empleados_proyecto(proyecto_id)
                    print("Empleados del proyecto:")
                    print(empleados_proyecto)
                elif sub_opcion == "3.8":
                    break

        elif opcion == "4":
            pass                
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()






"""
from views.menu import menu_principal, menu_empleado
from controllers.empleado_controller import EmpleadoController
from models.empleado import Empleado

# Instancia del controlador de empleados
empleado_controller = EmpleadoController()

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1.1":
                    # Código para crear empleado
                    rut = input("Ingrese el RUT del empleado: ")
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la dirección del empleado: ")
                    telefono = input("Ingrese el teléfono del empleado: ")
                    email = input("Ingrese el email del empleado: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    salario = float(input("Ingrese el salario del empleado: "))
                    departamento_id = int(input("Ingrese el ID del departamento: "))

                    nuevo_empleado = Empleado(
                        rut=rut, 
                        nombre=nombre, 
                        direccion=direccion, 
                        telefono=telefono, 
                        email=email, 
                        fecha_inicio=fecha_inicio, 
                        salario=salario, 
                        departamento_id=departamento_id
                    )
                    
                    empleado_controller.crear_empleado(nuevo_empleado)
                    print("Empleado creado exitosamente.")

                elif sub_opcion == "1.2":
                    # Código para listar empleados
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                        print(emp)

                elif sub_opcion == "1.3":
                    # Código para buscar empleado por RUT
                    rut = input("Ingrese el RUT del empleado a buscar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.4":
                    # Código para modificar empleado
                    rut = input("Ingrese el RUT del empleado a modificar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        nombre = input("Ingrese el nuevo nombre del empleado: ")
                        direccion = input("Ingrese la nueva dirección del empleado: ")
                        telefono = input("Ingrese el nuevo teléfono del empleado: ")
                        email = input("Ingrese el nuevo email del empleado: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
                        salario = float(input("Ingrese el nuevo salario del empleado: "))
                        departamento_id = int(input("Ingrese el nuevo ID del departamento: "))

                        empleado_modificado = Empleado(
                            id=empleado[0],
                            rut=rut,
                            nombre=nombre,
                            direccion=direccion,
                            telefono=telefono,
                            email=email,
                            fecha_inicio=fecha_inicio,
                            salario=salario,
                            departamento_id=departamento_id
                        )
                        
                        empleado_controller.modificar_empleado(empleado_modificado)
                        print("Empleado modificado exitosamente.")
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.5":
                    # Código para eliminar empleado
                    rut = input("Ingrese el RUT del empleado a eliminar: ")
                    empleado_controller.eliminar_empleado(rut)
                    print("Empleado eliminado exitosamente.")

                elif sub_opcion == "1.6":
                    break

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()
"""





"""# main.py
from views.menu import menu_principal, menu_empleado
from controllers.empleado_controller import EmpleadoController
from models.empleado import Empleado

db_config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'gestionproyectos'
}

empleado_controller = EmpleadoController(db_config)

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1.1":
                    # Código para crear empleado
                    pass
                elif sub_opcion == "1.2":
                    # Código para listar empleados
                    empleados = empleado_controller.listar_empleados()
                    for empleado in empleados:
                        print(empleado)
                elif sub_opcion == "1.6":
                    break
                # Agregar más casos para otras opciones
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()
"""