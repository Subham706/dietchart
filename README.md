# Smart BMI Calculator and Personalized Diet Plan Recommender

## Overview
The Smart BMI Calculator and Personalized Diet Plan Recommender is a web application designed to help users calculate their Body Mass Index (BMI) and receive personalized diet recommendations based on their BMI and activity level. The application uses Python and Flask for the backend, HTML and CSS for the frontend, and the Gemini API to fetch detailed diet charts.

## Features
- **BMI Calculation**: Accurate calculation of BMI based on user input (height, weight).
- **Personalized Diet Recommendations**: Tailored diet plans according to BMI categories (underweight, normal weight, overweight, obese).
- **Gemini API Integration**: Fetches comprehensive diet charts.
- **User-Friendly Interface**: Clean and intuitive design.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **API**: Gemini API

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Smart-BMI-Calculator-Diet-Plan-Recommender.git
    cd Smart-BMI-Calculator-Diet-Plan-Recommender
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    flask run
    ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter your height, weight, age, and activity level.
3. Click "Submit" to get your BMI and personalized diet recommendations.

## Screenshots
### Input Form
![Input Form](![Screenshot 2024-07-04 221252](https://github.com/Subham706/dietchart/assets/172019793/d4863454-c3c1-4414-91a2-534ebcbd7b47)
)

### Result Page
![Result Page](![Screenshot 2024-07-04 223659](https://github.com/Subham706/dietchart/assets/172019793/4be1a588-7523-4638-9515-fd1a93e1a3e6)
)

## Sample Inputs and Outputs
### Example 1
- **Input**:
  - Height: 170 cm
  - Weight: 65 kg
  - Age: 25
  - Activity Level: Moderately Active
- **Output**:
  - BMI: 22.5
  - Diet Recommendations: Balanced diet including fruits, vegetables, lean proteins, and whole grains.
  - Diet Chart: [Detailed chart fetched from Gemini API]

### Example 2
- **Input**:
  - Height: 160 cm
  - Weight: 80 kg
  - Age: 30
  - Activity Level: Lightly Active
- **Output**:
  - BMI: 31.2
  - Diet Recommendations: Strict diet plan with reduced calorie intake.
  - Diet Chart: [Detailed chart fetched from Gemini API]

## Challenges and Solutions
### Accuracy in BMI Calculation
**Challenge**: Ensuring precise BMI calculations.
**Solution**: Implemented and tested the BMI formula thoroughly.

### Personalized Diet Recommendations
**Challenge**: Providing relevant diet plans.
**Solution**: Researched nutritional guidelines and integrated the Gemini API.

### User Interface Design
**Challenge**: Creating a user-friendly interface.
**Solution**: Used HTML and CSS for a clean layout and conducted usability testing.

### Integration with Gemini API
**Challenge**: Fetching diet charts from an external API.
**Solution**: Implemented secure API calls and processed JSON responses.

## Future Enhancements
- Expand the range of diet plans.
- Integrate user authentication for personalized profiles.
- Add features like exercise recommendations and calorie tracking.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact:
- **Name**: Subham Panda
- **Email**:subhampanda250.gmail.com
- **LinkedIn**: [LinkedIn Profile]((https://www.linkedin.com/in/subham-panda-310ab5311/))

---

[GitHub Repository]((https://github.com/Subham706/dietchart))
