from flask import Flask,request,jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
app=Flask(__name__)
CORS(app)

@app.route("/result",methods=["POST"])

def result():

    
    
    Board=request.form.get('Board')
    total_marks=request.form.get("total_marks")

    
    if Board and total_marks:
        file="D:/login_nodejs/views/database.csv"
        df=pd.read_csv(file)
        df=df.drop(["S No"],axis=1)
        boards = pd.Categorical(df['Board'].unique())
        sum_dict = {}
        for i in boards:
            part_df = df[df['Board'] == i]
            sum = 0
            sum += part_df['Maths'].sum()
            sum += part_df['Science'].sum()
            sum += part_df['English'].sum()
            sum += part_df['Social Science'].sum()
            sum += part_df['Language Subject Marks'].sum()
            sum += part_df['Optional Subject Marks'].sum()
            sum_dict[i] = sum/(part_df.shape[0])
        dev_dict = {}
        df['Total'] = df['English']+df['Maths']+df['Science']+df['Social Science']+df['Language Subject Marks']+df['Optional Subject Marks']
        for i in boards:
            part_df = df[df['Board'] == i]
            var=0
            for index, row in part_df.iterrows():
                var+=(row['Total']-sum_dict[row['Board']])**2
            dev_dict[i] = (var/len(part_df))**(0.5)
            dev_dict
        deviation = dev_dict[Board]
        mean = sum_dict[Board]

        z1 = (int(total_marks)-mean)/deviation
        standard = (z1*100)+500
        return jsonify({"Data":standard})
    
    return jsonify({'error': 'Invalid file format. Please upload a CSV file'})




if __name__=='__main__':
    app.run(debug=True,port=2000)