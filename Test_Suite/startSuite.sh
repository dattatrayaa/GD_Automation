echo "Starting Robot suite"

pybot -n non-critical -d Test_Results -o lesson.xml -l loglesson.html -r lessonreport.html  ./Test_Suite/TestSuiteLessons.robot 
#pybot -n non-critical -d Test_Results -o cmp.xml -l logcmp.html -r cmpreport.html ./Test_Suite/TestSuiteCampaigns.robot

#pybot -n non-critical -d Test_Results -o lesson.xml -l loglesson.html -r reportlesson.html  ./Test_Suite/TestSuiteLesson.robot 

#pybot -n non-critical -d Test_Results -o track.xml -l logtrack.html -r reporttrack.html  ./Test_Suite/TestSuiteTrack.robot

#pybot -n non-critical -d Test_Results -o campaign.xml -l logcampaign.html -r reportcampaign.html  ./Test_Suite/TestSuiteCampaign.robot
#pybot -n non-critical -d Test_Results -o assigncampaign.xml -l logassigncampaign.html -r reportassigncampaign.html  ./Test_Suite/TestSuiteAssignCampaign.robot
#pybot -n non-critical -d Test_Results -o campaigntrack.xml -l logcampaigntrack.html -r reportcampaigntrack.html  ./Test_Suite/TestSuiteCampaignTracks.robot
#pybot -n non-critical -d Test_Results -o group.xml -l loggroup.html -r reportgroup.html  ./Test_Suite/TestSuiteGroup.robot
#pybot -n non-critical -d Test_Results -o tag.xml -l logtag.html -r reporttag.html  ./Test_Suite/TestSuiteTag.robot
#pybot -n non-critical -d Test_Results -o library.xml -l logtlibrary.html -r reportlibrary.html  ./Test_Suite/TestSuiteLibrary.robot
#pybot -n non-critical -d Test_Results -o api.xml -l logapi.html -r reportapi.html  ./Test_Suite/APITestSuite.robot
#pybot -n non-critical -d Test_Results -o user.xml -l loguser.html -r reportuser.html  ./Test_Suite/TestSuiteCreateUser.robot
#pybot -n non-critical -d Test_Results -o role.xml -l logrole.html -r reportrole.html  ./Test_Suite/TestSuiteRoles.robot
#pybot -n non-critical -d Test_Results -o home.xml -l loghome.html -r reporthome.html  ./Test_Suite/TestSuiteHome.robot

#rebot -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/lesson.xml  ./Test_Results/track.xml

#robot -v report:finalreport -v log:logfinal -l none -r none -o none ./Test_Suite/TestSuiteEmailAttach.robot



echo "Suite ended" 
 
