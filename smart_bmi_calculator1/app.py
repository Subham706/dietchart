from flask import Flask, render_template, request, session, redirect, url_for
import os
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Set the Google Generative AI API key directly for testing
os.environ["GOOGLE_API_KEY"] = "AIzaSyAfPybezBw-gGU7NG3lP2hPxBwjf1Kb3Ac"
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route('/')
def input_form():
    return render_template('input_form.html')

@app.route('/generate_diet_chart', methods=['POST'])
def generate_diet_chart():
    try:
        age = request.form['age']
        gender = request.form['gender']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        dietary_preferences = request.form['dietary_preferences']
        health_conditions = request.form['health_conditions']
        goals = request.form['goals']
        name = request.form['name']

        # Calculate BMI
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        bmi = round(bmi, 2)

        user_message = (
            f"Provide a detailed 7-days diet chart in tabular format with columns for Day, Meal, Food, Quantity, and Notes. "
            f"Each day must include 5 meals: Breakfast, Mid-morning Snack, Lunch, Evening Snack, and Dinner. "
            f"The diet chart is for a {age}-year-old {gender} named {name} with a BMI of {bmi}. "
            f"Dietary preferences: {dietary_preferences}. Health conditions: {health_conditions}. Goals: {goals}."
        )
        
        # Use the same conversation history for consistency
        convo = model.start_chat(history=[])
        convo = convo.send_message(user_message)
        response_text = convo.text

        # Extracting input details
        input_details = {
            'name': name,
            'age': age,
            'gender': gender,
            'weight': weight,
            'height': height,
            'dietary_preferences': dietary_preferences,
            'health_conditions': health_conditions,
            'goals': goals,
            'bmi': bmi
        }

        # Process the response to convert it into a table
        lines = response_text.split('\n')
        table_rows = []
        for line in lines:
            if '|' in line:
                columns = line.split('|')
                clean_columns = [col.replace('*', '').replace('---', '').strip() for col in columns]  # Remove '*' and '---' symbols
                table_rows.append(clean_columns)

        # Remove the first row if it contains headings
        if table_rows and ('day' in table_rows[0][1].lower() or 'meal' in table_rows[0][2].lower()):
            table_rows = table_rows[1:]

        # Remove empty rows
        table_rows = [row for row in table_rows if any(row)]

        # Generate HTML table
        table_html = "<table><thead><tr><th>Day</th><th>Meal</th><th>Food</th><th>Quantity</th><th>Notes</th></tr></thead><tbody>"
        for row in table_rows:
            if len(row) >= 5:  # Ensure that each row has at least 5 columns
                table_html += "<tr>"
                for col in row:
                    table_html += f"<td>{col.strip()}</td>"
                table_html += "</tr>"
        table_html += "</tbody></table>"

        # Store data in session
        session['diet_chart'] = {
            'table_html': table_html,
            'input_details': input_details
        }

        return redirect(url_for('show_output'))

    except Exception as e:
        response_text = f"An error occurred: {e}"
        return render_template('output.html', table_html="", input_details={}, error_message=response_text)

@app.route('/output')
def show_output():
    # Retrieve stored data from session
    diet_chart_data = session.get('diet_chart')
    if diet_chart_data:
        table_html = diet_chart_data.get('table_html', "")
        input_details = diet_chart_data.get('input_details', {})
        return render_template('output.html', table_html=table_html, input_details=input_details)
    else:
        return redirect(url_for('input_form'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)