bl_info = {
    'name': 'BS Modify Pivot',
    "author": "Bone-Studio - Juan Gea, RUben Begalov@gmail.com",
    'version': (1, 0, 5),
    'blender': (2, 80, 0),
    'location': 'Tools panel.',
    'description': 'Tool to modify pivot location and orientation.',
    'category': 'Object',
}

modulesNames = [
    'BSModifyPivotPanel',
    'BSModifyPivotCreate',
    'BSModifyPivotCommit',
    'BSResetPivotOrientation',
    'BSResetZeroLocation',
    'BSDeltaToTransform'
    ]

import sys
import importlib

modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)


def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()


def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()


if __name__ == "__main__":
    register()