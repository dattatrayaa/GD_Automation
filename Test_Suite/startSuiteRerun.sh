echo "Starting Robot suite"
pybot --rerunfailed "robot_results"/output-20180620-033414.xml --output "robot_results"/rerunl1.xml ./TestSuiteLesson.robot
pybot --rerunfailed "robot_results"/output-20180620-034620.xml --output "robot_results"/reruntr1.xml ./TestSuiteTrack.robot
pybot --rerunfailed "robot_results"/output-20180620-043234.xml --output "robot_results"/rerunc1.xml ./TestSuiteCampaign.robot
pybot --rerunfailed "robot_results"/output-20180620-044951.xml --output "robot_results"/rerunac1.xml ./TestSuiteAssignCampaign.robot
pybot --rerunfailed "robot_results"/output-20180620-052416.xml --output "robot_results"/rerunct1.xml ./TestSuiteCampaignTracks.robot
pybot --rerunfailed "robot_results"/output-20180620-061926.xml --output "robot_results"/rerung1.xml ./TestSuiteGroup.robot
pybot --rerunfailed "robot_results"/output-20180620-065135.xml --output "robot_results"/rerunt1.xml ./TestSuiteTag.robot
pybot --rerunfailed "robot_results"/output-20180620-061423.xml --output "robot_results"/rerunus1.xml ./TestSuiteCreateUser.robot
pybot --rerunfailed "robot_results"/output-20180620-060138.xml --output "robot_results"/rerunu1.xml ./TestSuiteUserAttributes.robot

echo "Suite ended" 
