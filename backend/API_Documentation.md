# API Documentation
Last updated 11/22/2024

The base API url is http://localhost:{portnumber}/api/

## Root endpoint

| **url**         | **Method** | **Description**                 |
|-----------------|------------|---------------------------------|
| /               | GET        | Returns all patient data.       |

### Parameters:

| Name                 | Data Type  | Required/Optional | Description                         |
|----------------------|------------|-------------------|-------------------------------------|
| patient_id           | string     | Optional          | The patient's id                    |
|----------------------|------------|-------------------|-------------------------------------|
| first_name           | string     | Optional          | The patient's first name            |
|----------------------|------------|-------------------|-------------------------------------|
| last_name            | string     | Optional          | The patient's last name             |
|----------------------|------------|-------------------|-------------------------------------|
| start_date           | Date       | Optional          | Query begin date (inclusive)        |
|----------------------|------------|-------------------|-------------------------------------|
| end_date             | Date       | Optional          | Query end date (inclusive)          |

### Responses:
```200``` - Successful request  
```404``` - Error - user not found