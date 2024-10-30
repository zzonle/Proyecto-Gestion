import os
from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto, menu_registro_tiempo, menu_exportar_datos
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.registrotiempo_controller import RegistroTiempoController
from controllers.exportarexcel_controller import ExportarExcel
from models.empleado import Empleado
from models.departamento import Departamento
from models.proyecto import Proyecto
from models.registrotiempo import RegistroTiempo


empleado_controller = EmpleadoController()
departamento_controller = DepartamentoController()
proyecto_controller = ProyectoController()
registrotiempo_controller = RegistroTiempoController()
exportarexcel_controller = ExportarExcel() 

def main():
    while True:
        try:
            
            menu_principal()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                while True:
                    menu_empleado()
                    sub_opcion = input("Seleccione una opción: ")
                    
                    if sub_opcion == "1.1":
                        # Código para crear empleado
                        try:
                            while True:

                                    rut = input("Ingrese el RUT del empleado(Ingrese sin gion y sin puntos): ")
                                    if empleado_controller.validar_rut(rut):
                                        
                                        empleado_existente = empleado_controller.buscar_empleado_por_rut(rut)
                    
                                        if empleado_existente:
                                            print("RUT existente.")
                                            continue
                                        else:
                                            break
                            
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
                        except ValueError as ve:
                            print(f"Error de valor {ve}")
                        except Exception as e:
                            print(f"Ocurrió un error inesperado: {e}")

                    elif sub_opcion == "1.2":
                        # Código para listar empleados
                        empleados = empleado_controller.listar_empleados()
                        for emp in empleados:
                            print(emp)

                    elif sub_opcion == "1.3":
                        # Código para buscar empleado por RUT
                        while True:
                            try:
                                rut = input("Ingrese el RUT del empleado(Ingrese sin gion y sin puntos): ")
                                if empleado_controller.validar_rut(rut):
                                    
                                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                                    if empleado:
                                        print("Empleado encontrado: ")
                                        print(empleado)
                                    else:
                                        print("Empleado no encontrado.")
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")

                    elif sub_opcion == "1.4":
                        # Código para modificar empleado
                        try:
                            while True:

                                    rut = input("Ingrese el RUT del empleado(Ingrese sin gion y sin puntos): ")
                                    if empleado_controller.validar_rut(rut):
                                        
                                        empleado_existente = empleado_controller.buscar_empleado_por_rut(rut)
                    
                                        if empleado_existente:
                                            break
                                        else:
                                            print("Empleado no encontrado.")
                                            continue
                            
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
                        except ValueError as ve:
                            print(f"Error de valor {ve}")
                        except Exception as e:
                            print(f"Ocurrió un error inesperado: {e}")
                                    
                    elif sub_opcion == "1.5":
                        # Código para eliminar empleado
                        try:
                            while True:

                                    rut = input("Ingrese el RUT del empleado(Ingrese sin gion y sin puntos): ")
                                    if empleado_controller.validar_rut(rut):
                                        
                                        empleado_existente = empleado_controller.buscar_empleado_por_rut(rut)
                    
                                        if empleado_existente:
                                            empleado_controller.eliminar_empleado(rut)
                                            print("Empleado eliminado exitosamente.")
                                            break
                                        else:
                                            print("Empleado no encontrado.")
                                            continue
                        except Exception as e:
                            print(f"Ocurrió un error inesperado: {e}")

                    elif sub_opcion == "1.6":
                        break
                    
                    else:
                        print("Opción inválida.")
                        
            elif opcion == "2":
                while True:
                    menu_departamento()
                    sub_opcion = input("Seleccione una opción: ")
                    
                    if sub_opcion == "2.1":
                        while True:
                            try:
                                nombre = input("Ingrese el nombre del departamento: ")
                                if not nombre:
                                    print("El nombre del departamento no puede estar vacío.")
                                    continue
                                
                                gerente_id = input("Ingrese el ID del gerente (opcional): ")
                                gerente_id = int(gerente_id) if gerente_id else None

                                nuevo_departamento = Departamento(
                                                    nombre=nombre, 
                                                    gerente_id=gerente_id
                                                )
                                departamento_controller.crear_departamento(nuevo_departamento)
                                print("Departamento creado exitosamente.")
                                
                                break
                            
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del gerente debe ser un número entero.")

                    elif sub_opcion == "2.2":
                        departamentos = departamento_controller.listar_departamentos()
                        for dep in departamentos:
                            print(f"ID: {dep.id}, Nombre: {dep.nombre}")

                    elif sub_opcion == "2.3":
                        while True:
                            try:
                                id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                                departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                                if departamento:
                                    print(departamento)
                                else:
                                    print("Departamento no encontrado.")
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del departamento debe ser un número entero.") 
                                  
                    elif sub_opcion == "2.4":
                        while True:
                            try:
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
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del gerente debe ser un número entero.")

                    elif sub_opcion == "2.5":
                        while True:
                            try:
                                id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                                        
                                departamento_existente = departamento_controller.buscar_departamento_por_id(id_dep)
                    
                                if departamento_existente:
                                    departamento_controller.eliminar_departamento(id_dep)
                                    print("Departamento eliminado exitosamente.")
                                    break
                                else:
                                    print("Departamento no encontrado.")
                                    continue
                                    
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del departamento debe ser un número entero.")
                        
                    elif sub_opcion == "2.6":
                        break
                    
                    else:
                        print("Opción inválida.")
                        
            elif opcion == "3":
                while True:
                    menu_proyecto()
                    sub_opcion = input("Seleccione una opción: ")
                    
                    if sub_opcion == "3.1":
                        while True:
                            try:
                                nombre = input("Ingrese el nombre del proyecto: ")
                                descripcion = input("Ingrese la descripción del proyecto: ")
                                fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                                if not nombre or not fecha_inicio or not descripcion:
                                    print("Todos los campos son obligatorios.")
                                else:
                                    nuevo_proyecto = Proyecto(
                                        nombre = nombre,
                                        descripcion= descripcion,
                                        fecha_inicio= fecha_inicio
                                    )
                                    
                                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                                    print("Proyecto creado exitosamente.")
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                    
                    elif sub_opcion == "3.2":
                        while True:
                            try:
                                id = int(input("Ingrese la ID del proyecto a buscar: "))
                                proyecto = proyecto_controller.buscar_proyecto_por_id(id)
                                if proyecto:
                                    print(proyecto)
                                else:
                                    print("Proyecto no encontrado.")
                                    
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del proyecto debe ser un número entero.")
                    
                    elif sub_opcion == "3.3":
                        while True:
                            try:
                                id = int(input("Ingrese la ID del proyecto a modificar: "))
                                
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
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del proyecto debe ser un número entero.")
                    
                    elif sub_opcion == "3.4":
                        while True:
                            try:
                                    id = int(input("Ingrese la ID del proyecto a eliminar:"))
                                    
                                        
                                    proyecto_existente = proyecto_controller.eliminar_proyecto(id)
                    
                                    if proyecto_existente:
                                        proyecto_controller.eliminar_proyecto(id)
                                        print("Proyecto eliminado exitosamente.")  
                                        break
                                    else:
                                        print("Proyecto no encontrado.")
                                        continue
                                    
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del proyecto debe ser un número entero.")                   
                    
                    elif sub_opcion == "3.5":
                        while True:
                            try:
                                empleado_id = int(input("Ingrese la ID del empleado para agregar al proyecto: "))
                                proyecto_id = int(input("Ingrese la ID del proyecto: "))
                                
                                empleado_existentes = empleado_controller.buscar_empleado_por_id(empleado_id)
                                proyecto_existente = proyecto_controller.buscar_proyecto_por_id(proyecto_id)
                                if empleado_existentes and proyecto_existente:
                                    proyectoempleado = proyecto_controller.agregar_empleado_proyecto(proyecto_id , empleado_id)
                                    
                                    if proyectoempleado is None:
                                        print("Empleado agregado al proyecto exitosamente.")
                                    else:
                                        print("Empleado o proyecto no encontrados.")
                                else:
                                    if not empleado_existentes:
                                        print("Empleado no encontrado.")
                    
                                    if not proyecto_existente:
                                        print("Proyecto no encontrado.")
                                        
                                     
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}") 
                            except ValueError:
                                print("Los IDs deben ser números enteros.")
                    
                    elif sub_opcion == "3.6":
                        
                        while True:
                            try:
                                proyecto_id = int(input("Ingrese la ID del proyecto: "))
                                empleado_id = int(input("Ingrese la ID del empleado a eliminar del proyecto: "))
                                
                                empleado_existentes = empleado_controller.buscar_empleado_por_id(empleado_id)
                                proyecto_existente = proyecto_controller.buscar_proyecto_por_id(proyecto_id)
                                
                                if empleado_existentes and proyecto_existente:
                                    
                                    proyecto_controller.eliminar_empleado_proyecto(proyecto_id, empleado_id)
                                    print("Empleado eliminado del proyecto exitosamente.") 
                                    break 
                                                                      
                                        
                                else:
                                    if not empleado_existentes:
                                        print("Empleado no encontrado.")
                                        
                                    if not proyecto_existente:
                                        print("Proyecto no encontrado.")
                                        
                                     
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}") 
                            except ValueError:
                                print("Los IDs deben ser números enteros.")         
                    
                    elif sub_opcion == "3.7":
                        while True:
                            try:
                                proyecto_id = int(input("Ingrese la ID del proyecto para buscar los empleados: "))
                                proyecto_existente = proyecto_controller.buscar_proyecto_por_id(proyecto_id)
                                
                                if proyecto_existente:
                                    empleados_proyecto = proyecto_controller.listar_empleados_proyecto(proyecto_id)
                                    print("Empleados del proyecto:")
                                    if empleados_proyecto:
                                        for empleado in empleados_proyecto:
                                            print(empleado)
                                    else:
                                        print("No hay empleados asigandos a este proyecto.")
                                else:
                                    print("Proyecto no encontrado.")
                                
                                break
                                
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del proyecto debe ser un número entero.")
                            
                    elif sub_opcion == "3.8":
                        break
                    
                    else:
                        print("Opción inválida.")
                        
            elif opcion == "4":
                while True:
                    menu_registro_tiempo()
                    sub_opcion = input("Seleccione una opción: ")             

                    if sub_opcion == "4.1":
                        while True:
                            try:
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
                                
                                if registrotiempo_controller.crear_registro(nuevo_registro):
                                    print("Registro creado exitosamente.")
                                else:
                                    print("Error al crear el registro.")
                                
                                break
                                               
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("Los valores ingresados no son válidos.")
                            
                    elif sub_opcion == "4.2":
                        registros = registrotiempo_controller.listar_registro()
                        if registros:
                            print("Lista de registros de tiempo:")
                            for registro in registros:
                                print("-" * 30)
                                print(f"ID: {registro[0]}")
                                print(f"Fecha de Inicio: {registro[1]}")
                                print(f"Horas Trabajadas: {registro[2]}")
                                print(f"Descripción: {registro[3]}")
                                print(f"ID Empleado: {registro[4]}")
                                print(f"ID Proyecto: {registro[5]}") 
                        else:
                            print("No hay registros de tiempo disponibles.")
                 
                    elif sub_opcion == "4.3":
                        
                        try:
                            registro_id = int(input("Ingrese el ID del registro a buscar: "))
                        except ValueError:
                            print("El ID ingresado debe ser un número entero.")
                        else:
                            registro = registrotiempo_controller.buscar_registro(registro_id)
                            
                            if registro:
                                if isinstance(registro, tuple):
                                    print(f"ID: {registro[0]}")
                                    print(f"Fecha de Inicio: {registro[1]}")
                                    print(f"Horas Trabajadas: {registro[2]}")
                                    print(f"Descripción: {registro[3]}")
                                    print(f"ID Empleado: {registro[4]}")
                                    print(f"ID Proyecto: {registro[5]}")
                            else:
                                print("Registro no encontrado.")        
                    
                    elif sub_opcion == "4.4":
                        while True:
                            try:
                                registro_id = int(input("Ingrese la ID del registro a modificar: "))
                                if registrotiempo_controller.buscar_registro_id(registro_id):
                        
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
                                    break
                                else:
                                    print("Registro no encontrado.")
                                    
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("Los valores ingresados no son válidos.")
                    
                    elif sub_opcion == "4.5":
                        while True:
                            try:
                                    id = int(input("Ingrese el ID del registro a eliminar: "))
                                    
                                        
                                    registro_existente = registrotiempo_controller.buscar_registro(id)
                    
                                    if registro_existente:
                                        registrotiempo_controller.eliminar_proyecto(id)
                                        print("Proyecto eliminado exitosamente.")  
                                        break
                                    else:
                                        print("Proyecto no encontrado.")
                                        continue
                                    
                            except Exception as e:
                                print(f"Ocurrió un error inesperado: {e}")
                            except ValueError:
                                print("El ID del proyecto debe ser un número entero.") 
                    
                    elif sub_opcion == "4.6":
                        
                        break
                    
                    else:
                        print("Opción inválida.")
                                
            elif opcion == "5":
                while True:
                    menu_exportar_datos()
                    sub_opcion = input("Seleccione una opción: ")
                    
                    if sub_opcion == "5.1":
                        try:
                            if not os.path.exists('Informes'):
                                os.makedirs('Informes')
                        
                            df = exportarexcel_controller.exportar()
                            nombre_informe = input("Ingrese nombre al informe: \n")
                            df.to_excel(f'Informes/{nombre_informe}.xlsx', index = False)
                            print("Informes genereado exitosamente.")
                        except Exception as e:
                            print(f"Ocurrió un error al generar el informe: {e}")
                                    
                    elif sub_opcion == "5.2":
                        break
            elif opcion == "6":
                print("Saliendo del sistema...")
                break     
            else:
                print("Opción inválida.")
        
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo...")
            break
if __name__ == "__main__":
    main()