import json
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
        """

        # Create Form
        html = html + """
                <form id="riskForm">
        """

        # Create Flight Information Fields
        html = html + """
                    <div class = "header"><h1>Flight Risk Assessment Tool</h1></div>
                    <div class = "container"><div class="containerleft">
        """
        # Create Input Box For Each Flight Information Field
        count = 1
        for field in data['FlightInformation']:
            if count == 4:
                html = html + """
                    </div><div class = "containerright">
                """
            html = html + """
                    <label for='""" + field['name'] + """'>""" + field['descrip'] + """ </label>
                    <input type="text" id='""" + field['name'] + """' name='""" + field['name'] + """' placeholder='Enter """ + field['descrip'] + """'><br><br>
            """
            count = count + 1

        html = html + """
                    </div></div>
                    <button type="button" class="collapsible">Pilot Qualifications and Experience</button>
                    <div class="content"><br>
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
                    </div>
                <div class ="container"></div>
    
                <button type="button" class="collapsible">Operating Environment</button>
                <div class="content">
                <br>
        """

        for field in data['OperatingEnviroment']:
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
                    </div>
                    <div class ="container"></div>

                    <button type="button" class="collapsible">Equipment</button>
                    <div class="content">
                    <br>
        """

        for field in data['Equipment']:
            html = html + """
                    <label for='""" + field['name'] + """'>""" + field['descrip'] + """: </label>
                    <select id='""" + field['name'] + """' name='""" + field['name'] + """'>"""
            for x in range(field['maxVal']+1):
                html = html + """
                <option value = '""" + str(x) + """'>""" + str(x) + """</option>"""

            html = html + """
                    </select><br><br>
            """

        # End Form
        html = html + """
                    </div>
                    <div class ="container"></div>
        
                    <br><br>
            
                    <div class = "submit-container">
                    <input id="submitButton" type="submit" class = "submit">
                    </div>
                    <p id = "riskContainer"></p>
                </form>
        """

        # Finish HTML Document
        html = html + """
                <script type="text/javascript">
                    const riskForm = document.querySelector("#riskForm");
                    if (riskForm) {
                        riskForm.addEventListener("submit", function(e) {
                            submitForm(e, this);
                        });
                    }
                    
                    function buildJsonFormData(form) {
                        const jsonFormData = { };
                        for (const pair of new FormData(form)) {
                            jsonFormData[pair[0]] = pair[1];
                        }
                        return jsonFormData;
                    }
                    
                    async function performPostHttpRequest(fetchLink, body) {                        
                        try{
                            const rawResponse = await fetch(fetchLink, {
                                method: "POST",
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(body)
                            })
                            .then(response => response.json()) 
                            .then(json => displayRiskValue(json));
                            const content = await rawResponse.json();
                            return content;
                        }catch(error){
                            console.error(error);
                        }
                    }
                    
                    async function submitForm(e, form) {
                        e.preventDefault();
                        const submitButton = document.getElementById("submitButton");
                        submitButton.disabled = true;
                        setTimeout(() => submitButton.disabled = false, 2000);
                        const jsonFormData = buildJsonFormData(form);
                        const response = await performPostHttpRequest("http://127.0.0.1:5000/submit_risk_form", jsonFormData);
                        console.log(response);
                    }
                    
                    function displayRiskValue(json) {
                        var paras = document.getElementById("riskContainer");                 
                    
                        var hs = document.head.getElementsByTagName('style');
                        for (var i=0, max = hs.length; i < max; i++) {
                            hs[i].parentNode.removeChild(hs[i]);
                        }
                        
                        paras.innerHTML = "Total Risk Value: " + json['risk value'] + "";
                        if (json['risk value'] < 15) {
                            paras.innerHTML += "<br>Good to fly";
                            var styles = "#riskContainer  { color: green; }";
                        }
                        else if (json['risk value'] < 20) {
                            paras.innerHTML += "<br>Exercise caution";
                            var styles = "#riskContainer  { color: orange; }";
                        }
                        else {
                            paras.innerHTML += "<br>Do not fly";
                            var styles = "#riskContainer { color: red; }";
                        }
                                                
                        var styleSheet = document.createElement("style");
                        styleSheet.innerText = styles;
                        document.head.appendChild(styleSheet);
                    }
                    
                    var coll = document.getElementsByClassName("collapsible");
                    var i;
                    
                    for (i = 0; i < coll.length; i++) {
                      coll[i].addEventListener("click", function() {
                        this.classList.toggle("active");
                        var content = this.nextElementSibling;
                        if (content.style.display === "flex") {
                          content.style.display = "none";
                        } else {
                          content.style.display = "flex";
                        }
                      });
                    }
                </script>
                <style>
                    html,
                    body{
                        margin: 0px;
                        font-family: Arial, Helvetica, sans-serif;
                    }
                    h1{
                        color: whitesmoke;
                    }
                    .header{
                        background-color: #32384e;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 55px;
                    }
                    .containerleft{
                        display: inline;
                        text-align: right;
                        margin-bottom: 20px;
                    }
                    .containerright{
                        text-align: right;
                        width: 50%;
                        margin-bottom: 20px;
                    }
                    .container{
                        display: flex;
                        margin-top: 20px;
                        margin-left: 2.5%;
                        width: 95%;
                        justify-content: center;
                        align-items: center;
                        border-bottom-style: solid;
                        border-bottom-color: rgb(226, 226, 226);
                        border-bottom-width: 2px;
                    }
                    input{
                        border-radius: 8px;
                        height: 20px;
                        padding: 5px;
                        border-color: rgb(226, 226, 226);
                        border-style: solid;
                        width: 300px;
                    }
                    input:focus,
                    select:focus{
                        outline:none;
                        border-color: #1e222f;
                        border-width: 1px;
                        box-shadow: .5px .5px 5px .5px rgb(51, 67, 110);
                    }
                    /* Style the button that is used to open and close the collapsible content */
                    .collapsible {
                        background-color: #eee;
                        color: #444;
                        cursor: pointer;
                        padding: 18px;
                        width: 95%;
                        border: none;
                        text-align: left;
                        outline: none;
                        font-size: 15px;
                        margin-top: 20px;
                        margin-left: 2.5%;
                      }
                      
                      /* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
                      .active, .collapsible:hover {
                        background-color: #ccc;
                      }
                      
                      /* Style the collapsible content. Note: hidden by default */
                      .content {
                        padding: 0 18px;
                        overflow: hidden;
                        display: none;
                        background-color: #f1f1f1;
                        width: 92.5%;
                        margin-left: 2.5%;
                        flex-wrap: wrap;
                        align-content: center;
                      }
                      .collapsible:after {
                        content: '+'; /* Unicode character for "plus" sign (+) */
                        font-size: 13px;
                        color: white;
                        float: right;
                        margin-left: 5px;
                      }
                      
                      .active:after {
                        content: "-"; /* Unicode character for "minus" sign (-) */
                      }
                      .submit-container{
                        width: 100%;
                        text-align: center;
                    }
                    .submit{
                        height: 50px;
                        width: 150px;
                        border-radius: 20px;
                        background-color:#32384e;
                        color: whitesmoke;
                        border-width: 1px;
                    }
                    .submit:hover{
                        background-color: #1e222f;
                        color:whitesmoke;
                    }
                    select{
                        border-radius: 8px;
                        width:40px;
                        height: 40px;
                        text-align: center;
                        margin: 5px 12px;
                    }
                    label{
                        width: 375px;
                        margin:15px 0px;
                    }
                    p{
                        text-align: center;
                    }
                      
                </style>
            </body>
        </html>
        """

        # Render HTML Document Called index.html
        f.write(html)
        f.close()