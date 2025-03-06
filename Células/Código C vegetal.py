import bpy
Objetivo = "Núcleo"
Explicación = "TNúcleo"

def MostrarNucleo(self, context):
    Objetivo = "Núcleo"
    Explicación = "TNucleo"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarCitoplasma(self, context):
    Objetivo = "Citoplasma"
    Explicación = "TCitoplasma"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarParedcelular(self, context):
    Objetivo = "Pared vegetal"
    Explicación = "TPared vegetal"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)


def MostrarReticula(self, context):
    Objetivo = "Reticulo endoplasmático"
    Explicación = "TReticulo endoplasmático"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarVacuola(self, context):
    Objetivo = "Vacuola"
    Explicación = "TVacuola"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarMitocondrias(self, context):
    Objetivo = "Mitocondrias"
    Explicación = "TMitocondrias"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def Mostrarlisosomas(self, context):
    Objetivo = "Lisosomas"
    Explicación = "TLisosomas"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarCloroplastos(self, context):
    Objetivo = "Cloroplastos"
    Explicación = "TCloroplastos"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarAparato(self, context):
    Objetivo = "Aparato de Golgi"
    Explicación = "Aparato de Golgi"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarMembrana(self, context):
    Objetivo = "Membrana plasmática"
    Explicación = "TMembrana plasmática"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    TExplicación = bpy.data.objects.text.get(Explicación)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        TExplicación.hide.set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarTodo(self, context):
    for obj in bpy.data.objects:
        obj.hide_set(False)

def OcultarPared(self, context):
    Pared = bpy.data.objects.get("Pared vegetal")
    Membrana = bpy.data.objects.get("Membrana plasmática")
    if Pared:
        Pared.hide_set(True)
    if Membrana:
        Membrana.hide_set(True)

class Panel_explicativo(bpy.types.Panel):
    bl_label = "Seleciona para la explicación"
    bl_idname = "OBJECT_PT_cubos"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Botones'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.mtodo", text="Mostrar todo")
        layout.operator("object.opared", text="Ocultar pared celular, y membrana plasmática")
        layout.operator("object.mye_pared_celular", text="Pared celular")
        layout.operator("object.mye_mplasmatica", text="Membrana plasmática")
        layout.operator("object.mye_citoplasma", text="Citoplasma")
        layout.operator("object.mye_nucleo", text="Núcleo")
        layout.operator("object.mye_reticulo", text="Retículo endoplasmático")
        layout.operator("object.mye_vacuola", text="Vacuola")
        layout.operator("object.mye_mitocondrias", text="Mitocondrias")
        layout.operator("object.mye_lisososmas", text="Lisosomas")
        layout.operator("object.mye_cloroplastos", text="Cloroplastos")
        layout.operator("object.mye_aparato_de_Golgi", text="Aparato de Golgi")

class OBJECT_OT_MostrarTodo(bpy.types.Operator):
    bl_idname = "object.mtodo"
    bl_label = "Mostrar todo"

    def execute(self, context):
        MostrarTodo(self, context)
        return {'FINISHED'}        

class OBJECT_OT_OcultarPared(bpy.types.Operator):
    bl_idname = "object.opared"
    bl_label = "Ocultar pared celular, y membrana plasmática"

    def execute(self, context):
        OcultarPared(self, context)
        return {'FINISHED'}     

class OBJECT_OT_Nucleo(bpy.types.Operator):
    bl_idname = "object.mye_nucleo"
    bl_label = "Núcleo"

    def execute(self, context,):
        MostrarNucleo(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Citoplasma(bpy.types.Operator):
    bl_idname = "object.mye_citoplasma"
    bl_label = "Citoplasma"
    def execute(self, context):
        MostrarCitoplasma(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_ParedCelular(bpy.types.Operator):
    bl_idname = "object.mye_pared_celular"
    bl_label = "Pared celular"

    def execute(self, context):
        MostrarParedcelular(self, context)
        return {'FINISHED'}

class OBJECT_OT_Reticulo_endoplasmatico(bpy.types.Operator):
    bl_idname = "object.mye_reticulo"
    bl_label = "Retículo endoplasmático"

    def execute(self, context):
        MostrarReticula(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Vacuola(bpy.types.Operator):
    bl_idname = "object.mye_vacuola"
    bl_label = "Vacuola"

    def execute(self, context):
        MostrarVacuola(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Mitocondrias(bpy.types.Operator):
    bl_idname = "object.mye_mitocondrias"
    bl_label = "Mitocondrias"

    def execute(self, context):
        MostrarMitocondrias(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Lisososmas(bpy.types.Operator):
    bl_idname = "object.mye_lisososmas"
    bl_label = "Lisosomas"

    def execute(self, context):
        Mostrarlisosomas(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_MembranaPasmatica(bpy.types.Operator):
    bl_idname = "object.mye_mplasmatica"
    bl_label = "Membrana plasmática"

    def execute(self, context):
        MostrarMembrana(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Cloroplastos(bpy.types.Operator):
    bl_idname = "object.mye_cloroplastos"
    bl_label = "Cloroplastos"

    def execute(self, context):
        MostrarCloroplastos(self, context)
        return {'FINISHED'}

class OBJECT_OT_Aparato(bpy.types.Operator):
    bl_idname = "object.mye_aparato_de_golgi"
    bl_label = "Aparato de Golgi"

    def execute(self, context):
        MostrarAparato(self, context)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(OBJECT_OT_Nucleo)
    bpy.utils.register_class(OBJECT_OT_MembranaPasmatica)
    bpy.utils.register_class(OBJECT_OT_MostrarTodo)
    bpy.utils.register_class(OBJECT_OT_Citoplasma)
    bpy.utils.register_class(OBJECT_OT_OcultarPared)
    bpy.utils.register_class(OBJECT_OT_ParedCelular)
    bpy.utils.register_class(Panel_explicativo)
    bpy.utils.register_class(OBJECT_OT_Vacuola)
    bpy.utils.register_class(OBJECT_OT_Reticulo_endoplasmatico)
    bpy.utils.register_class(OBJECT_OT_Mitocondrias)
    bpy.utils.register_class(OBJECT_OT_Aparato)
    bpy.utils.register_class(OBJECT_OT_Lisososmas)
    bpy.utils.register_class(OBJECT_OT_Cloroplastos)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Nucleo)
    bpy.utils.unregister_class(OBJECT_OT_MembranaPasmatica)
    bpy.utils.unregister_class(OBJECT_OT_MostrarTodo)
    bpy.utils.unregister_class(Panel_explicativo)
    bpy.utils.unregister_class(OBJECT_OT_Vacuola)
    bpy.utils.unregister_class(OBJECT_OT_Reticulo_endoplasmatico)
    bpy.utils.unregister_class(OBJECT_OT_Mitocondrias)
    bpy.utils.unregister_class(OBJECT_OT_Aparato)
    bpy.utils.unregister_class(OBJECT_OT_Lisososmas)
    bpy.utils.unregister_class(OBJECT_OT_Cloroplastos)
    bpy.utils.unregister_class(OBJECT_OT_Citoplasma)
    bpy.utils.unregister_class(OBJECT_OT_OcultarPared)
    bpy.utils.unregister_class(OBJECT_OT_ParedCelular)


if __name__ == "__main__":
    register()