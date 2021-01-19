def run():
  import PySimpleGUI as sg
  import shutil

  sg.theme('dark grey 9')

  layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Start Uninstalling'), sg.Button('Cancel')]]

  window = sg.Window('Uninstaller', layout)
  event, values = window.read()

  while True:

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
      window.close()
      break

    if event == 'Start Uninstalling':
      window['-OUTPUT-'].update("Starting the Uninstallation...")
      shutil.rmtree("Downloads")
      shutil.rmtree("Scripts")
      os.remove("Hub.py")
      window['-OUTPUT-'].update("Done Uninstallaling")
      window.close()
      break
