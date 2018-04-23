
# Automated vivarium with Raspberry pi

This project uses a Raspberry pi 2 Model B to observe and monitor a Crested Gecko housed in a custom built varvarium as well as control some environmental parameters.
* Capture night timelapse images using IR camera and IR LEDs.
* Automatically render images to video and then upload to Youtube.
* Record Temperature and Humidity values.
* Control coloured LED lights
 

## Hardware 
Raspberry pi 2 Model B v1.1

Belkin Wifi adapter

16GB Micro SD with Raspbian Stretch  

Raspberry pi NoIR infrared camera board v1.3 

4 Channel Relay Module  

12V power supply (for IR LEDs)  

36 Infrared LEDs (ESUMIC® IR Infrared 36 Led Illuminator Board Plate) 

DHT11 Temperature and Humidity sensor.

### Hardware configuration

* Relay control on GPIO.17 (Raspbery pi PIN11) for infrared LED ON/OFF
* DHT11 Data on GPIO.14 (Raspberry pi PIN08) for Temperature/Humidity logging


### Raspberry pi setup

Prepare the pi
```
sudo apt-get update
sudo apt-get upgrade
```
#### Installing packages

* Infrared LED relay control (install/update to latest version)
```
sudo apt-get install rpi.gpio
```
* Picamera (install/update on Raspbian)
```
sudo apt-get install python-picamera python3-picamera
```
  or for distros other than Raspbian
```
sudo pip install picamera
```
* FFMPEG for rendering images to video
```
sudo apt-get install ffmpeg
```

#### Youtube Uploader

To setup video to automatically upload to Youtube I used [tokland](https://github.com/tokland/youtube-upload), and followed the Youtube setup procedure for client secrets.




### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
