# Scheduler

Sample app for scheduling appointments.

## Docker

Download from https://hub.docker.com/repository/docker/williamheiderman/maven-sample

## Constraints

- all appointments must start and end on the hour or half hour
- all appointments are exactly 30 minutes long
- a user can only have 1 appointment on a calendar date

## Test

### Create Appointment

```{bash}
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"user_id":"17c900cd-bbd1-48c7-9adf-b471ab44ed62","start_time":"2021-06-16 00:00:00.000000"}' \
  http://localhost:5000/appointments
```

### Get Appointments

```{bash}
curl --header "Content-Type: application/json" -X GET \
 --data '{"user_id":"17c900cd-bbd1-48c7-9adf-b471ab44ed62"}' \
  http://localhost:5000/appointments
```