import pyautogui

if __name__ == "__main__":
  pyautogui.moveTo(500, 500, duration = 1)
  i = 0
  while i == 0:
      pyautogui.moveRel(50, 0, duration = .01)
      pyautogui.moveRel(-50, 0, duration = .01)
  print("This is happening")
