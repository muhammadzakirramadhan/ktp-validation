import core.application as model

class Router:
    @staticmethod
    def run(app):
        @app.route('/')
        def home():
            return {
            'message':'Tugas Kelompok Python A.I Dengan Ocr Studi Kasus KYC Extract'
            }

        @app.route('/v1/valid', methods=['POST'])
        def uploads():
            return model.ocr_ktp()    