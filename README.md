# openapi_array_issue

To recreate issue:

1. Download files to a directory of your choosing:
LogisticRegression.py
LogisticRegression.yaml
LogisticRegression_flask.py

2. Start up flask server
python LogisticRegression_flask.py

3. Run curl command
```
curl -X GET "http://127.0.0.1:8080/cloudmesh/LogisticRegression/fit?X=5.2%2C%203.5%2C%201.4%2C%200.2%2C%205.9%2C%203.0%2C%205.1%2C%201.8&y=0%2C2&sample_weight=1%2C1&X_shape_x=2&X_shape_y=4" -H "accept: text/plain"
```

4. Kill flask server, update LogisticRegression.yaml to use a different schema, and re-run through steps 2 and 3

  > ArrayOfAny
  
  > ArrayOfOneInList
