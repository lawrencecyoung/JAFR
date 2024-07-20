NOTE: To run test driver scripts type ". <test_driver_file>"
NOTE: All test cases are assumed to be run on 27/08/2023


For test_driver_john.sh
NOTE: Ensure meetings and tasks files are empty in tests/test_users/john/school before running test_driver_john.sh script
   test_1: {user = john}      Both meetings and tasks files empty
   test_2: {user = john}      Adding meeting
   test_3: {user = john}      Changing master directory
   test_4: {user = john}      Complete task option with no options available and Add Meetings

For test_driver_noah.sh
NOTE: Copy contents from original_tasks.md into tasks.md within tests/test_users/noah/uni prior to running test_driver_noah.sh script
   test_5: {user = noah}      Testing various meetings and tasks edge cases 
   test_6: {user = noah}      Completing tasks
   test_7: {user = noah}      Task sharing
   test_8: {user = noah}      Meeting sharing

For test_driver_missing_file.sh
   test_9: {user = oliver}    Master directory does not exist
   test_10: {user = peter}    Missing tasks.md file
   test_11: {user = rebecca}  Missing meeings.md file
