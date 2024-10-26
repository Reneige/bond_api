"""
written by Rene Alby - 26/10/2024

"""

import uvicorn
from config import HOST, PORT

def main():
	uvicorn.run(
		"api.endpoints:app",
		host=HOST,
		port=PORT,
		reload=True,
	)

if __name__=="__main__":
	main()