#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from geopy.geocoders import Nominatim
# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")
#Zipocde input
a = input ("Enter the zipcode:")
zipcode = a
# Using geocode()
location = geolocator.geocode(zipcode)
# Displaying address details
print ("Zipcode:",zipcode)
print ("Details of the Zipcode:")
print(location)

