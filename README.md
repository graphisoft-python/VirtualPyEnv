# VirtualPyEnv

## About

VirtualPyEnv is a plugin for the Python runtime environment in ARCHICAD. VirtualPyEnv uses a multi-interpreter working mode to provide a relatively independent python runtime environment for each vapp (virtual application) of the APPS directory project.

## Supported

* Archciad 22 (Windows)

## Install

* Install Archicad 
* Download Git（ https://git-scm.com ）
* Install Git（Check Use Git and optional Unix tools from Windows Command Prompt ）
* Run git --version in Terminal. Verify that Git is installed successfully（Shift+MouseRight）
* Start the terminal in the [Archicad Install Path]/Add-Ons directory
* Clone Project ( git clone https://github.com/graphisoft-python/VirtualPyEnv.git )
* Install the Python runtime environment（./Env/python-2.7.15.amd64.msi）
* Set Add python.exe to Path to Will be installed on local hard drive in the Customize Python tab during installation.
* Run python --version in Terminal. Verify that Python is installed successfully(python version must 2.7.15)
* Run pip --version in Terminal. Verify that Pip is installed successfully
* Installation completed

## Usage



## Feature

 [x] python 2.7 env

 [x] multi-thread

 [x] reboot vapp(virtual application)

 [ ] auto install requirements

 [ ] auto update vapp(virtual application)

 [ ] vapp(virtual application) market

## Directories

* `ACLibs`:Archicad Python APIs
* `APPS`:vapp(virtual application) install dirs
* `Env`:python2.7 installer 

## Group

* [graphisoft-python](https://github.com/graphisoft-python)


## Archicad Modules

* [GSRoot(v:0.0.1 Beta)](https://github.com/graphisoft-python/GSRoot)
* [DGLib(v:0.0.1 Beta)](https://github.com/graphisoft-python/DGLib)

