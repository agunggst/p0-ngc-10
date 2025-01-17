# NGC 10

## Task
Create an API using `FastAPI` to provide weather data for different locations. Implement `HTTPException` to handle errors, and add API Key authentication for secure access.

Assume we have a dictionary containing weather data for three locations: "New York City," "Los Angeles," and "Chicago". Each location has temperature and weather condition information, for example:
```py
{
  "New York City": {
    "temperature": "10˚C",
    "condition": "Cloudy",
  },
  "Los Angeles": {
    "temperature": "20˚C",
    "condition": "Sunny",
  },
  "Chicago": {
    "temperature": "15˚C",
    "condition": "Cloudy",
  },
}
```

Create a FastAPI app and define two endpoints:
- Endpoint 1: `/weather/{location}`

  This endpoint will provide weather data for a specific location.

- Endpoint 2: `/authenticate`

  This endpoint will handle API Key authentication.

> Use HTTPException to handle cases where the requested location is not available in the weather_data dictionary.

## Submission
1. Create a file to store your answers in `.py`.
2. Save this assignment with filename: `p0-ngc-10.py`.
3. Push your answer into your own GitHub repository.
4. Additionally, you can deploy your api to vercel
