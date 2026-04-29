---
layout: default
title: Geospatial Data Mini Project
---
# Geospatial Data Mini Project
In this project, I received the timestamped location data of Professor Wirfs-Brock during her first visit too Whitman College. I attempted to determine if her locations followed a routine. To do this, I clustered her location data. Then, I created a map of her location data in which each point was color coded by time of day, and labled with her location's cluster. If her location data was perfectly routine, then every point at similar times (with similar colors) would be in the same location cluster. If her location data did not follow a routine, then points with similar colors would be in different location clusters. This map is below. 

<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/PWB_Locations" 
  width="600" 
  height="400">
</iframe>

The timestamps are likely not in PST because, if they were, Professor Wirfs-Brock would be in the Science Building at 1am, and most of her time on Whitman's campus would be late and night. However, I can still draw conclusions about her routine using these timestamps.

If Professor Wirfs-Brock completely followed a routine, then all dots of similar color (excluding the ones near the airport) would be in the same geographic cluster. This is true for some colors, but not for others.

For example, all blue to light orange points (from about 10:00am to 4pm) are in cluster 8, which is near the Marcus Whitman Hotel. This is part of a consistent routine.

However, dark blue points (from around 1:30 am to 3am) are in clusters 6,7, and 8. This time frame is not as dictated by routine.

My conclusion is that some times of day were more governed by routine than others.
