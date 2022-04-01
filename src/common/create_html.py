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
                <form id="riskForm">
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
                    <input id="submitButton" type="submit">
                </form>
        """

        # Finish HTML Document
        html = html + """
                <script type="text/javascript">
                    const risk Form = document.querySelector("#riskForm");
                    if (riskForm) {
                        riskForm.addEventListener("submit", function(e) {
                            submitform(e, this);
                        });
                    }
                    
                    function buildJsonFormData(form) {
                        const jsonFormData = { };
                        for (const pair of new FormData(form)) {
                            jsonFormData[pair[0]] = pair[1];
                        }
                        return jsonFormData;
                    }
                    
                    async performPostHttpRequest(fetchLink, header, body) {
                        if (!fetchLink || !headers || !body) {
                            // throw new Error
                        }
                        
                        try {
                            const rawResponse = await fetch(fetchLink, {
                                method: "POST",
                                body: JSON.stringify(body)
                            });
                            const content = await rawResponse.json();
                            return content;
                        }
                    }
                    
                    async function submitForm(e, form) {
                        e.preventDefault();
                        const submitButton = document.getElementById("submitButton");
                        submitButton.disabled = true;
                        setTimeout(() => submitButton.disabled = false, 2000);
                        const jsonFormData = buildJsonFormData(form);
                        const response = await fetchService.performnPostHttpRequest("http://127.0.0.1:5000", headers, jsonFormData);
                        console.log(response);
                    }
                </script>
            </body>
        </html>
        """

        # Render HTML Document Called index.html
        f.write(html)
        f.close()