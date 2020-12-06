import core.application as model

class Router:
    @staticmethod
    def run(app):
        @app.route('/')
        def home():
            return {
                'message':'Tugas Kelompok Dengan Python, Studi Kasus Extract KTP & Validasi KTP Dengan Metode OCR',
                'developer':'Muhammad Zakir Ramadhan'
            }

        @app.route('/api/extract_ktp', methods=['POST'])
        def extract():
            return model.extract_ktp()    

        @app.route('/api/valid', methods=['POST'])
        def valid():
            return model.valid_ktp()

        @app.route('/api/match', methods=['POST'])
        def match():
            return model.match_ktp_nik()    