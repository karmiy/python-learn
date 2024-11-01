import subprocess


def get_wifi_passwords():
    # 获取所有 Wi-Fi 配置的名称
    wifi_profiles = subprocess.check_output(
        "netsh wlan show profiles", shell=True
    ).decode("mbcs")
    profiles = [
        line.split(":")[1].strip()
        for line in wifi_profiles.splitlines()
        if "所有用户配置文件" in line
    ]

    wifi_passwords = {}
    for profile in profiles:
        # 获取 Wi-Fi 配置的密码
        profile_info = subprocess.check_output(
            f'netsh wlan show profile name="{profile}" key=clear', shell=True
        ).decode("mbcs")
        password_lines = [
            line for line in profile_info.splitlines() if "关键内容" in line
        ]

        # 提取密码，如果有的话
        if password_lines:
            password = password_lines[0].split(":")[1].strip()
        else:
            password = None

        wifi_passwords[profile] = password

    return wifi_passwords


# 打印结果
wifi_passwords = get_wifi_passwords()
for wifi, password in wifi_passwords.items():
    print(f"Wi-Fi: {wifi}, Password: {password}")
