*** Settings ***
Force Tags      Library

#Config
Library   ../Master/BaseTestClass.py

#Functions to Assign Tags
Library   ../TestCases/Library/TagDocLesson.py
Library   ../TestCases/Library/TagLessonCombinedLesson.py
Library   ../TestCases/Library/TagLessonImage.py
Library   ../TestCases/Library/TagLessonTextLesson.py
Library   ../TestCases/Library/TagQuesLesson.py
Library   ../TestCases/Library/TagTrackLessonDocument.py
Library   ../TestCases/Library/TagTracklessonFiveTextImageQuestion.py
Library   ../TestCases/Library/TagTrackLessonImage.py
Library   ../TestCases/Library/TagTrackLessonOneTextImageVideoDocumentQuestion.py
Library   ../TestCases/Library/TagTrackLessonQuestion.py
Library   ../TestCases/Library/TagTrackLessonText.py
Library   ../TestCases/Library/TagTrackLessonTwoTextImageVideoDocumentQuestion.py
Library   ../TestCases/Library/TagTrackLessonVideo.py
Library   ../TestCases/Library/TagTrackWithfourlessonsFourFiveSixSeven.py
Library   ../TestCases/Library/TagTrackWithfourlessonsSevenEightNineTen.py
Library   ../TestCases/Library/TagTrackWithfourlessonsTenTwelveThree.py
Library   ../TestCases/Library/TagTrackWiththreelessons_Five_Six_Seven.py
Library   ../TestCases/Library/TagTrackWiththreelessonsThreeFourFive.py
Library   ../TestCases/Library/TagTrackWithTwolessonsOneTwo.py
Library   ../TestCases/Library/TagTrackWithTwolessons_Two_Three.py

Library   ../Master/CloseBrowser.py
*** Test Cases ***
TC0 - User Login
    User Login
   
TC3 - TagLessonImage   
	TagLessonImage.Taglesson With Image Upload Card

TC4 - TagLessonTextLesson    
    TagLessonTextLesson.Taglesson With Text Card  
     
TC5 - TagQuesLesson
	Tag For Question Card Lesson Main
      
TC7 - TagTracklessonFiveTextImageQuestion
    Taglesson With Text Image Question Card   
    
TC8 -TagTrackLessonImage
       TagTrackLessonImage.Lesson Image Assign Tag    
TC10 - TagTrackLessonQuestion
     TagTrackLessonQuestion.Taglesson With Question Answer Card        
TC13 - TagTrackLessonVideo    
    Lesson Video Assign Tag    
TC16 -TagTrackWithfourlessonsTenTwelveThree
     Tagtrack Withfourlessons Ten Twelve Three         
TC19 - TagTrackWithTwolessonsOneTwo
 
     Tag Track With Twolessons One Two    
TC20 -TagTrackWithTwolessons_Two_Three
    Tagtrack With Two Lessons Imgand Vid
TC1 -TagDocLesson
    Taglesson With Document Upload Card
    
TC2 - TagLessonCombinedLesson
    Tag Lesson Combined  
TC6 - TagTrackLessonDocument
    Lesson With Document Assign Tag
TC9 - TagTrackLessonOneTextImageVideoDocumentQuestion
    Tagtrack With All Cards  
TC12 - TagTrackLessonTwoTextImageVideoDocumentQuestion
       	Tagtrack With All Card Two Time    
TC14 - TagTrackWithfourlessons_Four_Five_Six_Seven
	Tagtrack Tag Withfourlessons Four Five Six Seven
	          
TC15 -TagTrackWithfourlessons_seven_Eight_Nine_Ten
    
    	Tagtrack With Four Lessons Seven Eight Nine Ten   
TC17 - TagTrackWiththreelessons_Five_Six_Seven
    Tagtrack With Ques All Card One And Two Time Lessons    
     
TC18 -TagTrackWiththreelessons_Three_Four_Five

    Tagtrack Withthreelessons Three Four Five
TC11 -TagTrackLessonText
  	Assign Lesson And Track For Tag Track Lesson Text
Close Browser
    Close Browser Suite

    
    
    
    
    
    
    
    
    
    
    
    
