import requests
from uuid import uuid4
class Bypass():
	def __init__(self):
		self.username=input("Username: ")
		self.passowrd =input("Password: ")
		##############To
	def login(self):
		# Login Acc
		url_login = "https://i.instagram.com/api/v1/accounts/login/"
		headers_login = {
			'User-Agent':'Instagram 103.1.0.15.119 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-G988N; z3q; exynos8895; en_US; 164094540)'
			}	

		data_login= {
			'uuid':uuid4(),
			'password':self.passowrd,
			'username':self.username,
			'device_id':uuid4(),
			'from_reg':'false',
			'_csrftoken':'missing',
			'login_attempt_count':'0'
			}
		req_login = requests.post(url=url_login,data=data_login,headers=headers_login)

		if 'logged_in_user' in req_login.text:
					print(f"[+] Logged in with {self.username}")
					self.session_id = req_login.cookies.get("sessionid")
					self.get_csrftoken = req_login.cookies.get("csrftoken")
					self.info()
		else:
			print(req_login.text)
			# Try Again Login ..
			return Bypass()
			
	def info(self):
		change_name=input("New Name : ")
		# Change Name ..
		url_user='https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
		header_user={		
			'Cookie': f'sessionid={self.session_id}',
			'X-Ig-Capabilities':'3brTvw==',
			'X-Ig-App-Id': '567067343352427',
			'User-Agent': 'Instagram 103.1.0.15.119 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-G988N; z3q; exynos8895; en_US; 164094540)',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			}

		req_user = requests.get(url=url_user,headers=header_user)
		if "user" in req_user.text and '"status":"ok"' in req_user.text:
			email = req_user.json()['user']['email']
			full_name = req_user.json()['user']['full_name']
			phone_number = req_user.json()['user']['phone_number']
			biography = req_user.json()['user']['biography']
			external_url = req_user.json()['user']['external_url']
			
			
			url_edit = 'https://i.instagram.com/api/v1/accounts/edit_profile/'

			header_edit = {
				'Host': 'i.instagram.com',
				'Cookie': f'sessionid={self.session_id}',
				'X-Ig-Capabilities':'3brTvw==',
				'User-Agent': 'Instagram 103.1.0.15.119 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-G988N; z3q; exynos8895; en_US; 164094540)',
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				}

			data_edit = {
				"external_url":external_url,
				"phone_number":phone_number,
				"username":self.username,
				"first_name":change_name,
				"_csrftoken": self.get_csrftoken,
				"_uid":"48403763438",
				"device_id":uuid4(),
				"_uuid":uuid4(),
				"biography":biography,
				"email":email
				}

			req_edit = requests.post(url=url_edit,data=data_edit,headers=header_edit)
			if "user" in req_edit.text and '"status":"ok"' in req_user.text:
				full_name = req_edit.json()['user']['full_name']
				if full_name == change_name:
					print(f"has changed to {change_name}")
					exit("Press Enter To Exit ..")
					# End 
			else:
				print(req_edit.text)
				# return Try Again
					
if __name__ == '__main__':
	r1 = Bypass().login()