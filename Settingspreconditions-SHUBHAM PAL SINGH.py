#!/usr/bin/env python
# coding: utf-8

# import uiautomator2 as u2
# import time
# d=u2.connect('4309fc4a')
# d.unlock()

# In[2]:


import uiautomator2 as u2
import time
d=u2.connect('e636f294')
d.unlock()
d.unlock()
import time
d.screen_on()
#main--------------------------------------------


# In[3]:


#-------------------------------------------Skiping Setupwizard------------------------------
## To skip Setupwizard
d(className="android.widget.LinearLayout",resourceId="com.oneplus.setupwizard:id/emergency_icon").click()
d(text="*").click()
d(text="#").click()
d(text="3").click()
d(text="6").click()
d(text="8").click()
d(text="#").click()


# In[5]:


#-----------------------------------------Wifi Settings----------------------------------
## To connect Wifi
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d(text="Wi-Fi & Network").click()
d(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view").child(className="android.widget.LinearLayout")[1].child(className="android.widget.LinearLayout")[0].click()
d(text="OnePlus Guest").click()
d(className="android.widget.EditText",resourceId="com.android.settings:id/password").set_text("1+NeverSettle")
d.press("enter")
time.sleep(3)
d.press('recent')
d(text="Clear All").click()


# In[7]:


#------------------------------------Bluetooth Settings-------------------------
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d(text="Bluetooth & Device Connection").click()
d(text="NFC").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[8]:


#-----------------------------------------------Security Settings------------------------------------------
## To security lock to None
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d.press('down')
d(text="Security & Lock Screen").click()
d(text="Lockscreen passcode").click()
d(text="None").click()
time.sleep(4)
d.press('home')
d.press('recent')
d(text="Clear All").click()


# In[16]:


#-------------------------------------------------Display Settings-------------------------------------------
## To security lock to None
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d.press('down')
d(text="Security & Lock Screen").click()
d(text="Lockscreen Passcode").click()
d(text="None").click()
time.sleep(4)
d.press('home')
d.press('recent')
d(text="Clear All").click()


# In[20]:


#-------------------------------------------------Display Settings-------------------------------------------
## To keep Sleep mode after 30mins
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d(text="Display").click()
d(text="Sleep").click()
d(text="30 minutes").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[14]:


## To turn off Adaptive Brightness
d(text="Adaptive Brightness").click()
time.sleep(2)
## to turn off Ambient Display
d.press('down')
d.press('down')
d(text="Ambient Display").click()
d(text="On").click()
time.sleep(4)
d.press('recent')
d(text="Clear All").click()


# In[21]:


#------------------------------------------Sound and vibration settings----------------------
## To turn off Touch Vibration
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d(text="Sounds & Vibration").click()
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d(text="Touch Vibration").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[22]:


#-----------------------------------------Buttons and Guestures-------------------------------------
## To turn off the double tap guesture
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d.press('down')
d(text="Buttons & Gestures").click()
d(text="Quick Gestures").click()
d(text="Double Tap to Wake").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[25]:


#-----------------------------------------Account Settings--------------------
## To turn off Automatically sync App data
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d(text="Accounts").click()
d(text="Automatically sync app data").click()
time.sleep(1)
d(text="OK").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[26]:


#---------------------------------------------Utilities Settings
## To Turn off Pocket Mode
time.sleep(2)
d.open_quick_settings()
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d(text="Utilities").click()
d(text="Pocket Mode").click()
time.sleep(2)
d.press('recent')
d(text="Clear All").click()


# In[ ]:




