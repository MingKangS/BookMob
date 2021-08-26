import jwt, datetime
from .config import SECRET

def create_token(user_id):
	payload = {
		'id': user_id,
		'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
		'iat': datetime.datetime.utcnow()
	}

	token = jwt.encode(payload, SECRET, algorithm='HS256')
	return token