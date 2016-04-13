ModuleName: CMP-murgen  



# Module

* CMP-murgen

## Name

murgen-dev-kit

## Description

Getting a home-made open-source ultrasound machine (dev-kit) up and running in your garage / hackerspace / fablab for less than 500$ for the beaglebone black. 

## Narrative

This project is born from a fork from the echOpen project (which aims at providing a low cost, open source ultrasound tool for doctors), with a specific target of providing a technological kit to allow scientists, academics, hackers, makers or OSH fans to hack their way to ultrasound imaging.

# Function: 

The murgen dev-kit sti

# Solutions

(list of solutions, by cliquing it open the corresponding page or dropdown list)

## Constraints 
(contraintes de type commande logique ou alimentation du module)

## Pros

* Dense electronic board
* Use of ICs for all non-trivial functions
* Limited costs (130€ of components + PCB)
* Theoritically compatible with the BeagleBone Black.

## Cons

* Debug is taking time
* PRUs software not yet 

# Interfaces

## Input

* 5V from the CMP-murgen-alim
* 3.3V from the CMP-murgen-alim
* Interfacing with a Trinket Pro: CMP-murgen-trinket
* Transducer: CMP-murgen-transducer

## Output

* Transducer: CMP-murgen-transducer
* Servomotor: CMP-murgen-servo
* Analog outputs on the different TestPoints: CMP-murgen-bitscope

# Versioning

* Version: V1.0
* Date: 19/02/2016
* Technology: Assembling ICs
* Language: python, for the signal processing
* Contributor: Kelu, Murgen, Sofian

# ToDos

* PRUs software
