#Geotechnical parameters 

import math

class GeotechnicalParameters:
    @staticmethod
    def undrained_shear_strength(sptn, pi, effective_stress, cbr, plnet, cpt, sptn60):
        """Calculate undrained shear strength using various methods"""
        cu_1 = 98.1 + 0.06 * sptn
        cu_2 = (0.11 + 0.0037 * pi) * effective_stress
        cu_3 = ((8910 / math.pow(pi, 3)) + 4.36) * sptn
        cu_4 = cbr / 0.09
        cu_5 = 98.1 * 0.29 * math.pow(sptn, 0.72)
        cu_6 = (cpt - effective_stress) / 1.7
        cu_7 = (98.1 * 0.29) * math.pow(sptn60, 0.6)
        cu_8 = 6.25 * sptn
        cu_9 = 12 * sptn
        cu_10 = 4.43 * sptn + 8.07
        cu_11 = 12.5 * sptn
        cu_12 = 15 * sptn60

        if plnet < 300:
            cu_13 = plnet / 5.5
        else:
            cu_13 = plnet / 10

        if pi > 30:
            cu_14 = 4.2 * sptn
        elif pi < 20:
            cu_14 = 6.5 * sptn
        else:
            cu_14 = 4.5 * sptn

        if pi > 20:
            cu_15 = 12 * sptn
        elif pi < 10:
            cu_15 = 7.25 * sptn
        else:
            cu_15 = 3.63 * sptn

        cu_16 = 25 + (plnet / 10)
        cu_17 = 98.1 * 0.21 * math.pow((plnet / 98.1), 0.75)

        return {
            "Kulhawy-Mayne (1990)": round(cu_1, 0),
            "Skempton-Bjerrum (1957)": round(cu_2, 0),
            "Stroud": round(cu_3, 0),
            "Carter ve Bentley (1990)": round(cu_4, 0),
            "Hara vd (1974)": round(cu_5, 0),
            "Lunne vd. (1997)": round(cu_6, 0),
            "Hara vd. (1971)": round(cu_7, 0),
            "Terzaghi ve Peck (1967)": round(cu_8, 0),
            "Nixon (1982)": round(cu_9, 0),
            "İyisan ve Ansal (1990)": round(cu_10, 0),
            "Decourt (1990)": round(cu_11, 0),
            "Decourt (1990) N60": round(cu_12, 0),
            "Amar vd. (1991)": round(cu_13, 0),
            "Stroud (1974)": round(cu_14, 0),
            "Sowers": round(cu_15, 0),
            "Amar and Jezequel (1972)": round(cu_16, 0),
            "Baguelin et. al. (1978)": round(cu_17, 0),
        }

    @staticmethod
    def effective_phi(pi):
        """Calculate effective friction angle"""
        phi_1 = 43 - (11 * (math.log10(pi)))
        phi_2 = (0.0058 * math.pow(pi, 1.73) - 0.32 * pi) + 36.2
        phi_3 = (0.084 * math.pow(pi, 1.4) - 0.75 * pi) + 31.9

        return {
            "Sorensen ve Okkels (2013)": round(phi_1, 1),
            "Gibson (1953)": round(phi_2, 1),
            "Gibson (1953) Residual": round(phi_3, 1),
        }

    @staticmethod
    def compression_index(liquid_limit, pi, wn, e0):
        """Calculate compression index (Cc)"""
        cc1 = 0.007 * (liquid_limit - 10)
        cc2 = pi / 74
        cc3 = 0.01 * (liquid_limit - 13)
        cc4 = 0.012 * wn
        cc5 = 1.15 * (e0 - 0.35)
        cc6 = 0.65 * (e0 - 0.35)

        return {
            "Skempton (1944)": round(cc1, 3),
            "Kulhawy-Mayne (1990)": round(cc2, 3),
            "USACE (1990) LL": round(cc3, 3),
            "USACE (1990) Wn": round(cc4, 3),
            "Azzouz (1976)": round(cc5, 3),
            "Nishida (1956)": round(cc6, 3),
        }

    @staticmethod
    def recompression_index(pi):
        """Calculate recompression index (Cr)"""
        cr1 = pi / 370
        return {"Kulhawy-Mayne (1990)": round(cr1, 3)}

    @staticmethod
    def swelling_index(pi):
        """Calculate swelling index (Cs)"""
        cs = 0.00194 * (pi - 4.6)
        return {"Nakase (1988)": round(cs, 3)}

    @staticmethod
    def consolidation_coefficient(liquid_limit):
        """Calculate coefficient of consolidation (Cv)"""
        cv = 103.97 * math.pow(liquid_limit, -2.8535)
        return {"Cv": round(cv, 3)}

    @staticmethod
    def volume_compressibility(pi, sptn):
        """Calculate coefficient of volume compressibility (Mv)"""
        mv = math.pow(pi, 2.07) / (sptn * (56000 + 435 * math.pow(pi, 2.07)))
        return {"Midland Geotechnical Society": round(mv, 6)}

    @staticmethod
    def overconsolidation_ratio(sptn, effective_stress):
        """Calculate overconsolidation ratio (OCR)"""
        ocr = 0.193 * math.pow((sptn * 1000 / effective_stress), 0.689)
        return {"Mayne ve Kemper (1988)": round(ocr, 6)}

    @staticmethod
    def swelling_potential(pi, liquid_limit):
        """Calculate swelling potential"""
        swelling1 = (3.6 * math.pow(10, -5) * math.pow((pi / liquid_limit), 2.44) * 
                    math.pow(liquid_limit, 3.44))
        swelling2 = 3.6 * math.pow(10, -5) * math.pow(pi, 2.44) * 60

        return {
            "Seed et al. (1962)": round(swelling1, 2),
            "Seed, Woodwars ve Ludgren": round(swelling2, 2),
        }

    @staticmethod
    def deformation_modulus(sptn, cu, cpt):
        """Calculate deformation modulus"""
        deformation_modulus_1 = 900 * sptn
        deformation_modulus_2 = 270 * cu
        deformation_modulus_3 = 3 * cpt
        deformation_modulus_4 = 6 * sptn * 100

        return {
            "Seed et al. (1962)": round(deformation_modulus_1, 0),
            "Stroud (1975)": round(deformation_modulus_2, 0),
            "Bowles (1997)": round(deformation_modulus_3, 0),
            "Yoshida ve Yoshinaka (1972)": round(deformation_modulus_4, 0),
        }

    @staticmethod
    def preconsolidation_pressure(sptn):
        """Calculate preconsolidation pressure"""
        sigma_c = 98.1 * 67 * math.pow(sptn, 0.83)
        return {"Seed": round(sigma_c, 3)}

    @staticmethod
    def friction_angle(sptn, sptn160, effective_stress, cpt):
        """Calculate friction angle for cohesionless soils"""
        phi_1 = 25 + (math.sqrt((100 * sptn) / (70 + effective_stress))) * 3.2
        phi_2 = 27.1 + (0.3 * sptn160) - (0.00054 * math.pow(sptn160, 2))
        phi_3 = math.sqrt(15 * sptn160) + 15
        phi_4 = math.sqrt(20 * sptn160) + 20
        phi_5 = 17.6 + 11 * math.log10(cpt)

        return {
            "OCDI Japan (2002)": round(phi_1, 1),
            "Wollf (1989)": round(phi_2, 1),
            "JRA (1996)": round(phi_3, 1),
            "Hatanaka-Uchida (1996)": round(phi_4, 1),
            "Kulhawy-Mayne (1990)": round(phi_5, 1),
        }

    @staticmethod
    def elastic_modulus(sptn, sptn60, poisson):
        """Calculate elasticity modulus"""
        elastic_modulus = 718 * (1 - math.pow(poisson, 2)) * sptn
        return {"Ferrent (1963)": round(elastic_modulus, 0)}

    @staticmethod
    def dynamic_friction_angle(sptn160, effective_stress):
        """Calculate dynamic friction angle"""
        phi_d = 0.83 * sptn160
        return {"Srbulov (2005)": round(phi_d, 1)}


def main():
    """Main function to run calculations based on user input"""
    choice = input("""
    Which parameter do you want to calculate?

    Cohesive soil
    
    1.Undrained shear strength
    2.Effective friction angle
    3.The compression index
    4.Recompression index
    5.Swelling index
    6.Coefficient of consolidation
    7.The coefficient of volume compressibility
    8.OCR
    9.Swelling potential
    10.Deformation Modulus
    11.Pre consolidation pressure

    Cohesionless soil

    12. Friction angle
    13. Elasticitiy modulus
    14. Dynamic friction angle

    Enter your choice (1-14): """)

    geo = GeotechnicalParameters()

    if choice == "1":
        sptn = float(input("SPT-N?: "))
        sptn60 = float(input("SPT-N 60?: "))
        effective_stress = float(input("Effective stress (kPa)?: "))
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        cbr = float(input("CBR?: "))
        plnet = float(input("PLnet?: "))
        cpt = float(input("qc (kPa)?: "))
        pi = liquid_limit - plastic_limit

        result = geo.undrained_shear_strength(sptn, pi, effective_stress, cbr, plnet, cpt, sptn60)
        print("\nCalculated undrained shear strength values (kPa):")
        for method, cu in result.items():
            print(f"- {method}: {cu:.2f}")

    elif choice == "2":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit

        result = geo.effective_phi(pi)
        print("\nCalculated effective phi values:")
        for method, effective_phi in result.items():
            print(f"- {method}: {effective_phi:.2f}")

    elif choice == "3":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit
        wn = float(input("Su muhtevası (%)?: "))
        e0 = float(input("e0?: "))

        result = geo.compression_index(liquid_limit, pi, wn, e0)
        print("\nCalculated Cc values:")
        for method, cc in result.items():
            print(f"- {method}: {cc:.3f}")

    elif choice == "4":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit

        result = geo.recompression_index(pi)
        print("\nCalculated Cr values:")
        for method, cr in result.items():
            print(f"- {method}: {cr:.3f}")

    elif choice == "5":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit

        result = geo.swelling_index(pi)
        print("\nCalculated Cs values:")
        for method, cs in result.items():
            print(f"- {method}: {cs:.3f}")

    elif choice == "6":
        liquid_limit = float(input("Liquid limit?: "))

        result = geo.consolidation_coefficient(liquid_limit)
        print("\nCalculated Cv values:")
        for method, cv in result.items():
            print(f"- {method}: {cv:.3f}")

    elif choice == "7":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit
        sptn = float(input("SPT-N?: "))

        result = geo.volume_compressibility(pi, sptn)
        print("\nCalculated Mv values:")
        for method, mv in result.items():
            print(f"- {method}: {mv:.6f}")

    elif choice == "8":
        sptn = float(input("SPT-N?: "))
        effective_stress = float(input("Effective stress (kPa)?: "))

        result = geo.overconsolidation_ratio(sptn, effective_stress)
        print("\nCalculated OCR values:")
        for method, ocr in result.items():
            print(f"- {method}: {ocr:.6f}")

        ocr_value = list(result.values())[0]
        if ocr_value == 1:
            print("\nThis soil is normally consolidated")
        elif ocr_value > 1:
            print("\nThis soil is overconsolidated")
        else:
            print("\nThis soil is underconsolidated")

    elif choice == "9":
        liquid_limit = float(input("Liquid limit?: "))
        plastic_limit = float(input("Plastic limit?: "))
        pi = liquid_limit - plastic_limit

        result = geo.swelling_potential(pi, liquid_limit)
        print("\nCalculated swelling values:")
        for method, swelling in result.items():
            print(f"- {method}: {swelling:.2f}")

    elif choice == "10":
        sptn = float(input("SPT-N?: "))
        cu = float(input("Undrained shear strength (kPa)?: "))
        cpt = float(input("qc (kPa)?: "))

        result = geo.deformation_modulus(sptn, cu, cpt)
        print("\nCalculated deformation modulus values (kPa):")
        for method, deformation_modulus in result.items():
            print(f"- {method}: {deformation_modulus:.0f}")

    elif choice == "11":
        sptn = float(input("SPT-N?: "))

        result = geo.preconsolidation_pressure(sptn)
        print("\nCalculated preconsolidation pressure (kPa):")
        for method, sigma_c in result.items():
            print(f"- {method}: {sigma_c:.3f}")

    elif choice == "12":
        sptn = float(input("SPT-N?: "))
        sptn160 = float(input("SPT-N1 60?: "))
        effective_stress = float(input("Effective stress (kPa)?: "))
        cpt = float(input("qc (kPa)?: "))

        result = geo.friction_angle(sptn, sptn160, effective_stress, cpt)
        print("\nCalculated friction angle values (degrees):")
        for method, phi in result.items():
            print(f"- {method}: {phi:.1f}")

    elif choice == "13":
        sptn = float(input("SPT-N?: "))
        sptn60 = float(input("SPT-N 60?: "))
        poisson = float(input("Poisson ratio?: "))

        result = geo.elastic_modulus(sptn, sptn60, poisson)
        print("\nCalculated elastic modulus values (kPa):")
        for method, elastic_modulus in result.items():
            print(f"- {method}: {elastic_modulus:.0f}")

    elif choice == "14":
        sptn160 = float(input("SPT-N1 60?: "))
        effective_stress = float(input("Effective stress (kPa)?: "))

        result = geo.dynamic_friction_angle(sptn160, effective_stress)
        print("\nCalculated dynamic friction angle values (degrees):")
        for method, phi_d in result.items():
            print(f"- {method}: {phi_d:.1f}")

    else:
        print("Invalid choice. Please enter a number between 1-14.")


if __name__ == "__main__":
    main()