# NBA Player Roster for 2017

This dataset includes all players for all teams in the NBA in the year 2017. 

# Pre-requisites

- You need to have Python installed
- You need to have the Python CSV moduled (normally installed by default along with Python)
- Edit nba.py to reflect your Riak host and its correspinding HTTP port
- Obviously, the RIAK_HOST value should reflect your corresponding Riak host and its HTTP port

# Setup

## Initialize the search index
```
export RIAK_HOST="http://localhost:10018"

curl -XPUT $RIAK_HOST/search/index/people

curl -XPUT $RIAK_HOST/search/index/people \
     -H 'Content-Type: application/json' \
     -d '{"schema":"_yz_default"}'
```

## Initialize the bucket
```
bin/riak-admin bucket-type create nba_players '{"props":{}}'
bin/riak-admin bucket-type activate nba_players
```

## Set the bucket to use the search index
```
curl -XPUT $RIAK_HOST/types/nba_players/buckets/players/props \
     -H 'Content-Type: application/json' \
     -d '{"props":{"search_index":"people"}}'

curl -XPUT $RIAK_HOST/buckets/players/props \
     -H'content-type:application/json' \
     -d'{"props":{"search_index":"people"}}'
```

# Import the data

```
python nba.py nba.csv
```

# Run a test query

## Retrieve information about Paul Pierce 

```
curl "$RIAK_HOST/types/nba_players/buckets/players/keys/34LosAngelesClippers"
```

## Retrieve a list of players on the Los Angeles Lakers team

```
curl "$RIAK_HOST/search/query/people?wt=json&indent=true&q=team_s:*Lakers"
```

## Retrieve a list of players on the Pacific division with pagination showing 5 entries each (cursorMark)

```
curl "$RIAK_HOST/search/query/people?wt=json&indent=true&q=division_s:Pacific&sort=_yz_id+asc&rows=5&cursorMark=*"
```

If you want to traverse the next page, use the `nextCursorMark` value in the `cursorMark` parameter

# Warning

`nba.py` uses `shell=True` and is dangerous
