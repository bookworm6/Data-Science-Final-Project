---
layout: default
title: Final Project Presentation
---
# An Analysis of the Balance Between Sexes Across Subjects at Whitman College

I was one of three girls in my high school computer science class, so a gender gap in computer science felt normal (though not good) to me. I expected that I would experience a similar overwhelmingly large gender gap in computer science in college, so I was surprised to discover that, though my computer science classes are still male dominated, the difference at Whitman does not feel as large as it did in high school. Since Whitman collects data on biological sex but not gender, I will explore "Sex Gaps," the gaps in representation of biological sexes across various subjects. At a personal level, I am doing this project because I wanted to know how my experience fits into larger patterns of sex gaps over time. At a larger level, I hope to explore how sex gaps at Whitman are related to national economic outcomes. 

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

### Interactive Graphs
Every graph on this website is interactive in some way. Some general tips:
* Hover over data points to get more information. 
* Click on tiems in the keys to turn lines on and off
* Follow other directions as stated 


### Whitman's Demographics
Before analyzing the sex gaps in subjects overtime, we must understand Whitman's overall demographic trends. 

This is a graph of the percentage of class seats filled by people of each demographic in every term. I chose to base these demographics off of class seats instead of enrolled students because some students take more classes than others and I wanted the demographic analysis to reflect the demographic make up of an average class. 

<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/demographics" 
  width="600" 
  height="400">
</iframe>
Excluded Data: Students of unknown Race/Ethnicity or Sex were excluded because those categories are not very interpetable and clutter an already crowded graph. This graph also excludes data from the summer of 2008 because only a few students took classes, which allowed randomness to cause outliers.

* Across all Race/Ethnicity categories except international, female students tend to make up a larger percentage of the population then male. However, international students are split much more evently.
* Most students at Whitman are white, but the percentage of white students trends down overtime while the percentage of students of color and international students trends slightly up. 
* Demographic data is variable enough that I must analyze a demographic's representation in a subject in relation to that demographics overall population in a semester

### Exploring Whitman's Sex Gaps Over Time
Before we can explore Whitman's sex gaps, we need to measure them. 
#### A Metric For Sex Gaps: Percent Over/Under Represented
The demographic exploration shows that members of a demographic group fill some percentage of Whitman's total number of class seats every semester, and that the percentage filled by a demographic group can change overtime. That means that, in the "average" subject at Whitman in a given term, the demographic group would fill a percentage of seats equal to the percentage of class seats they fill at Whitman in that term. 

The difference between the percentage of class seats filled in the "average" subject and and actual subject can be attributed to some combination of luck/random variation and the subject area iteself. So, it makes sense to measure sex gaps in a subject area using this difference

Percent Over/Under Represented = the percentage of seats a demographic group fills in a subject in a given term - the percentage of seats they would fill in the "average" class at Whitman that term. 

If this value is negative, the demographic group is under represented. If this value is positive, the demographic group is over represented. 

#### Sex Gaps in Subjects Over Time
Every subjects's sex gap has changed differently overtime. Some subjects are fairly evenly split between sexes and have been for decades. Some subjects have large gaps and the gaps are getting worse. In some subjects, large gaps are getting better. I will highlight the sex gaps of a few subjects that I find interesting. 

##### Computer Science
<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/CS_Over_Time" 
  width="600" 
  height="400">
</iframe>

Female students have been about 30% under represented in CS at Whitman since the department was founded in 2015. This gap was fairly constant through 2021, but then it started to narrow very slowly in the spring of 2022. This is interesting because it is not a sudden change, it is gradual. 

Chat GPT launched in the fall of 2022, which was the beginning of a [20% decrease in employment for new CS grads](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf). Did this slow down the rate at which the gap might have closed? Speed it up? Have no effect at all? The data can't tell us. 

##### English
<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/ENGL_Over_Time" 
  width="600" 
  height="400">
</iframe>

Female and male students were fairly evenly represented in English classes until 2014. In 2014, there started to be a clear gap in which female students were over represented and male students were underrepresented. This is interesting because a sudden change probably has a very specific cause, but I have not been able to speculate what that cause was.

##### Choose Your Own Adventure
At this point, you might be wondering about the Sex Gap in your college major, or maybe you are wondering which major's have the largest sex gaps. This tool allows you to explore to your hearts content.

Every point on the top numberlines is the average percent over/under represented of a sex in a subject . The further left you go, the more under represented a sex is. The further right, the more over represented. 

Click on a point to see a graph of the sex gap of that subject over time. Though the gaps in representation of race/ethnicy, sex pairs are toggled off by default, you can toggle them on by clicking in the key. 

<iframe 
  src="https://data-science-final-project.onrender.com/" 
  width="600" 
  height="900">
</iframe>
Excluded Data: If, in any term, fewer than 10 people took classes in a subject, luck had a disproportionate influence on the representation of a sex in the subject that term. Therefore, the subject is excluded for that term only. It is not included in the average percent over/under represented or in the graph of the sex gap of a subject overtime


## The Representation of Sexes in Whitman's classes in Relation to The National Median Mid-Career Salary of That Major
So what? Some sexes are over represented in some majors and under represented in others. Why does this matter? 

Let's look at the money
<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/SalaryGraphFemale" 
  width="600" 
  height="400">
</iframe>
<iframe 
  src="https://bookworm6.github.io/Data-Science-Final-Project/SalaryGraphMale" 
  width="600" 
  height="400">
</iframe>
Excluded Data: Students of unknown sex were excluded because there were no meaningful patterns and no way to make sense of unknown sex. Aditionally, there was not salary data about all majors. Subjects whose major did not have salary data were excluded. 

For female students, representation in a subject is negatively correlated with the national median mid-career salary of majors in that subject. For male students, this correlation is positive. 

In other words...

Female students at Whitman are underrepresented in subjects that, nationally, lead to higher paying careers. Male students are over represented in these subjects.











