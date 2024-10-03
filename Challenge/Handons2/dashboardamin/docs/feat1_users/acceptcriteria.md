# API User Create - Acceptance Criteria

## Validation Criteria

1. **Email Format**
    - The email address must be in a valid format (e.g., user@example.com).
    - The email address must contain an "@" symbol and a domain name.

2. **Email Uniqueness**
    - The email address must be unique.
    - The system should check the database to ensure no duplicate email addresses exist.

3. **Username Length**
    - The username must be greater than 5 characters and less than 9 characters in length.
    - The system should reject any username that does not meet this length requirement.

## Error Handling

- If the email format is invalid, the system should return an error message: "Invalid email format."
- If the email is not unique, the system should return an error message: "Email already exists."
- If the username length is not within the specified range, the system should return an error message: "Username must be between 6 and 8 characters long."

## Example Request

```json
{
  "email": "user@example.com",
  "username": "user123"
}
```

## Example Response

- **Success:** 
  ```json
  {
     "message": "User created successfully."
  }
  ```

- **Failure:** 
  ```json
  {
     "error": "Invalid email format."
  }
  ```
  ```json
  {
     "error": "Email already exists."
  }
  ```
  ```json
  {
     "error": "Username must be between 6 and 8 characters long."
  }
  ```