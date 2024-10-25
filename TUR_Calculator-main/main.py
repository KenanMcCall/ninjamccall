# İçe Aktarma
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')

# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size=size, 
                            lights=lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )

# Form sayfası
@app.route('/form')
def form():
    return render_template('form.html')

# Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Form verilerini al
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        date = request.form['date']

        # Verileri bir .txt dosyasına kaydet
        with open('form_data.txt', 'a', encoding='utf-8') as f:
            f.write(f'Name: {name}\n')
            f.write(f'Email: {email}\n')
            f.write(f'Address: {address}\n')
            f.write(f'Date: {date}\n')
            f.write('---------------------------\n')

        return 'Form successfully submitted!'
    except Exception as e:
        return f'An error occurred: {e}'

if __name__ == '__main__':
    app.run(debug=True)
