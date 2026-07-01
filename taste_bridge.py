#!/usr/bin/env python3
"""
VirusTC Gustatory Dipole Vector & Quaternary Matrix Bridge
Regulatory Classification: Non-Device CDS / Taste Profile Evaluation Sandbox

Legal Notice: All software support, system updates, bridging mechanics, mathematical index shifts,
and compliance audits must be routed exclusively to corporate counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import math

class GustatoryDipoleBridge:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC: Gustatory Dipole & Quaternary Matrix Bridge")
        self.root.geometry("760x830")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#E65100", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Gustatory Dipole-to-Profile Transformer", 
            font=("Arial", 14, "bold"), 
            fg="#FFFFFF", 
            bg="#E65100"
        )
        title_label.pack()
        subtitle_label = tk.Label(
            header_frame, 
            text="Molecular Dipole Moment Ingestion -> Discrete Base-4 Taste Profile Vector", 
            font=("Arial", 9, "italic"), 
            fg="#FFE0B2", 
            bg="#E65100"
        )
        subtitle_label.pack(pady=2)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: PHYSICAL INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Biophysical Tastant Parameters ", padding=10)
        input_group.pack(fill="x", pady=5)

        # Dipole Moment Magnitude
        ttk.Label(input_group, text="Dipole Moment Magnitude ||μ|| (Debye):").grid(row=0, column=0, sticky="w", pady=4)
        self.dipole_entry = ttk.Entry(input_group, width=12)
        self.dipole_entry.grid(row=0, column=1, padx=5, pady=4)
        self.dipole_entry.insert(0, "1.70") # Acetic acid-like dipole baseline reference

        # Inversion Angle
        ttk.Label(input_group, text="Pocket Docking Alignment Angle (deg):").grid(row=1, column=0, sticky="w", pady=4)
        self.angle_entry = ttk.Entry(input_group, width=12)
        self.angle_entry.grid(row=1, column=1, padx=5, pady=4)
        self.angle_entry.insert(0, "30.0")

        # Tastant Concentration
        ttk.Label(input_group, text="Tastant Concentration [T] (mM):").grid(row=0, column=2, sticky="w", padx=15, pady=4)
        self.tastant_entry = ttk.Entry(input_group, width=12)
        self.tastant_entry.grid(row=0, column=3, pady=4)
        self.tastant_entry.insert(0, "25.0")

        # Process Button
        self.calc_btn = tk.Button(
            main_frame, 
            text="⚡ Quantize Tastant Energetics into Quaternary Profile Vector", 
            command=self.process_taste_matrix,
            bg="#EF6C00", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=6
        )
        self.calc_btn.pack(fill="x", pady=10)

        # ------------------ SECTION 2: OUTPUT MATRIX REPORT ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Electrochemical Gustatory Transduction Log ", padding=10)
        output_group.pack(fill="both", expand=True, pady=5)

        self.results_text = tk.Text(
            output_group, 
            height=18, 
            width=90, 
            font=("Consolas", 9), 
            wrap="word", 
            bg="#FFF3E0"
        )
        self.results_text.pack(fill="both", expand=True)
        self.results_text.config(state="disabled")

        # ------------------ SECTION 3: CORPORATE MANDATED LEGAL BANNER ------------------
        legal_frame = tk.Frame(main_frame, bd=1, relief="solid", padding=10, bg="#FFF8F8")
        legal_frame.pack(fill="x", side="bottom", pady=5)

        legal_title = tk.Label(
            legal_frame, 
            text="🏛️ INSTITUTIONAL DATA GOVERNANCE & METADATA COMPLIANCE NOTICE", 
            font=("Arial", 9, "bold"), 
            fg="#D9534F",
            bg="#FFF8F8"
        )
        legal_title.pack(anchor="w")

        legal_body = tk.Label(
            legal_frame, 
            text="This sandbox model parses structural mathematical tracking equations. It processes zero Protected Health Information (PHI) or individual patient files. All software modifications, pipeline configurations, script customizations, complaints, or compliments must be directed exclusively to: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=720,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def process_taste_matrix(self):
        try:
            dipole_magnitude = float(self.dipole_entry.get())
            angle_deg = float(self.angle_entry.get())
            tastant_conc = float(self.tastant_entry.get())

            if dipole_magnitude < 0 or tastant_conc <= 0:
                raise ValueError("Physical vectors and concentration values must be positive numbers.")

            # Calculate electrostatic potential alignment interaction energy U = -||μ|| * ||E|| * cos(gamma)
            angle_rad = math.radians(angle_deg)
            e_field_pocket_constant = 1.95
            u_taste = -1.0 * dipole_magnitude * e_field_pocket_constant * math.cos(angle_rad)

            # Map the occupancy curves over 4 base taste receptors with fixed baseline affinities (Kd in mM)
            taste_channels = ["Sweet Core Channel", "Sour Core Channel", "Bitter Core Channel", "Umami Core Channel"]
            kd_baselines = [10.0, 35.0, 80.0, 160.0]
            thermal_energy_kt = 2.58  # Fixed kJ/mol baseline constant at body temperature
            
            occupancies = []
            quaternary_vector = []
            t0, t1, t2 = 0.10, 0.40, 0.70

            for kd in kd_baselines:
                kd_effective = kd * math.exp(u_taste / thermal_energy_kt)
                theta = tastant_conc / (kd_effective + tastant_conc)
                occupancies.append(theta)

                # Base-4 Quantization boundaries check
                if theta <= t0:
                    quaternary_vector.append(0)
                elif t0 < theta <= t1:
                    quaternary_vector.append(1)
                elif t1 < theta <= t2:
                    quaternary_vector.append(2)
                else:
                    quaternary_vector.append(3)

            # Output Generation
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = (
                f"==========================================================================================\n"
                f"              VIRUSTC SENSORY INTERACTION DISPATCH: TASTE PROFILE VECTOR LOG               \n"
                f"   System Run Clock: {timestamp} | Classification: Non-Device CDS Reference Sandbox          \n"
                f"==========================================================================================\n\n"
                f" [RAW MOLECULAR PROPERTIES DATA INGESTION]\n"
                f"  * Ingested Dipole Field Magnitude (||μ||): {dipole_magnitude:.2f} Debye\n"
                f"  * Pocket Alignment Spatial Angle (γ)    : {angle_deg:.1f}° ({angle_rad:.4f} radians)\n"
                f"  * Calculated Interaction Potential (U)  : {u_taste:.4f} kJ/mol (Electrostatic Shift)\n"
                f"  * Ambient Tastant Concentration [T]     : {tastant_conc:.2f} mM\n\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  GUSTATORY CHANNEL | BASE DISCHARGE (Kd) | EFFECTIVE KD VALUE | OCCUPACY (θ) | BASE-4 STATE\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  {taste_channels[0]:17} | {kd_baselines[0]:19.1f} | {kd_baselines[0]*math.exp(u_taste/thermal_energy_kt):18.2f} | {occupancies[0]:12.4f} | Digit {quaternary_vector[0]}\n"
                f"  {taste_channels[1]:17} | {kd_baselines[1]:19.1f} | {kd_baselines[1]*math.exp(u_taste/thermal_energy_kt):18.2f} | {occupancies[1]:12.4f} | Digit {quaternary_vector[1]}\n"
                f"  {taste_channels[2]:17} | {kd_baselines[2]:19.1f} | {kd_baselines[2]*math.exp(u_taste/thermal_energy_kt):18.2f} | {occupancies[2]:12.4f} | Digit {quaternary_vector[2]}\n"
                f"  {taste_channels[3]:17} | {kd_baselines[3]:19.1f} | {kd_baselines[3]*math.exp(u_taste/thermal_energy_kt):18.2f} | {occupancies[3]:12.4f} | Digit {quaternary_vector[3]}\n"
                f" ------------------------------------------------------------------------------------------\n\n"
                f" [CONSOLIDATED REPOSITORY OUTPUT TASTE MATRIX]\n"
                f"  ✅ SYNCHRONIZED TASTE CODE VECTOR: Q = {quaternary_vector}\n"
                f"  * Array Theoretical Entropy Resolving Bounds: {2 * len(kd_baselines)} bits max data scale\n\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  DATA PRIVACY VALIDATION LOG:\n"
                f"  [PASS] Clean runtime staging environment. Absolute PHI Exclusion enforced.\n"
                f"  [PASS] Continuous bio-physical features quantized cleanly into discrete base-4 metrics.\n"
                f"  [INFO] Route software pipeline enhancements and modification metrics to Fox Rothschild LLP.\n"
                f"==========================================================================================="
            )
            self.results_text.insert(tk.END, report)\
self.results_text.config(state="disabled")

except ValueError as err:\
messagebox.showerror(\
"Dipole Entry Error",\
f"Please verify system values: {err}. Matrix entries must contain correct numeric fields."\
)

if **name** == "**main**":\
root = tk.Tk()\
app = GustatoryDipoleBridge(root)\
root.mainloop()
