import bpy

class TestOperatorOperator(bpy.types.Operator):
    bl_idname = "object.test_operator"
    bl_label = "Test Operator"

    def execute(self, context):
        self.report({'INFO'}, f"オペレータ『{self.bl_idname}』を実行しました")
        
        return {"FINISHED"}