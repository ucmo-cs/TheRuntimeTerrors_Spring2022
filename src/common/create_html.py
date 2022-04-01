import json
class MakeJson:
    def make_json(self):
        # Get JSON File and Save As Dictionary Called Data
        # response = requests.get('http://127.0.0.1:5000/riskassessments')
        # data = response.json()
        f = open('src/common/risk_assessment.json')
        data = json.load(f)

        # Create HTML Document
        f = open('src/models/index.html','w')

        html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Flight Risk Assessment Tool</title>
            </head>
            <body>
            <form>
                <label for="deleteID">Delete ID:</label>
                <input type="text" id="deleteID" name="deleteID"><br><br>
                <input type="submit" value="Submit" onclick="deleteByID()">
            </form>
        """

        # Create Form
        html = html + """
                <form>
        """

        # Create Flight Information Fields
        html = html + """
                    <h1>Flight Information</h1>
        """
        # Create Input Box For Each Flight Information Field
        for field in data['FlightInformation'].keys():
            html = html + """
                    <label for='""" + field + """'>""" + field + """: </label><br>
                    <input type="text" id='""" + field + """' name='""" + field + """'><br><br>
            """

        html = html + """
                    <h1>Pilot Qualifications and Experience</h1>
        """

        for field in data['PilotQualificationsAndExperience']:
            html = html + """
                    <label for='""" + field['name'] + """'>""" + field['descrip'] + """: </label>
                    <select id='""" + field['name'] + """' name='""" + field['name'] + """'>"""
            for x in range(field['maxVal']+1):
                html = html + """
                        <option value = '""" + str(x) + """'>""" + str(x) + """</option>"""

            html = html + """
                    </select><br><br>
            """

        html = html + """
                    <h1>Operating Environment</h1>
        """

        for field in data['OperatingEnviroment']:
            html = html + """
                    <label for='""" + field['name'] + """'>""" + field['descrip'] + """: </label>
                    <select id='""" + field['name'] + """' name='""" + field['name'] + """'>"""
            for x in range(field['maxVal']+1):
                html = html + """<option value = '""" + str(x) + """'>""" + str(x) + """</option>"""

            html = html + """
                    </select><br><br>
            """

        html = html + """
                    <h1>Equipment</h1>
        """

        for field in data['Equipment']:
            html = html + """
                    <label for='""" + field['name'] + """'>""" + field['descrip'] + """: </label>
                    <select id='""" + field['name'] + """' name='""" + field['name'] + """'>"""
            for x in range(field['maxVal']+1):
                html = html + """<option value = '""" + str(x) + """'>""" + str(x) + """</option>"""

            html = html + """
                    </select><br><br>
            """

        # End Form
        html = html + """
                    <input type="submit" onclick="createByID()">
                </form>
        """

        # Finish HTML Document
        html = html + """
                <script type="text/javascript">
                    function deleteByID() {
                        var id = document.getElementById("deleteID").value;
                        fetch('http://127.0.0.1:5000/riskassessments/delete/' + id, {
                            method: 'DELETE'
                        });
                    }
                    function createByID() {
                        var tripNumber = document.getElementById("Release/Trip #").value;
                        fetch('http://127.0.0.1:5000/submit_risk_assessment' + tripNumber, {
                            method: 'POST'
                        });
                    }
                </script>
            </body>
        </html>
        """

        # Render HTML Document Called index.html
        f.write(html)
        f.close()