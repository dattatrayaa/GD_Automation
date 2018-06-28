*** Settings ***
Force Tags      Campaign
#Config
Library   ../Master/BaseTestClass.py
#Functions to create AssignCampagn
Library           ../TestCases/Campaign/AssignCampAllCardsLessonToLearner.py
Library           ../TestCases/Campaign/AssignCampLessonToGroupTriggered.py
Library           ../TestCases/Campaign/AssignCampNewHireTriggeredOneTrackAndOneLesson.py
Library           ../TestCases/Campaign/AssignCampOneLessonToCreator.py
Library           ../TestCases/Campaign/AssignCampOneLessonToLA.py
Library           ../TestCases/Campaign/AssignCampOneLessonToMA.py
Library           ../TestCases/Campaign/AssignCampOneLessonTrackToLearner.py
Library           ../TestCases/Campaign/AssignCampOneTrackContainsFourLessons.py
Library           ../TestCases/Campaign/AssignCampTenLessonsWithGraded.py
Library           ../TestCases/Campaign/AssignCampTwoLessonsTwoTracksGraded.py
Library           ../TestCases/Campaign/AssignCampCreateTwoTriggers.py
Library           ../TestCases/Campaign/AssignCampForTwoGroupsTriggered.py
Library           ../TestCases/Campaign/AssignCampLessonTriggeredForGroupCheckNewUser.py
Library           ../TestCases/Campaign/AssignCampTrigWithoutCurrentUser.py

Library           ../TestCases/Campaign/AssignCampToCancelSentAssignment.py
Library           ../TestCases/Campaign/AssignCampEditCampignAndAssign.py
Library           ../TestCases/Campaign/AssignCampEditTrigger.py
Library           ../TestCases/Campaign/AssignCampNoOfLearnersTriggeredGroup.py
Library           ../TestCases/Campaign/AssignCampTrigToGroupAndDeleteTrigger.py
Library           ../TestCases/Campaign/AssignCampDuplicateOfTriggeredAssignment.py
Library           ../TestCases/Campaign/AssignCampVerifyManageAssignmentForPage.py
Library           ../TestCases/Campaign/AssignCampVerifyPlanAssignmentPage.py
Library           ../TestCases/Campaign/AssignCampCheckDueSoon.py
Library           ../TestCases/Campaign/AssignCampCheckDueTodayStaus.py
Library           ../TestCases/Campaign/AssignCampCompleteAssignment.py
Library           ../TestCases/Campaign/AssignCampDeleteLesson.py
Library           ../TestCases/Campaign/AssignCampToNoOfGroupTriggered.py
Library           ../TestCases/Campaign/AssignCampVerifyingCampDetailsPageLink.py
Library           ../TestCases/Campaign/AssignCampGetLinkOne.py
Library           ../TestCases/Campaign/AssignCampGetLinkTwo.py
Library           ../TestCases/Campaign/AssignCampGetLinkToUnknownUser.py
Library           ../TestCases/Campaign/AssignCampSelfEnrollNoDueDate.py
Library           ../TestCases/Campaign/AssignCampSelfEnrollWithDueDate.py
Library           ../Master/CloseBrowser.py

*** Test Cases ***
TC0 Login
    User Login

TC1 - AssignCampAllCardsLessonToLearner
    Assign Camp All Cardsto Learner

TC2 - AssignCampLessonToGroupTriggered
    Assign Camp With One Lesson For Group Triggered

TC3 - AssignCampNewHireTriggeredOneTrackAndOneLesson
    Assign Camp New Hire Triggered One Track One Lesson

TC4 - AssignCampOneLessonToCreator
    Assign Camp One For Lesson To Creator

TC5 - AssignCampOneLessonToLA
    Assign Camp One For Lesson To LA

TC6 - GrovoTC/AssignCampOneLessonToMA
    Assign Camp One For Lesson To MA

TC7 - AssignCampOneLessonTrackToLearner
    Assign Camp One Lesson Track Learner

TC9 - AssignCampTenLessonsWithGraded
    Assign Camp With Ten Lessons Graded

TC10 - AssignCampTwoLessonsTwoTracksGraded
    Assign Camp With Two Track Two Lesson Graded

TC11 - AssignCampCreateTwoTriggers
    Assign Camp For Two Triggers

TC13 - AssignCampLessonTriggeredForGroupCheckNewUser
    Assign Camp With One Lesson For Group Triggered Check Assignment For New User

TC14 - AssignCampTrigWithoutCurrentUser
    Assign Camp TO Group Without Current User

TC15 - AssignCampToCancelSentAssignment
    Assign Camp To Cancel Assignment

TC16 - AssignCampEditCampignAndAssign
    Assign Edited Campaign

TC17 - AssignCampEditTrigger
    Assign Camp Edit Trigger Delete Trigger

TC18 - AssignCampNoOfLearnersTriggeredGroup
    Assign Camp For Five Learners

TC19 - AssignCampTrigToGroupAndDeleteTrigger
    Assign Camp Triggred To Group Delete Trigger And Check For User

TC20 - AssignCampDuplicateOfTriggeredAssignment
    Assign Camp To Duplicate

TC21 - AssignCampDeleteLesson
    Assign Camp Delete Lesson Edit Camp Add New Lesson

TC22 - AssignCampToNoOfGroupTriggered
    Assign Camp No Of Groups Triggered

#TC23 - AssignCampVerifyingCampDetailsPageLink
    #Assign Camp For Verify Campaign Details Page

#TC24 - AssignCampVerifyManageAssignmentForPage
   # Assign Camp To Verify Manage Assignment For Page

#TC25 - AssignCampVerifyPlanAssignmentPage
    #Assign Camp To Verify Plan Assignment For Page

TC26 - AssignCampCheckDueSoon
    Assign Camp To Check Due Soon Status For User

TC27 - AssignCampCheckDueTodayStaus
    Assign Camp To Check Due Today Status For User

TC28 - AssignCampCompleteAssignment
    Assign Camp To Check Complete Assignment Status
TC29 - AssignCampGetLinkOne
    Get Link One Main

TC30 - AssignCampGetLinkTwo
    Get Link Two Main

TC31 - AssignCampGetLinkToUnknownUser
    Unknown User

TC32 - AssignCampSelfEnrollNoDueDate
    Assign Camp With Enroll Link No Due Date

TC33 - AssignCampSelfEnrollWithDueDate
    Assign Camp With Enroll Link With Due Date
TC12 - AssignCampForTwoGroupsTriggered
    Assign Camp With Two Groups Triggered Main

TC8 - AssignCampOneTrackContainsFourLessons
    Assign Camp One Track Contains Four Lessons

Close Browser
    Close Browser Suite
