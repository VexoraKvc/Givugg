import requests

# Ganti dengan token API Linode Anda
TOKEN = 'bd9f46893f0a27bfd364ed4edeee75e45adcae4e6d871db6f3d5128c654d18e0

# URL dasar untuk API Linode
BASE_URL = 'https://api.linode.com/v4/'

def get_available_images():
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.get(BASE_URL + 'images', headers=headers)
    if response.status_code == 200:
        images = response.json()['data']
        for image in images:
            print(f"ID: {image['id']}, Label: {image['label']}")
    else:
        print(f"Gagal mendapatkan daftar gambar. Kode status: {response.status_code}")
        print(response.text)

def create_linode_vm(label, region, type, image, root_pass):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'label': label,
        'region': region,
        'type': type,
        'image': image,
        'root_pass': root_pass,
    }
    response = requests.post(BASE_URL + 'linode/instances', json=data, headers=headers)
    if response.status_code == 200:
        print("VM berhasil dibuat!")
    else:
        print(f"Gagal membuat VM. Kode status: {response.status_code}")
        print(response.text)

def list_linode_vm():
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.get(BASE_URL + 'linode/instances', headers=headers)
    if response.status_code == 200:
        instances = response.json()['data']
        print("Daftar VM:")
        for instance in instances:
            print(f"Label: {instance['label']}, ID: {instance['id']}")
    else:
        print(f"Gagal mendapatkan daftar VM. Kode status: {response.status_code}")
        print(response.text)

def restart_linode_vm(label):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.post(BASE_URL + f'linode/instances/{label}/reboot', headers=headers)
    if response.status_code == 200:
        print(f"VM dengan label {label} berhasil di-restart!")
    else:
        print(f"Gagal melakukan restart VM. Kode status: {response.status_code}")
        print(response.text)

def delete_linode_vm(label):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.delete(BASE_URL + f'linode/instances/{label}', headers=headers)
    if response.status_code == 204:
        print(f"VM dengan label {label} berhasil dihapus!")
    else:
        print(f"Gagal menghapus VM. Kode status: {response.status_code}")
        print(response.text)

def main():
    print("Selamat datang di Linode CLI!")
    print("Fitur yang tersedia:")
    print("1. create - Membuat VM baru")
    print("2. vmlist - Melihat daftar VM")
    print("3. vmrestart - Me-restart VM")
    print("4. vmdelete - Menghapus VM")
    
    option = input("Silakan pilih fitur yang akan digunakan: ")
    
    if option == 'create':
        label = input("Masukkan label untuk VM: ")
        region = input("Masukkan region (misalnya, us-east): ")
        type = input("Masukkan jenis VM (misalnya, g6-standard-1): ")
        image = input("Masukkan ID gambar (image) untuk VM: ")
        root_pass = input("Masukkan password root untuk VM: ")
        create_linode_vm(label, region, type, image, root_pass)
    elif option == 'vmlist':
        list_linode_vm()
    elif option == 'vmrestart':
        label = input("Masukkan label VM yang akan di-restart: ")
        restart_linode_vm(label)
    elif option == 'vmdelete':
        label = input("Masukkan label VM yang akan dihapus: ")
        delete_linode_vm(label)
    else:
        print("Fitur yang Anda pilih tidak valid.")

if __name__ == "__main__":
    main(