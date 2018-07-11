echo "Starting Robot suite"

#pybot -n noncritical -d Test_Results -o lesson.xml -l loglesson.html -r lessonreport.html  ./Test_Suite/TestSuiteLessons.robot 

#pybot -n noncritical -d Test_Results -o cmp.xml -l logcmp.html -r cmpreport.html ./Test_Suite/TestSuiteCampaigns.robot

#echo “Starting Lesson Suite”
#pybot -n Lesson -d Test_Results -o lesson.xml -l loglesson.html -r reportlesson.html  ./Test_Suite/TestSuiteLesson.robot 

#echo “Starting Tracks suite”
#pybot -n Tracks -d Test_Results -o track.xml -l logtrack.html -r reporttrack.html  ./Test_Suite/TestSuiteTrack.robot


#echo “Starting Campaign suite”
#pybot -n Campaign -d Test_Results -o campaign.xml -l logcampaign.html -r reportcampaign.html  ./Test_Suite/TestSuiteCampaign.robot

#pybot -n Campaign -d Test_Results -o assigncampaign.xml -l logassigncampaign.html -r reportassigncampaign.html  ./Test_Suite/TestSuiteAssignCampaign.robot

#pybot -n Campaign -d Test_Results -o campaigntrack.xml -l logcampaigntrack.html -r reportcampaigntrack.html  ./Test_Suite/TestSuiteCampaignTracks.robot


#echo “Starting Admin suite”
#pybot -n Admin -d Test_Results -o group.xml -l loggroup.html -r reportgroup.html  ./Test_Suite/TestSuiteGroup.robot 

#pybot -n Admin -d Test_Results -o tag.xml -l logtag.html -r reporttag.html  ./Test_Suite/TestSuiteTag.robot 
 
#pybot -n Admin -d Test_Results -o api.xml -l logapi.html -r reportapi.html  ./Test_Suite/APITestSuite.robot 

#pybot —n Admin -d Test_Results -o user.xml -l loguser.html -r reportuser.html  ./Test_Suite/TestSuiteCreateUser.robot
 
#pybot -n Admin -d Test_Results -o attribute.xml -l logattribute.html -r reportattribute.html  ./Test_Suite/TestSuiteUserAttributes.robot

#pybot -n Admin -d Test_Results -o role.xml -l logrole.html -r reportrole.html  ./Test_Suite/TestSuiteRoles.robot


#echo “Starting Library suite”
#pybot -n Library -d Test_Results -o library.xml -l logtlibrary.html -r reportlibrary.html  ./Test_Suite/TestSuiteLibrary.robot
#echo "starting bamboo"


#echo “Starting Home suite”
#pybot -n Home -d Test_Results -o home.xml -l loghome.html -r reporthome.html  ./Test_Suite/TestSuiteHome.robot


#echo “Generating report and log files”
#rebot -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/api.xml ./Test_Results/Final_output.xml 

#rebot -n Campaign -n Admin -n Lesson -n Tracks -n Library -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/lesson.xml  ./Test_Results/track.xml ./Test_Results/user.xml ./Test_Results/attribute.xml ./Test_Results/campaign.xml ./Test_Results/assigncampaign.xml ./Test_Results/campaigntrack.xml ./Test_Results/tag.xml ./Test_Results/group.xml ./Test_Results/library.xml 

robot -n Create -n Campaign -n Admin -d Test_Results -o demoouput.xml -l demolog.html -r demoreport.html  ./Test_Suite/Demo.robot 

#Collecting Robot results
#rebot -n Create -n Campaign -n Admin -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/demoouput.xml  ./Test_Results/bamboo.xml

echo “Sending mail”
robot -v report:demoreport -v log:demolog -l none -r none -o none ./Test_Suite/TestSuiteEmailAttach.robot



echo "Suite ended" 
 
 
 
