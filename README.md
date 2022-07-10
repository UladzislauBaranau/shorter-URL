# Shorter URL: service for shortening long links

[![Project](https://img.shields.io/badge/Deploy-project-green)](https://shorter-url-links.herokuapp.com/)
[![Testing](https://github.com/UladzislauBaranau/shorter-URL/actions/workflows/testing.yaml/badge.svg)](https://github.com/UladzislauBaranau/shorter-URL/actions/workflows/testing.yaml)
[![Codecov](https://codecov.io/gh/UladzislauBaranau/shorter-URL/branch/master/graph/badge.svg)](https://app.codecov.io/gh/UladzislauBaranau/shorter-URL)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The user enters an original long URL address and gets a short unique URL as a response.
The project includes four pages. 
There is an authorization page, registration page, page for shortening your links, and page with all your short and original links. 

## Technical Requirements/Installation and Running

### Requirements
1. Python 3.8+
2. Django 3.2+

### Installation and running
The project is always available [here](https://shorter-url-links.herokuapp.com/).
If you want to start the project locally, run the following commands, after that, it will be launched on your local server `http://127.0.0.1:8000/`. 

##### Development tools
```
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

##### Running migrations
```
python3 manage.py migrate
```

##### Running local server 
```
python3 manage.py runserver
```

## License
See [MIT license](https://github.com/UladzislauBaranau/shorter-URL/blob/master/LICENSE).

<hr>

# SQL requests

#### 1-st task
```
select client_number, sum(outcome = 'win') as win, sum(outcome = 'lose') as lose from 
bid inner join event_value on bid.play_id = event_value.play_id and bid.coefficient = event_value.value 
group by client_number;
```
#### 2-nd task
```
select concat(A, '-',B) as game, count(1) as games_count from 
(select least(home_team, away_team) as A, greatest(home_team, away_team) as B 
from event_entity order by A, B) as teams 
group by A, B order by games_count;
```
