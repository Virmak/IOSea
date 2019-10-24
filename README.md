# IOSea

Sea level rise visualisation tools - NASA Space Apps Challenge

## Getting Started

These project uses Leaflet Js library to display a map and elevation points of the island of kerkena, to get started follow installation instructions
### Prerequisites

This project uses python as backend to fetch elevation values from NASA's SRTM elevations data. Before installing the dependencies make sure to create a new virtual environment by running : 
```
python -m venv venv
```

### Installing

Install the dependencies

```
pip install -r requirements.txt
```

## Usage

Activate the virtual environment


```
source ./venv/bin/activate
```

Start a local http server

```
python -m http.server
```

Open the map webpage in a browser

```
http://127.0.0.1:8000
```
## Generate new elevation data
Start the SRTM elevation extractor server run

```
./run_server.sh
```
This will start a flask web app to get elevation for a specific point, the url to use :

http://127.0.0.1:5000/elevation/{Lat}/{Long}

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [LeafLet](https://leafletjs.com/reference-1.5.0.html) - Map JS Library


## Authors

* **Mohamed Ben Amar** - *This web map* - [Virmak](https://github.com/Virmak)
* **Jed Fakhfekh** - 3D Simulation using UE4

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Todo

* Add three.js 3d map
* Simulate water level rise by selecting time or the quantity of ice melting from glaciers 
* Add UE4 3D Simulation Executable
