import random
import time
import sys
import os
import platform
from datetime import datetime
try:
    from colorama import init, Fore, Back, Styles
    colorama_available = True
    init()  
except ImportError:
    colorama_available = False
    print("For the best experience, install colorama: pip install colorama")

class CyberSecurityGame:
    def __init__(self):
        self.player_name = ""
        self.player_level = 1
        self.player_score = 0
        self.completed_challenges = []
        self.current_network = "Training Lab"
        self.game_over = False
        self.terminal_width = 80  
        self.try_set_terminal_size()
        
    def try_set_terminal_size(self):
        """Try to get actual terminal size."""
        try:
            terminal_size = os.get_terminal_size()
            self.terminal_width = terminal_size.columns
        except:
            pass
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def green_text(self, text):
        """Return text in green if colorama is available."""
        if colorama_available:
            return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
        return text
    
    def red_text(self, text):
        """Return text in red if colorama is available."""
        if colorama_available:
            return f"{Fore.RED}{text}{Style.RESET_ALL}"
        return text
    
    def yellow_text(self, text):
        """Return text in yellow if colorama is available."""
        if colorama_available:
            return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
        return text
    
    def cyan_text(self, text):
        """Return text in cyan if colorama is available."""
        if colorama_available:
            return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
        return text
    
    def blue_text(self, text):
        """Return text in blue if colorama is available."""
        if colorama_available:
            return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
        return text
    
    def bright_green_text(self, text):
        """Return text in bright green if colorama is available."""
        if colorama_available:
            return f"{Style.BRIGHT}{Fore.GREEN}{text}{Style.RESET_ALL}"
        return text
    
    def slow_print(self, text, delay=0.03):
        """Print text with a typing effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def hacker_print(self, text, delay=0.01, color_func=None):
        """Print text with a hacker-like effect."""
        if color_func:
            text = color_func(text)
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def display_ascii_banner(self):
        """Display a cool ASCII art banner."""
        banner = """
         ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
        ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████║███████║██║     █████╔╝ 
        ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██║██╔══██║██║     ██╔═██╗ 
        ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗
         ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
        """
        if colorama_available:
            print(f"{Fore.GREEN}{banner}{Style.RESET_ALL}")
        else:
            print(banner)
    
    def display_terminal_header(self):
        """Display a terminal-like header."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"┌{'─' * (self.terminal_width - 2)}┐"
        system_info = f"│ {self.bright_green_text('SYSTEM')}: {platform.system()} {platform.release()} | {self.bright_green_text('USER')}: {self.player_name} | {self.bright_green_text('TIME')}: {now} │"
        padding = self.terminal_width - len(system_info) + len(self.bright_green_text('SYSTEM')) + len(self.bright_green_text('USER')) + len(self.bright_green_text('TIME'))
        if colorama_available:
            system_info = system_info[:padding - 3] + " │"
        footer = f"└{'─' * (self.terminal_width - 2)}┘"
        
        print(self.green_text(header))
        print(system_info)
        print(self.green_text(footer))
    
    def display_loading_bar(self, duration=2, width=40):
        """Display a loading bar animation."""
        print(self.green_text("\n[+] Initializing system..."))
        for i in range(width + 1):
            progress = "█" * i + " " * (width - i)
            sys.stdout.write(f"\r[{self.green_text(progress)}] {i * 100 // width}%")
            sys.stdout.flush()
            time.sleep(duration / width)
        print("\n")
    
    def simulate_typing(self, text, min_delay=0.01, max_delay=0.05):
        """Simulate realistic typing with variable speed."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            delay = random.uniform(min_delay, max_delay)
            if char in ['.', ',', '!', '?']:
                delay *= 2  # Pause longer at punctuation
            time.sleep(delay)
        print()
    
    def intro(self):
        """Display game introduction."""
        self.clear_screen()
        self.display_ascii_banner()
        time.sleep(0.5)
        
        print(self.green_text("\n[*] Establishing secure connection..."))
        time.sleep(0.5)
        self.display_loading_bar(1.5)
        
        print(self.green_text("[+] Connection established."))
        self.hacker_print("Welcome to the CYBERHACK training program.", color_func=self.bright_green_text)
        self.hacker_print("This terminal provides access to simulated security scenarios.", color_func=self.green_text)
        time.sleep(0.3)
        
        self.hacker_print("\n[*] As a cybersecurity operative, your mission is to identify and neutralize", color_func=self.cyan_text)
        self.hacker_print("    digital threats before they can compromise critical systems.", color_func=self.cyan_text)
        self.hacker_print("[*] Your performance will be monitored and rated.", color_func=self.cyan_text)
        self.hacker_print("[*] Ethical conduct is mandatory - all operations are logged.", color_func=self.cyan_text)
        
        print(self.green_text("\n[+] Please identify yourself to continue:"))
        self.player_name = input(self.green_text(">>> "))
        
        print(self.green_text("\n[+] Authenticating..."))
        time.sleep(1)
        self.hacker_print(f"Welcome, Agent {self.player_name}. Your session begins now.", color_func=self.bright_green_text)
        
        input(self.green_text("\n[Press ENTER to access the terminal]"))
    
    def show_stats(self):
        """Display player stats in hacker style."""
        stats_box_top = f"┌{'─' * 21}┬{'─' * (self.terminal_width - 24)}┐"
        stats_box_mid = f"├{'─' * 21}┼{'─' * (self.terminal_width - 24)}┤"
        stats_box_bottom = f"└{'─' * 21}┴{'─' * (self.terminal_width - 24)}┘"
        
        print(self.cyan_text(stats_box_top))
        print(self.cyan_text(f"│ {self.yellow_text('AGENT')}:{' ' * (15 - len('AGENT'))} │ {self.player_name}{' ' * (self.terminal_width - 24 - len(self.player_name) - 1)}│"))
        print(self.cyan_text(stats_box_mid))
        print(self.cyan_text(f"│ {self.yellow_text('ACCESS LEVEL')}:{' ' * (15 - len('ACCESS LEVEL'))} │ {self.player_level}{' ' * (self.terminal_width - 24 - len(str(self.player_level)) - 1)}│"))
        print(self.cyan_text(stats_box_mid))
        print(self.cyan_text(f"│ {self.yellow_text('REPUTATION')}:{' ' * (15 - len('REPUTATION'))} │ {self.player_score}{' ' * (self.terminal_width - 24 - len(str(self.player_score)) - 1)}│"))
        print(self.cyan_text(stats_box_mid))
        print(self.cyan_text(f"│ {self.yellow_text('CURRENT NETWORK')}:{' ' * (15 - len('CURRENT NETWORK'))} │ {self.current_network}{' ' * (self.terminal_width - 24 - len(self.current_network) - 1)}│"))
        print(self.cyan_text(stats_box_mid))
        print(self.cyan_text(f"│ {self.yellow_text('MISSIONS COMPLETE')}:{' ' * (15 - len('MISSIONS COMPLETE'))} │ {len(self.completed_challenges)}{' ' * (self.terminal_width - 24 - len(str(len(self.completed_challenges))) - 1)}│"))
        print(self.cyan_text(stats_box_bottom))
    
    def main_menu(self):
        """Display main game menu with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        self.show_stats()
        
        print(self.green_text("\n[root@cyberhack]$ select_operation\n"))
        
        menu_options = [
            ("View Available Missions", "missions.sh"),
            ("Browse Security Toolkit", "tools.sh"),
            ("Mission History", "history.log"),
            ("Security Knowledge Base", "knowledge.db"),
            ("System Logout", "exit.sh")
        ]
        
        for i, (option, command) in enumerate(menu_options, 1):
            print(f"{self.bright_green_text(str(i))}. {self.green_text(option)} {self.yellow_text('(' + command + ')')}")
        
        choice = input(f"\n{self.green_text('[root@cyberhack]$')} ")
        
        # Simulate command execution
        if choice in ["1", "2", "3", "4", "5"]:
            command_map = {
                "1": "missions.sh",
                "2": "tools.sh",
                "3": "history.log",
                "4": "knowledge.db",
                "5": "exit.sh"
            }
            print(f"{self.green_text('[root@cyberhack]$')} ./{command_map[choice]}")
            time.sleep(0.3)
        
        if choice == "1":
            self.show_challenges()
        elif choice == "2":
            self.show_tools()
        elif choice == "3":
            self.show_completed_missions()
        elif choice == "4":
            self.learn_concepts()
        elif choice == "5":
            self.exit_game()
        else:
            self.hacker_print("Command not recognized. Try again.", color_func=self.red_text)
            input(self.green_text("\n[Press ENTER to continue]"))
            self.main_menu()
    
    def show_challenges(self):
        """Show available challenges with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text("\n[root@cyberhack]$ cat /var/missions/available.list\n"))
        time.sleep(0.2)
        
        print(self.cyan_text("┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("AVAILABLE MISSIONS") + self.cyan_text(" " * (self.terminal_width - 20) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        if self.player_level == 1:
            missions = [
                ("PWD_ANALYZER.exe", "Create a tool to evaluate password security"),
                ("NETSCAN.exe", "Identify open ports on a virtual network"),
                ("PHISH_DETECT.exe", "Spot phishing attempts in sample emails")
            ]
        elif self.player_level == 2:
            missions = [
                ("CRYPTO.exe", "Implement a basic encryption/decryption algorithm"),
                ("FIREWALL_CFG.exe", "Configure rules to protect a virtual server"),
                ("WEBSEC_SCAN.exe", "Find common web vulnerabilities")
            ]
        else:
            missions = [
                ("PENTEST.exe", "Test security on a complex virtual network"),
                ("FORENSIC.exe", "Analyze a system for signs of compromise"),
                ("ZERODAY.exe", "React to a new security threat")
            ]
        
        for i, (mission_code, description) in enumerate(missions, 1):
            print(f"{self.bright_green_text(str(i))}. {self.green_text(mission_code)} - {description}")
        
        print(f"\n{self.bright_green_text('0')}. {self.green_text('RETURN.sh')} - Return to main terminal")
        
        choice = input(f"\n{self.green_text('[root@cyberhack]$')} ")
        
        if choice == "0":
            print(f"{self.green_text('[root@cyberhack]$')} ./RETURN.sh")
            time.sleep(0.2)
            self.main_menu()
        elif choice in ["1", "2", "3"]:
            challenge_id = int(choice)
            print(f"{self.green_text('[root@cyberhack]$')} ./{missions[challenge_id-1][0]}")
            time.sleep(0.3)
            self.start_challenge(challenge_id)
        else:
            self.hacker_print("Invalid command. Access denied.", color_func=self.red_text)
            input(self.green_text("\n[Press ENTER to continue]"))
            self.show_challenges()
    
    def start_challenge(self, challenge_id):
        """Start a specific challenge with hacker aesthetic."""
        self.clear_screen()
        
        # Simulate loading the challenge
        print(self.green_text("[+] Initializing virtual environment..."))
        self.display_loading_bar(1.5)
        
        if self.player_level == 1:
            if challenge_id == 1:
                self.password_challenge()
            elif challenge_id == 2:
                self.network_scanner_challenge()
            elif challenge_id == 3:
                self.phishing_challenge()
        elif self.player_level == 2:
            self.hacker_print("ADVANCED MISSION ACCESS: PENDING", color_func=self.yellow_text)
            self.hacker_print("This module will be available in the next security update.", color_func=self.green_text)
            input(self.green_text("\n[Press ENTER to continue]"))
            self.show_challenges()
        else:
            self.hacker_print("ELITE MISSION ACCESS: PENDING", color_func=self.yellow_text)
            self.hacker_print("This module will be available in the next security update.", color_func=self.green_text)
            input(self.green_text("\n[Press ENTER to continue]"))
            self.show_challenges()
    
    def password_challenge(self):
        """Password strength analyzer challenge with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        challenge_name = "PASSWORD STRENGTH ANALYZER"
        print(self.cyan_text("\n┌" + "─" * (len(challenge_name) + 4) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text(challenge_name) + self.cyan_text(" │"))
        print(self.cyan_text("└" + "─" * (len(challenge_name) + 4) + "┘"))
        
        self.hacker_print("\n[MISSION BRIEFING]", color_func=self.bright_green_text)
        self.hacker_print("Develop a password strength analyzer to evaluate security level.", color_func=self.green_text)
        self.hacker_print("The analyzer must check for:", color_func=self.green_text)
        
        print(self.yellow_text(" ✓ Minimum length of 8 characters"))
        print(self.yellow_text(" ✓ Presence of uppercase and lowercase letters"))
        print(self.yellow_text(" ✓ Presence of numbers"))
        print(self.yellow_text(" ✓ Presence of special characters"))
        
        print(self.green_text("\n[+] Starting virtual development environment..."))
        time.sleep(1)
        
        print(self.cyan_text("\n┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.bright_green_text("CODE EDITOR") + self.cyan_text(" " * (self.terminal_width - 14) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        code = """
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password should contain numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Password should contain special characters")
    
    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        "strength": strength,
        "score": score,
        "max_score": 5,
        "feedback": feedback
    }

# Test the function
test_password = "P@ssw0rd123"
result = check_password_strength(test_password)
print(f"Password: {test_password}")
print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}/{result['max_score']}")

if result['feedback']:
    print("Feedback:")
    for item in result['feedback']:
        print(f"- {item}")
"""
        
        
        for line in code.strip().split('\n'):
            if line.startswith('def ') or line.startswith('if ') or line.startswith('else ') or line.startswith('elif '):
                print(self.cyan_text(line))
            elif 'return' in line:
                print(self.yellow_text(line))
            elif '"' in line or "'" in line:
                print(self.green_text(line))
            elif '#' in line:
                comment_pos = line.find('#')
                print(line[:comment_pos] + self.bright_green_text(line[comment_pos:]))
            else:
                print(line)
        
        print(self.green_text("\n[+] Running code analysis..."))
        time.sleep(1.5)
        
       
        print(self.green_text("\n[+] Test results:"))
        print(self.yellow_text("Password: P@ssw0rd123"))
        print(self.yellow_text("Strength: Strong"))
        print(self.yellow_text("Score: 5/5"))
        
        print(self.green_text("\n[+] Testing additional passwords:"))
        test_passwords = ["password", "Password1", "Passw0rd!", "p@ss"]
        for pwd in test_passwords:
            time.sleep(0.5)
            if len(pwd) < 8:
                strength = "Weak"
                score = 2
            elif any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~" for c in pwd):
                strength = "Strong"
                score = 5
            else:
                strength = "Medium"
                score = 3
            
            print(self.yellow_text(f"Password: {pwd}"))
            print(self.yellow_text(f"Strength: {strength}"))
            print(self.yellow_text(f"Score: {score}/5"))
            print()
        
        self.hacker_print("\n[MISSION COMPLETE]", color_func=self.bright_green_text)
        self.hacker_print("Password analyzer successfully developed and tested.", color_func=self.green_text)
        
        self.player_score += 100
        self.completed_challenges.append("Password Strength Analyzer")
        
        if len(self.completed_challenges) >= 3:
            self.player_level += 1
            self.hacker_print(f"\n[SYSTEM NOTIFICATION]", color_func=self.bright_green_text)
            self.hacker_print(f"Security clearance upgraded to Level {self.player_level}!", color_func=self.green_text)
            self.hacker_print(f"New missions available.", color_func=self.green_text)
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.show_challenges()
    
    def network_scanner_challenge(self):
        """Network scanner simulation challenge with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        challenge_name = "NETWORK SCANNER SIMULATION"
        print(self.cyan_text("\n┌" + "─" * (len(challenge_name) + 4) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text(challenge_name) + self.cyan_text(" │"))
        print(self.cyan_text("└" + "─" * (len(challenge_name) + 4) + "┘"))
        
        self.hacker_print("\n[MISSION BRIEFING]", color_func=self.bright_green_text)
        self.hacker_print("Develop a basic port scanner to identify open network services.", color_func=self.green_text)
        self.hacker_print("Your scanner should check common ports for security vulnerabilities.", color_func=self.green_text)
        
        print(self.green_text("\n[+] Target IP for simulation: ") + self.yellow_text("192.168.1.1"))
        print(self.green_text("[+] Ports to scan: ") + self.yellow_text("21, 22, 80, 443, 3306, 8080"))
        
        print(self.green_text("\n[+] Initializing network scanner..."))
        time.sleep(1)
        
        # ASCII network diagram
        network_diagram = """
        ┌─────────────┐       ┌─────────────┐
        │             │       │             │
        │  SCANNER    │━━━━━━▶│  TARGET     │
        │  SYSTEM     │◀━━━━━━│  192.168.1.1│
        │             │       │             │
        └─────────────┘       └─────────────┘
        """
        print(self.cyan_text(network_diagram))
        
        # Simulate port scanning
        self.hacker_print("\n[+] Initiating port scan simulation...", color_func=self.green_text)
        time.sleep(0.5)
        
        ports = [
            {"port": 21, "service": "FTP", "open": False},
            {"port": 22, "service": "SSH", "open": True},
            {"port": 80, "service": "HTTP", "open": True},
            {"port": 443, "service": "HTTPS", "open": True},
            {"port": 3306, "service": "MySQL", "open": False},
            {"port": 8080, "service": "HTTP-ALT", "open": False}
        ]
        
        print(self.cyan_text("\n┌" + "─" * (self.terminal_width - 2) + "┐"))
        header = " PORT     SERVICE      STATUS     POTENTIAL RISK"
        print(self.cyan_text("│") + self.yellow_text(header) + self.cyan_text(" " * (self.terminal_width - len(header) - 2) + "│"))
        print(self.cyan_text("├" + "─" * (self.terminal_width - 2) + "┤"))
        
        total_open = 0
        for port in ports:
            time.sleep(0.7)
            status = "OPEN" if port["open"] else "CLOSED"
            status_color = self.red_text if port["open"] else self.green_text
            risk = "High" if port["open"] and port["port"] in [21, 3306] else "Medium" if port["open"] else "Low"
            risk_color = self.red_text if risk == "High" else self.yellow_text if risk == "Medium" else self.green_text
            
            port_info = f" {port['port']:<8} {port['service']:<12} {status_color(status):<10} {risk_color(risk)}"
            print(self.cyan_text("│") + port_info + self.cyan_text(" " * (self.terminal_width - len(port_info) - 21) + "│"))
            
            if port["open"]:
                total_open += 1
        
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        self.hacker_print(f"\n[+] Scan complete! Found {total_open} open ports.", color_func=self.green_text)
        
        # Show analysis
        self.hacker_print("\n[+] Security Analysis:", color_func=self.bright_green_text)
        self.hacker_print("SSH (Port 22) - Recommended Action: Ensure strong passwords and key-based auth", color_func=self.green_text)
        self.hacker_print("HTTP (Port 80) - Recommended Action: Redirect to HTTPS", color_func=self.green_text)
        self.hacker_print("HTTPS (Port 443) - Recommended Action: Verify TLS configuration", color_func=self.green_text)
        
        self.hacker_print("\n[MISSION COMPLETE]", color_func=self.bright_green_text)
        self.hacker_print("Network scanner successfully developed and tested.", color_func=self.green_text)
        
        self.player_score += 150
        self.completed_challenges.append("Network Scanner Simulation")
        
        if len(self.completed_challenges) >= 3:
            self.player_level += 1
            self.hacker_print(f"\n[SYSTEM NOTIFICATION]", color_func=self.bright_green_text)
            self.hacker_print(f"Security clearance upgraded to Level {self.player_level}!", color_func=self.green_text)
            self.hacker_print(f"New missions available.", color_func=self.green_text)
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.show_challenges()
    
    def phishing_challenge(self):
        """Phishing identification challenge with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        challenge_name = "SOCIAL ENGINEERING DEFENSE"
        print(self.cyan_text("\n┌" + "─" * (len(challenge_name) + 4) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text(challenge_name) + self.cyan_text(" │"))
        print(self.cyan_text("└" + "─" * (len(challenge_name) + 4) + "┘"))
        
        self.hacker_print("\n[MISSION BRIEFING]", color_func=self.bright_green_text)
        self.hacker_print("Analyze incoming communications for social engineering attempts.", color_func=self.green_text)
        self.hacker_print("Identify phishing emails based on common indicators.", color_func=self.green_text)
        
        emails = [
            {
                "id": "EMAIL-001",
                "sender": "security@bankofamerica.net",
                "subject": "Urgent: Your Account Has Been Compromised",
                "body": "Dear Customer,\n\nOur security system has detected unusual activity on your account. Please click the link below to verify your identity and secure your account immediately: http://secure-bankofamerica.com.phish.net/login\n\nFailure to verify within 24 hours will result in account suspension.\n\nRegards,\nBank of America Security Team",
                "is_phishing": True,
                "indicators": ["Urgency tactics", "Suspicious URL", "Threatening language"]
            },
            {
                "id": "EMAIL-002",
                "sender": "newsletter@amazon.com",
                "subject": "Your Amazon Weekly Newsletter",
                "body": "Hello valued customer,\n\nCheck out this week's deals on electronics, books, and more! Shop now at amazon.com.\n\nYou can manage your email preferences in your account settings.\n\nAmazon Customer Service",
                "is_phishing": False,
                "indicators": []
            },
            {
                "id": "EMAIL-003",
                "sender": "prize.notification@sweepstakes.winner.org",
                "subject": "CONGRATULATIONS! YOU'VE WON $1,000,000!",
                "body": "CONGRATULATIONS LUCKY WINNER!!!\n\nYou have been selected as the winner of our $1,000,000 prize! To claim your prize, please send us your bank account details and a processing fee of $100 to cover transfer costs.\n\nReply immediately to claim your prize!\n\nSincerely,\nInternational Lottery Association",
                "is_phishing": True,
                "indicators": ["Too good to be true", "Requests payment", "ALL CAPS text", "Suspicious sender domain"]
            }
        ]
        
        self.hacker_print("\n[+] Initializing email scanner...", color_func=self.green_text)
        time.sleep(1)
        
        
        correct_answers = 0
        for i, email in enumerate(emails):
            print(self.cyan_text("\n┌" + "─" * (self.terminal_width - 2) + "┐"))
            print(self.cyan_text("│ ") + self.bright_green_text(f"EMAIL {i+1} of {len(emails)}") + self.cyan_text(" " * (self.terminal_width - 14 - len(str(i+1)) - len(str(len(emails)))) + "│"))
            print(self.cyan_text("├" + "─" * (self.terminal_width - 2) + "┤"))
            
            print(self.cyan_text("│ ") + self.yellow_text("FROM: ") + email["sender"] + self.cyan_text(" " * (self.terminal_width - 7 - len(email["sender"]) - 2) + "│"))
            print(self.cyan_text("│ ") + self.yellow_text("SUBJECT: ") + email["subject"] + self.cyan_text(" " * (self.terminal_width - 10 - len(email["subject"]) - 2) + "│"))
            print(self.cyan_text("├" + "─" * (self.terminal_width - 2) + "┤"))
            
            # Display email body with word wrap
            body_lines = []
            words = email["body"].split()
            current_line = "│ "
            for word in words:
                if len(current_line) + len(word) + 1 > self.terminal_width - 2:
                    body_lines.append(current_line + self.cyan_text(" " * (self.terminal_width - len(current_line) - 1) + "│"))
                    current_line = "│ " + word + " "
                else:
                    current_line += word + " "
            if current_line != "│ ":
                body_lines.append(current_line + self.cyan_text(" " * (self.terminal_width - len(current_line) - 1) + "│"))
            
            for line in body_lines:
                print(line)
            
            print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
            
           
            print(self.green_text("\n[?] Is this email legitimate or phishing?"))
            print(self.bright_green_text("1") + self.green_text(". Legitimate Email"))
            print(self.bright_green_text("2") + self.green_text(". Phishing Attempt"))
            
            answer = input(f"{self.green_text('[root@cyberhack]$')} ")
            
            is_correct = (answer == "2" and email["is_phishing"]) or (answer == "1" and not email["is_phishing"])
            
        
            if is_correct:
                correct_answers += 1
                print(self.green_text("\n[+] Correct assessment!"))
            else:
                print(self.red_text("\n[-] Incorrect assessment!"))
            
           
            if email["is_phishing"]:
                print(self.yellow_text("\n[!] This is a phishing email."))
                print(self.yellow_text("[!] Indicators:"))
                for indicator in email["indicators"]:
                    print(self.yellow_text(f" - {indicator}"))
            else:
                print(self.green_text("\n[+] This appears to be a legitimate email."))
            
            input(self.green_text("\n[Press ENTER to continue]"))
        
        
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.cyan_text("\n┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("MISSION RESULTS") + self.cyan_text(" " * (self.terminal_width - 17) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        score = (correct_answers / len(emails)) * 100
        print(self.green_text(f"\n[+] Emails analyzed: {len(emails)}"))
        print(self.green_text(f"[+] Correct assessments: {correct_answers}"))
        print(self.green_text(f"[+] Accuracy: {score:.0f}%"))
        
        if score >= 70:
            self.hacker_print("\n[MISSION COMPLETE]", color_func=self.bright_green_text)
            self.hacker_print("You've successfully completed the social engineering training.", color_func=self.green_text)
            
            self.player_score += 120
            self.completed_challenges.append("Phishing Detection")
            
            if len(self.completed_challenges) >= 3:
                self.player_level += 1
                self.hacker_print(f"\n[SYSTEM NOTIFICATION]", color_func=self.bright_green_text)
                self.hacker_print(f"Security clearance upgraded to Level {self.player_level}!", color_func=self.green_text)
                self.hacker_print(f"New missions available.", color_func=self.green_text)
        else:
            self.hacker_print("\n[MISSION FAILED]", color_func=self.red_text)
            self.hacker_print("Training module requires a minimum 70% accuracy.", color_func=self.yellow_text)
            self.hacker_print("Review the indicators and try again.", color_func=self.yellow_text)
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.show_challenges()
    
    def show_tools(self):
        """Display security tools with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text("\n[root@cyberhack]$ ls -la /usr/bin/security/tools/\n"))
        time.sleep(0.2)
        
        print(self.cyan_text("┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("SECURITY TOOLKIT") + self.cyan_text(" " * (self.terminal_width - 18) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        tools = [
            ("CRYPTO.app", "Encryption/decryption tools and algorithms", "Level 1"),
            ("FORENSIC.app", "Digital forensics and file recovery", "Level 2"),
            ("NETMAP.app", "Network mapping and reconnaissance", "Level 1"),
            ("VULNSCAN.app", "Vulnerability assessment scanner", "Level 2"),
            ("MALWARE.app", "Malware analysis sandbox", "Level 3")
        ]
        
        print(f"{self.cyan_text('NAME'):<20} {self.cyan_text('DESCRIPTION'):<40} {self.cyan_text('REQ LEVEL')}")
        print("─" * (self.terminal_width))
        
        for tool_name, description, level in tools:
            level_color = self.green_text if int(level.split()[1]) <= self.player_level else self.red_text
            print(f"{self.green_text(tool_name):<20} {description:<40} {level_color(level)}")
        
        print("\n" + self.green_text("[+] Enter tool name to use or 0 to return:"))
        tool_choice = input(f"{self.green_text('[root@cyberhack]$')} ")
        
        if tool_choice == "0":
            self.main_menu()
            return
            
        found = False
        for tool_name, _, level_req in tools:
            if tool_choice.upper() == tool_name:
                found = True
                level_num = int(level_req.split()[1])
                if level_num <= self.player_level:
                    print(self.green_text(f"\n[+] Launching {tool_name}..."))
                    time.sleep(1)
                    self.display_loading_bar(1)
                    self.hacker_print("Tool functionality not implemented in this version.", color_func=self.yellow_text)
                else:
                    self.hacker_print(f"\nACCESS DENIED: Security clearance level {level_num} required.", color_func=self.red_text)
        
        if not found:
            self.hacker_print("\nTool not found in database. Check your spelling.", color_func=self.red_text)
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.show_tools()
    
    def show_completed_missions(self):
        """Show completed missions with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text("\n[root@cyberhack]$ cat /var/log/mission_history.log\n"))
        time.sleep(0.2)
        
        print(self.cyan_text("┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("MISSION HISTORY") + self.cyan_text(" " * (self.terminal_width - 17) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        if not self.completed_challenges:
            self.hacker_print("\nNo missions completed yet. Access the mission terminal to begin.", color_func=self.yellow_text)
        else:
            print(f"{self.cyan_text('MISSION'):<40} {self.cyan_text('STATUS')}")
            print("─" * (self.terminal_width))
            
            for i, mission in enumerate(self.completed_challenges, 1):
                print(f"{i}. {mission:<37} {self.green_text('COMPLETED')}")
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.main_menu()
    
    def learn_concepts(self):
        """Display security concepts with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text("\n[root@cyberhack]$ access_database /security/knowledge\n"))
        time.sleep(0.2)
        
        print(self.cyan_text("┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("SECURITY KNOWLEDGE BASE") + self.cyan_text(" " * (self.terminal_width - 24) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        topics = [
            "Password Security",
            "Social Engineering",
            "Network Security",
            "Cryptography",
            "Malware Analysis",
            "Return to Main Terminal"
        ]
        
        for i, topic in enumerate(topics, 1):
            print(f"{self.bright_green_text(str(i))}. {self.green_text(topic)}")
        
        choice = input(f"\n{self.green_text('[root@cyberhack]$')} ")
        
        if choice == "6":
            self.main_menu()
            return
            
        if choice in ["1", "2", "3", "4", "5"]:
            topic_index = int(choice) - 1
            self.display_security_topic(topics[topic_index])
        else:
            self.hacker_print("Invalid selection. Access denied.", color_func=self.red_text)
            input(self.green_text("\n[Press ENTER to continue]"))
            self.learn_concepts()
    
    def display_security_topic(self, topic):
        """Display information about a security topic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text(f"\n[root@cyberhack]$ view_document /security/topics/{topic.lower().replace(' ', '_')}.txt\n"))
        time.sleep(0.5)
        
        print(self.cyan_text("┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text(topic.upper()) + self.cyan_text(" " * (self.terminal_width - len(topic) - 4) + "│"))
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘\n"))
        
        topics_content = {
            "Password Security": [
                "BEST PRACTICES FOR PASSWORD SECURITY:",
                "",
                "1. Use long, complex passwords (12+ characters)",
                "2. Combine uppercase, lowercase, numbers, and special characters",
                "3. Avoid common words, phrases, or personal information",
                "4. Use different passwords for different accounts",
                "5. Change passwords regularly (every 90 days)",
                "6. Consider using a password manager",
                "7. Enable multi-factor authentication when available",
                "",
                "COMMON PASSWORD ATTACKS:",
                "",
                "- Brute Force: Trying all possible combinations",
                "- Dictionary Attacks: Testing common words and variations",
                "- Credential Stuffing: Using leaked credentials from other sites",
                "- Phishing: Tricking users into revealing passwords",
                "- Keylogging: Recording keystrokes to capture passwords"
            ],
            "Social Engineering": [
                "COMMON SOCIAL ENGINEERING TACTICS:",
                "",
                "1. Phishing: Deceptive emails or messages to steal information",
                "2. Pretexting: Creating a fabricated scenario to extract information",
                "3. Baiting: Offering something enticing to steal information",
                "4. Quid Pro Quo: Offering a service in exchange for information",
                "5. Tailgating: Following someone into a restricted area",
                "",
                "RED FLAGS TO WATCH FOR:",
                "",
                "- Urgency or pressure tactics",
                "- Requests for sensitive information",
                "- Poor spelling and grammar",
                "- Mismatched or suspicious URLs",
                "- Threats or dire consequences",
                "- Offers that seem too good to be true",
                "- Unexpected attachments or downloads"
            ],
            "Network Security": [
                "ESSENTIAL NETWORK SECURITY MEASURES:",
                "",
                "1. Firewalls: Filter network traffic based on security rules",
                "2. Intrusion Detection Systems (IDS): Monitor networks for suspicious activity",
                "3. Virtual Private Networks (VPN): Encrypt connections over public networks",
                "4. Network Segmentation: Divide network into secured zones",
                "5. Regular Vulnerability Scanning: Identify and patch security gaps",
                "",
                "COMMON NETWORK VULNERABILITIES:",
                "",
                "- Open ports and services",
                "- Weak encryption protocols",
                "- Default credentials",
                "- Unpatched systems",
                "- Misconfigured network devices",
                "- Man-in-the-middle attacks",
                "- Denial of Service (DoS) vulnerabilities"
            ],
            "Cryptography": [
                "FUNDAMENTAL CRYPTOGRAPHY CONCEPTS:",
                "",
                "1. Encryption: Converting data into an unreadable format",
                "2. Decryption: Converting encrypted data back to its original format",
                "3. Symmetric Encryption: Same key for encryption and decryption",
                "4. Asymmetric Encryption: Different keys for encryption and decryption",
                "5. Hashing: One-way function to verify data integrity",
                "",
                "COMMON CRYPTOGRAPHIC PROTOCOLS:",
                "",
                "- TLS/SSL: Secure web communications",
                "- PGP/GPG: Email and file encryption",
                "- AES: Advanced Encryption Standard",
                "- RSA: Public-key cryptography algorithm",
                "- SHA: Secure Hash Algorithm family",
                "- Digital Signatures: Authentication and non-repudiation"
            ],
            "Malware Analysis": [
                "MALWARE ANALYSIS TECHNIQUES:",
                "",
                "1. Static Analysis: Examining malware without executing it",
                "2. Dynamic Analysis: Observing malware behavior during execution",
                "3. Memory Analysis: Examining RAM contents for malware traces",
                "4. Behavioral Analysis: Studying how malware interacts with the system",
                "",
                "COMMON MALWARE TYPES:",
                "",
                "- Viruses: Self-replicating malicious code",
                "- Worms: Self-propagating across networks",
                "- Trojans: Disguised as legitimate software",
                "- Ransomware: Encrypts files and demands payment",
                "- Spyware: Monitors user activity",
                "- Rootkits: Provides persistent access while hiding presence",
                "- Fileless Malware: Operates in memory without files on disk"
            ]
        }
        
        if topic in topics_content:
            for line in topics_content[topic]:
                if line and line[0].isdigit() and ". " in line:
                    # Numbered points
                    point_num, point_text = line.split(". ", 1)
                    print(f"{self.bright_green_text(point_num + '.')} {self.green_text(point_text)}")
                elif line and line.startswith("- "):
                    # Bullet points
                    print(f"{self.yellow_text('•')} {self.green_text(line[2:])}")
                elif line and line.isupper():
                    # Headers
                    print(self.bright_green_text(line))
                else:
                    # Regular text
                    print(self.green_text(line))
        
        input(self.green_text("\n[Press ENTER to continue]"))
        self.learn_concepts()
    
    def exit_game(self):
        """Exit the game with hacker aesthetic."""
        self.clear_screen()
        self.display_terminal_header()
        
        print(self.green_text("\n[root@cyberhack]$ exit\n"))
        time.sleep(0.3)
        
        self.hacker_print("Terminating secure connection...", color_func=self.green_text)
        time.sleep(0.5)
        
        print(self.green_text("\n[+] Clearing session data..."))
        self.display_loading_bar(1)
        
        print(self.green_text("\n[+] Logging session results..."))
        time.sleep(0.5)
        
        print(self.cyan_text("\n┌" + "─" * (self.terminal_width - 2) + "┐"))
        print(self.cyan_text("│ ") + self.yellow_text("SESSION SUMMARY") + self.cyan_text(" " * (self.terminal_width - 17) + "│"))
        print(self.cyan_text("├" + "─" * (self.terminal_width - 2) + "┤"))
        
        print(self.cyan_text("│ ") + self.yellow_text(f"Agent: {self.player_name}") + self.cyan_text(" " * (self.terminal_width - 9 - len(self.player_name) - 2) + "│"))
        print(self.cyan_text("│ ") + self.yellow_text(f"Final Security Level: {self.player_level}") + self.cyan_text(" " * (self.terminal_width - 22 - len(str(self.player_level)) - 2) + "│"))
        print(self.cyan_text("│ ") + self.yellow_text(f"Reputation Score: {self.player_score}") + self.cyan_text(" " * (self.terminal_width - 19 - len(str(self.player_score)) - 2) + "│"))
        print(self.cyan_text("│ ") + self.yellow_text(f"Completed Missions: {len(self.completed_challenges)}") + self.cyan_text(" " * (self.terminal_width - 21 - len(str(len(self.completed_challenges))) - 2) + "│"))
        
        print(self.cyan_text("└" + "─" * (self.terminal_width - 2) + "┘"))
        
        self.hacker_print("\nThank you for using the CYBERHACK training program.", color_func=self.bright_green_text)
        self.hacker_print("Remember: Security is an ongoing process, not a destination.", color_func=self.green_text)
        
        time.sleep(1)
        self.game_over = True
        
        print(self.green_text("\n[Session terminated]\n"))

def main():
    """Main function to run the game."""
    game = CyberSecurityGame()
    game.intro()
    
    while not game.game_over:
        game.main_menu()

if __name__ == "__main__":
    main()
