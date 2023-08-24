---
title: 'RM: Computational Methods in Psychology and Neuroscience'
subtitle: 'Psychology 4215/7215 --- Fall 2023'
author: Per B. Sederberg, PhD
documentclass: scrartcl
date: Version 2023-08-24
header-includes:
    - \usepackage{array,hyperref}
    - \usepackage[letterpaper, margin=1in]{geometry}
    - \usepackage{libertine} 
    - \usepackage[libertine]{newtxmath}
---


# Quick Reference

Credit:
:    3 units

Time:
:    Thursday, 14:00 -- 16:30

Place:
:    Shannon House rm. 107

Text:
:    Assigned readings

Course Web Page:
:    GitHub (https://github.com/compmem/compsy)

Course assistants:
:    Becky Waugh (and CompMem lab members)

Instructor:
:    Dr. Per Sederberg

Office:
:    Gilmer Hall, rm. 412

E-mail:
:    pbs5u@virginia.edu

Lab Website:
:    Computational Memory Lab (https://compmem.org)

Office hours:
:    TBA

Final:
:    Project-based



# Overview and Course Objectives

In the late 1800s, Hermann Ebbinghaus and Georg Elias Müller were busy launching the systematic study of human memory. They painstakingly wrote out study lists and and kept track of their own and their participants' memory performance by hand after studying the items. Müller even built a "memory drum" that had stimuli wrapped around a rotating drum that revealed them one at a time at a fixed rate. All analysis and visualization of their results involved tabulating data by hand in notebooks. Nonetheless, through years of dedicated work they were able to lay the foundation for the next century of memory research. Today, we have the help of computers, which have become an indispensable tool in Psychology and Neuroscience. Yet, in these same fields, computers are rarely employed to their full potential, limiting the productivity, reproducibility, and quality of our work. 

Science is hard.  We need as many tools as possible at our disposal to make our job easier.  These days computers play an integral role in our scientific workflow and psychologists typically rely on a limited number of large-scale software packages to assist at each stage of this process (e.g., EPrime, Microsoft Excel, SPSS and, if we're willing to branch out into the land of programming, Matlab or R).  This course is designed to break the fetters of commercial, and often inflexible, applications with the power of computer programming. With few assumptions of prior programming experience, we focus on the Python language and specifically on how it can help with *every* stage of our scientific workflow in Psychology and Neuroscience.  The goal is that you will gain a better understanding of how a computer works (and can work for you), improve how you solve problems, and optimize and speed up your workflow, but, most importantly, that you will lessen the need to tailor your research questions based on the status quo.


# Resources

Note, all materials for the course are either freely available online or I will provide them to you. I strongly believe that paywalls should not be a barrier to science.

The main sources for some lesson materials at the start of the course are:

- Downey, Allen (2016). Think Python: How to think like a computer scientist (2nd Edition). 
  Needham, MA: Green Tea Press. 
  - Free downloadable copy at https://greenteapress.com/wp/think-python-2e/

- Gael Varoquaux, Valentin Haenel, Pierre de Buyl, Gert-Ludwig Ingold, Emmanuelle Gouillart, Michael Hartmann, ... João Felipe Santos. (2023). Scientific Python Lectures: Release 2023.1rc0
  - https://lectures.scientific-python.org/index.html

In addition, we will make use of a number of other online resources, including documentation and user manuals for the various Python libraries and packages that you will be learning to use. Finally, there will be scientific articles for class discussion associated with some of the experiments we implement and analyze. I will provide these on our GitHub class page. 


# Computing Requirements

This is a computational class and all work will be performed on a computer, and almost entirely with the Python programming language within Jupyter notebooks. You will need to bring a laptop running Windows, OSX, or Linux to every class. 

You will run the [Jupyter](https://jupyter.org) notebooks directly on your computer. This will also allow you to incorporate these approaches into your own research more easily. Thus, my recommendation is that you install and use the [Anaconda Python](https://www.anaconda.com/download/) distribution for your OS. 

We will spend time on the first day of class to ensure everyone has a functioning computer that will be able to run everything necessary for the course.


# Assistance

I am eager for you to get as much as possible from this course, so please feel free to come to me with any questions you have. That said, science is a team effort and in order to reduce duplication of questions and discussions, we will be using Discord for all class communication and discussions. Please do not email me unless there is an issue with Discord. We will set up channels for general discussion. If you'd prefer to have a one-on-one discussion it is possible to send direct messages in Discord to either me or the TAs. We will spend some time on the first day ensuring everyone is set up to use Discord. I will also have weekly office hours to which you are always welcome to come and have virtual in-person discussions.

If you anticipate any issues related to the format, materials, or requirements of this course, please meet with me outside of class so we can explore potential options. Students with disabilities may also wish to work with the Student Disability Access Center to discuss a range of options to removing barriers in this course, including official accommodations. Please visit their website (http://sdac.studenthealth.virginia.edu/) for information on this process and to apply for services online. If you have already been approved for accommodations through SDAC, please send me your accommodation letter if I have not yet received it and meet with me so we can develop an implementation plan together.


# Equity, Free Speech, and Class Discussions

The University of Virginia is a community in which the ideals of freedom of inquiry, thought, and expression are respected and sustained. The University of Virginia is also dedicated to providing a safe and equitable learning environment for all students. Discrimination and harassment on the basis of race, color, sex, gender identity, sexual orientation, national or ethnic origin, religion, political affiliation, age, marital status, veteran status, or family medical or genetic information will not be tolerated. All students are expected to be respectful of others during class discussions.



# Support for Undocu+ Students

Students of all immigration statuses are welcomed and valued in this classroom, including undocumented students, students from mixed-status families, and students with Temporary Protected Status. As an educator, I aim to create a learning environment that respects and affirms the diversity of students' experiences and perspectives. If your status is impacting your success in the course, please come see me to discuss things I can do to accommodate you (assignments, attendance, etc.). I pledge to keep your status confidential unless required by judicial warrant.
 

# Inclusive Teaching Philosophy

I recognize and value the many perspectives my students bring to the classroom. Many factors--- social identities, visible and invisible disabilities, family circumstances, physical location, mental health, access to the internet--- all influence the experiences that every individual can have in my courses this and every semester. I am committed to building an environment to support your learning, one in which you will be supported and rewarded for going out on a limb to communicate and defend your ideas.
 


# Supporting Black Lives and Other Students of Color

I acknowledge that racism and white supremacy are baked into both the history of UVA as an institution and the history of higher education as a whole. I believe that my pedagogical philosophies and practices can either reinforce inequities or work to eliminate them. I am committed and actively working to be a better, more careful listener; continuing to learn about the ways systemic injustices disadvantage my Black students and colleagues and other students and colleagues of color in and out of the classroom; and advocating for and implementing anti-racist educational practices. I will hold myself accountable, encourage you to help me do so, and invite you to join me in this work.
 

# Mental Health and Well-being

If you are feeling overwhelmed, stressed, or isolated, there are many individuals here to help. The Student Health and Wellness Center offers Counseling and Psychological Services (CAPS) for its students; call 434-243-5150 to speak with an on-call counselor and/or schedule an appointment. If you prefer to speak anonymously, you can call Madison House's HELP Line at any hour of any day: 434-295-TALK. Alternatively, you can call or text the Disaster Distress Helpline (1-800-985-5990, or text TalkWithUs to 66746) to connect with a trained crisis counselor; this is toll free, multilingual, and confidential, available to all residents in the US and its territories.


# AI Policy

We have entered into an age where artificial intelligence models are able to help us with many aspects of our lives. There certainly are cases where that "help" actually inhibits learning (e.g., when you ask an AI model to write something that you would be unable to write yourself.) It is very unlikely that an AI model, such as ChatGPT or Bard, would be able to produce output for this class that would be fully correct without significant knowledge transfer from the user. We are also at a point where we should be actively exploring the boundaries of what AI can do and what it we should not be relying on it to do. Thus, my policy for this year is that, *unless specified in the assignment*, you are free to use AI models such as ChatGPT or Bard as long as you follow these guidelines:

- State on your submitted work what AI model you used (including version, such as ChatGPT 3.5).
- Where applicable, include the prompts you used to generate the output.
- Double-check the output for accuracy because that's a major avenue for learning (and we can not fully trust the output from these models).

Note, I am also interested in continuing the discussion about the ethics and utility of AI throughout the semester.

# Schedule

The following is the general order of the topics covered in the course. Please note that sometimes we may cover multiple topics in a single lecture, or spend more than one lecture on a single topic, and this list is subject to modification at any time. That said, all major changes will also include an update to the syllabus, so it will remain a point of reference.

0. Intro and Ecosystem setup
1. Python programming (throughout)
2. Experiment design and implementation
3. Data collection and processing
4. Data visualization
5. Data analysis and statistics
6. Repeat 2 through 5 for various topics: Attention, Perception, Working Memory, Long-term memory, Decision-making
7. Neural data analysis
8. Advanced topics (e.g., machine learning, computational modeling, etc...)

Lectures, in the form of Jupyter Notebooks, will typically be posted the day of class, so you can follow along. Assignments, from smaller exercises to larger projects (see below), will be assigned in class with clear due dates spread throughout the semester.


# Evaluation

This is a upper-level course, which means that much of the burden of staying motivated to learn is transferred to the student. As such, there will not be any in-class exams. Students will be evaluated on the basis of:

- Lesson exercises / class participation (30 pts)
  - Includes article discussions
- List generation project (10 pts)
- Experiment project (10 pts)
- Experiment labs (30 pts)
- Final project (20 pts)

for a total of 100 points.

Graduate students will have the following additional course requirements:

- Experiment motivation and design document (10 pts)
- Final write-up with results and discussion (20 pts)

for a total of 30 additional points.

The course will be graded using the standard grading scale with your percentage of points earned out of the total possible points rounding to the nearest whole percentage point.




