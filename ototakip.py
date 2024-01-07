import requests
import time

def create_account(username, password):
    # TikTok API'sine POST isteği göndererek yeni bir hesap oluşturur.
    url = "https://www.tiktok.com/api/v2/auth/signup"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    data = {
        "username": username,
        "password": password,
        "phone_number": "",
        "email": "",
        "country_code": "",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def follow_account(username):
    # TikTok API'sine POST isteği göndererek verilen kullanıcıyı takip eder.
    url = "https://www.tiktok.com/api/v2/user/follow"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    data = {
        "user_id": username,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def main():
    # TikTok profil linkini iste.
    print("TikTok profil linkinizi girin:")
    link = input()

    # 100 hesap oluşturun.
    for i in range(100):
        # Rastgele bir kullanıcı adı ve şifre oluşturun.
        username = "random_user_" + str(i)
        password = "random_password_" + str(i)

        # Hesabı oluşturun.
        response = create_account(username, password)

        # Hesabın oluşturulduğunu doğrulayın.
        if response.get("code") == 0:
            print("Hesap oluşturuldu:", username)
        else:
            print("Hesap oluşturulamadı:", response)

    # Verilen linkteki hesabı takip edin.
    response = follow_account(link)

    # Takibin başarılı olduğunu doğrulayın.
    if response.get("code") == 0:
        print("Hesap takip edildi:", link)
    else:
        print("Hesap takip edilemedi:", response)

if __name__ == "__main__":
    main()
