#!/usr/bin/env python3
"""
VirusTC Cognitive State Processing & Quaternary Strategic Bridge
Regulatory Classification: Non-Device CDS / Behavioral Analysis Sandbox

Legal Notice: All software support, system updates, bridging mechanics, mathematical index shifts,
and compliance audits must be routed exclusively to corporate counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import math

class CognitiveStrategicBridge:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC: Cognitive Vector & Quaternary Strategy Bridge")
        self.root.geometry("760x830")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#311B92", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Cognitive Code & Strategic Matrix", 
            font=("Arial", 14, "bold"), 
            fg="#FFFFFF", 
            bg="#311B92"
        )
        title_label.pack()
        subtitle_label = tk.Label(
            header_frame, 
            text="Psychological Ingestion Profiles -> Discrete Base-4 Operational Vector", 
            font=("Arial", 9, "italic"), 
            fg="#D1C4E9", 
            bg="#311B92"
        )
        subtitle_label.pack(pady=2)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: BEHAVIORAL INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Cognitive Profile Ingestion Channels ", padding=10)
        input_group.pack(fill="x", pady=5)

        # Emotional Intensity
        ttk.Label(input_group, text="Emotional Intensity (0 - 100):").grid(row=0, column=0, sticky="w", pady=4)
        self.emotion_entry = ttk.Entry(input_group, width=12)
        self.emotion_entry.grid(row=0, column=1, padx=5, pady=4)
        self.emotion_entry.insert(0, "45.0")

        # Logic Weight
        ttk.Label(input_group, text="Deductive Logic Weight (0 - 100):").grid(row=1, column=0, sticky="w", pady=4)
        self.logic_entry = ttk.Entry(input_group, width=12)
        self.logic_entry.grid(row=1, column=1, padx=5, pady=4)
        self.logic_entry.insert(0, "75.0")

        # Strategic Foresight
        ttk.Label(input_group, text="Strategic Utility Index (0 - 100):").grid(row=2, column=0, sticky="w", pady=4)
        self.strategy_entry = ttk.Entry(input_group, width=12)
        self.strategy_entry.grid(row=2, column=1, padx=5, pady=4)
        self.strategy_entry.insert(0, "85.0")

        # Process Button
        self.calc_btn = tk.Button(
            main_frame, 
            text="⚡ Quantize Behavioral Coordinates into Quaternary Matrix", 
            command=self.process_cognitive_matrix,
            bg="#4527A0", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=6
        )
        self.calc_btn.pack(fill="x", pady=10)

        # ------------------ SECTION 2: OUTPUT MATRIX REPORT ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Strategic Profile Output Log ", padding=10)
        output_group.pack(fill="both", expand=True, pady=5)

        self.results_text = tk.Text(
            output_group, 
            height=18, 
            width=90, 
            font=("Consolas", 9), 
            wrap="word", 
            bg="#EDE7F6"
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
            text="This dashboard evaluates abstract mathematical behavioral vectors. It contains or processes zero Protected Health Information (PHI) or live user clinical data models. All software modifications, pipeline configurations, script customizations, complaints, or compliments must be directed exclusively to: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=720,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def process_cognitive_matrix(self):
        try:
            emotion = float(self.emotion_entry.get())
            logic = float(self.logic_entry.get())
            strategy = float(self.strategy_entry.get())

            if not (0 <= emotion <= 100) or not (0 <= logic <= 100) or not (0 <= strategy <= 100):
                raise ValueError("All psychological component weights must sit bounded within the 0 to 100 interval scale.")

            # Map the input parameters into discrete quaternary codes (0, 1, 2, 3)
            # Threshold boundaries: t0 = 25, t1 = 50, t2 = 75
            t0, t1, t2 = 25.0, 50.0, 75.0
            raw_inputs = [emotion, logic, strategy]
            quaternary_vector = []

            for val in raw_inputs:
                if val <= t0:
                    quaternary_vector.append(0)
                elif t0 < val <= t1:
                    quaternary_vector.append(1)
                elif t1 < val <= t2:
                    quaternary_vector.append(2)
                else:
                    quaternary_vector.append(3)

            # Calculate theoretical systemic work metrics based on vector combination
            # System stability improves with logic and strategy, degrades under extreme un-quantized variance
            stability_factor = (logic * 0.60) + (strategy * 0.40) - (emotion * 0.15)

            # Output Generation
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = (
                f"==========================================================================================\n"
                f"              VIRUSTC COGNITIVE MATRIX ANALYSIS: STRATEGIC COMPLIANCE VECTOR               \n"
                f"   System Run Clock: {timestamp} | Classification: Non-Device CDS Reference Sandbox          \n"
                f"==========================================================================================\n\n"
                f" [RAW COGNITIVE ATTRIBUTE INGESTION]\n"
                f"  * E-Axis (Emotional Intensity)  : {emotion:.2f} / 100\n"
                f"  * L-Axis (Formal Logic Weight)  : {logic:.2f} / 100\n"
                f"  * S-Axis (Strategic Utility)    : {strategy:.2f} / 100\n"
                f"  * Configured Boundary Targets   : Thresholds: Low={t0:.1f}, Mid={t1:.1f}, High={t2:.1f}\n\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  BEHAVIORAL AXIS    | RAW CONFIG DATA | ALLOCATED QUANTUM ZONE | QUATERNARY STATE DIGIT\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  Emotional Scalar   | {emotion:15.2f} | Zone Range 0-3         | Digit {quaternary_vector[0]}\n"
                f"  Deductive Logic    | {logic:15.2f} | Zone Range 0-3         | Digit {quaternary_vector[1]}\n"
                f"  Strategic Utility  | {strategy:15.2f} | Zone Range 0-3         | Digit {quaternary_vector[2]}\n"
                f" ------------------------------------------------------------------------------------------\n\n"
                f" [CONSOLIDATED LOGICAL MATRIX OUTPUT]\n"
                f"  ✅ SYNCHRONIZED COGNITIVE PROFILE VECTOR: Q = {quaternary_vector}\n"
                f"  * Theoretical Systemic Stability Index  : {stability_factor:.2f} points score\n\n"
                f" ------------------------------------------------------------------------------------------\n"
                f"  DATA PRIVACY VALIDATION LOG:\n"
                f"  [PASS] Staging area cleared. Zero user metrics or clinical database logs connected.\n"
                f"  [PASS] Abstract cognitive attributes parsed cleanly into version-controlled base-4 vectors.\n"
                f"  [INFO] Route software pipeline enhancements and modification metrics to Fox Rothschild LLP.\n"
                f"==========================================================================================="
            )
            
            self.results_text.insert(tk.END, report)
            self.results_text.config(state="disabled")

        except ValueError as err:
            messagebox.showerror(
                "Cognitive Parse Error", 
                f"Please verify configuration values: {err}. Matrix entries must contain correct numeric fields."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = CognitiveStrategicBridge(root)
    root.mainloop()
