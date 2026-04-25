# Perrin's Data Science Final Project
## Initial Ideas 
### Idea 1: Gender gaps across school subjects at different levels of education overtime. 

#### Questions:
- Does the level of education effect the rate at which gender gaps close? 
- Does the level of education effect the time that gender gaps start to close? For example, it is plausible that a gender gap in computer science could start to close at the colege level a few years after it starts to close at the highschool level as the cohort of original highschoolers enter college.
- How do gender gaps across different school subjects vary by region? Does this change overtime?
  
#### Potential Challenges:
- Gender is a spectrum, but I will be shocked if I can find data about gender gaps that acknowledges this. Older data will probably record biological sex, and new data will probably record gender as man, woman, and other. Depending on who collected the data, the other category could just contain non binary and gender fluid people, or it could also contain trans people. Should I anlayse the extremely broad and undescriptive "other" category as its own gender?
- Lots of subjects branch into more sub-subjects as education level progresses. Math in middle school can become math, computer science, and physics in highschool. Computer science in high school can become computer science, computer engineering, data science, cyber security, etc. in college. How can I accound for this in my analysis? How can i even track which subjects branch in what ways? Should I focus mostly on named college majors that match named classes in highschool?
  
### Idea 2: (Probably) unconcious patterns in fiction writing

#### Questions:
- How consistent are authors about the order in which they list their characters names?
- For the authors that are consistent, is there any correlation between this order and the importance, gender, race, or age of chatecters?
- How do the demongraphics of authors correlate to the demographics of major charaters with significant amounts of dialogue?

#### Potential Challenges:
- This project may involve a lot of manual collection of data from text files. Some things, like the order of name lists and the amount of dialogue attributed to a character I *might* be able to scrape from text files myself. However, things like figuring out the demographics and importance of a character would be hard. I might be able to call on an AI, but I would probably have to pay to access their APIs. I generally think that unless I can find a really good data set for this, I might strugle to make my own big enough.

### Idea 3: According to [Our World In Data](https://ourworldindata.org/light-at-night) the price of lighting in the UK has fallen drastically since the 1300s. I want to explore possible causes and effects of this.

#### Potential Questions
- What correlations exist between the cost of light and levels of education?
- What correlations exist between the cost of light and innovation?
- What correlations exist between the cost of light and GDP?

## Week 10 Update:
This will be a solo project on gender gaps in classes and majors at Whitman, and how they are related to race. If the College Board responds to my data request, then I also hope to discuss how gender gaps at Whitman are related to gender gaps in high school AP classes.

I hope to use the following Data Sources: 

### Data Source 1: Whitman's Institutional Research
I have contacted Neal Christopherson to ask for data, but I have not heard back yet. As a result, my Pros/Cons list is speculative.

#### Pros 
* Specifically about Whitman, so very relevent to me and my audience of other Whitman people.
* I expect that the data will probably be quite complete and require minimal cleaning
* The data was collected by a group of people I can contact easily. So, I will be able to answer questions about who created the data and why.
* I will be able to clarify any parts of the dataset with confusing documentation.

#### Cons
* The data will probably have rigid categories
* Since I know people at Whitman personally, I will need to ensure that the data I ask for would not allow me to guess who the person it describes is.
* Using data specifically about Whitman students means that I need to narrow the scope of my project to just focus on Whitman. I won't be able to draw broader conclusions

### Data Source 2: College Board
I have submitted a request for data about the demographics of AP classes to the college board. I don't know if they will allow me to access this data or not. I will honestly be kind of suprised if they do.  

#### Pros
* This would be a massive dataset that would cover the entire nation. It would allow me to draw broader conclusions
* I expect that this data set would be clean and complete

#### Cons
* AP classes are more common in wealthier schools and the students taking AP classes are often of higher socioeconomic status. As a result my data would disproportionately represent wealthier students.
* I might not get this data from the college board
* The data will probably have rigid categories

### Research Questions (That I could answer without College Board data)
* How have gender gaps at Whitman changed overtime? Which majors/subjects have the largest gender gaps? Has this always been the case?
* How does intersectionality affect gender gaps at Whitman? Do gender gaps close for white people before they close for everyone else?
* How much do gender gaps in classes within a department compare to the gender gaps in the majors?

## Week 11 Update

### Description of my data source

#### Data Source
I decided to work with the data collected by Whitman's Office of Instituional Research about the demographics of individual anonymized students and the classes those students took from. 

#### Motivation
This data was collected by Whitman's Office of Institutional Research, which is presumably funded by Whitman College. According to its [website](https://www.whitman.edu/institutional-research), the Office of Institional Research's purpose is to "[provide] data and analytical support to Whitman College faculty and administration" for use in strategic planning, accreditation review, and student outcomes. The Office of Institutional Research is also responsible for reporting data to external organizations like the department of education. 

Neal Christopherson anonymized the data and broadened the demographic categories so that individual people were not identifiable in the data I received. 

#### Composition
I received two files. In one, student's unique Fake ID numbers are paired to classes they took and the semester they took it. This data represents every class student pair sense the fall of 2000. The second file is demographic data about each student identified by their Fake ID. The demographic data shows all students who graduated in May 2001 or later. I does not show students who graduated earlier than that, students who left the college without graduating, or students who are currently at whitman but did not graduate.

The categories of the demographic data are quite broad in order to protect the privacy of individual students. Gender is represented as M, F (I don't know how they count non-binary people). Race is represented as White, Student of Color, or International (I assume that International students are counted as International regardless of their Race/Ethnicity) and place of origin is represented as Oregon, Washington, Caligornia, Other State, or International. For each of these categories, only one value is listed. The category of major is represented as Arts and Humanities, Science and Math, Social Science, or Interdiciplinary. Multiple majors can be listed. Aditionally, the demographic data includes graduation year. 

#### Collection Process
The collection process is not very clear. Some data, such as courses taken by each student, was probably collected authomatically by the computer system. Other data, such as race, gender, and home state may have been collected during the admissions process. The students represented in data were not compensated, but I would guess that the staff collecting and organizing the data were. 

Consent of the students represente in the data is a little murky. As a student, I was aware that the college collected all of the data that shows up on my transcript such as classes and major. I was also aware that they collected demographic information and shared non personally identifiable demographic information because I have seen published demographic information. The College's data policies comply with FERPA (which is why all of the data was anonymized before I received it). However, I don't ever remember explicitly signing a consent form (though I may have signed one that I don't remember). 

#### Uses
* The demographic data only represents students who have graduated, so it should not be used to make claims about all students.
* The data only represents Whitman students, so it can not be used to represent broader populations such as college students
* This data can not be published 


### Why I Chose This Data
I chose to use this data because it is data specifically about students at Whitman. This means that any conclusions I draw from this is extremely relevent to my experience at Whitman and the experience of my classmates. Aditionally, the Office of Institional Research collects data about every single student who graduates, so I am able to use data from the entire population (who graduated) without worrying about biased sampling methods. I do have to account for the fact that I don't have demographic information about students who did not graduate. Finally, this dataset is nice because I know who compiled it and can ask questions relating to it. I am not relying on documentation that may or may not contain all relevant information. 
I would have liked to encorporate data on AP class enrollment into my analysis, but the college board would not release that data to me.

### Process of Aquiring Data
To aquire this data, I emailed Neal, Whitman's Director of Institutional Research. I described my project to him, and we discussed the data he could give me. His main concern was ensuring that students were not identifiable from their demographic information, so so we discussed how important different variables were. Neal eventually compiled a data set in which anonimized students with were represented individually via identification numbers.  He requested that I do not post the data on a public GitHub.

### Important Considerations
* The demographic data only represents students who have graduated, so it should not be used to make claims about all students.
* The data only represents Whitman students, so it can not be used to represent broader populations such as college students
* This data can not be published
* Many categories are broad and mutually exclusive in a way that does not necessarily reflect real life. Gender is not actually man, woman, or other. There are many categories lumped into "Student of Color" that may experience racism differently, and people can be multi-racial.

### Preliminary Exploration and Cleaning
* Most of my prelimary work has been centered on understanding the categories and cleaning the data. I have not done any real analysis. I looked at the unique categories in every column of categorical data, and in some cases I reformated to data table to represent the categories more clearly. For example, all categories of majors of a specific person were previously listed together. This would have made dealing with double majors more difficult, so I seperated each category into its own column that contained a boolean. I also re-interpreted Term to be a number where the part before the decimal represents the year and the part after the decimal represents the semester. This is easier to analyze than a string.
* Aditionally, I merged the data set of classes and the data set of demographics.
* I need to make decisions about how I will deal with the missing demographic information about people who have not graduated. Should I just make "ungraduated" its own category? Should I change my questions to focus on people who have graduated? Should I exclude classes from before the spring of 2021 since I don't have demographic information on peole who graduated before then?

### Unanticipated Challenges
* I think that my largest challenge will be working with the extremely broad categories and dealing with the missing demographic information of people who have not graduated.

## Week 12 Update: Preliminary Exploration
#### What I did: 
This week, I reached out to Neal asking for data on students who have not graduated. He said he will be able to send it to me sometime next week. In the mean time, I explored the general demographics of whitman college overtime. I wanted to make sure that, when I analyze gender gaps in specific subjects, I do so in relation to the demographics of whitman. I want to get a sense the average demographics of courses every semester, so counted the number of course, student pairs for every student in a demographic, and I devided that by the total number of course student pairs. Weighting the demographics by the number of courses each student was taking gave me the percentage of students in every demographic who would be in an "average" course.

#### Analysis:
* Across all Race/Ethnicity categories except International, Women tend to make up a larger percentage of the population then Men. However, International is split much more evently.
* There is a large spike in some demographic categories and a coresponding drop in others in the summer of 2008. After examining the courses taught that summer, it looks like Whitman ran two off campus study-abroad programs (a Chinese one and an Anthropology one). They were small and were the only courses being taught in the summer, so the demographics of active students that summer could be effected a lot by a difference of only a few people.
* Most students at Whitman are white, but the percentage of white students trends down overtime while the percentage of students of color and international students trends slightly up. 
<iframe 
  src="https://github.com/bookworm6/Data-Science-Final-Project/blob/main/demographics.html" 
  title="Description of embedded content" 
  width="600" 
  height="400">
</iframe>
  
