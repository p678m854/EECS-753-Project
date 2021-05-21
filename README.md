# EECS-753-Project

Author: Patrick McNamee

Date: May 21, 2021

## Description

Implementation of the Bezier CNN to use as part of a real-time controller for the DeepPicar. Developed as part of a class project for EECS 753 Real-Time Embedded Systems at the University of Kansas. Class was taught by Dr. Yun during the Spring 2021 semester.

## Repository Structure

```
EECS-753-Project
├── data
│   └── external
│       ├── DeepPicar-data                     <- Data from Github Repo for Data Augmentation.
│       └── DeepPicar-v2-data                  <- Data from Github Repo for Training/Testing.
├── deeppicar-scripts                          <- Additional scripts to running DeepPicar.
├── LICENSE
├── models                                     <- Holds all timal models and any temporary ones
│   └── temporary
├── notebooks                                  <- Jupyter notebooks used for data exploration and model testing and evaluation
├── README.md
└── reports                                    <- All PDF generated and some finalized results videos.
    ├── deeppicar-testing                      <- Implementation of CNN on DeepPicar for testing.
    ├── figures                                <- Figures for the LaTEX reports.
    ├── final-report                           <- Final Report turned in.
    ├── presentation                           <- Final presentation, results not as complete as Final Report.
    ├── proposal                               <- Porject proposal for the class.
    ├── training-history                       <- Training history of the models as numpy arrays.
    └── video-quality-checks                   <- Overlayed Model Predicted and Recorded values on video.
        ├── image-to-curve
        │   └── final-bezier                   <- Bezier CNN as 2 Hz outerloop with 20 Hz inner loop.
        └── image-to-point
            ├── domain-augmentation-results    <- Trained on DeepPicar repository.
            ├── final-bezier-cnn               <- Bezier CNN as 20 Hz controller.
            └── final-strandard-cnn-model      <- DAVE-2 CNN as 20 Hz controller.
```

## Setup and Run Instructions

This project uses the hardware described in [DeepPicar-v2](https://github.com/mbechtel2/DeepPicar-v2) with some data not hosted here from [DeepPiCar](https://github.com/dctian/DeepPiCar), specifically the lane navigation data. If you wish to simply download this repository and try the notebooks, there is a custom package that will need to be installed from the author's [EECS Masters work](https://github.com/p678m854/EECS-Masters) which is not currently, as of May 21 2021, a public repository. If you are simply wishing to setup a DeepPicar to test out the resulting models yourself, the steps are below. Note this has changed slightly from the original [DeepPicar instructions](https://github.com/mbechtel2/DeepPicar-v2/wiki/Setup-and-Operation) as this work used a Raspberry Pi 3A+ and there are some package dependency/installation issues that are not obvious.

### Necessary Repositories

There are three repositories, including this one, that need to be downloaded onto the Raspberry Pi 3A+. They are are:

1. EECS-753-Project i.e. this repository
2. DeepPicar-v2 i.e. the original DeepPicar work
3. drv8835-motor-driver-rpi

Navigate to where you wish to have the three repositories and clone the GitHub repositories. Clone to the appropriate depth where a depth of 2 of this repository will yield the appropriate python scripts and models for running the DeepPicar with the CNN of this repository.

```
$ git clone https://github.com/p678m854/EECS-753-Project
$ git clone --depth=1 https://github.com/mbechtel2/DeepPicar-v2
$ git clone https://github.com/pololu/drv8835-motor-driver-rpi
```

### Python libraries

One issue of this project is that since the Raspberry Pi 3A+ has such limited memeory, you will not be able to install some current versions of `TensorFlow` or its dependency `gRPC` so the versioning of these is crucial for the DeepPicar to get all packages necessary. The installation flow will follow installing for the DeepPicar-v2 repository with adjustments before installing the drv8835 package from the GitHub repository. There is a known implementation [issue](https://stackoverflow.com/questions/56002315/undefined-symbol-pythreadstate-current-when-importing-tensorflow) where `TensorFlow` does not run with on the Raspberry Pi 3A+ with `Python 3.7` but will with the now depreciated `Python 3.5` which forces the implementation usage of `Python 2.7` to avoid this issue. Another implementation sticking point is that the motor library uses the `wiringpi` library which requires to run python scrips as the super user. Some other packages do not require this but as the `drv88355` module does, all python scripts will need to be run as the super user.


### Installation Steps

1. Install necessary python.

```
$ sudo apt-get install python-dev python-pip
```


2. Install `wiriingpi` system wide and Python 2.7 accessable.
```
$ sudo pip install wiringpi
```

3. From the clone GitHub Repository, install the drv8835 module. Navigate to the local repository and
```
$ sudo python setup.py install
```

4. Install libraries for computer vision and image manipulations
```
$ sudo apt-get install python-opencv
$ sudo pip install pillow
$ sudo apt-get install python-imaging
```

5. Install some tensorflow dependencies which may be version critical.
```
$ sudo apt-get install libhdf5-dev
$ sudo pip install Cython==0.29.16
$ sudo pip install grpcio==1.18.0
```

6. Install `TensorFlow 1.11` which was used in the DeepPicar-v2 repository. While this version does not have the NormalizeLayer layer that DAVE-2 it does have BathNormalize layer. NormalizeLayer doesn't appear until `TensorFlow 1.14` which is viable with `Python 2.7` but too large to be installed on the Raspberry Pi 3A+. If you do not specify the `--no-cache-dir` flag, the installation will terminate due to an OOM.

```
$ sudo pip install --no-cache-dir tensorflow==1.11.0
```

7. Copy the python scripts from deeppicar-scripts directory into the main directory of the DeepPicar-v2.

8. Run the new scipts in the DeepPicar-v2 repository. There are defaults you can change but this is all that is necessary to run with the various CNN although by loading the model by file, it was assumed that this repository and DeepPicar-v2 are sibling subdirectories for relative pathing to work.

```
$ sudo python picar-mini-kbd-<controller specifier>.py -d
```

## Controller Specifications

1. i2p: Standard CNN which takes an image and maps to a wheel angle. Operates at 20 Hz.
2. i2bc: Bezier CNN which takes an image and maps to a cubic polynomial at 2 Hz with an inner loop sampling the cubic at 20 Hz.
3. i2bp: Bezier CNN which takes an image and maps to a cubic polynomial but controller takes the first pole only i.e. t = 0. Operates at 20 Hz.
