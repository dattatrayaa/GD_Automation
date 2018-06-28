echo "Starting Robot suite"

#pybot -n non-critical -d Test_Results -o lesson.xml -l loglesson.html -r lessonreport.html  ./Test_Suite/TestSuiteLessons.robot 


#pybot -n non-critical -d Test_Results -o cmp.xml -l logcmp.html -r cmpreport.html ./Test_Suite/TestSuiteCampaigns.robot


#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteLesson.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteTrack.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteCampaign.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteAssignCampaign.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteCampaignTracks.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteUserAttributes.robot
pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteGroup.robot
pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteTag.robot
pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteLibrary.robot
pybot -T -n non-critical -d Test_Results ./Test_Suite/APITestSuite.robot
#pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteCreateUser.robot
pybot -T -n non-critical -d Test_Results ./Test_Suite/TestSuiteRoles.robot

#rebot -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/cmp.xml  ./Test_Results/lesson.xml

#robot -v report:finalreport -v log:logfinal -l none -r none -o none ./Test_Suite/TestSuiteEmailAttach.robot



echo "Suite ended" 
 
