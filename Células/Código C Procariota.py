import bpy
Objetivo = "Núcleo"

def MostrarCromosomas(self, context):
    Objetivo = "Cromosomas"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarCitoplasma(self, context):
    Objetivo = "Citoplasma"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarCápsula(self, context):
    Objetivo = "Cápsula"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)


def MostrarFlajelo(self, context):
    Objetivo = "Flajelo"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarFímbrias(self, context):
    Objetivo = "Fímbrias"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarParedcelular(self, context):
    Objetivo = "Pared celular"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarPlásmidos(self, context):
    Objetivo = "Plásmidos"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarRibosoma(self, context):
    Objetivo = "Ribosoma"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarMembrana(self, context):
    Objetivo = "Membrana plasmática"
    for obj in bpy.data.objects:
        obj.hide_set(True)
    Mostrado = bpy.data.objects.get(Objetivo)
    Cito = bpy.data.objects.get("Citoplasma")
    Sol = bpy.data.objects.get("Sun")
    if Mostrado:
        Mostrado.hide_set(False)
        Cito.hide_set(False)
        Sol.hide_set(False)

def MostrarTodo(self, context):
    for obj in bpy.data.objects:
        obj.hide_set(False)

def OcultarPared(self, context):
    Pared = bpy.data.objects.get("Pared celular")
    Membrana = bpy.data.objects.get("Membrana plasmática")
    Capsula = bpy.data.objects.get("Cápsula")
    if Pared:
        Pared.hide_set(True)
    if Membrana:
        Membrana.hide_set(True)
    if Capsula:
        Capsula.hide_set(True)

class Panel_explicativo(bpy.types.Panel):
    bl_label = "Seleciona para la explicación"
    bl_idname = "OBJECT_PT_cubos"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Botones'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.mtodo", text="Mostrar todo")
        layout.operator("object.opared", text="Ocultar pared celular, membrana plasmática y cápsula")
        layout.operator("object.mye_flajelo", text="Flajelo")
        layout.operator("object.mye_fimbrias", text="fímbrias")
        layout.operator("object.mye_capsula", text="Cápsula")
        layout.operator("object.mye_paredcelular", text="Pared celular")
        layout.operator("object.mye_mplasmatica", text="Membrana plasmática")
        layout.operator("object.mye_citoplasma", text="Citoplasma")
        layout.operator("object.mye_cromosomas", text="Cromosomas")
        layout.operator("object.mye_plasmidos", text="Plásmidos")
        layout.operator("object.mye_rimosoma", text="Ribosoma")

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

    
class OBJECT_OT_Citoplasma(bpy.types.Operator):
    bl_idname = "object.mye_citoplasma"
    bl_label = "Citoplasma"

    def execute(self, context):
        MostrarCitoplasma(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Cromosomas(bpy.types.Operator):
    bl_idname = "object.mye_cromosomas"
    bl_label = "Cromosomas"

    def execute(self, context):
        MostrarCromosomas(self, context)
        return {'FINISHED'}

class OBJECT_OT_Flajelo(bpy.types.Operator):
    bl_idname = "object.mye_flajelo"
    bl_label = "Flajelo"

    def execute(self, context):
        MostrarFlajelo(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Fimbrias(bpy.types.Operator):
    bl_idname = "object.mye_fimbrias"
    bl_label = "Fímbrias"

    def execute(self, context):
        MostrarFímbrias(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Plasmidos(bpy.types.Operator):
    bl_idname = "object.mye_plasmidos"
    bl_label = "Plasmidos"

    def execute(self, context):
        MostrarPlásmidos(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Paredcelular(bpy.types.Operator):
    bl_idname = "object.mye_paredcelular"
    bl_label = "Pared celular"

    def execute(self, context):
        MostrarParedcelular(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_MembranaPasmatica(bpy.types.Operator):
    bl_idname = "object.mye_mplasmatica"
    bl_label = "Membrana plasmática"

    def execute(self, context):
        MostrarMembrana(self, context)
        return {'FINISHED'}

class OBJECT_OT_Rimosomas(bpy.types.Operator):
    bl_idname = "object.mye_rimosoma"
    bl_label = "Rimosomas"

    def execute(self, context):
        MostrarRibosoma(self, context)
        return {'FINISHED'}
    
class OBJECT_OT_Capsula(bpy.types.Operator):
    bl_idname = "object.mye_capsula"
    bl_label = "Cápsula"

    def execute(self, context):
        MostrarCápsula(self, context)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(OBJECT_OT_Cromosomas)
    bpy.utils.register_class(OBJECT_OT_MembranaPasmatica)
    bpy.utils.register_class(OBJECT_OT_MostrarTodo)
    bpy.utils.register_class(OBJECT_OT_Citoplasma)
    bpy.utils.register_class(OBJECT_OT_OcultarPared)
    bpy.utils.register_class(OBJECT_OT_Fimbrias)
    bpy.utils.register_class(Panel_explicativo)
    bpy.utils.register_class(OBJECT_OT_Flajelo)
    bpy.utils.register_class(OBJECT_OT_Plasmidos)
    bpy.utils.register_class(OBJECT_OT_Rimosomas)
    bpy.utils.register_class(OBJECT_OT_Paredcelular)
    bpy.utils.register_class(OBJECT_OT_Capsula)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Cromosomas)
    bpy.utils.unregister_class(OBJECT_OT_MembranaPasmatica)
    bpy.utils.unregister_class(OBJECT_OT_MostrarTodo)
    bpy.utils.unregister_class(Panel_explicativo)
    bpy.utils.unregister_class(OBJECT_OT_Fimbrias)
    bpy.utils.unregister_class(OBJECT_OT_Flajelo)
    bpy.utils.unregister_class(OBJECT_OT_Plasmidos)
    bpy.utils.unregister_class(OBJECT_OT_Rimosomas)
    bpy.utils.unregister_class(OBJECT_OT_OcultarPared)
    bpy.utils.unregister_class(OBJECT_OT_Citoplasma)
    bpy.utils.unregister_class(OBJECT_OT_OcultarPared)
    bpy.utils.unregister_class(OBJECT_OT_Capsula)

if __name__ == "__main__":
    register()