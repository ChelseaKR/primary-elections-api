from flask import Flask
import json

app = Flask(__name__)


class PrimaryElectionsAPI:
    def __init__(self):
        self.fn = 'mock_data.json'

    @app.route('/winning_primary_candidates', methods=['GET'])
    def get_winning_primary_candidates(self):
        f = open(self.fn)
        data = json.load(f)
        f.close()

        winners = {}
        for state in data:
            winners[state] = data[state]
            for county in data[state]:
                winners[state][county] = data[state][county]
                for party in data[state][county]:
                    winners[state][county][party] = max(data[state][county][party], key=data[state][county][party].get)

        return winners


if __name__ == '__main__':
    app.run(debug=False)