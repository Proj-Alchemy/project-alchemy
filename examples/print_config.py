import requests


def send_get(handle):
    url = "https://fierce-garden-89071.herokuapp.com/" + handle
    payload = {}
    headers = {"Authorization": "Basic YWxjaGVteTphbGNoZW15"}
    return requests.request("GET", url, headers=headers, data=payload)


def print_config(uuid):
    response = send_get("config/" + uuid)
    print(response.json()["config"])


def main():
    response = send_get("device/")
    for device in response.json()["results"]:
        uuid = device["id"]
        print(
            """
        ###########
        ## {0}  #
        ###########
        """.format(
                device["name"]
            )
        )
        print_config(uuid)


if __name__ == "__main__":
    main()
