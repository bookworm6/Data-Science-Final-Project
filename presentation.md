---
layout: default
title: Final Project Presentation
---
# An Analysis of the Balance Between Sexes Across Subjects at Whitman College
## Background 
### Motivation
I was one of three girls in my high school computer science class, so a gender gap in computer science felt normal (though not good) to me. I expected that I would experience a similar overwhelmingly large gender gap in computer science in college, so I was surprised to discover that, though my computer science classes are still male dominated, the difference at Whitman does not feel as large as it did in high school. I am doing this project because I wanted to know how my experience fit into larger patterns of gender gaps over time. However, the insitutional data collected by Whitman documents biological sex. This led me to analyze the balance between biological sexes in various departments at Whitman.

### Questions
* How have Whitman's overall demographics changed overtime?
* In which departments is the balance between the sexes least representative of Whitman's overall demographics?
* How have the gaps in representation of the sexes in various subjects changed overtime?
* How does the tepresentation of sexes in a major At whitman relate to the national median mid-career salary of that major?

### A Note About Data
##### Whitman Institutional Data
Most of my data came from Whitman College's office of institutional research and described the demographics of students taking classes across various subjects. However, this data does not include information about the gender of students, just their biological sex. So, I had to analyse the biological sex of students. The options are as follows:
* M: Male
* F: Female
* U: Unknown (This is mostly non degree seeking students)

Similarly, the data on "Race/Ethnicity" categorizes students broadly one of the following:
* White
* Student of Color
* International
* Unknown
Because these categories are so broad and reductive, I have de emphasized race and ethnicity in my analysis. However, if you are interested, options to show data on race and ethnicity exist in most visualizations.

I beleive strongly is transparency, but I can not publish Whitman's instutional data in a non agregated form. So, I will be explicit about all decisions I make that excludes data or removes detail from the data.  

##### National Salary Data By Major
Data on national mid career median salaries by major came from the [Wall Street Journal](https://www.wsj.com/public/resources/documents/info-Degrees_that_Pay_you_Back-sort.html). Though I could not find metadata, I think that this data is quite old. I manually mapped its major names onto Whitman's departments, and you can view the pairs [here](https://bookworm6.github.io/Data-Science-Final-Project/codesToMajorNames). Not all of Whitman's departments correspond to majors with salary data. 

### Defining the Term "Sex Gap"
I have data about biological sex, but not gender. So, I am analyzing the blanace between the sexes in subjects in relation to Whitman's overall demographics. I am calling the difference between the balance between the sexes in a subject and in Whitman as a whole, the "sex gap," and I will use this (made up) term thoughout. 

### What Do I Mean When I Say "Percent Over/Under Represented"?
Members of a demographic group fill some percentage of Whitman's total number of class seats every semester. That means that, in the "average" class at Whitman, the demographic group would fill a percentage of seats equal to the percentage of class seats they fill at Whitman. 

Percent Over/Under Represented = the percentage of seats a demographic group fills in a class - the percentage of seats they would fill in the "average" class at Whitman. 

If this value is negative, the demographic group is under represented. If this value is positive, the demographic group is over represented. 

### Interactive Graphs
Every graph on this website is interactive in some way. Some general tips:
* Hover over data points to get more information. 
* Click on tiems in the keys to turn lines on and off
* Follow other directions as stated 

## Analysis Of Whitman's General Demographic Trends
Before analyzing the sex gaps in subjects overtime. I wanted to look at Whitman's overall demographic trends. This is important context for any analysis of sex gaps.

I calculated the percentage of class seats filled by people of each demographic in every term, and graphed it. I chose to base these demographics off of class seats instead of enrolled students because some students take more classes than others and I wanted the demographic analysis to reflect the demographic make up of an average class.

This graph excludes unknown Race/Ethnicity or Sex categories because those categories are not very interpetable and clutter an already crowded graph. 




