echo "Starting Robot suite"

#pybot --rerunfailed "Test_Results"/lesson.xml --output "Test_Results"/rerunlesson.xml ./Test_Suite/TestSuiteLesson.robot
#pybot --rerunfailed "Test_Results"/track.xml --output "robot_results"/reruntrack.xml ./Test_Suite/TestSuiteTrack.robot
#pybot --rerunfailed "Test_Results"/campaign.xml --output "robot_results"/reruncampaign.xml ./Test_Suite/TestSuiteCampaign.robot
#pybot --rerunfailed "Test_Results"/assigncampaign.xml --output "robot_results"/rerunassigncampaign.xml ./Test_Suite/TestSuiteAssignCampaign.robot
#pybot --rerunfailed "Test_Results"/campaigntrack.xml --output "robot_results"/reruncampaigntrack.xml ./Test_Suite/TestSuiteCampaignTracks.robot
#pybot --rerunfailed "Test_Results"/group.xml --output "robot_results"/rerungroup.xml ./Test_Suite/TestSuiteGroup.robot
#pybot --rerunfailed "Test_Results"/tag.xml --output "robot_results"/reruntag.xml ./Test_Suite/TestSuiteTag.robot
#pybot --rerunfailed "Test_Results"/library.xml --output "robot_results"/rerunapi.xml ./Test_Suite/TestSuiteLibrary.robot
#pybot --rerunfailed "Test_Results"/api.xml --output "robot_results"/rerunuser.xml ./Test_Suite/APITestSuite.robot
#pybot --rerunfailed "Test_Results"/role.xml --output "robot_results"/rerunrole.xml ./Test_Suite/TestSuiteRoles.robot
#pybot --rerunfailed "Test_Results"/user.xml --output "robot_results"/rerunrole.xml ./Test_Suite/TestSuiteCreateUser.robot
#pybot --rerunfailed "Test_Results"/home.xml --output "robot_results"/rerunhome.xml ./Test_Suite/TestSuiteHome.robot

rebot -d Test_Results --output Final_output.xml -l logfinal.html -r  finalreport.html ./Test_Results/lesson.xml  ./Test_Results/track.xml

robot -v report:finalreport -v log:logfinal -l none -r none -o none ./Test_Suite/TestSuiteEmailAttach.robot

echo "Suite ended" 
