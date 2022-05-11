
# 21cineplex Clone

Scraping data dari 21cineplex dan Parsing data dari Rest API untuk ditampilkan di client side.


## Screenshots

[![Desain-tanpa-judul-2.png](https://i.postimg.cc/ryf3CqW8/Desain-tanpa-judul-2.png)](https://postimg.cc/JtBpRVPg)


## 🔗 Demo in Vercel.app
 [![VercelLogo](https://img.shields.io/badge/Vercel-000?style=for-the-badge&logo=vercel&logoColor=white)](https://cinema21-clone.vercel.app/)
- [Details Specific Movies](https://cinema21-clone.vercel.app/details/22DSMM)
- [Book Movies](https://cinema21-clone.vercel.app/book/22DSMM)
- [Get Foods & Beverages](https://cinema21-clone.vercel.app/food/DPRTSM)


## Build With

 - [Python3](https://www.python.org/)
 - [Flask](https://pypi.org/project/Flask/)
 - [Flask Caching](https://pypi.org/project/Flask-Caching/)
 - [Flask-Cors](https://pypi.org/project/Flask-Cors/)
 - [Requests](https://pypi.org/project/requests/)
 - [FlixgoTemplate](https://www.templateshub.net/template/FlixGo-Online-Movies-Template)
 - [Jquery Ajax](https://api.jquery.com/jquery.ajax/)



## Installation

Git Clone this project

```bash
  cd 21cineplexclone-py
  pip install .\requirements.txt
```


## Note

✅This project uses the Caching API so that it doesn't reload continuously


## Run Locally

Clone the project

```bash
  git clone https://github.com/sandrocods/21cineplexclone-py/
```

Go to the project directory

```bash
  cd 21cineplexclone-py
```

Install dependencies

```bash
   pip install .\requirements.txt
```

Start the Flask server

```bash
  python3 index.py
```


## Flask Route Reference

### Gets the list of movies that are currently playing, coming soon and details movie

```http
    GET /
```

### Gets specific details movie

```http
    GET /details/<id>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. Movie ID  |



### Booking Specific Movie

```http
    GET /book/<id>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. Movie ID  |

### Gets food and beverage items available at that cinema

```http
    GET /food/<id>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `theater_id` | `string` | **Required**. theater_id or cinemaId  |


### Gets all Cinema from CityId

```http
    GET /getTheaters/<id>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Id` | `string` | **Required**. CityId  |


### Gets all CityId

```http
    GET /getCityId
```

### Gets the schedule of a movie in a cinema

```http
    GET /getSchedule/<id>/<movieId>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. cinemaId  |
| `movieId` | `string` | **Required**. movieId  |

## Authors

- [@sandrocods](https://www.github.com/sandrocods)

