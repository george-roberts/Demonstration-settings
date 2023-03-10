#Author-
#Description-
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        app.executeTextCommand('NuCommands.ViewEnvironmentCmd ViewEnvPhotoBoothCommand')
        app.executeTextCommand('NuCommands.ViewDomeCmd ViewDomeOffCommand')
        app.executeTextCommand('NuCommands.ViewVisualStyleCmd ViewVisualStyleShadedWithEdgesHLR')
        app.executeTextCommand('NuCommands.ViewGroundShadowCmd ViewGroundShadowOffCommand')
        app.executeTextCommand('NuCommands.ViewGroundReflectionCmd ViewGroundReflectionOffCommand')
        app.executeTextCommand('NuCommands.ViewGroundPlaneCmd ViewGroundPlaneOffCommand')
        app.executeTextCommand('NuCommands.ViewObjectShadowCmd ViewObjectShadowSoft2Command')
        app.executeTextCommand('NuCommands.ViewAmbientOcclusionCmd ViewAmbientOcclusionOnCommand')
        app.executeTextCommand('NuCommands.ViewCameraCmd ViewCameraPerspWithOrthoFacesCommand')
        app.executeTextCommand('options.set HealthStatusVisibility 2')
        app.executeTextCommand('NuCommands.ViewLayoutGridOnCmd ViewLayoutGridOffCommand')        
        app.executeTextCommand('NuCommands.ShowWorkspaceFullScreenCmd')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
