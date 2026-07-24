class Classifier:


    def detect(self, rule):

        text = str(rule).lower()


        if "windows" in text:
            return "🪟 Windows"


        if "linux" in text:
            return "🐧 Linux"


        if "ivanti" in text:
            return "🔒 Ivanti"


        if "fortinet" in text:
            return "🧱 Fortinet"


        if "cisco" in text:
            return "🛰 Cisco"


        if "firewall" in text:
            return "🛡 Firewall"


        if "vpn" in text:
            return "🌐 VPN"


        if "network" in text:
            return "🌐 Network"


        return "📦 Other"