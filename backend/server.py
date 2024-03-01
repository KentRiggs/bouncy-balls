from flask import Flask, request, jsonify
import pygame
import sys
import math
import random

app = Flask(__name__)

@app.route('/run_pygame', methods=['POST'])
def run_pygame():
    data = request.json
    num_balls = data.get('numBalls', 20)  # Default to 20 if not provided
    width = data.get('width', 800)       # Default to 800 if not provided
    height = data.get('height', 600)     # Default to 600 if not provided

    # need to adapt pygame script to use these values
    # main(num_balls, width, height)

    return jsonify({"message": "Pygame started with {} balls, width: {}, height: {}".format(num_balls, width, height)})

if __name__ == "__main__":
    app.run(debug=True)
