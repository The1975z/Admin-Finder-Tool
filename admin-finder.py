import requests
import argparse
import urllib3
from urllib.parse import urljoin
from colorama import Fore, Style, init
from requests.exceptions import ConnectionError
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

creator_name = "Dev Scottz"
creator_website = "https://xgcottz.com"

print(f"""{Fore.CYAN}
██████╗ ███████╗██╗   ██╗      ███████╗██╗███╗   ██╗██████╗ ███████╗
██╔══██╗██╔════╝██║   ██║      ██╔════╝██║████╗  ██║██╔══██╗██╔════╝
██████╔╝█████╗  ██║   ██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║███████╗
██╔═══╝ ██╔══╝  ╚██╗ ██╔╝╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║╚════██║
██║     ███████╗ ╚████╔╝       ██║     ██║██║ ╚████║██████╔╝███████║
╚═╝     ╚══════╝  ╚═══╝        ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝
                Admin Finder Tool by {creator_name} | {creator_website}
{Style.RESET_ALL}""")

generic_admin_paths = [
    "admin/", "admin/login", "administrator/", "admin1/", "admin2/", "user/login",
    "admin3/", "admin4/", "admin5/", "usuarios/", "usuario/", "administrator", 
    "moderator/", "webadmin/", "adminarea/", "bb-admin/", "adminLogin/", 
    "admin_area/", "panel-administracion/", "instadmin/", "memberadmin/", "wp-admin",
    "/admin.%XT%", "/login/", "/login.%XT%", "/adm/", "/admin/", "phpinfo.php", "site/login",
    "/adminitem/", "/adminitem.%XT%", "/adminitems/", "/adminitems.%XT%", 
    "/administrator.%XT%", "/administration/", "/administration.%XT%", 
    "/adminLogin/", "/adminlogin.%XT%", "/admin_area/admin.%XT%", "/admin_area/",
    "/admin_area/login.%XT%", "/access/", "/acct_login/", "/_adm_/", "/_adm/", 
    "/adm/", "/adm2/", "/_admin_/", "/_admin/", "/admin/", "/Admin/", "/ADMIN/", 
    "/phpMyAdmin/", "/phpmyadmin/", "/PMA/", "/admin/", "/dbadmin/", "/mysql/", 
    "/myadmin/", "/phpmyadmin2/", "/phpMyAdmin2/", "/phpMyAdmin-2/", "/php-my-admin/",
    "/backend/", "control-panel/", "/sysadmin/", "/management/", "/system/",
    "/security/", "super-admin/", "/root/", "/admin-dashboard/", "/admin-panel/",
     "admin-secret/", "admin-hidden/", "super-admin/", "root-access/", 
    "admin-master/", "system-control/", "secure-admin/", "management-panel/", 
    "admin-dashboard/", "control-center/", "backend-access/", "sys-admin/", 
    "admin-portal/", "network-admin/", "infrastructure-control/", "it-admin/", 
    "security-panel/", "admin-console/", "enterprise-admin/", "global-admin/", 
    "admin-restricted/", "top-secret-admin/", "admin-vault/", "admin-shield/", 
    "power-admin/", "admin-core/", "admin-ultra/", "admin-prime/", "admin-max/",
    "admin_control/", "admin-control/", "__admin/", "_admin/", "admin__/",
    "adm1n/", "4dm1n/", "admin_sys/", "sys_admin/", "admin_core/",
    "internal-admin/", "classified-admin/", "admin-bridge/", "admin-gateway/", 
    "admin-matrix/", "admin-nexus/", "admin-kernel/", "admin-central/", 
    "admin-mainframe/", "admin-fortress/", "admin-command/", "admin-headquarters/"
]

php_admin_paths = [
    "admin.php", "administrator/index.php", "admin/login.php", "adminpanel.php", 
    "cpanel.php", "login.php", "admin_area/login.php", "admin_area/index.php",
    "controlpanel.php", "admincp.php", "adminLogin.php", "adm.php", "adminpage.php",
    "admin/index.php", "admin/login.php", "admin_area/admin.php", "admin_area/login.php",
    "cms/admin.php", "admincontrol/login.php", "admincontrol/index.php", "AdminDashboard/index.php",
    "AdminDashboard/?mmmadmin=formdownload" ,
    "admin/administrator.php", "admin/user.php", "admin/log.php", "admin/member.php", 
    "admin/logon.php", "admin_console.php", "administrator/admin.php",
    "admin/admin_area.php", "adminpanel/admin_login.php", "admin_area/admin_login.php", 
    "admin_login/admin.php", "admin_manager.php", "admin/main.php", "manager.php",
    "admin_control.php", "adminlogin.php", "panel.php","wp-login.php", "wp-admin/", 
    "wp-admin/admin.php", "wp-login.php?action=register", "wp-admin/setup-config.php", 
    "wp-admin/admin-post.php", "wp-admin/admin-ajax.php", "wp-admin/network/", 
    "wp-admin/user-new.php", "wp-admin/options-general.php", "wp-admin/edit.php", 
    "wp-admin/themes.php", "wp-admin/plugins.php", "wp-admin/customize.php",  "admin.php", "administrator/index.php", "admin/login.php", "AdminDashboard.php","adminDashboard.php",
    "cpanel.php", "login.php", "admin_area/login.php", "admin_area/index.php",
    "controlpanel.php", "admincp.php", "adminLogin.php", "adm.php", "adminpage.php",
    "panel.php", "wp-login.php", "wp-admin/", "admin/admin_index.php",
    "admin_panel/admin_login.php", "dashboard/admin.php", "admin_portal/login.php",
    "wp-admin/profile.php",
    "admin_secret.php", "admin_hidden.php", "super_admin.php", "root_access.php", 
    "admin_master.php", "system_control.php", "secure_admin.php", "management_panel.php", 
    "admin_dashboard.php", "control_center.php", "backend_access.php", "sys_admin.php", 
    "admin_portal.php", "network_admin.php", "infrastructure_control.php", "it_admin.php", 
    "security_panel.php", "admin_console.php", "enterprise_admin.php", "global_admin.php", 
    "admin_restricted.php", "top_secret_admin.php", "admin_vault.php", "admin_shield.php",
    "admin_system.php", "admin_core.php", "admin_ultra.php", "admin_prime.php", 
    "admin_max.php", "admin_advanced.php", "admin_pro.php", "admin_elite.php",
    "admin_backdoor.php", "admin_kernel.php", "admin_bridge.php", "admin_gateway.php", 
    "admin_matrix.php", "admin_nexus.php", "admin_central.php", "admin_mainframe.php", 
    "admin_fortress.php", "admin_command.php", "admin_headquarters.php",
    "adm1n.php", "4dm1n.php", "admin_5ys.php", "syst3m_admin.php", 
    "4dministr4tor.php", "4cc3ss_control.php", "__admin.php", "_admin.php",
    "wp-admin/network/admin.php", "wp-admin/network/sites.php", 
    "wp-admin/network/users.php", "wp-admin/network/themes.php", 
    "wp-admin/network/plugins.php", "wp-admin/network/settings.php",
    "wp-admin/includes/admin.php", "wp-admin/includes/upgrade.php",
    "wp-admin/includes/user.php", "wp-admin/includes/post.php",
    "joomla/administrator/index.php", "joomla/administrator/login.php",
    "drupal/admin/index.php", "drupal/admin/login.php",
    "magento/admin/index.php", "magento/admin/login.php",
    "prestashop/admin/index.php", "prestashop/admin/login.php",
    "admin_dev.php", "admin_test.php", "admin_staging.php", 
    "admin_debug.php", "admin_monitor.php", "admin_logs.php",
    "devops_admin.php", "cloud_admin.php", "container_admin.php", 
    "kubernetes_admin.php", "infrastructure_management.php", 
    "network_operations.php", "system_engineering.php", 
    "cloud_management.php", "platform_admin.php", "service_management.php"
]

asp_admin_paths = [
    "admin.asp", "admin/login.asp", "administrator/index.asp", "admin_area/login.asp", 
    "admin_area/index.asp", "controlpanel.asp", "admincp.asp", "adminLogin.asp",
    "adm/admloginuser.asp", "adm/admloginuser.php", "adm.asp", "adm_auth.asp",
    "adm.asp", "login.asp", "adminpage.asp", "cpanel.asp", "admin_login.asp",
    "admin/index.asp", "admin/login.asp", "admin_area/admin.asp", "admin_area/login.asp",
    "cms/admin.asp", "admincontrol/login.asp", "admincontrol/index.asp",
    "admin/administrator.asp", "admin/user.asp", "admin/log.asp", "admin/member.asp", 
    "admin/logon.asp", "admin_console.asp", "administrator/admin.asp",
    "admin/admin_area.asp", "adminpanel/admin_login.asp", "admin_area/admin_login.asp", 
    "admin_login/admin.asp", "admin_manager.asp", "admin/main.asp", "manager.asp",
    "admin_control.asp", "adminlogin.asp", "panel.asp" , "admin.asp", "admin/login.asp", "administrator/index.asp", "control_panel.asp",
    "admincp.asp", "adminLogin.asp", "admin_console.asp", "adm.asp",
    "dashboard/index.asp", "manager/admin.asp", "admin_area/admin.asp", 
    "admin_login/admin.asp", "login.asp", "panel.asp", "admin/controlpanel.asp",
    "admin_page.asp", "AdminDashboard/index.asp", "Dashboard/admin_login.asp",
    "super-admin.asp", "root-access.asp", "admin-master.asp", 
    "system-control.asp", "secure-admin.asp", "management-panel.asp", 
    "admin-dashboard.asp", "control-center.asp", "backend-access.asp", 
    "sys-admin.asp", "admin-portal.asp", "network-admin.asp", 
    "infrastructure-control.asp", "it-admin.asp", "security-panel.asp", 
    "admin-console.asp", "enterprise-admin.asp", "global-admin.asp", 
    "admin-restricted.asp", "top-secret-admin.asp", "admin-vault.asp", 
    "admin-shield.asp", "power-admin.asp", "admin-core.asp", 
    "admin-ultra.asp", "admin-prime.asp", "admin-max.asp",
    "admin_control.asp", "adm1n.asp", "4dm1n.asp", "admin_sys.asp", 
    "sys_admin.asp", "admin_core.asp", "__admin.asp", "_admin.asp",
    "internal-admin.asp", "classified-admin.asp", "admin-bridge.asp", 
    "admin-gateway.asp", "admin-matrix.asp", "admin-nexus.asp", 
    "admin-kernel.asp", "admin-central.asp", "admin-mainframe.asp", 
    "admin-fortress.asp", "admin-command.asp", "admin-headquarters.asp"
]

admin_subdomains = [
    "admin", "cpanel", "webmail", "dashboard", "secure", "portal", 
    "support", "manage", "staff", "control", "panel", "login", "access", 
    "adminpanel", "cms", "administrator", "backend", "system", "sysadmin",
    "root", "master", "superadmin", "management", "it-admin", "network-admin",
    "security", "helpdesk", "console", "ops", "infrastructure", "control-center",
    "admin-ultra", "admin-prime", "admin-max", "global-admin", "enterprise-admin",
    "top-secret", "classified", "internal", "sys-control", "power-admin", 
    "admin-core", "admin-vault", "admin-shield", "admin-bridge", "admin-gateway",
    "admin-matrix", "admin-nexus", "admin-kernel", "admin-central", 
    "admin-mainframe", "admin-fortress", "admin-command", "admin-headquarters",
    "devops", "cloud-admin", "container-admin", "kubernetes-admin", 
    "infrastructure-management", "network-operations", "system-engineering", 
    "cloud-management", "tech-support", "platform-admin", "service-management"
]

def is_login_page(content):
    """Check if the page contains login-related elements."""
    login_keywords = ["login", "sign in", "authentication", "password", "username"]
    return any(keyword.lower() in content.lower() for keyword in login_keywords)

def check_admin_login(base_url, paths):
    found_panels = []
    for path in paths:
        full_url = urljoin(base_url, path)
        print(f"{Fore.YELLOW}Scanning: {full_url}{Style.RESET_ALL}")
        try:
            response = requests.get(full_url, timeout=3, verify=False)
            if response.status_code == 200 and is_login_page(response.text):
                print(f"{Fore.GREEN}[+] Admin panel found: {full_url}{Style.RESET_ALL}")
                found_panels.append(full_url)
            elif response.status_code == 403:
                print(f"{Fore.RED}[*] Forbidden: {full_url}{Style.RESET_ALL}")
        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}[-] Connection error: {full_url}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
    return found_panels


def check_admin_subdomains(domain, admin_paths):
    """Scan subdomains for admin panels."""
    found_panels = []
    for subdomain in admin_subdomains:
        subdomain_url = f"https://{subdomain}.{domain}"
        print(f"{Fore.YELLOW}Checking subdomain: {subdomain_url}{Style.RESET_ALL}")
        try:
            response = requests.get(subdomain_url, timeout=3, verify=False)
            if response.status_code == 200:
                found_panels.extend(check_admin_login(subdomain_url, admin_paths))
            else:
                print(f"{Fore.YELLOW}[-] Skipping: {subdomain_url} not accessible.{Style.RESET_ALL}")
        except ConnectionError:
            print(f"{Fore.RED}[-] Connection error: {subdomain_url}{Style.RESET_ALL}")
    return found_panels

def main():
    parser = argparse.ArgumentParser(description="Admin Login Finder Tool")
    parser.add_argument("url", help="Target URL (e.g., https://example.com)")
    args = parser.parse_args()

    base_url = args.url.strip()
    if not base_url.startswith("http"):
        base_url = f"http://{base_url}"

    print(f"{Fore.CYAN}Starting scan on: {base_url}{Style.RESET_ALL}")

    print("\nChoose Technology:")
    print("1. PHP")
    print("2. ASP")
    print("3. All (General)")

    tech_choice = input("Enter choice (1, 2, or 3): ").strip()

    if tech_choice == "1":
        admin_paths = generic_admin_paths + php_admin_paths
    elif tech_choice == "2":
        admin_paths = generic_admin_paths + asp_admin_paths
    elif tech_choice == "3":
        admin_paths = generic_admin_paths + php_admin_paths + asp_admin_paths
        print(f"{Fore.CYAN}[*] Running Admin Login Finder for all paths (General).{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] Invalid choice. Exiting.{Style.RESET_ALL}")
        return

    results = check_admin_login(base_url, admin_paths)
    if results:
        print(f"\n{Fore.GREEN}[+] Found Admin Panels:{Style.RESET_ALL}")
        for panel in results:
            print(f"{Fore.GREEN} - {panel}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] No admin panels found.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()