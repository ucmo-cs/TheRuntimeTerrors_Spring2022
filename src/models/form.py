class Form():
    def __init__(self, request):
        self.flightDate = request['flightDate']
        self.tripNumber = request['tripNumber']
        self.tailNumber = request['tailNumber']
        self.departure = request['departure']
        self.destination = request['destination']
        self.captainLessThan200 = request['captainLessThan200']
        self.officerLessThan200 = request['officerLessThan200']
        self.singlePilot = request['singlePilot']
        self.capLess100in90 = request['capLess100in90']
        self.offLess100in90 = request['offLess100in90']
        self.duty12Hours = request['duty12Hours']
        self.flightTime = request['flightTime']
        self.crewRest = request['crewRest']
        self.verticalGuidance = request['verticalGuidance']
        self.circlingApproach = request['circlingApproach']
        self.publishedApproach = request['publishedApproach']
        self.mountainous = request['mountainous']
        self.controlTower = request['controlTower']
        self.uncontrolledAir = request['uncontrolledAir']
        self.alternatePort = request['alternatePort']
        self.elevation = request['elevation']
        self.wetRunway = request['wetRunway']
        self.contaiminatedRunway = request['contaiminatedRunway']
        self.winter = request['winter']
        self.twilight = request['twilight']
        self.night = request['night']
        self.stopDist = request['stopDist']
        self.repositioning = request['repositioning']
        self.popUp = request['popUp']
        self.international = request['international']
        self.weatherReport = request['weatherReport']
        self.storms = request['storms']
        self.turbulence = request['turbulence']
        self.visability = request['visability']
        self.rain = request['rain']
        self.snow = request['snow']
        self.ice = request['ice']
        self.surfaceWinds = request['surfaceWinds']
        self.crossWinds = request['crossWinds']
        self.brakeAction = request['breakAction']
        self.permit = request['permit']
        self.safetyItems = request['saftyItems']
        self.limitations = request['limitations']

    # @property
    # def data(self):
    #     return {
    #         'flightInformation':
    #             {
    #                 'date': self.flightDate,
    #                 'trip': self.tripNumber,
    #                 'tailNumber': self.tailNumber,
    #                 'departure': self.departure,
    #                 'destination': self.destination
    #             }
    #         ,
    #         'pilotQualificationsAndExperience': 
    #             {
    #                 'captainLessThan200': self.captainLessThan200,
    #                 'officerLessThan200': self.officerLessThan200,
    #                 'singlePilot': self.singlePilot,
    #                 'capLess100in90': self.capLess100in90,
    #                 'duty12Hours': self.duty12Hours,
    #                 'flightTime': self.flightTime,
    #                 'crewRest': self.crewRest
    #             }
    #         ,
    #         'operatingEnvironment':
    #             {
    #                 'verticalGuidance': self.verticalGuidance,
    #                 'circlingApproach': self.circlingApproach,
    #                 'publishedApproach': self.publishedApproach,
    #                 'mountianous': self.mountainous,
    #                 'controlTower': self.controlTower,
    #                 'uncontrolledAir': self.uncontrolledAir,
    #                 'alternatePort': self.alternatePort,
    #                 'elevation': self.elevation,
    #                 'wetRunway': self.wetRunway,
    #                 'contaminatedRunway': self.contaiminatedRunway,
    #                 'winter': self.winter,
    #                 'twilight': self.twilight,
    #                 'night': self.night,
    #                 'stopDist': self.stopDist,
    #                 'repositioning': self.repositioning,
    #                 'popUp': self.popUp,
    #                 'international': self.international,
    #                 'weatherReport': self.weatherReport,
    #                 'storms': self.storms,
    #                 'turbulence': self.turbulence,
    #                 'visability': self.visability,
    #                 'rain': self.rain,
    #                 'snow': self.snow,
    #                 'ice': self.ice,
    #                 'surfaceWinds': self.surfaceWinds,
    #                 'crossWinds': self.crossWinds,
    #                 'brakeAction': self.brakeAction,
    #             }
    #         ,
    #         'equipment':
    #             {
    #                 'permit': self.permit,
    #                 'safetyItems': self.safetyItems,
    #                 'limitations': self.limitations
    #             }
            
    #     }

    @property
    def data(self):
        return {
            "FlightInformation": 
                {
                'date': self.flightDate,
                'trip': self.tripNumber,
                'tailNumber': self.tailNumber,
                'departure': self.departure,
                'destination': self.destination
                },
            "PilotQualificationsAndExperience": [
                {
                "name": "CaptainLessThan200",
                "descrip": "Captain with less than 200 hours in type",
                "maxVal": 5,
                "inputVal": self.captainLessThan200
                },
                {
                "name": "OfficerLessThan200",
                "descrip": "First Officer with less than 200 hours in type",
                "maxVal": 5,
                "inputVal": self.officerLessThan200
                },
                {
                "name": "SinglePilot",
                "descrip": "Single Pilot Flight",
                "maxVal": 5,
                "inputVal": self.singlePilot
                },
                {
                "name": "CapLess100in90",
                "descrip": "Captain with less than 100 hours last 90 days",
                "maxVal": 3,
                "inputVal": self.capLess100in90
                },
                {
                "name": "OffLess100in90",
                "descrip": "Officer with less than 100 hours in last 90 days",
                "maxVal": 3,
                "inputVal": self.offLess100in90
                },
                {
                "name": "Duty12Hours",
                "descrip": "Duty day greater than 12 hours",
                "maxVal": 4,
                "inputVal": self.duty12Hours
                },
                {
                "name": "FlightTime",
                "descrip": "Flight time greater than 8 hours in the duty day",
                "maxVal": 4,
                "inputVal": self.flightTime
                },
                {
                "name": "CrewRest",
                "descrip": "Crew Rest less than 10 hours prior to the duty day",
                "maxVal": 5,
                "inputVal": self.crewRest
                }
            ],
            "OperatingEnviroment": [
                {
                "name": "VerticalGuidance",
                "descrip": "VOR/GPS/LOC/ADF (Best approach available w/o vertical guidance)",
                "maxVal": 3,
                "inputVal": self.verticalGuidance
                },
                {
                "name": "CirclingApproach",
                "descrip": "Circling approach (best available approach)",
                "maxVal": 4,
                "inputVal": self.circlingApproach
                },
                {
                "name": "PublishedApproach",
                "descrip": "No published approaches",
                "maxVal": 4,
                "inputVal": self.publishedApproach
                },
                {
                "name": "Mountianous",
                "descrip": "Mountainous airport",
                "maxVal": 5,
                "inputVal": self.mountainous
                },
                {
                "name": "ControlTower",
                "descrip": "Control tower not operational at ETA or ETD",
                "maxVal": 3,
                "inputVal": self.controlTower
                },
                {
                "name": "UncontrolledAir",
                "descrip": "Uncontrolled airport",
                "maxVal": 5,
                "inputVal": self.uncontrolledAir
                },
                {
                "name": "AlternatePort",
                "descrip": "Alternate airport not selected",
                "maxVal": 4,
                "inputVal": self.alternatePort
                },
                {
                "name": "Elevation",
                "descrip": "Elevation of primary airport greater than 5000 ft. MSL)",
                "maxVal": 3,
                "inputVal": self.elevation
                },
                {
                "name": "WetRunway",
                "descrip": "Wet runway",
                "maxVal": 3,
                "inputVal": self.wetRunway
                },
                {
                "name": "ContaminatedRunway",
                "descrip": "Contaminated runway",
                "maxVal": 3,
                "inputVal": self.contaiminatedRunway
                },
                {
                "name": "Winter",
                "descrip": "Winter operation",
                "maxVal": 3,
                "inputVal": self.winter
                },
                {
                "name": "Twilight",
                "descrip": "Twilight operation",
                "maxVal": 2,
                "inputVal": self.twilight
                },
                {
                "name": "Night",
                "descrip": "Night operation",
                "maxVal": 5,
                "inputVal": self.night
                },
                {
                "name": "StopDist",
                "descrip": "Stopping distance greater than 80% of available runway",
                "maxVal": 5,
                "inputVal": self.stopDist
                },
                {
                "name": "Repositioning",
                "descrip": "Repositioning flight (no passengers or cargo)",
                "maxVal": 5,
                "inputVal": self.repositioning
                },
                {
                "name": "PopUp",
                "descrip": "Pop up trip (Less than 4 hours crew notice)",
                "maxVal": 3,
                "inputVal": self.popUp
                },
                {
                "name": "International",
                "descrip": "International operation",
                "maxVal": 2,
                "inputVal": self.international
                },
                {
                "name": "WeatherReport",
                "descrip": "No weather reporting at destination ",
                "maxVal": 5,
                "inputVal": self.weatherReport
                },
                {
                "name": "Storms",
                "descrip": "Thunderstorms at departure and/or destination",
                "maxVal": 4,
                "inputVal": self.storms
                },
                {
                "name": "Turbulence",
                "descrip": "Severe Turbulence",
                "maxVal": 5,
                "inputVal": self.turbulence
                },
                {
                "name": "Visability",
                "descrip": "Ceiling & visibility at destination less than 500 ft. / 2 sm",
                "maxVal": 3,
                "inputVal": self.visability
                },
                {
                "name": "Rain",
                "descrip": "Heavy rain at departure and/or destination",
                "maxVal": 5,
                "inputVal": self.rain
                },
                {
                "name": "Snow",
                "descrip": "Frozen precipitation at departure and/or destination",
                "maxVal": 3,
                "inputVal": self.snow
                },
                {
                "name": "Ice",
                "descrip": "Icing (moderate-severe)",
                "maxVal": 5,
                "inputVal": self.ice
                },
                {
                "name": "SurfaceWinds",
                "descrip": "Surface winds greater than 30 knots",
                "maxVal": 4,
                "inputVal": self.surfaceWinds
                },
                {
                "name": "CrossWinds",
                "descrip": "Crosswinds greater than 15 knots",
                "maxVal": 4,
                "inputVal": self.crossWinds
                },
                {
                "name": "BrakeAction",
                "descrip": "Runway braking action less than good",
                "maxVal": 5,
                "inputVal": self.brakeAction
                }
            ],
            "Equipment": [
                {
                "name": "Permit",
                "descrip": "Special Flight Permit Operation (ferry permit)",
                "maxVal": 3,
                "inputVal": self.permit
                },
                {
                "name": "MEL/CDL",
                "descrip": "MEL / CDL Items (items related to safety of flight)",
                "maxVal": 2,
                "inputVal": self.safetyItems
                },
                {
                "name": "Limitations",
                "descrip": "Special flight limitations based on AFM equipment limitations",
                "maxVal": 2,
                "inputVal": self.limitations
                }
            ]
        }