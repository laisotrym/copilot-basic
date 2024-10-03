# Test Case: Create User

| Test Case ID | Description | Preconditions | Test Steps | Expected Result |
|--------------|-------------|----------------|------------|-----------------|
| TC001        | Validate email format | None | 1. Navigate to the create user form. <br> 2. Enter an invalid email format in the email field. <br> 3. Submit the form. | The system should display an error message indicating the email format is invalid. |
| TC002        | Validate email uniqueness | A user with email `existing@example.com` already exists. | 1. Navigate to the create user form. <br> 2. Enter `existing@example.com` in the email field. <br> 3. Submit the form. | The system should display an error message indicating the email is already in use. |
| TC003        | Validate username length | None | 1. Navigate to the create user form. <br> 2. Enter a username with less than 5 characters. <br> 3. Submit the form. | The system should display an error message indicating the username is too short. |
| TC004        | Validate username length | None | 1. Navigate to the create user form. <br> 2. Enter a username with more than 50 characters. <br> 3. Submit the form. | The system should display an error message indicating the username is too long. |
| TC005        | Validate username with spaces | None | 1. Navigate to the create user form. <br> 2. Enter a username containing spaces. <br> 3. Submit the form. | The system should display an error message indicating the username cannot contain spaces. |

