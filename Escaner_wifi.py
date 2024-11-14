import tkinter as tk
from tkinter import ttk, messagebox
import scapy.all as scapy
import threading
import time
from datetime import datetime
import socket
import requests
import json
from ttkthemes import ThemedTk

class NetworkScanner(ThemedTk):
    def __init__(self):
        super().__init__(theme="azure")
        self.title("Network Scanner Pro")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")
        self.devices = {}
        self.scanning = False
        self.create_widgets()
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", padding=10, font=('Helvetica', 10))
        self.style.configure("Custom.TLabel", font=('Helvetica', 11))
        self.style.configure("Treeview", rowheight=25, font=('Helvetica', 9))
        self.style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
        self.toggle_scan()

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="Network Scanner Professional", 
                              style="Custom.TLabel", font=('Helvetica', 16, 'bold'))
        title_label.pack(side=tk.LEFT)
        
        self.status_label = ttk.Label(header_frame, text="Estado: Inactivo", 
                                    style="Custom.TLabel")
        self.status_label.pack(side=tk.RIGHT)
        
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.scan_button = ttk.Button(control_frame, text="Iniciar Escaneo", 
                                    style="Custom.TButton", command=self.toggle_scan)
        self.scan_button.pack(side=tk.LEFT, padx=5)
        
        self.export_button = ttk.Button(control_frame, text="Exportar Datos", 
                                      style="Custom.TButton", command=self.export_data)
        self.export_button.pack(side=tk.LEFT, padx=5)
        
        columns = ('IP', 'MAC', 'Fabricante', 'Hostname', 'Última vez visto', 
                  'Estado', 'Tipo de dispositivo')
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings', 
                                style="Custom.Treeview")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140)
        
        scrollbar_y = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, 
                                  command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, 
                                  command=self.tree.xview)
        
        self.tree.configure(yscrollcommand=scrollbar_y.set, 
                          xscrollcommand=scrollbar_x.set)
        
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    def get_network_info(self):
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            base_ip = '.'.join(local_ip.split('.')[:-1])
            return f"{base_ip}.0/24"
        except:
            messagebox.showerror("Error", "No se pudo obtener la información de red")
            return None

    def scan_network(self):
        while self.scanning:
            network = self.get_network_info()
            if network:
                try:
                    arp_request = scapy.ARP(pdst=network)
                    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                    responses = scapy.srp(broadcast/arp_request, timeout=3, 
                                        verbose=False)[0]
                    
                    current_time = datetime.now().strftime("%H:%M:%S")
                    devices_found = set()
                    
                    for sent, received in responses:
                        ip = received.psrc
                        mac = received.hwsrc.upper()
                        devices_found.add(ip)
                        
                        if ip not in self.devices:
                            hostname = self.get_hostname(ip)
                            vendor = self.get_vendor_api(mac)
                            device_type = self.detect_device_type(mac, hostname)
                            
                            self.devices[ip] = {
                                'mac': mac,
                                'vendor': vendor,
                                'hostname': hostname,
                                'last_seen': current_time,
                                'status': 'Activo',
                                'type': device_type
                            }
                        else:
                            self.devices[ip]['last_seen'] = current_time
                            self.devices[ip]['status'] = 'Activo'
                    
                    for ip in list(self.devices.keys()):
                        if ip not in devices_found:
                            self.devices[ip]['status'] = 'Inactivo'
                    
                    self.update_tree()
                    
                except Exception as e:
                    print(f"Error durante el escaneo: {e}")
            time.sleep(3)

    def get_hostname(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return "Desconocido"

    def get_vendor_api(self, mac):
        try:
            mac_prefix = mac.replace(":", "")[:6]
            response = requests.get(f"https://api.macvendors.com/{mac_prefix}")
            if response.status_code == 200:
                return response.text
            return "Desconocido"
        except:
            return "Desconocido"

    def detect_device_type(self, mac, hostname):
        hostname = hostname.lower()
        if "phone" in hostname or "android" in hostname or "iphone" in hostname:
            return "Móvil"
        elif "laptop" in hostname or "notebook" in hostname:
            return "Portátil"
        elif "tv" in hostname or "smart-tv" in hostname:
            return "Smart TV"
        return "Desconocido"

    def update_tree(self):
        self.after(0, self._update_tree)

    def _update_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for ip, info in self.devices.items():
            status_color = 'green' if info['status'] == 'Activo' else 'red'
            self.tree.insert('', tk.END, values=(
                ip,
                info['mac'],
                info['vendor'],
                info['hostname'],
                info['last_seen'],
                info['status'],
                info['type']
            ), tags=(status_color,))
        
        self.tree.tag_configure('green', foreground='green')
        self.tree.tag_configure('red', foreground='red')

    def toggle_scan(self):
        if not self.scanning:
            self.scanning = True
            self.scan_button.configure(text="Detener Escaneo")
            self.status_label.configure(text="Estado: Escaneando...")
            threading.Thread(target=self.scan_network, daemon=True).start()
        else:
            self.scanning = False
            self.scan_button.configure(text="Iniciar Escaneo")
            self.status_label.configure(text="Estado: Inactivo")

    def export_data(self):
        try:
            with open('network_scan.json', 'w') as f:
                json.dump(self.devices, f, indent=4)
            messagebox.showinfo("Éxito", "Datos exportados correctamente")
        except:
            messagebox.showerror("Error", "No se pudieron exportar los datos")

    def on_closing(self):
        self.scanning = False
        self.destroy()

if __name__ == "__main__":
    app = NetworkScanner()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()