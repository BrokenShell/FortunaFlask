import Fortuna
from flask import Flask, jsonify

__all__ = ("API",)
API = Flask(__name__)


@API.route("/")
def canonical():
    return jsonify(result=Fortuna.canonical())


@API.route("/triangular/<low>,<high>,<mode>")
def triangular(low: str, high: str, mode: str):
    return jsonify(result=Fortuna.triangular(float(low), float(high), float(mode)))


@API.route("/d<sides>")
def d(sides: str):
    return jsonify(result=Fortuna.d(int(sides)))


@API.route("/dice/<rolls>d<sides>")
def dice(rolls: str, sides: str):
    return jsonify(result=Fortuna.dice(int(rolls), int(sides)))


@API.route("/percent-true/<percent>")
def percent_true(percent: str):
    return jsonify(result=Fortuna.percent_true(float(percent)))


@API.route("/random-range/<start>,<stop>,<step>")
def random_range(start: str, stop: str, step: str):
    return jsonify(Fortuna.random_range(int(start), int(stop), int(step)))
