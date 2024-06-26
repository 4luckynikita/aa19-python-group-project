# BeatRate
https://beatrate.onrender.com/
#
BeatRate is a platform that connects musicians to music connoisseurs. The sole purpose of BeatRate is simple: Musicians post albums, and users review them. The website's structure allows people to check out their favorite artists' profiles, check out other users' profiles to see what they're into, see what's regarded as a musician's best works, and express their own feelings on what hits hardest. BeatRate's simple but robust layout allows for many exciting experiences like hearing about new releases on the home page and learning more about a musician or fellow user via their profile details.

## Run BeatRate Locally

**Prerequisites**
- NPM
- A version of Node.js >= 14 on your local machine
- Python 3.9
- PostgreSQL or SQLite3 in dev environment

**Installation**
- Clone the repo
- Install dependencies ```pipenv install -r requirements.txt```
- `cd react-app` and run `npm install`
- Create a **.env** file based on the example with proper settings for your development environment
- Setup a PostgreSQL database, user, and password and make sure they match your **.env** file.
- Get into your pipenv, migrate your database, seed your database, and run your app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   python run.py

- Start the backend Flask server: `python run.py` 
- Start the frontend Vite server: `npm run dev`
- Ctrl/Command click the ```localhost:XXXX``` link in the Vite server to open the live link!


# Connect
[Erik Hervall](https://www.linkedin.com/in/erikhervall/) | [Cece Potakey](https://www.linkedin.com/in/cecepot/) | [Nikita Kastyshyn](https://www.linkedin.com/in/nikitakastyshyn/) 

---
## This project was built with:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)


## Endpoints
Start by logging in:
### Log In User
- Method: POST
- URL: `/api/auth/login`
- Body:

    ```json
    {
      "email": "demo@aa.io",
      "password": "password"
    }
    ```

- Successful Response:
  ```json
  {
    "is_musician": false,
    "email": "demo@aa.io",
    "firstname": "Demo",
    "id": 3,
    "lastname": "User",
    "username": "demouser",
    "description": "This is the demo user's bio",
    "image_url": "https://demo.image/url.jpg"
  }
  ```

---

## Albums
### Create an album
- Method: POST
- URL: `/api/albums`
- Body:

    ```json
    {  
    "title": "Album Name",
   "release_date": "Tue, 11 Jun 2021",
   "description": "This is an album!",
   "image_url": "https://this.is.an/image.url",
   "user_id": 1
    }
    ```

- Successful Response:
    ```json
    {  
    "id": 10,  
    "title": "Album Name",
   "release_date": "Tue, 11 Jun 2021",
   "description": "This is an album!",
   "image_url": "https://this.is.an/image.url",
   "user_id": 1,
   "created_at": "Tue, 11 Jun 2024 14:15:49 GMT",
   "updated_at": "Tue, 11 Jun 2024 14:15:49 GMT"
    }
    ```

---

### View all albums
- Method: GET
- URL: `/api/albums/`
- Body: none

- Successful Response:
  ```json
  {
       "albums": [
       {
          "id": 10,  
    "title": "Album Name",
   "release_date": "Tue, 11 Jun 2021",
   "description": "This is an album!",
   "image_url": "https://this.is.an/image.url",
   "user_id": 1,
   "created_at": "Tue, 11 Jun 2024 14:15:49 GMT",
   "updated_at": "Tue, 11 Jun 2024 14:15:49 GMT",
           "songs": [
               {
                   "name": "Main Song",
                   "created_at": "Fri, 24 May 2024 05:00:36 GMT",
                   "duration": 78,
                   "id": 1,
                   "updated_at": "Fri, 24 May 2024 05:00:36 GMT"
               },
              ]
       },
       {
          "id": 11,  
    "title": "Album Name 2",
   "release_date": "Tue, 11 Jun 2021",
   "description": "This is an album!",
   "image_url": "https://this.is.an/image.url",
   "user_id": 1,
   "created_at": "Tue, 11 Jun 2024 14:15:49 GMT",
   "updated_at": "Tue, 11 Jun 2024 14:15:49 GMT",
           "songs": [
               {
                   "name": "Another song",
                   "created_at": "Fri, 24 May 2024 05:00:36 GMT",
                   "duration": 78,
                   "id": 1,
                   "updated_at": "Fri, 24 May 2024 05:00:36 GMT"
               },
              ]
       }
       ]
  }
  ```

---

### View a specific Album
- Method: GET
- URL: `/api/albums/:albumId`
- Body: none

- Successful Response:
  ```json
      "album": [
       {
          "id": 10,  
    "title": "Album Name",
   "release_date": "Tue, 11 Jun 2021",
   "description": "This is an album!",
   "image_url": "https://this.is.an/image.url",
   "user_id": 1,
   "created_at": "Tue, 11 Jun 2024 14:15:49 GMT",
   "updated_at": "Tue, 11 Jun 2024 14:15:49 GMT",
           "songs": [
               {
                   "name": "Main Song",
                   "created_at": "Fri, 24 May 2024 05:00:36 GMT",
                   "duration": 78,
                   "id": 1,
                   "updated_at": "Fri, 24 May 2024 05:00:36 GMT"
               },
              ]
       }
      ]
  ```

---

### Update an Album
- Method: PUT
- URL: `/api/albums/:albumId`
- Body:

    ```json
    {  
    "title": "Album name but edited",
   "release_date": "Tue, 11 Jun 2029",
   "description": "This is an album description but updated!",
   "image_url": "https://this.is.an/image.url/but/updated/woohoo",
   "user_id": 1
    }
    ```

- Successful Response:
    ```json
    {  
    "id": 10,  
    "title": "Album name but edited",
   "release_date": "Tue, 11 Jun 2029",
   "description": "This is an album description but updated!",
   "image_url": "https://this.is.an/image.url/but/updated/woohoo",
   "user_id": 1,
   "created_at": "Tue, 11 Jun 2024 14:15:49 GMT",
   "updated_at": "Tue, 16 Jun 2024 94:95:49 GMT"
    }
    ```

---

### Delete an album
- Method: DELETE
- URL: `/api/albums/:albumId`
- Body: none

- Successful Response:
  ```json
    {
    "message": "Album deleted successfully"
    }
  ```

---

## Songs
### Create a song by Album ID
- Method: POST
- URL: `/api/songs/albums/:albumId`
- Body:

    ```json
    {
   "album_id": 1,
   "title": "A new song",
   "duration": 5,
   "image_url": "https://example.image/url.jpg"
    }
    ```

- Successful Response:
  ```json
  {
   "album_id": 1,
   "title": "A new song",
   "duration": 5,
   "image_url": "https://example.image/url.jpg",
   "created_at": "Tue, 11 Jun 2024 15:37:38 GMT",
   "id": 40,
   "updated_at": "Tue, 11 Jun 2024 15:37:38 GMT"
  }

  ```

---
### Delete a song by album ID
- Method: DELETE
- URL: `/api/songs/:songId`
- Body: none

- Successful Response:
  ```json
    {
    "message": "Your song has been deleted sucessfully"
    }
  ```

---

## Reviews

### View all reviews for an album
- Method: GET
- URL: `/api/reviews/albums/:albumId`
- Body: none

- Successful Response:
  ```json
  {
    "reviews": [
      {
        "created_at": "Tue, 13 Jun 2024 14:18:29 GMT",
        "id": 26,
        "comment": "Great album!",
        "rating": 5,
        "album_id": 1,
        "user_id": 5,
        "updated_at": "Tue, 13 Jun 2024 14:18:29 GMT"
      },
      {
        "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
        "id": 27,
        "comment": "Ok album!",
        "rating": 3,
        "album_id": 1,
        "user_id": 1,
        "updated_at": "Tue, 11 Jun 2024 14:18:29 GMT"
      }
    ]
  }

---

### Create a Review
- Method: POST
- URL: `/api/reviews/albums/:albumId`
- Body:

    ```json
    {
    "comment": "Great album!",
    "rating": 5,
    "album_id": 1,
    "user_id": 5
    }

    ```

- Successful Response:
  ```json
  {
  "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
  "id": 27,
  "comment": "Great album!",
  "rating": 5,
  "album_id": 1,
  "user_id": 5,
  "updated_at": "Tue, 11 Jun 2024 14:18:29 GMT"
  }
  ```

---

### Update a Review
- Method: PUT
- URL: `/api/restaurants/:restaurantId/reviews/:reviewId`
- Body:

    ```json
    {
    "comment": "I changed my mind, this album is mid.",
    "rating": 3
    }

    ```

- Successful Response:
  ```json
  {
  "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
  "id": 27,
  "comment": "I changed my mind, this album is mid.",
  "rating": 3,
  "album_id": 1,
  "user_id": 5,
  "updated_at": "Tue, 13 Jun 2024 13:38:39 GMT"
  }
  ```

---

### Delete a Review
- Method: DELETE
- URL: `/api/restaurants/:restaurantId/reviews/:reviewId`
- Body: none

- Successful Response:
  ```json
  {
    "message": "Succesfully deleted your review"
    }
  ```

---

## Reviews

### View all reviews for an album
- Method: GET
- URL: `/api/reviews/albums/:albumId`
- Body: none

- Successful Response:
  ```json
  {
    "reviews": [
      {
        "created_at": "Tue, 13 Jun 2024 14:18:29 GMT",
        "id": 26,
        "comment": "Great album!",
        "rating": 5,
        "album_id": 1,
        "user_id": 5,
        "updated_at": "Tue, 13 Jun 2024 14:18:29 GMT"
      },
      {
        "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
        "id": 27,
        "comment": "Ok album!",
        "rating": 3,
        "album_id": 1,
        "user_id": 1,
        "updated_at": "Tue, 11 Jun 2024 14:18:29 GMT"
      }
    ]
  }

---

### Create a Review
- Method: POST
- URL: `/api/reviews/albums/:albumId`
- Body:

    ```json
    {
    "comment": "Great album!",
    "rating": 5,
    "album_id": 1,
    "user_id": 5
    }

    ```

- Successful Response:
  ```json
  {
  "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
  "id": 27,
  "comment": "Great album!",
  "rating": 5,
  "album_id": 1,
  "user_id": 5,
  "updated_at": "Tue, 11 Jun 2024 14:18:29 GMT"
  }
  ```

---

### Update a Review
- Method: PUT
- URL: `/api/restaurants/:restaurantId/reviews/:reviewId`
- Body:

    ```json
    {
    "comment": "I changed my mind, this album is mid.",
    "rating": 3
    }

    ```

- Successful Response:
  ```json
  {
  "created_at": "Tue, 11 Jun 2024 14:18:29 GMT",
  "id": 27,
  "comment": "I changed my mind, this album is mid.",
  "rating": 3,
  "album_id": 1,
  "user_id": 5,
  "updated_at": "Tue, 13 Jun 2024 13:38:39 GMT"
  }
  ```

---

### Delete a Review
- Method: DELETE
- URL: `/api/restaurants/:restaurantId/reviews/:reviewId`
- Body: none

- Successful Response:
  ```json
  {
    "message": "Succesfully deleted your review"
    }
  ```

---