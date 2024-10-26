"""
written by Rene Alby - 26/10/2024

"""

import uvicorn

def main():
	uvicorn.run(
		"api.endpoints:app",
		host="127.0.0.1",
		port=8000,
		reload=True,
	)

if __name__=="__main__":
	main()