from pynput.keyboard import Key,Controller
import time
import Audio
import strlists
import os
import engine
import pyautogui

def typein():
    try:
        while 1:
            text = Audio.get_audio()
            k=Controller()

            if text in strlists.VOICETYPING_KEYPRESSES_STR:
                for phrase in strlists.VOICETYPING_KEYPRESSES_STR:
                    
                    if "select all" in text:
                        pyautogui.hotkey('ctrl','a')
                    elif "undo" in text:
                        pyautogui.hotkey('ctrl','z')
                    elif "redo" in text:
                        pyautogui.hotkey('ctrl','y')
                    elif "copy" in text:
                        pyautogui.hotkey('ctrl','c')
                    elif "paste" in text:
                        pyautogui.hotkey('ctrl','v')
                    elif "italic" in text:
                        pyautogui.hotkey('ctrl','i')
                    elif "cut" in text:
                        pyautogui.hotkey('ctrl','x')
                        pass

                    elif phrase in text:
                        pyautogui.press(phrase)
                    
            
            
            elif 'switch off voice typing' in text:
                engine.speak("getting out of voice typing master")
                time.sleep(2)
                break

            else:
                k.type(text)
                continue


                        
                        
    
    
    except:
        engine.speak("something went wrong master!!")

        