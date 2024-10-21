from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto, menu_registro_tiempo
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.registrotiempo_controller import RegistroTiempoController
from models.empleado import Empleado
from models.departamento import Departamento
from models.proyecto import Proyecto
from models.registrotiempo import RegistroTiempo


empleado_controller = EmpleadoController()
departamento_controller = DepartamentoController()
proyecto_controller = ProyectoController()
registrotiempo_controller = RegistroTiempoController()

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
                    print("Proyecto eliminado exitosamente.")                    
                elif sub_opcion == "3.5":
                    empleado_id = input("Ingrese la ID del empleado para agregar al proyecto: ")
                    proyecto_id = input("Ingrese la ID del proyecto: ")
                    
                    proyectoempleado = proyecto_controller.agregar_empleado_proyecto(proyecto_id , empleado_id)
                    
                    if proyectoempleado:
                        print("Empleado o proyecto no encontrados.")
                    else:
                        print("Empleado agregado al proyecto exitosamente.")     
                elif sub_opcion == "3.6":
                    proyecto_id = int(input("Ingrese la ID del proyecto: "))
                    empleado_id = int(input("Ingrese la ID del empleado a eliminar del proyecto: "))
                    
                    proyecto_controller.eliminar_empleado_proyecto(proyecto_id, empleado_id)
                    print("Empleado eliminado del proyecto exitosamente.")           
                elif sub_opcion == "3.7":
                    proyecto_id = input("Ingrese la ID del proyecto para buscar los empleados: ")
                    
                    empleados_proyecto = proyecto_controller.listar_empleados_proyecto(proyecto_id)
                    print("Empleados del proyecto:")
                    print(empleados_proyecto)
                elif sub_opcion == "3.8":
                    break
        elif opcion == "4":
            while True:
                menu_registro_tiempo()
                sub_opcion = input("Seleccione una opción: ")             

                if sub_opcion == "4.1":
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    horas_trabajadas = float(input("Ingrese las horas trabajadas en (HH-MM-SS): "))
                    descripcion = input("Ingrese la descripción del registro: ")
                    empleado_id = input("Ingrese la ID del empleado: ")
                    proyecto_id = input("Ingrese la ID del proyecto: ")
                    
                    nuevo_registro = RegistroTiempo(
                        fecha_inicio=fecha_inicio,
                        horas_trabajadas=horas_trabajadas,
                        descripcion=descripcion,
                        empleado_id=empleado_id,
                        proyecto_id=proyecto_id
                    )
                    registrotiempo_controller.crear_registro(nuevo_registro)
                    if nuevo_registro:
                        print("Registro creado exitosamente.")
                    else:
                        print("Error al crear el registro.")                   
                elif sub_opcion == "4.2":
                    registros = registrotiempo_controller.listar_registro()
                    for registro in registros:
                        print(registro)                  
                elif sub_opcion == "4.3":
                    registro_id = input("Ingrese el ID del registro a buscar: ")
                    registro = registrotiempo_controller.buscar_registro(registro_id)
                    if registro:
                        print(registro)
                    else:
                        print("Registro no encontrado.")           
                elif sub_opcion == "4.4":
                    registro_id = input("Ingrese la ID del registro a modificar: ")
                    fecha = input("Ingrese la fecha a modificar: ")
                    proyecto_id = input("Ingrese la ID del proyecto: ")
                    empleado_id = input("Ingrese la ID del empleado: ")
                    descripcion = input("Descripcion del registro: ")
                    hora = float(input("Ingrese la horas del registro: "))
                    
                    registro_modificado = RegistroTiempo(
                        id=registro_id,
                        fecha_inicio=fecha,
                        horas_trabajadas=hora,
                        descripcion=descripcion,
                        empleado_id=empleado_id,
                        proyecto_id=proyecto_id
                        )
                    registrotiempo_controller.modificar_registro(registro_modificado)
                    if registro_modificado:
                        print("Registro modificado exitosamente.")
                    else:
                        print("Registro no modificado.")
                elif sub_opcion == "4.5":
                    id = input("Ingrese el ID del registro a eliminar: ")
                    
                    if registrotiempo_controller.eliminar_registro(id):
                        print("Registro no eliominado.")
                    else:
                        print("Registro eliminado exitosamente.")
                elif sub_opcion == "4.6":
                    break
                
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()