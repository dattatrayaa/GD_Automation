*** Settings ***
Force Tags        Tracks
Library           ../Master/BaseTestClass.py    
Library           ../TestCases/Create/Tracks/TrackWithTxtImgQueLesson.py    
Library           ../TestCases/Create/Tracks/TrackWithDocumentLesson.py
Library           ../TestCases/Create/Tracks/TrackWithImageLesson.py
Library           ../TestCases/Create/Tracks/TrackWithQuestionLesson.py
Library           ../TestCases/Create/Tracks/TrackWithDocumentLesson.py
Library           ../TestCases/Create/Tracks/TrackWithQuestionLesson.py
Library           ../TestCases/Create/Tracks/TrackWithTextLesson.py
Library           ../TestCases/Create/Tracks/TrackWithVideoLesson.py
Library           ../TestCases/Create/Tracks/TrackWithVidLessonDocLesssonQuesLesson.py
Library           ../TestCases/Create/Tracks/TrackWithImgLessonVidLesson.py
Library           ../TestCases/Create/Tracks/TrackWithTxtLessonImgLesson.py
Library           ../TestCases/Create/Tracks/TrackWithTxtVidQueLesson.py
Library           ../TestCases/Create/Tracks/TrackWithVidDocQueLesson.py
Library           ../TestCases/Create/Tracks/TrackWithAllCardsOne.py
Library           ../TestCases/Create/Tracks/TrackWithAllCardsTwoTimes.py
Library           ../TestCases/Create/Tracks/TrackWithFourLessons.py
Library           ../TestCases/Create/Tracks/TrackWithFourLessonsDifferentCombiOfLessons.py
Library           ../TestCases/Create/Tracks/TrackWithFourLessonsDifferentCombiOfLessons2.py
Library           ../TestCases/Create/Tracks/TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons.py
Library           ../TestCases/Create/Tracks/TrackDeleteLesson.py
Library           ../TestCases/Create/Tracks/TrackDuplicate.py
Library           ../TestCases/Create/Tracks/TrackEditDetailsValidation.py
Library           ../TestCases/Create/Tracks/TrackGetLinkBuilderTrackForLearner.py
Library           ../TestCases/Create/Tracks/TrackGetLinkBuilderTrackForMA.py
Library           ../TestCases/Create/Tracks/TrackGetLinkPublishedTrackForLearner.py
Library           ../TestCases/Create/Tracks/TrackGetLinkPublishedTrackForMA.py
Library           ../Master/DeleteLesson.py
Library           ../Master/CloseBrowser.py

*** Test Cases ***
TC0 - User Login
    User Login
    #Test cases for Track creation

TC1 - TrackWithImgLessonVidLesson
    Track With Two Lessons Imgand Vid

TC2 - TrackWithTxtLessonImgLesson
    Track With Two Lessons Txt And Img

TC3 - TrackWithTxtVidQueLesson
    Lesson With Text Video Question Card

TC4 - TrackWithVidDocQueLesson
    Lesson With Video Document Question Card

TC5 - TrackWithAllCardsOne
    Track With All Cards

TC6 - TrackWithAllCardsTwoTimes
    Track With All Card Two Time

TC7 - TrackWithFourLessons
    Track With Four Lessons

TC8 - TrackWithFourLessonsDifferentCombiOfLessons
    Track With Four Lessons Diff Combi 1

TC9 - TrackWithFourLessonsDifferentCombiOfLessons2
    Track With Four Lessons Different Combi 2

TC10 - TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons
    Track With Ques All Card One And Two Time Lessons

TC11 - TrackWithVidLessonDocLesssonQuesLesson
    Track With Two Lessons Vid Doc Ques

TC12 - TrackWithDocumentLesson
    Lesson With Document Card

TC13 - TrackWithImageLesson
    Lesson With Image Card

TC14 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card

TC15 - TrackWithTextLesson
    Track With Lesson Contains Text Card

TC16 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card

TC17 - TrackWithVideoLesson
    Lesson With Video Card

TC18 - TrackDeleteLesson
    Track Delete Lesson Check In Track Page Main

TC19 - TrackDuplicate
    Track Duplicate Main

TC20 - TrackEditDetailsValidation
    Track Edit Check All Details

TC21 - TrackGetLinkBuilderTrackForLearner
    Track Get Link Builder For Learner Main

TC22 - TrackGetLinkBuilderTrackForMA
    Track Get Link Builder For MA Main

TC23 - TrackGetLinkPublishedTrackForLearner
    Track Get Link Published For Learner Main

TC24 - TrackGetLinkPublishedTrackForMA
    Track Get Link Published For MA Main

Close Browser
    Close Browser Suite
