# import tkinter as tk

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# window.mainloop()


# Part 2 of tkinter

# import tkinter as tk

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# window.mainloop()


# part 3 --------------------------


# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""

# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )

# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# window.mainloop()


# part  4---------------------

# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     output_box.insert(
#         tk.END,
#         "SOC Analysis Started...\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Selected File:\n{selected_file}\n"
#     )


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=15,
#     width=80
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()


# part 5-------------------

# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=15,
#     width=80
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()


# part  6 ------------ timestamp analysis / top 3 attackers ranking show


# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     first_event = ""
#     last_event = ""

#     for line in logs:

#         parts = line.split()

#         if len(parts) < 2:
#             continue

#         timestamp = (
#             parts[0]
#             + " "
#             + parts[1]
#         )

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if first_event == "":

#                 first_event = timestamp

#             last_event = timestamp

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     ranking_list = []

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         ranking_list.append(
#             (
#                 ip,
#                 attempts
#             )
#         )

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"First Event : {first_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Last Event : {last_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TOP 3 ATTACKERS ==========\n"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         output_box.insert(
#             tk.END,
#             f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=20,
#     width=90
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()




# version 20 pie chart feature-----------------



# import tkinter as tk
# from tkinter import filedialog
# import matplotlib.pyplot as plt
# from tkinter import messagebox

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "1000x700"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     first_event = ""
#     last_event = ""

#     for line in logs:

#         parts = line.split()

#         if len(parts) < 2:
#             continue

#         timestamp = (
#             parts[0]
#             + " "
#             + parts[1]
#         )

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if first_event == "":

#                 first_event = timestamp

#             last_event = timestamp

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     ranking_list = []

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         ranking_list.append(
#             (
#                 ip,
#                 attempts
#             )
#         )

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"First Event : {first_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Last Event : {last_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TOP 3 ATTACKERS ==========\n"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         output_box.insert(
#             tk.END,
#             f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1


#     messagebox.showinfo(
#         "Analysis Complete",
#         "SOC Analysis Completed Successfully!"
#     )


#     if (
#         high_risk +
#         medium_risk +
#         low_risk
#     ) > 0:

#         plt.figure(
#             figsize=(6, 6)
#         )

#         plt.pie(
#            [
#                  high_risk,
#                  medium_risk,
#                  low_risk
#            ],
#            labels=[
#                "High Risk",
#                "Medium Risk",
#                "Low Risk"
#             ],
#             autopct="%1.1f%%"
#         )

#         plt.title(
#             "SOC Risk Distribution"
#         )

#         plt.show()


#         top_ips = []

#         top_attempts = []

#         for ip, attempts in ranking_list[:3]:

#             top_ips.append(
#                 ip
#             )

#             top_attempts.append(
#                 attempts
#             )

#         plt.figure(
#             figsize=(8, 5)
#         )

#         plt.bar(
#             top_ips,
#             top_attempts
#         )

#         plt.title(
#             "Top 3 Attackers"
#         )

#         plt.xlabel(
#             "IP Address"
#         )

#         plt.ylabel(
#             "Failed Attempts"
#         )

#         plt.show()
# 
#         
          


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# frame = tk.Frame(
#     window
# )

# frame.pack(
#     pady=20
# )

# scrollbar = tk.Scrollbar(
#     frame
# )

# scrollbar.pack(
#     side=tk.RIGHT,
#     fill=tk.Y
# )

# output_box = tk.Text(
#     frame,
#     height=20,
#     width=100,
#     yscrollcommand=scrollbar.set
# )

# output_box.pack(
#     side=tk.LEFT
# )

# scrollbar.config(
#     command=output_box.yview
# )

# window.mainloop()



# version 21 ------------Report generate in pdf 





# import tkinter as tk
# from tkinter import filedialog
# import matplotlib.pyplot as plt
# from tkinter import messagebox
# from reportlab.pdfgen import canvas

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "1000x700"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     first_event = ""
#     last_event = ""

#     for line in logs:

#         parts = line.split()

#         if len(parts) < 2:
#             continue

#         timestamp = (
#             parts[0]
#             + " "
#             + parts[1]
#         )

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if first_event == "":

#                 first_event = timestamp

#             last_event = timestamp

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     ranking_list = []

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         ranking_list.append(
#             (
#                 ip,
#                 attempts
#             )
#         )

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"First Event : {first_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Last Event : {last_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TOP 3 ATTACKERS ==========\n"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         output_box.insert(
#             tk.END,
#             f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1


#     messagebox.showinfo(
#         "Analysis Complete",
#         "SOC Analysis Completed Successfully!"
#     )


#     if (
#         high_risk +
#         medium_risk +
#         low_risk
#     ) > 0:

#         plt.figure(
#             figsize=(6, 6)
#         )

#         plt.pie(
#            [
#                  high_risk,
#                  medium_risk,
#                  low_risk
#            ],
#            labels=[
#                "High Risk",
#                "Medium Risk",
#                "Low Risk"
#             ],
#             autopct="%1.1f%%"
#         )

#         plt.title(
#             "SOC Risk Distribution"
#         )

#         plt.show()


#         top_ips = []

#         top_attempts = []

#         for ip, attempts in ranking_list[:3]:

#             top_ips.append(
#                 ip
#             )

#             top_attempts.append(
#                 attempts
#             )

#         plt.figure(
#             figsize=(8, 5)
#         )

#         plt.bar(
#             top_ips,
#             top_attempts
#         )

#         plt.title(
#             "Top 3 Attackers"
#         )

#         plt.xlabel(
#             "IP Address"
#         )

#         plt.ylabel(
#             "Failed Attempts"
#         )

#         plt.show() 

# def generate_pdf():

#            pdf = canvas.Canvas(
#                "SOC_Report.pdf"
#            )

#            pdf.setFont(
#                "Helvetica-Bold",
#                16
#             )

#            pdf.drawString(
#                 100,
#                 800,
#                 "SOC INCIDENT REPORT"
#            )

#            pdf.setFont(
#                 "Helvetica",
#                 12
#            )

#            content = output_box.get(
#                 "1.0",
#                 tk.END
#             )

#            y = 760

#            for line in content.split("\n"):

#             pdf.drawString(
#                 50,
#                 y,
#                 line
#             )

#             y -= 20

#             if y < 50:

#                 pdf.showPage()
 
#                 y = 800

#            pdf.save()

#            messagebox.showinfo(
#                "PDF Generated",
#                "SOC_Report.pdf Created Successfully"
#            )   


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# pdf_button = tk.Button(
#     window,
#     text="Generate PDF Report",
#     command=generate_pdf
# )

# pdf_button.pack(
#     pady=10
# )


# frame = tk.Frame(
#     window
# )

# frame.pack(
#     pady=20
# )

# scrollbar = tk.Scrollbar(
#     frame
# )

# scrollbar.pack(
#     side=tk.RIGHT,
#     fill=tk.Y
# )

# output_box = tk.Text(
#     frame,
#     height=20,
#     width=100,
#     yscrollcommand=scrollbar.set
# )

# output_box.pack(
#     side=tk.LEFT
# )

# scrollbar.config(
#     command=output_box.yview
# )

# window.mainloop()




# version -----------------------22 apecific ip check from file 




import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox
from reportlab.pdfgen import canvas

window = tk.Tk()

window.title(
    "SOC Log Analyzer Pro"
)

window.geometry(
    "1000x700"
)

selected_file = ""

ip_count = {}


def browse_file():

    global selected_file

    selected_file = filedialog.askopenfilename(
        filetypes=[
            ("Log Files", "*.log")
        ]
    )

    file_label.config(
        text=selected_file
    )


def search_ip():

    search_ip_value = search_entry.get()

    if search_ip_value == "":

        output_box.delete(
            "1.0",
            tk.END
        )

        output_box.insert(
            tk.END,
            "Please Enter IP Address"
        )

        return

    if search_ip_value in ip_count:

        attempts = ip_count[search_ip_value]

        if attempts >= 5:

            severity = "HIGH"

        elif attempts >= 2:

            severity = "MEDIUM"

        else:

            severity = "LOW"

        output_box.delete(
            "1.0",
            tk.END
        )

        output_box.insert(
            tk.END,
            f"IP Address : {search_ip_value}\n\n"
        )

        output_box.insert(
            tk.END,
            f"Attempts : {attempts}\n\n"
        )

        output_box.insert(
            tk.END,
            f"Severity : {severity}"
        )

    else:

        output_box.delete(
            "1.0",
            tk.END
        )

        output_box.insert(
            tk.END,
            "IP Not Found"
        )

def analyze_logs():

    global ip_count

    output_box.delete(
        "1.0",
        tk.END
    )

    ip_count = {}

    if selected_file == "":

        output_box.insert(
            tk.END,
            "Please Select a Log File First"
        )

        return

    log_file = open(
        selected_file,
        "r"
    )

    logs = log_file.readlines()

    ip_count = {}

    first_event = ""
    last_event = ""

    for line in logs:

        parts = line.split()

        if len(parts) < 2:
            continue

        timestamp = (
            parts[0]
            + " "
            + parts[1]
        )

        if "Failed login" in line:

            words = line.split()

            ip = words[-1]

            if first_event == "":

                first_event = timestamp

            last_event = timestamp

            if ip in ip_count:

                ip_count[ip] += 1

            else:

                ip_count[ip] = 1

    log_file.close()

    total_failed = sum(
        ip_count.values()
    )

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    top_attacker_ip = ""
    top_attacker_attempts = 0

    ranking_list = []

    for ip, attempts in ip_count.items():

        if attempts >= 5:

            high_risk += 1

        elif attempts >= 2:

            medium_risk += 1

        else:

            low_risk += 1

        if attempts > top_attacker_attempts:

            top_attacker_attempts = attempts

            top_attacker_ip = ip

        ranking_list.append(
            (
                ip,
                attempts
            )
        )

    ranking_list.sort(
        key=lambda x: x[1],
        reverse=True
    )

    output_box.insert(
        tk.END,
        "========== SOC DASHBOARD ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Total Failed Logins : {total_failed}\n\n"
    )

    output_box.insert(
        tk.END,
        f"High Risk IPs : {high_risk}\n"
    )

    output_box.insert(
        tk.END,
        f"Medium Risk IPs : {medium_risk}\n"
    )

    output_box.insert(
        tk.END,
        f"Low Risk IPs : {low_risk}\n\n"
    )

    output_box.insert(
        tk.END,
        "---------- TOP ATTACKER ----------\n\n"
    )

    output_box.insert(
        tk.END,
        f"IP Address : {top_attacker_ip}\n"
    )

    output_box.insert(
        tk.END,
        f"Failed Attempts : {top_attacker_attempts}\n"
    )

    output_box.insert(
        tk.END,
        "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"First Event : {first_event}\n"
    )

    output_box.insert(
        tk.END,
        f"Last Event : {last_event}\n"
    )

    output_box.insert(
        tk.END,
        "\n\n========== TOP 3 ATTACKERS ==========\n"
    )

    rank = 1

    for ip, attempts in ranking_list[:3]:

        output_box.insert(
            tk.END,
            f"\n{rank}. {ip} --> {attempts} Attempts"
        )

        rank += 1


    messagebox.showinfo(
        "Analysis Complete",
        "SOC Analysis Completed Successfully!"
    )


    if (
        high_risk +
        medium_risk +
        low_risk
    ) > 0:

        plt.figure(
            figsize=(6, 6)
        )

        plt.pie(
           [
                 high_risk,
                 medium_risk,
                 low_risk
           ],
           labels=[
               "High Risk",
               "Medium Risk",
               "Low Risk"
            ],
            autopct="%1.1f%%"
        )

        plt.title(
            "SOC Risk Distribution"
        )

        plt.show()


        top_ips = []

        top_attempts = []

        for ip, attempts in ranking_list[:3]:

            top_ips.append(
                ip
            )

            top_attempts.append(
                attempts
            )

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(
            top_ips,
            top_attempts
        )

        plt.title(
            "Top 3 Attackers"
        )

        plt.xlabel(
            "IP Address"
        )

        plt.ylabel(
            "Failed Attempts"
        )

        plt.show() 

def generate_pdf():

           pdf = canvas.Canvas(
               "SOC_Report.pdf"
           )

           pdf.setFont(
               "Helvetica-Bold",
               16
            )

           pdf.drawString(
                100,
                800,
                "SOC INCIDENT REPORT"
           )

           pdf.setFont(
                "Helvetica",
                12
           )

           content = output_box.get(
                "1.0",
                tk.END
            )

           y = 760

           for line in content.split("\n"):

            pdf.drawString(
                50,
                y,
                line
            )

            y -= 20

            if y < 50:

                pdf.showPage()
 
                y = 800

           pdf.save()

           messagebox.showinfo(
               "PDF Generated",
               "SOC_Report.pdf Created Successfully"
           )   


heading = tk.Label(
    window,
    text="SOC LOG ANALYZER PRO",
    font=("Arial", 20, "bold")
)

heading.pack(
    pady=20
)

browse_button = tk.Button(
    window,
    text="Browse Log File",
    command=browse_file
)

browse_button.pack(
    pady=10
)

file_label = tk.Label(
    window,
    text="No File Selected"
)

file_label.pack(
    pady=10
)

search_label = tk.Label(
    window,
    text="Enter IP Address"
)

search_label.pack(
    pady=5
)

search_entry = tk.Entry(
    window,
    width=30
)

search_entry.pack(
    pady=5
)

analyze_button = tk.Button(
    window,
    text="Analyze Logs",
    command=analyze_logs
)

analyze_button.pack(
    pady=10
)

search_button = tk.Button(
    window,
    text="Search IP",
    command=search_ip
)

search_button.pack(
    pady=10
)

pdf_button = tk.Button(
    window,
    text="Generate PDF Report",
    command=generate_pdf
)

pdf_button.pack(
    pady=10
)


frame = tk.Frame(
    window
)

frame.pack(
    pady=20
)

scrollbar = tk.Scrollbar(
    frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

output_box = tk.Text(
    frame,
    height=20,
    width=100,
    yscrollcommand=scrollbar.set
)

output_box.pack(
    side=tk.LEFT
)

scrollbar.config(
    command=output_box.yview
)

window.mainloop()
