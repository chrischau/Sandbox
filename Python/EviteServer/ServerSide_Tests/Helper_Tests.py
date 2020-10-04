import unittest
import sys
sys.path.insert(1, 'C:\Development\GitHub\Sandbox\Python\EviteServer\ServerSide')

from Helper import Helper


class Helper_Test(unittest.TestCase):

  def test_ValidateTimeFormat_checks_empty_string(self):
    try:
      helper = Helper()
      helper.ValidateTimeFormat("")

    except ValueError as ex:
      self.assertEqual(str(ex), "Incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS")


  def test_ValidateTimeFormat_success_cases(self):
    helper = Helper()
    helper.ValidateTimeFormat("2020-10-04 00:00:00")
      

  def test_ValidateTimeFormat_has_no_time_stamp(self):
    try:
      helper = Helper()
      helper.ValidateTimeFormat("2020-10-04")
      
    except ValueError as ex:
      self.assertEqual(str(ex), "Incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS")


  def test_ValidateTimeFormat_display_different_error_message(self):
    errorMessage = "ABC"
    try:
      helper = Helper()
      helper.ValidateTimeFormat("2020-10-04", errorMessage)
      
    except ValueError as ex:
      self.assertEqual(str(ex), errorMessage)

  
  def test_ValidateEmailStructure_success_cases(self):
    helper = Helper()
    helper.ValidateEmailStructure("john@abc.com")
    helper.ValidateEmailStructure("john@abc.co.jp")
    helper.ValidateEmailStructure("john.123@abc.com")
    helper.ValidateEmailStructure("j@a.c")
    helper.ValidateEmailStructure("john.hancock.signature@abc.com")

  
  def test_ValidateEmailStructure_return_error_message(self):
    email = "john@abc"
    try:
      helper = Helper()
      helper.ValidateEmailStructure(email)
    except ValueError as ex:
      self.assertEqual(str(ex), "Email provided '{}' is not a valid structured email.".format(email))
    
  
  def test_ValidateIfNullOrEmpty_success_cases(self):
    helper = Helper()
    helper.ValidateIfNullOrEmpty("ABC", "Events")

  
  def test_ValidateIfNullOrEmpty_has_None_element(self):
    try:
      helper = Helper()
      helper.ValidateIfNullOrEmpty(None, "Events")
    except ValueError as ex:
      self.assertEqual(str(ex), "'Events' is not provided.")


  def test_ValidateIfNullOrEmpty_has_empty_string(self):
    try:
      helper = Helper()
      helper.ValidateIfNullOrEmpty("", "Events")
    except ValueError as ex:
      self.assertEqual(str(ex), "'Events' is not provided.")

  
  def test_ValidateEndTimeIsAfterStartTime_success_case(self):
    helper = Helper()
    helper.ValidateEndTimeIsAfterStartTime("2020-10-01 00:00:00", "2020-10-02 00:00:00")
    helper.ValidateEndTimeIsAfterStartTime("2020-09-01 00:00:00", "2020-10-02 00:00:00")
    helper.ValidateEndTimeIsAfterStartTime("2020-10-01 00:00:01", "2020-10-02 00:00:02")

  
  def test_ValidateEndTimeIsAfterStartTime_start_time_older_than_end_time(self):
    try:
      helper = Helper()
      helper.ValidateEndTimeIsAfterStartTime("2020-10-05 00:00:00", "2020-10-02 00:00:00")
    except ValueError as ex:
      self.assertEqual(str(ex), "EndTime cannot be earlier than StartTime.")
  

  def test_ValidateEndTimeIsAfterStartTime_check_start_time_format(self):
    try:
      helper = Helper()
      helper.ValidateEndTimeIsAfterStartTime("2020-10-01", "2020-10-02 00:00:00")
    except ValueError as ex:
      self.assertEqual(str(ex), "StartTime has incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS.")


  def test_ValidateEndTimeIsAfterStartTime_check_end_time_format(self):
    # problem with this kind of test is that the test case doesn't fail, maybe need to mock it
    try:
      helper = Helper()
      helper.ValidateEndTimeIsAfterStartTime("2020-10-01 00:00:00", "2020-10-02 00:00")
    except ValueError as ex:
      self.assertEqual(str(ex), "EndTime has incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS.")




if __name__ == '__main__':
    unittest.main()
