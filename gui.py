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




# version -----------------------22 specific ip check from file 




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

# ip_count = {}


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


# def search_ip():

#     search_ip_value = search_entry.get()

#     if search_ip_value == "":

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             "Please Enter IP Address"
#         )

#         return

#     if search_ip_value in ip_count:

#         attempts = ip_count[search_ip_value]

#         if attempts >= 5:

#             severity = "HIGH"

#         elif attempts >= 2:

#             severity = "MEDIUM"

#         else:

#             severity = "LOW"

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             f"IP Address : {search_ip_value}\n\n"
#         )

#         output_box.insert(
#             tk.END,
#             f"Attempts : {attempts}\n\n"
#         )

#         output_box.insert(
#             tk.END,
#             f"Severity : {severity}"
#         )

#     else:

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             "IP Not Found"
#         )

# def analyze_logs():

#     global ip_count

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     ip_count = {}

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

# search_label = tk.Label(
#     window,
#     text="Enter IP Address"
# )

# search_label.pack(
#     pady=5
# )

# search_entry = tk.Entry(
#     window,
#     width=30
# )

# search_entry.pack(
#     pady=5
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# search_button = tk.Button(
#     window,
#     text="Search IP",
#     command=search_ip
# )

# search_button.pack(
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




# version 23 -----------Real time  Log monitoring 



# import tkinter as tk
# from tkinter import filedialog
# import matplotlib.pyplot as plt
# from tkinter import messagebox
# from reportlab.pdfgen import canvas

# import time
# import threading


# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "1000x700"
# )

# selected_file = ""

# monitoring = False

# ip_count = {}


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


# def search_ip():

#     search_ip_value = search_entry.get()

#     if search_ip_value == "":

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             "Please Enter IP Address"
#         )

#         return

#     if search_ip_value in ip_count:

#         attempts = ip_count[search_ip_value]

#         if attempts >= 5:

#             severity = "HIGH"

#         elif attempts >= 2:

#             severity = "MEDIUM"

#         else:

#             severity = "LOW"

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             f"IP Address : {search_ip_value}\n\n"
#         )

#         output_box.insert(
#             tk.END,
#             f"Attempts : {attempts}\n\n"
#         )

#         output_box.insert(
#             tk.END,
#             f"Severity : {severity}"
#         )

#     else:

#         output_box.delete(
#             "1.0",
#             tk.END
#         )

#         output_box.insert(
#             tk.END,
#             "IP Not Found"
#         )

# def analyze_logs():

#     global ip_count

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     ip_count = {}

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


# def start_monitoring():

#     global monitoring

#     monitoring = True

#     thread = threading.Thread(
#         target=monitor_logs
#     )

#     thread.daemon = True

#     thread.start()


# def monitor_logs():

#     if selected_file == "":

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     log_file.seek(
#         0,
#         2
#     )

#     while monitoring:

#         line = log_file.readline()

#         if not line:

#             time.sleep(
#                 1
#             )

#             continue

#         if "Failed login" in line:

#             output_box.insert(
#                 tk.END,
#                 "\n\n⚠ NEW ATTACK DETECTED\n"
#             )

#             output_box.insert(
#                 tk.END,
#                 line
#             )

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

# search_label = tk.Label(
#     window,
#     text="Enter IP Address"
# )

# search_label.pack(
#     pady=5
# )

# search_entry = tk.Entry(
#     window,
#     width=30
# )

# search_entry.pack(
#     pady=5
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# search_button = tk.Button(
#     window,
#     text="Search IP",
#     command=search_ip
# )

# search_button.pack(
#     pady=10
# )

# monitor_button = tk.Button(
#     window,
#     text="Start Monitoring",
#     command=start_monitoring
# )

# monitor_button.pack(
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





# version 24----------- change dashboard Look



import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox
from reportlab.pdfgen import canvas

import time
import threading


window = tk.Tk()

window.title(
    "SOC Log Analyzer Pro"
)

window.geometry(
    "1300x800"
)

window.configure(
    bg="#1e1e1e"
)

selected_file = ""

monitoring = False

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

    linux_ssh_detected = False

    for line in logs:

        parts = line.split()

        if len(parts) < 2:
            continue

        timestamp = (
            parts[0]
            + " "
            + parts[1]
        )

        if (
             "Failed login" in line
             or
             "Failed password" in line
        ):
            
            if "Failed password" in line:

                linux_ssh_detected = True

            words = line.split()

            ip = "Unknown"

            if "from" in words:

                from_index = words.index(
                    "from"
                )

                if from_index + 1 < len(words):

                    ip = words[
                         from_index + 1
                    ]

            else:

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

    high_label.config(
        text=f"HIGH RISK : {high_risk}"
    )

    medium_label.config(
        text=f"MEDIUM RISK : {medium_risk}"
    )

    low_label.config(
        text=f"LOW RISK : {low_risk}"
    )

    total_label.config(
         text=f"TOTAL FAILED : {total_failed}"
    )

    output_box.insert(
        tk.END,
        "\n========== LIVE THREAT SUMMARY ==========\n\n",
        "title"
    )

    if linux_ssh_detected:

        output_box.insert(
            tk.END,
            "🐧 LINUX SSH AUTH.LOG DETECTED\n\n",
            "medium"
        )

    if high_risk > 0:

       output_box.insert(
           tk.END,
           "⚠ SSH BRUTE FORCE ATTACK DETECTED\n\n",
           "high"
        )

    if high_risk > 0:

        output_box.insert(
            tk.END,
            f"🔴 HIGH RISK ATTACKS DETECTED : {high_risk}\n",
            "high"
        )

    if medium_risk > 0:

        output_box.insert(
            tk.END,
            f"🟠 MEDIUM RISK ATTACKS DETECTED : {medium_risk}\n",
            "medium"
        )

    if low_risk > 0:

        output_box.insert(
           tk.END,
           f"🟢 LOW RISK ATTACKS DETECTED : {low_risk}\n",
           "low"
        )

    output_box.insert(
        tk.END,
        "\n"
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

    if high_risk > 0:

        messagebox.showwarning(
            "SOC EMAIL ALERT",
            f"High Risk Attack Detected!\n\nTop Attacker: {top_attacker_ip}\nAttempts: {top_attacker_attempts}"
        )    


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

def clear_output():

    output_box.delete(
        "1.0",
        tk.END
    )   

    output_box.insert(
        tk.END,
        "\n========== SOC DASHBOARD SUMMARY ==========\n\n"
    )     

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


def start_monitoring():

    global monitoring

    monitoring = True

    status_label.config(
        text="🟢 Monitoring Active",
        fg="lime"
    )

    thread = threading.Thread(
        target=monitor_logs
    )

    thread.daemon = True

    thread.start()


def monitor_logs():

    if selected_file == "":

        return

    log_file = open(
        selected_file,
        "r"
    )

    log_file.seek(
        0,
        2
    )

    while monitoring:

        line = log_file.readline()

        if not line:

            time.sleep(
                1
            )

            continue

        if "Failed login" in line:

            output_box.insert(
                tk.END,
                "\n\n⚠ NEW ATTACK DETECTED\n"
            )

            output_box.insert(
                tk.END,
                line
            )

heading = tk.Label(
    window,
    text="SOC LOG ANALYZER PRO\nReal-Time Threat Detection",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="#00ff00"
)

heading.pack(
    pady=20
)

summary_frame = tk.Frame(
    window,
    bg="#1e1e1e"
)

summary_frame.pack(
    pady=10
)

high_label = tk.Label(
    summary_frame,
    text="HIGH RISK : 0",
    bg="#1e1e1e",
    fg="red",
    font=("Arial", 10, "bold")
)

high_label.grid(
    row=0,
    column=0,
    padx=15
)

medium_label = tk.Label(
    summary_frame,
    text="MEDIUM RISK : 0",
    bg="#1e1e1e",
    fg="orange",
    font=("Arial", 10, "bold")
)

medium_label.grid(
    row=0,
    column=1,
    padx=15
)

low_label = tk.Label(
    summary_frame,
    text="LOW RISK : 0",
    bg="#1e1e1e",
    fg="lime",
    font=("Arial", 10, "bold")
)

low_label.grid(
    row=0,
    column=2,
    padx=15
)

total_label = tk.Label(
    summary_frame,
    text="TOTAL FAILED : 0",
    bg="#1e1e1e",
    fg="cyan",
    font=("Arial", 10, "bold")
)

total_label.grid(
    row=0,
    column=3,
    padx=15
)

status_label = tk.Label(
    window,
    text="🔴 Monitoring Stopped",
    bg="#1e1e1e",
    fg="red",
    font=("Arial", 11, "bold")
)

status_label.pack(
    pady=5
)

button_frame = tk.Frame(
    window,
    bg="#1e1e1e"
)

button_frame.pack(
    pady=15
)

browse_button = tk.Button(
    button_frame,
    text="Browse Log File",
    command=browse_file,
    bg="#0078D7",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

browse_button.pack(
    side=tk.LEFT,
    padx=5
)

file_label = tk.Label(
    window,
    text="No File Selected",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 10, "bold")
)

file_label.pack(
    pady=10
)

search_label = tk.Label(
    window,
    text="Enter IP Address",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 10, "bold")
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
   button_frame,
    text="Analyze Logs",
    command=analyze_logs,
    bg="#28A745",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

analyze_button.pack(
    side=tk.LEFT,
    padx=5
)

search_button = tk.Button(
   button_frame,
    text="Search IP",
    command=search_ip,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

search_button.pack(
    side=tk.LEFT,
    padx=5
)

monitor_button = tk.Button(
    button_frame,
    text="Start Monitoring",
    command=start_monitoring,
    bg="#DC3545",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

monitor_button.pack(
    side=tk.LEFT,
    padx=5
)

pdf_button = tk.Button(
   button_frame,
    text="Generate PDF Report",
    command=generate_pdf,
    bg="#6F42C1",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

pdf_button.pack(
    side=tk.LEFT,
    padx=5
)

clear_button = tk.Button(
   button_frame,
    text="Clear Output",
    command=clear_output,
    bg="#343A40",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20
)

clear_button.pack(
    side=tk.LEFT,
    padx=5
)


output_box = tk.Text(
    window,
    height=25,
    width=140,
    bg="#111111",
    fg="#00ff00",
    insertbackground="white",
    font=("Consolas", 10)
)

output_box.pack(
    pady=20,
    fill="both",
    expand=True,
    padx=20
)

output_box.tag_config(
    "high",
    foreground="red"
)

output_box.tag_config(
    "medium",
    foreground="orange"
)

output_box.tag_config(
    "low",
    foreground="lime"
)

output_box.tag_config(
    "title",
    foreground="cyan"
)


window.mainloop()

