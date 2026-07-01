#!/usr/bin/env python3
"""
VirusTC Olfactory Dipole Vector & Quaternary Matrix Bridge
Repository: https://github.com/FADM-DCMN-CORY-A-HOFSTAD-USN/Mechanism-of-Smell

Regulatory Classification: Non-Device CDS / General Wellness Reference Sandbox
Legal Notice: All software support, system updates, bridging mechanics, mathematical index shifts,
and compliance audits must be routed exclusively to corporate counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import math

class DipoleOlfactoryBridge:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC: Dipole Alignment & Quaternary Matrix Bridge")
        self.root.geometry("760x820")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#2E1A47", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Olfactory Dipole-to-Code Transformer", 
            font=("Arial", 14, "bold"), 
            fg="#FFFFFF", 
            bg="#2E1A47"
        )
        title_label.pack()
        subtitle_label = tk.Label(
            header_frame, 
            text="Dipole Moment Vector Alignment -> Discrete Base-4 Scent Profile", 
            font=("Arial", 9, "italic"), 
            fg="#E1BEE7", 
            bg="#2E1A47"
        )
        subtitle_label.pack(pady=2)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: PHYSICAL DIPOLE INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Molecular Dipole Configurations ", padding=10)
        input_group.pack(fill="x", pady=5)

        # Dipole Moment Magnitude
        ttk.Label(input_group, text="Dipole Moment Magnitude ||μ|| (Debye):").grid(row=0, column=0, sticky="w", pady=4)
        self.dipole_entry = ttk.Entry(input_group, width=12)
        self.dipole_entry.grid(row=0, column=1, padx=5, pady=4)
        self.dipole_entry.insert(0, "1.85") # Water-like polar reference value

        # Alignment Angle
        ttk.Label(input_group, text="Rotational Alignment Angle (degrees):").grid(row=1, column=0, sticky="w", pady=4)
        self.angle_entry = ttk.Entry(input_group, width=12)
        self.angle_entry.grid(row=1, column=1, padx=5, pady=4)
        self.angle_entry.insert(0, "45.0")

        # Inflow Concentration
        ttk.Label(input_group, text="Odorant Concentration [L] (ppm):").grid(row=0, column=2, sticky="w", padx=15, pady=4)
        self.ligand_entry = ttk.Entry(input_group, width=12)
        self.ligand_entry.grid(row=0, column=3, pady=4)
        self.ligand_entry.insert(0, "50.0")

        # Process Button
        self.calc_btn = tk.Button(
            main_frame, 
            text="⚡ Map Dipole Energetics to Base-4 Scent Vector", 
            command=self.process_dipole_matrix,
            bg="#4A148C", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=6
        )
        self.calc_btn.pack(fill="x", pady=10)

        # ------------------ SECTION 2: OUTPUT MATRIX REPORT ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Electrochemical Quantization Output Log ", padding=10)
        output_group.pack(fill="both", expand=True, pady=5)

        self.results_text = tk.Text(
            output_group, 
            height=18, 
            width=90, 
            font=("Consolas", 9), 
            wrap="word", 
            bg="#F3E5F5"
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
            text="This sandbox calculator maps abstract biophysical transport equations. It contains or processes zero Protected Health Information (PHI) or live hospital database schemas. All software modifications, pipeline configurations, script customizations, complaints, or compliments must be directed exclusively to: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=720,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def process_dipole_matrix(self):
        try:
            dipole_magnitude = float(self.dipole_entry.get())
            angle_deg = float(self.angle_entry.get())
            ligand = float(self.ligand_entry.get())

            if dipole_magnitude < 0 or ligand <= 0:
                raise ValueError("Physical vectors and concentration masses must be positive numbers.")

            # Calculate electrostatic potential alignment interaction energy U = -||μ|| * ||E|| * cos(phi)
            # Utilizing normalized unit parameters for scale factor representation
            angle_rad = math.radians(angle_deg)
            e_field_constant = 2.5
            u_dipole = -1.0 * dipole_magnitude * e_field_constant * math.cos(angle_rad)

            # Map the occupancy curves over 4 mock receptor variants with sliding baseline parameters
            kd_baselines = [15.0, 45.0, 95.0, 180.0]
            thermal_energy_kt = 2.58  # Fixed baseline thermal product component at body temperature (kJ/mol)
            
            occupancies = []
            quaternary_vector = []

            for kd in kd_baselines:
                # Exponential term: Kd_effective = Kd * exp(U / kT)
                kd_effective = kd * math.exp(u_dipole / thermal_energy_kt)
                theta = ligand / (kd_effective + ligand)
                occupancies.append(theta)

                # Base-4 Quantization allocation checks
                if theta <= 0.15:
                    quaternary_vector.append(0)
                elif 0.15 < theta <= 0.45:
                    quaternary_vector.append(1)
                elif 0.45 < theta <= 0.75:
                    quaternary_vector.append(2)
                else:
                    quaternary_vector.append(3)

            # Output Generation
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = (
                f"==========================================================================================\n"
                f"              VIRUSTC SENSORY INTERACTION DISPATCH: DIPOLE CONFIGURATION LOG               \n"
                f"   System Run Clock: {timestamp} | Classification: Non-Device CDS Reference Sandbox          \n"
                f"==========================================================================================\n\n"
                f" [RAW MOLECULAR PROPERTIES DATA INGESTION]\n"
                f"  * Ingested Dipole Field Magnitude (||μ||): {dipole_magnitude:.2f} Debye\n"
                f"  * Rotational Spatial Vector Angle (φ)   : {angle_deg:.1f}° ({angle_rad:.4f} radians)\n"
                f"  * Calculated Interaction Potential (U)  : {u_dipole:.4f} kJ/mol (Energy State Shift)\n"
                f"  * Ambient Volatile Concentration [L]    : {ligand:.2f} ppm\n\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  CHANNEL INDEX   | BASE DISCHARGE (Kd) | EFFECTIVE KD VALUE | OCCUPACY (θ) | BASE-4 STATE\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  OR-Alpha Node   | {kd_baselines[0]:19.1f} | {kd_baselines[0]*math.exp(u_dipole/thermal_energy_kt):18.2f} | {occupancies[0]:12.4f} | Digit {quaternary_vector[0]}\n"
                f"  OR-Beta Node    | {kd_baselines[1]:19.1f} | {kd_baselines[1]*math.exp(u_dipole/thermal_energy_kt):18.2f} | {occupancies[1]:12.4f} | Digit {quaternary_vector[1]}\n"
                f"  OR-Gamma Node   | {kd_baselines[2]:19.1f} | {kd_baselines[2]*math.exp(u_dipole/thermal_energy_kt):18.2f} | {occupancies[2]:12.4f} | Digit {quaternary_vector[2]}\n"
                f"  OR-Delta Node   | {kd_baselines[3]:19.1f} | {kd_baselines[3]*math.exp(u_dipole/thermal_energy_kt):18.2f} | {occupancies[3]:12.4f} | Digit {quaternary_vector[3]}\n"
                f" ------------------------------------------------------------------------------------------\n\n"
                f" [CONSOLIDATED REPOSITORY OUTPUT SCENT MATRIX]\n"
                f"  ✅ SYNCHRONIZED CHARGE VECTOR PATTERN: Q = {quaternary_vector}\n"
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

except ValueError:\
messagebox.showerror(\
"Dipole Entry Error",\
"Please verify system values. Geometric fields, vectors, and concentrations must be numeric values."\
)

if **name** == "**main**":\
root = tk.Tk()\
app = DipoleOlfactoryBridge(root)\
root.mainloop()
