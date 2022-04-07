from unittest import TestCase
import RiskForm


class test(TestCase):
    def test_post(self):
        payload = {"flightDate":"1/2/23","tripnumber":"23","tailnumber":"432","departure":"MCI","destination":"LAX","captainLessThan200":"3","officerLessThan200":"0","singlePilot":"0","capLess100in90":"0","offLess100in90":"0","duty12Hours":"0","flightTime":"0","crewRest":"0","verticalGuidance":"0","circlingApproach":"0","publishedApproach":"0","mountainous":"0","controlTower":"2","uncontrolledAir":"0","alternatePort":"0","elevation":"0","wetRunway":"0","contaminatedRunway":"0","winter":"0","twilight":"0","night":"0","stopDist":"0","repositioning":"0","popUp":"0","international":"0","weatherReport":"3","storms":"0","turbulence":"0","visability":"0","rain":"0","snow":"0","ice":"0","surfaceWinds":"0","crossWinds":"0","breakAction":"0","permit":"2","safetyItems":"0","limitations":"0"}

        #initialize
        response = RiskForm.RiskForm(payload)