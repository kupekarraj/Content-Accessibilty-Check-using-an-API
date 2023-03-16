#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import json
import requests
import requests


# In[ ]:


#API Key goes here
key='xxx'


# In[ ]:


#import file here
scorebuddy= pd.read_csv(r"/Users/rajkupekar/Desktop/scorebuddy_accessibility.csv")


# In[ ]:


blog_urls=scorebuddy["Blog_URLs"]


# In[ ]:


blog_url=[]
error_counts=[]
contrast_errors=[]
alert_errors=[]
feature_errors=[]
structure_errors=[]
aria_errors=[]
wave_urls=[]


# In[ ]:


for i in range(len(blog_urls)):
    response=requests.get("https://wave.webaim.org/api/request?key={}&url={}".format(key,blog_urls[i]))
    response_json=response.json()
    
    try:
        error_count= response_json["categories"]["error"]["count"]
        error_counts.append(error_count)
    except:
        error_counts.append("error_counts")
    
    try:
        contrast_error= response_json["categories"]["contrast"]["count"]
        contrast_errors.append(contrast_error)
    except:
        contrast_errors.append("contrast_errors")
    
    try:
        alert_error= response_json["categories"]["alert"]["count"]
        alert_errors.append(alert_error)
    except:
        alert_errors.append("alert_errors")
        
    try:
        feature_error= response_json["categories"]["feature"]["count"]
        feature_errors.append(feature_error)
    except:
        feature_errors.append("feature_errors")
        
    try:
        structure_error= response_json["categories"]["structure"]["count"]
        structure_errors.append(structure_error)
    except:
        structure_errors.append("structure_errors")
        
    try:
        aria_error= response_json["categories"]["aria"]["count"]
        aria_errors.append(aria_error)
    except:
        aria_errors.append("aria_errors")
        
    try:
        wave_url= response_json["statistics"]["waveurl"]
        wave_urls.append(wave_url)
    except:
        wave_urls.append("wave_urls")
        
    
    blog_url.append(blog_urls[i])
    
    print("Finished for ",blog_urls[i]," credit left ", response_json["statistics"]["creditsremaining"])
    
    
    


# In[ ]:


data = {
    "Blog_URL":blog_url,
    "error_counts": error_counts,
    "contrast_errors": contrast_errors,
    "alert_errors" : alert_errors,
    "feature_errors": feature_errors,
    "structure_errors": structure_errors,
    "aria_errors" : aria_errors,
    "wave_urls" : wave_urls
}

df = pd.DataFrame(data)


# In[ ]:


df.head(30)


# In[ ]:


df.to_csv(r'/Users/rajkupekar/Desktop/Scorebudyy_Accessibility.csv', encoding="UTF-8",index=False)

