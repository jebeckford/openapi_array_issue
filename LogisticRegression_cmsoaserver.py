
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='<wherever LogisticRegression.py is located>')

# Read the yaml file to configure the endpoints
app.add_api('/<whatever directory>/LogisticRegression.yaml')

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=8080,
            debug=False,
            server='flask')
