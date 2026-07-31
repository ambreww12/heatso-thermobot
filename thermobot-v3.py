import discord
from discord import app_commands
from discord.ui import Button, View, Select
import random
import os

# ====================== THERMODYNAMICS QUESTIONS ======================
QUESTIONS = {
    "Novice": [
        # === OLD QUESTIONS ===
        ("A solid is heated at a pressure below its triple-point pressure. What phase change does it go through??",
         ["Deposition", "Fusion/Melting", "Vapourization", "Sublimation"], 3),
        ("Which law of thermodynamics defines temperature through thermal equilibrium?",
         ["First Law", "Second Law", "Zeroth Law", "Third Law"], 2),
        ("For an ideal gas, internal energy depends only on:",
         ["Pressure", "Volume", "Temperature", "Entropy"], 2),
        ("Work done in an isochoric process is:",
         ["Maximum", "PΔV", "Zero", "Equal to Q"], 2),
        ("An isobaric process on a PV diagram is represented by a:",
         ["Vertical line", "Horizontal line", "Hyperbola", "Steep curve"], 1),
        ("The First Law is a statement of:",
         ["Direction of processes", "Conservation of energy", "Increase of entropy", "Absolute zero"], 1),
        ("Heat capacity at constant volume is related to:",
         ["ΔH = nCpΔT", "ΔU = nCvΔT", "W = PΔV", "Q = 0"], 1),
        ("Which process has Q = 0?",
         ["Isothermal", "Isobaric", "Adiabatic", "Isochoric"], 2),
        ("Entropy is a measure of:",
         ["Temperature", "Energy dispersal / disorder", "Pressure", "Volume"], 1),
        ("Absolute zero corresponds to:",
         ["0 °C", "273 K", "0 K", "−273 °C only"], 2),
        ("Cp − Cv for an ideal gas equals:",
         ["0", "R", "γ", "1"], 1),
        # === NEW FROM SCIOLY WIKI ===
        ("According to the caloric theory, which of the following assumptions is the only one considered true?",
         ["Heat is a fluid that flows from hot to cold", "Heat is conserved", "Heat is weightless", "Sensible heat causes temperature increase"], 2),
        ("The kinetic theory of heat states that the average kinetic energy of gas particles depends only on:",
         ["Pressure", "Volume", "Temperature", "The number of collisions"], 2),
        ("Boyle’s Law states that at constant temperature, pressure and volume are:",
         ["Directly proportional", "Inversely proportional", "Equal", "Independent"], 1),
        ("Charles’ Law states that at constant pressure, volume is directly proportional to:",
         ["Celsius temperature", "Kelvin temperature", "Pressure", "Number of moles"], 1),
        ("An open thermodynamic system allows which of the following to cross its boundary?",
         ["Only heat", "Only matter", "Matter, heat, and work", "Nothing"], 2),
        ("A closed system allows heat and work to cross the boundary but does not allow:",
         ["Energy", "Matter", "Entropy", "Temperature change"], 1),
        # === NEW HISTORY QUESTIONS ===
        ("The SI unit of energy is named after:",
         ["James Clerk Maxwell", "James Prescott Joule", "Daniel Fahrenheit", "Walther Nernst"], 1),
        ("Who is often called the 'Father of Thermodynamics'?",
         ["James Joule", "Rudolf Clausius", "Sadi Carnot", "Lord Kelvin"], 2),
        ("Who introduced the concept of entropy in 1865?",
         ["Lord Kelvin", "Sadi Carnot", "Rudolf Clausius", "Walther Nernst"], 2),
        ("Which scientist formulated the Third Law of Thermodynamics?",
         ["James Joule", "Lord Kelvin", "Walther Nernst", "James Clerk Maxwell"], 2),
        ("Which famous physicist proposed the thought experiment known as 'Maxwell's Demon'?",
         ["Lord Kelvin", "James Clerk Maxwell", "Rudolf Clausius", "Sadi Carnot"], 1),
        ("Who invented the mercury thermometer?",
         ["Galileo Galilei", "Daniel Gabriel Fahrenheit", "Anders Celsius", "Lord Kelvin"], 1),
        ("The Celsius temperature scale was originally proposed by:",
         ["Carl Linnaeus", "Anders Celsius", "Daniel Fahrenheit", "Lord Kelvin"], 1),
        ("Absolute temperature is measured using the scale named after:",
         ["Joule", "Celsius", "Kelvin", "Clausius"], 2),
        ("Which scientist built the first open thermometer?",
         ["Daniel Fahrenheit", "Galileo Galilei", "Anders Celsius", "James Joule"], 1),
        # === NEW FROM BINDER ===
        ("The conversion from Celsius to Kelvin is:",
         ["T_K = T_C − 273.15", "T_K = T_C + 273.15", "T_K = (9/5)T_C + 32", "T_K = T_C × 273.15"], 1),
        ("In the sign convention ΔU = Q − W, positive W means:",
         ["Heat enters the system", "The system does work on the surroundings", "Surroundings do work on the system", "Heat leaves the system"], 1),
        ("Which of the following is a state function?",
         ["Heat", "Work", "Internal energy", "Both heat and work"], 2),
        ("For an isochoric process, work done by the system is:",
         ["PΔV", "nRT ln(V2/V1)", "Zero", "Equal to Q"], 2),
        ("The specific heat of water is approximately:",
         ["334 J/kg·K", "2256 J/kg·K", "4184 J/kg·K", "1000 J/kg·K"], 2),
        ("Latent heat of fusion of ice is approximately:",
         ["2256 kJ/kg", "334 kJ/kg", "4184 J/kg", "100 kJ/kg"], 1),
        ("An open system allows which of the following to cross its boundary?",
         ["Only energy", "Only matter", "Both matter and energy", "Neither matter nor energy"], 2),
        ("A closed system allows energy but not:",
         ["Work", "Heat", "Matter", "Temperature change"], 2),
        ("Temperature intervals in Celsius and Kelvin are:",
         ["Different by a factor of 9/5", "Identical in size", "Offset by 32", "Unrelated"], 1),
        ("Heat is best described as:",
         ["A substance stored in an object", "Energy transferred due to a temperature difference", "The same as temperature", "Internal energy"], 1),
        ("Extensive properties depend on:",
         ["The amount of matter", "The type of substance only", "Temperature only", "Pressure only"], 0),
        ("An intensive property is one that:",
         ["Depends on the size of the system", "Does not depend on the amount of matter", "Is always a state function", "Can only be temperature"], 1),
        ("In free expansion of an ideal gas into vacuum, work is:",
         ["Maximum", "Zero", "Equal to Q", "Negative"], 1),
        ("The ideal-gas law is written as:",
         ["PV = nRT", "P/V = nRT", "PV = nR/T", "P + V = nRT"], 0),
        ("On a P-V diagram the area under a process curve represents:",
         ["Heat", "Work", "Change in internal energy", "Entropy"], 1),
        # === NEW ADDITIONS ===
        ("Which of the following is NOT a state function?",
         ["Internal energy", "Enthalpy", "Heat", "Entropy"], 2),
        ("The process in which both pressure and volume change but temperature stays constant is called:",
         ["Isobaric", "Isochoric", "Isothermal", "Adiabatic"], 2),
        ("Latent heat of vaporization of water is approximately:",
         ["334 kJ/kg", "2260 kJ/kg", "4184 J/kg·K", "100 kJ/kg"], 1),
        ("In an isothermal process for an ideal gas, ΔU is:",
         ["Positive", "Negative", "Zero", "Equal to W"], 2),
        ("The slope of an isobar on a P-V diagram is:",
         ["Infinite", "Zero", "Negative", "Positive and finite"], 1),
        ("Which quantity is path-dependent?",
         ["ΔU", "ΔH", "ΔS", "W"], 3),
        ("Absolute zero is the temperature at which:",
         ["All molecular motion stops", "A perfect crystal has zero entropy (Third Law)", "Water freezes", "Gases liquefy"], 1),
        ("Cp is always greater than Cv for an ideal gas because:",
         ["The gas does expansion work at constant pressure", "Molecules are closer together", "R is negative", "Entropy decreases"], 0),
        ("A process with Q = W is:",
         ["Isobaric", "Isochoric", "Isothermal (ideal gas)", "Adiabatic"], 2),
        ("The SI unit of entropy is:",
         ["J/K", "J", "W/K", "K"], 0),
    ],
    "Intermediate": [
        # === OLD QUESTIONS ===
        ("A hot object is cooling in a room held at constant temperature T_a = 25 °C. At time t = 0 its temperature is T_0 = 85 °C. After 8 minutes its temperature has fallen to 65 °C. Estimate the object's temperature after 20 minutes.",
         ["26 °C", "32 °C", "47 °C", "63 °C"], 2),
        ("A liquid has a vapour pressure of P_1=20 kPa at T_1=300 K. Its molar enthalpy of vapourization is ΔH_vap=40 kJ/mol Find the approximate vapour pressure at T_2=320 K",
         ["12.5 kPa", "23.5 kPa", "35 kPa", "54.5 kPa"], 2),
        ("An ideal gas expands isothermally. Which quantity is zero?",
         ["Q", "W", "ΔU", "ΔS"], 2),
        ("For a reversible adiabatic process on an ideal gas:",
         ["PV = constant", "TV^{γ−1} = constant", "T/V = constant", "P/T = constant"], 1),
        ("A system absorbs 300 J of heat and does 120 J of work. ΔU is:",
         ["420 J", "180 J", "−180 J", "−420 J"], 1),
        ("Carnot efficiency between 450 K and 300 K is:",
         ["25%", "33.3%", "50%", "66.7%"], 1),
        ("In an isobaric process, Q equals:",
         ["ΔU", "ΔH", "W", "0"], 1),
        ("On a PV diagram, a vertical line represents:",
         ["Isobaric", "Isothermal", "Isochoric", "Adiabatic"], 2),
        ("When ice melts reversibly at 0 °C, ΔS of the system is:",
         ["Zero", "Positive", "Negative", "Undefined"], 1),
        ("For an ideal gas in reversible adiabatic expansion:",
         ["Temperature increases", "Internal energy decreases", "Entropy of system increases", "Heat is absorbed"], 1),
        ("The Zeroth Law is most closely related to:",
         ["Energy conservation", "Definition of temperature", "Direction of heat flow", "Maximum efficiency"], 1),
        ("In an isolated system, a spontaneous irreversible process always increases:",
         ["Internal energy", "Enthalpy", "Entropy", "Gibbs free energy"], 2),
        # === NEW FROM SCIOLY WIKI ===
        ("Gay-Lussac’s Law states that at constant volume, pressure is directly proportional to:",
         ["Celsius temperature", "Kelvin temperature", "Volume", "Number of moles"], 1),
        ("Joule’s Second Law states that the internal energy of an ideal gas depends only on:",
         ["Pressure and volume", "Temperature", "The path taken", "Work done"], 1),
        ("An isolated thermodynamic system allows which of the following to cross its boundary?",
         ["Heat only", "Matter only", "Work only", "Nothing"], 3),
        ("A diathermic boundary allows:",
         ["Matter to pass", "Heat to pass", "Work to pass", "Nothing to pass"], 1),
        ("The caloric theory of heat was primarily developed by:",
         ["James Clerk Maxwell", "Antoine Lavoisier", "Sadi Carnot", "James Joule"], 1),
        ("According to the kinetic theory, collisions between gas molecules are assumed to be:",
         ["Inelastic", "Perfectly elastic", "Partially elastic", "Negligible"], 1),
        # === NEW HISTORY QUESTIONS ===
        ("Which scientist is credited with discovering the mechanical equivalent of heat, helping establish the First Law of Thermodynamics?",
         ["James Prescott Joule", "Sadi Carnot", "Rudolf Clausius", "Lord Kelvin"], 0),
        ("Which scientist first clearly formulated the Second Law of Thermodynamics?",
         ["James Joule", "Rudolf Clausius", "Lord Kelvin", "James Clerk Maxwell"], 1),
        ("Maxwell's Demon was designed to challenge which law of thermodynamics?",
         ["Zeroth Law", "First Law", "Second Law", "Third Law"], 2),
        ("The Fahrenheit temperature scale is named after:",
         ["A Swedish astronomer", "A Dutch-German physicist", "A Scottish physicist", "A German chemist"], 1),
        ("Who coined the word 'thermodynamics'?",
         ["James Joule", "Lord Kelvin", "Rudolf Clausius", "Walther Nernst"], 1),
        ("Who is credited with determining the value of absolute zero?",
         ["Lord Kelvin", "James Joule", "Sadi Carnot", "James Clerk Maxwell"], 0),
        ("Who developed the Nernst equation, widely used in electrochemistry?",
         ["Walther Nernst", "Rudolf Clausius", "James Clerk Maxwell", "Lord Kelvin"], 0),
        ("Which scientist founded the Uppsala Astronomical Observatory?",
         ["James Clerk Maxwell", "Anders Celsius", "Lord Kelvin", "Galileo Galilei"], 1),
        # === NEW FROM BINDER ===
        ("For an ideal gas, ΔU equals:",
         ["nCpΔT", "nCvΔT", "PΔV", "nR ln(V2/V1)"], 1),
        ("For an ideal gas, ΔH equals:",
         ["nCvΔT", "nCpΔT", "W", "Q − W"], 1),
        ("In an isobaric process for an ideal gas, Q equals:",
         ["nCvΔT", "nCpΔT", "Zero", "W only"], 1),
        ("The relationship Cp − Cv for an ideal gas is:",
         ["Zero", "R", "γ", "1"], 1),
        ("γ is defined as:",
         ["Cv/Cp", "Cp/Cv", "Cp − Cv", "R/Cv"], 1),
        ("During a phase change at constant pressure, temperature:",
         ["Increases steadily", "Decreases steadily", "Remains approximately constant", "Fluctuates randomly"], 2),
        ("The equation Q = mL is used for:",
         ["Temperature change with no phase change", "Phase changes", "Adiabatic processes only", "Isothermal compression"], 1),
        ("Conduction heat transfer through a slab is proportional to:",
         ["1/thickness", "Thickness squared", "The square of the temperature difference", "Surface roughness only"], 0),
        ("Newton’s law of cooling states that the rate of temperature change is proportional to:",
         ["The absolute temperature", "The temperature difference with surroundings", "The square of the temperature", "Time only"], 1),
        ("In the expression T(t) = T∞ + (T0 − T∞)e^(−kt), k is the:",
         ["Thermal conductivity", "Cooling constant", "Specific heat", "Latent heat"], 1),
        ("A diathermal boundary allows:",
         ["Matter to pass", "Heat to pass", "Work only", "Nothing to pass"], 1),
        ("An adiabatic boundary prevents:",
         ["Matter transfer", "Heat transfer", "Work transfer", "Volume change"], 1),
        ("For a cyclic process, ΔU is:",
         ["Positive", "Negative", "Zero", "Equal to Q"], 2),
        ("The First Law applied to a complete cycle gives:",
         ["ΔU = Q", "Q_net = W_net", "W = 0", "Q = 0"], 1),
        ("Coffee-cup calorimetry is approximately a:",
         ["Constant-volume process", "Constant-pressure process", "Adiabatic process", "Isothermal process"], 1),
        # === NEW ADDITIONS ===
        ("An ideal gas is compressed isothermally. The heat released by the gas is:",
         ["Zero", "Equal to the work done on the gas", "Equal to ΔU", "Greater than the work done on the gas"], 1),
        ("For a reversible isothermal expansion of an ideal gas, ΔS_system is:",
         ["Zero", "nR ln(V2/V1)", "Negative", "nCv ln(T2/T1)"], 1),
        ("Newton’s law of cooling is most accurate when the temperature difference is:",
         ["Very large", "Moderate", "Near absolute zero", "Independent of the difference"], 1),
        ("In a P-T phase diagram, the slope of the solid-liquid line for water is:",
         ["Positive", "Negative", "Zero", "Infinite"], 1),
        ("The change in enthalpy for an ideal gas depends only on:",
         ["Pressure", "Volume", "Temperature", "The path"], 2),
        ("Which process has the largest magnitude of work done by the system for the same volume change (ideal gas)?",
         ["Isothermal", "Adiabatic", "Isochoric", "Isobaric"], 3),
        ("A diathermic, rigid, impermeable wall allows:",
         ["Heat and matter", "Only heat", "Only work", "Nothing"], 1),
        ("The efficiency of any real heat engine is always:",
         ["Equal to Carnot efficiency", "Greater than Carnot efficiency", "Less than Carnot efficiency", "Independent of temperatures"], 2),
        ("When 1 kg of ice at 0 °C melts completely at constant pressure, the entropy change of the system is approximately:",
         ["0", "1.22 kJ/K", "334 kJ/K", "2260 kJ/K"], 1),
        ("For an ideal gas, the difference Cp − Cv equals:",
         ["R only for monatomic gases", "R for any ideal gas", "γR", "Zero"], 1),
    ],
    "Hard": [
        # === OLD QUESTIONS ===
        ("An ideal gas expands reversibly and isothermally from V to 2V. The work done by the gas is:",
         ["nRT", "nRT ln(2)", "0", "½ nRT"], 1),
        ("A Carnot refrigerator operates between −10 °C and 25 °C. Its COP is closest to:",
         ["4.5", "7.5", "10.2", "12.8"], 1),
        ("In free expansion of an ideal gas into vacuum:",
         ["W > 0 and Q > 0", "W = 0, Q = 0, ΔU = 0", "Temperature decreases", "ΔU > 0"], 1),
        ("For a reversible adiabatic process:",
         ["ΔS_system > 0", "ΔS_system = 0", "ΔU = 0", "Q ≠ 0"], 1),
        ("Heat absorbed at constant pressure is equal to the change in:",
         ["Internal energy", "Enthalpy", "Entropy", "Helmholtz free energy"], 1),
        ("Compared to an isothermal curve, an adiabatic curve on a PV diagram is:",
         ["Less steep", "Steeper", "Identical", "Horizontal"], 1),
        ("For an ideal gas, (∂U/∂V)_T equals:",
         ["R", "Cv", "0", "Cp − R"], 2),
        ("A system has ΔU = −250 J and performs 100 J of work. Heat transferred to the system is:",
         ["−350 J", "−150 J", "+150 J", "+350 J"], 1),
        ("Which of the following is a state function?",
         ["Heat", "Work", "Internal energy", "Both heat and work"], 2),
        ("In a Carnot cycle the two isothermal processes are accompanied by:",
         ["No entropy change of the universe", "Positive entropy change of the universe", "Negative entropy change of the system", "Zero heat transfer"], 0),
        # === NEW FROM SCIOLY WIKI ===
        ("In the Carnot cycle, the process in which the gas is thermally isolated and expands while its temperature decreases is:",
         ["Isothermal expansion", "Reversible adiabatic expansion", "Isothermal compression", "Adiabatic compression"], 1),
        ("Maxwell’s Demon appears to violate the Second Law by:",
         ["Creating energy from nothing", "Separating fast and slow molecules to create a temperature difference without work", "Destroying entropy", "Reaching absolute zero"], 1),
        ("The resolution to Maxwell’s Demon paradox involves the fact that the demon:",
         ["Must expend energy / increase entropy to observe and sort molecules", "Cannot exist in reality", "Violates the First Law", "Only works at absolute zero"], 0),
        ("Joule’s First Law relates heat dissipated in a resistor to:",
         ["Voltage and time only", "I²Rt", "Power only", "Resistance and voltage"], 1),
        ("An isentropic process is one that occurs at constant:",
         ["Temperature", "Pressure", "Entropy", "Volume"], 2),
        ("For a reversible process, an adiabatic process is also:",
         ["Isobaric", "Isothermal", "Isentropic", "Isochoric"], 2),
        # === NEW HISTORY QUESTIONS ===
        ("The Carnot cycle was first described in which publication?",
         ["On the Mechanical Theory of Heat", "Reflections on the Motive Power of Fire", "Experimental Researches on Electricity", "The Kinetic Theory of Gases"], 1),
        ("Walther Nernst was awarded the 1920 Nobel Prize in:",
         ["Physics", "Chemistry", "Medicine", "Mathematics"], 1),
        ("Which scientist's work on heat engines inspired much of modern thermodynamics despite being based on caloric theory?",
         ["James Joule", "Sadi Carnot", "Rudolf Clausius", "Lord Kelvin"], 1),
        ("Carnot's work on heat engines was published in:",
         ["1799", "1824", "1850", "1865"], 1),
        ("Clausius introduced the term 'entropy' in:",
         ["1824", "1850", "1865", "1905"], 2),
        ("Which scientist's work demonstrated that heat and mechanical work are equivalent?",
         ["Carnot", "Joule", "Kelvin", "Nernst"], 1),
        # === NEW FROM BINDER ===
        ("The ideal-gas entropy change at constant volume is given by:",
         ["nCv ln(T2/T1)", "nCp ln(T2/T1)", "nR ln(V2/V1)", "Zero"], 0),
        ("The ideal-gas entropy change involving pressure is:",
         ["nCv ln(T2/T1) + nR ln(V2/V1)", "nCp ln(T2/T1) − nR ln(P2/P1)", "nR ln(T2/T1)", "Cv ln(P2/P1)"], 1),
        ("For a reversible phase change at temperature T_trans, ΔS equals:",
         ["mL / T_trans", "m c ΔT", "Zero", "nR ln(V2/V1)"], 0),
        ("Carnot efficiency is given by:",
         ["1 − Qc/Qh", "1 − Tc/Th (temperatures in kelvin)", "W/Qc", "Th/Tc"], 1),
        ("COP of a refrigerator is defined as:",
         ["W/Qc", "Qc/W", "Qh/W", "W/Qh"], 1),
        ("COP of a heat pump is:",
         ["Qc/W", "Qh/W", "W/Qh", "The same as refrigerator COP"], 1),
        ("On a P-V diagram a clockwise cycle represents:",
         ["Net work input", "Net work output", "Zero net work", "An isentropic process"], 1),
        ("The Otto cycle models:",
         ["A steam power plant", "A spark-ignition engine with constant-volume heat addition", "A gas turbine", "A refrigerator"], 1),
        ("The Diesel cycle features heat addition at:",
         ["Constant volume", "Constant pressure", "Constant temperature", "Constant entropy"], 1),
        ("Thermal resistance for conduction is:",
         ["kA/L", "L/(kA)", "hA", "1/(hA)"], 1),
        ("In series thermal resistances, total resistance is:",
         ["The reciprocal of the sum", "The sum of the individual resistances", "The product of the resistances", "The average resistance"], 1),
        ("Wien’s displacement law relates:",
         ["Pressure and volume", "Wavelength of maximum emission and temperature", "Heat capacity and temperature", "Entropy and volume"], 1),
        ("The Stefan-Boltzmann law gives net radiation heat transfer proportional to:",
         ["T", "T²", "T³", "T⁴"], 3),
        ("For an isolated system, a spontaneous process always results in:",
         ["ΔS_universe < 0", "ΔS_universe = 0", "ΔS_universe > 0", "ΔU > 0"], 2),
        ("The Third Law states that the entropy of a perfect crystal approaches zero as:",
         ["Pressure approaches zero", "Temperature approaches absolute zero", "Volume approaches zero", "The system becomes isolated"], 1),
        # === NEW ADDITIONS ===
        ("An ideal gas expands from V to 3V in a reversible adiabatic process. If γ = 1.4, the final temperature is:",
         ["T / 3^{0.4}", "T × 3^{0.4}", "T / 3", "T × 3"], 0),
        ("A Carnot engine has efficiency 1/3. If the sink temperature is 27 °C, the source temperature is:",
         ["400 K", "450 K", "500 K", "600 K"], 1),
        ("In free expansion of an ideal gas, which of the following is true?",
         ["ΔS_system = 0", "ΔS_universe = 0", "ΔS_system > 0 and ΔS_universe > 0", "Q = W ≠ 0"], 2),
        ("The Maxwell relation from dH = T dS + V dP is:",
         ["(∂T/∂P)_S = (∂V/∂S)_P", "(∂T/∂P)_S = −(∂V/∂S)_P", "(∂S/∂P)_T = −(∂V/∂T)_P", "(∂S/∂V)_T = (∂P/∂T)_V"], 2),
        ("For a polytropic process with n = 0, the process is:",
         ["Isothermal", "Isobaric", "Isochoric", "Adiabatic"], 1),
        ("The work done in a reversible adiabatic expansion of an ideal gas can also be written as:",
         ["nR ln(V2/V1)", "nCp(T1 − T2)", "nCv(T1 − T2)", "P1V1 − P2V2"], 2),
        ("At the critical point of a pure substance, the number of degrees of freedom F is:",
         ["0", "1", "2", "3"], 0),
        ("A refrigerator has a COP of 4. If it removes 800 J from the cold reservoir, the work input required is:",
         ["160 J", "200 J", "3200 J", "1000 J"], 1),
        ("For an ideal gas, (∂H/∂P)_T equals:",
         ["0", "V", "−V", "T(∂V/∂T)_P − V"], 0),
        ("In the Otto cycle, the heat rejection occurs at:",
         ["Constant pressure", "Constant volume", "Constant temperature", "Constant entropy"], 1),
    ],
    "Very Hard": [
        # === OLD QUESTIONS ===
        ("A small metal object obeys Newton’s Law of Cooling. In a room held at a constant 25 °C, the object cools from 95 °C to 65 °C in exactly six minutes. The object is then immediately transferred into a second room whose temperature is held constant at 5 °C. Assuming k doesn't change, determine the temperature of the object 8 mins after it was transferred.",
         ["33.5 °C", "38.2 °C", "41.0 °C", "44.9 °C"], 0),
        ("An ideal gas is taken through a cycle consisting of isothermal expansion, isochoric cooling, and adiabatic compression back to the original state. Net work is:",
         ["Positive (engine)", "Negative (refrigerator)", "Zero", "Cannot be determined without numbers"], 0),
        ("For a reversible process, ∮ dQ/T equals:",
         ["ΔS_system", "0", "ΔS_universe", "Q_net / T"], 1),
        ("A heat engine absorbs 800 J from a 600 K reservoir and rejects heat to a 300 K reservoir. Maximum possible work output is:",
         ["200 J", "400 J", "500 J", "600 J"], 1),
        ("In a throttling process (Joule-Thomson expansion) for an ideal gas:",
         ["Temperature always drops", "Enthalpy is constant", "Entropy is constant", "Internal energy increases"], 1),
        ("The Maxwell relation derived from dU = T dS − P dV is:",
         ["(∂T/∂V)_S = (∂P/∂S)_V", "(∂T/∂V)_S = −(∂P/∂S)_V", "(∂T/∂P)_S = (∂V/∂S)_P", "(∂S/∂V)_T = (∂P/∂T)_V"], 1),
        ("An ideal gas undergoes a process in which PV² = constant. The molar heat capacity for this process is:",
         ["Cv + R/2", "Cv + 2R", "Cp − R", "Cv + R"], 0),
        ("For a van der Waals gas, the internal pressure (∂U/∂V)_T is equal to:",
         ["0", "a/V_m²", "b", "R/V_m"], 1),
        ("The efficiency of a Carnot engine is 40%. If the temperature of the sink is 27 °C, the temperature of the source is:",
         ["227 °C", "327 °C", "500 °C", "77 °C"], 0),
        ("During a reversible adiabatic process for an ideal gas, which remains constant?",
         ["TV^{γ−1}", "T/V", "PV", "P/T"], 0),
        ("The change in entropy of the universe when 1 mole of ideal gas expands freely into vacuum to double its volume is:",
         ["0", "R ln 2", "−R ln 2", "Cv ln 2"], 1),
        # === NEW FROM SCIOLY WIKI ===
        ("In the Carnot cycle, the net change in entropy of the universe is:",
         ["Positive", "Negative", "Zero", "Dependent on the temperatures"], 2),
        ("The two adiabatic processes in the Carnot cycle are characterized by:",
         ["ΔS = 0 (isentropic)", "Q ≠ 0", "ΔU = 0", "Constant pressure"], 0),
        ("According to the Third Law, the entropy of a perfect crystal approaches zero as temperature approaches:",
         ["0 °C", "The melting point", "Absolute zero", "Room temperature"], 2),
        ("van der Waals’ equation corrects the ideal gas law for:",
         ["Only molecular volume", "Only attractive forces", "Both attractive forces and molecular volume", "Temperature dependence of R"], 2),
        ("Carnot’s Principle states that no heat engine operating between two temperatures can be more efficient than a:",
         ["Real irreversible engine", "Reversible engine operating between the same temperatures", "Steam engine", "Engine using ideal gas"], 1),
        ("In the caloric theory, “frigoric” referred to:",
         ["A type of work", "The absence or lack of caloric (cold)", "Latent heat", "Sensible heat"], 1),
        # === NEW HISTORY QUESTIONS ===
        ("The Third Law of Thermodynamics is also commonly called:",
         ["Joule's Law", "Nernst Heat Theorem", "Kelvin Principle", "Carnot Principle"], 1),
        ("Which early theory of heat was replaced by Joule's experiments?",
         ["Atomic theory", "Wave theory", "Caloric theory", "Kinetic theory"], 2),
        ("Before Joule's experiments, Carnot's original analysis of heat engines was based primarily on:",
         ["The kinetic theory of gases", "The caloric theory of heat", "Statistical mechanics", "Electromagnetism"], 1),
        ("Which pair of scientists are most directly associated with the Second and Third Laws of Thermodynamics, respectively?",
         ["Joule and Kelvin", "Clausius and Nernst", "Carnot and Maxwell", "Fahrenheit and Celsius"], 1),
        # === NEW FROM BINDER ===
        ("The Clapeyron equation is:",
         ["dP/dT = ΔH_trans / (T ΔV)", "dP/dT = ΔV / (T ΔH)", "ln(P2/P1) = −ΔH/R (1/T2 − 1/T1)", "Both A and C are related forms"], 0),
        ("The integrated Clausius-Clapeyron equation is most often used for:",
         ["Solid-solid transitions", "Vapourization or sublimation", "Isothermal compression", "Adiabatic expansion"], 1),
        ("Gibbs phase rule for a non-reacting system is:",
         ["F = C + P − 2", "F = C − P + 2", "F = C − P − 2", "F = P − C + 2"], 1),
        ("At the triple point of a single-component system, the number of degrees of freedom F is:",
         ["2", "1", "0", "3"], 2),
        ("For a reversible adiabatic process on an ideal gas, which is true?",
         ["PV = constant", "TV^{γ−1} = constant", "T/V = constant", "P/T^γ = constant"], 1),
        ("The work done in a reversible adiabatic process for an ideal gas can be written as:",
         ["nRT ln(V2/V1)", "nCv(T1 − T2)", "PΔV", "Zero"], 1),
        ("In Newton’s law of cooling, after one time constant τ the remaining temperature difference is approximately:",
         ["50%", "36.8%", "25%", "10%"], 1),
        ("The time constant τ for a lumped thermal system is:",
         ["hA / mc", "mc / hA", "kA / L", "L / kA"], 1),
        ("A plot of ln|T − T∞| versus time should be approximately linear with slope:",
         ["+k", "−k", "k²", "1/k"], 1),
        ("Bomb calorimetry is carried out at constant:",
         ["Pressure", "Volume", "Temperature", "Entropy"], 1),
        ("Coffee-cup calorimetry approximates constant:",
         ["Volume", "Pressure", "Temperature", "Entropy"], 1),
        ("When calculating final temperature of several objects mixed with no phase change:",
         ["Tf = Σ (mi ci Ti) / Σ (mi ci)", "Tf = Σ mi Ti / Σ mi", "Tf = average of all Ti", "Tf is always the highest Ti"], 0),
        ("Net radiation heat transfer between a surface and large surroundings is:",
         ["εσA(Ts − Tsur)", "εσA(Ts⁴ − Tsur⁴)", "σA(Ts⁴ − Tsur⁴) only", "hA(Ts − Tsur)"], 1),
        ("An isentropic process is equivalent to a reversible:",
         ["Isothermal process", "Isobaric process", "Adiabatic process", "Isochoric process"], 2),
        ("For a heat engine exchanging heat only with two reservoirs, ΔS of the reservoirs is:",
         ["−QH/TH + QC/TC ≥ 0", "QH/TH − QC/TC ≥ 0", "Always zero", "Always negative"], 0),
        # === NEW ADDITIONS ===
        ("An ideal gas undergoes a process in which T ∝ V². The molar heat capacity for this process is:",
         ["Cv + R/2", "Cv + 2R", "Cp − R", "Cv + R"], 1),
        ("One mole of van der Waals gas expands isothermally from V1 to V2. The change in internal energy is:",
         ["0", "a(1/V1 − 1/V2)", "RT ln((V2−b)/(V1−b))", "−a(1/V1 − 1/V2)"], 1),
        ("A Carnot engine operating between 600 K and 300 K produces 400 J of work. The heat rejected to the cold reservoir is:",
         ["200 J", "400 J", "600 J", "800 J"], 1),
        ("The Joule-Thomson coefficient for an ideal gas is zero because:",
         ["Enthalpy depends only on temperature", "Internal energy depends only on temperature", "Both of the above", "Neither"], 2),
        ("In a reversible cycle, ∮ (dQ/T) equals:",
         ["ΔS_system", "0", "ΔS_universe", "Q_net / T_avg"], 1),
        ("For a photon gas, the internal energy U is related to volume and temperature by U ∝:",
         ["VT", "VT²", "VT³", "VT⁴"], 3),
        ("The critical compressibility factor Zc for a van der Waals gas is exactly:",
         ["3/8", "1/4", "1/2", "1/8"], 0),
        ("When two identical bodies at temperatures T1 and T2 are brought into thermal contact in an isolated system, the maximum work that can be extracted is:",
         ["Cv(T1 − T2)", "Cv(√T1 − √T2)²", "0", "Cv(T1 + T2)/2"], 1),
        ("The entropy change of the universe for the free expansion of an ideal gas into vacuum is equal to:",
         ["0", "nR ln(V2/V1)", "nCv ln(T2/T1)", "−nR ln(V2/V1)"], 1),
        ("In the derivation of the Clausius inequality, the key statement is that for any real cycle:",
         ["∮ dQ/T ≤ 0", "∮ dQ/T ≥ 0", "∮ dQ/T = 0", "∮ dQ = 0"], 0),
    ],
    "Impossible": [
        # === OLD QUESTIONS ===
        ("An ideal gas follows the process TV^{x} = constant. For the molar heat capacity to be 4R, the value of x is: (take γ = 1.4)",
         ["0.5", "1.0", "1.5", "2.0"], 0),
        ("A Carnot engine operates between T and T/2. Another identical engine operates between T/2 and T/4. The ratio of their efficiencies is:",
         ["1 : 1", "1 : 2", "2 : 1", "3 : 1"], 0),
        ("One mole of a van der Waals gas expands isothermally from V1 to V2. The work done is:",
         ["RT ln((V2−b)/(V1−b))", "RT ln(V2/V1)", "RT ln((V2−b)/(V1−b)) + a(1/V1 − 1/V2)", "None of these"], 2),
        ("For a thermodynamic system, the Helmholtz free energy F = U − TS. The natural variables of F are:",
         ["S, V", "T, V", "T, P", "S, P"], 1),
        ("In a reversible polytropic process PV^n = constant, the expression for work done by the gas is:",
         ["(P1V1 − P2V2)/(n−1)", "nR(T1 − T2)/(n−1)", "Both A and B are equivalent", "R(T1 − T2) ln(V2/V1)"], 2),
        ("The Joule-Thomson coefficient μ = (∂T/∂P)_H. For an ideal gas μ is:",
         ["Positive", "Negative", "Zero", "Infinite"], 2),
        ("A system goes from state A to B via two different paths. The difference in heat absorbed along the two paths equals the difference in:",
         ["Internal energy", "Work done", "Enthalpy", "Entropy"], 1),
        ("For a photon gas (blackbody radiation), the pressure P is related to energy density u by:",
         ["P = u/3", "P = u", "P = 3u", "P = u/2"], 0),
        ("The critical compressibility factor Zc = PcVc / RTc for a van der Waals gas is:",
         ["0.375", "0.25", "0.5", "0.125"], 0),
        ("In the T-S diagram of a Carnot cycle, the heat absorbed during the isothermal expansion is represented by:",
         ["Area under the upper horizontal line", "Height of the rectangle", "Width of the rectangle", "Diagonal of the rectangle"], 0),
        # === NEW FROM SCIOLY WIKI ===
        ("In the detailed Carnot cycle analysis, the relationship Q₂ / Q₁ = T_C / T_H is derived by combining the isothermal work expressions with the adiabatic condition that:",
         ["V₂ / V₁ = V₃ / V₄", "V₂ / V₄ = V₃ / V₁", "T_H V₂^{γ−1} = T_C V₃^{γ−1}", "Both the volume ratios and the adiabatic relation"], 3),
        ("Maxwell’s Demon decreases the entropy of the gas by sorting molecules, but the total entropy of the universe still increases because:",
         ["The demon must acquire information (using energy) and the mechanism itself gains entropy", "The First Law is violated", "Absolute zero is reached", "The process is irreversible by definition"], 0),
        ("According to the Scioly wiki treatment of the Third Law, two objects at different temperatures can never reach exactly the same temperature because:",
         ["Heat transfer stops completely", "The approach is asymptotic (exponential decay/growth)", "The Second Law forbids it", "Measurement tools are imperfect"], 1),
        ("Hess’ Law (mentioned in the gas-laws section) is essentially a consequence of:",
         ["The First Law (enthalpy is a state function)", "The Second Law", "The Third Law", "Boyle’s Law"], 0),
        ("In the Carnot cycle, the entropy change of the hot reservoir is +Q₁/T_H while the cold reservoir is −Q₂/T_C. Their sum is zero because:",
         ["Q₁/T_H = Q₂/T_C", "The processes are adiabatic", "No heat is transferred", "The cycle is irreversible"], 0),
        ("Statistical thermodynamics (as contrasted with classical) explains macroscopic laws by considering:",
         ["Only measurable laboratory properties", "Microscopic molecular motions and statistical distributions", "Chemical reaction pathways only", "Non-equilibrium systems exclusively"], 1),
        # === NEW HISTORY QUESTIONS ===
        ("Which of the following scientists died before the concept of entropy was introduced?",
         ["Rudolf Clausius", "Sadi Carnot", "Lord Kelvin", "Walther Nernst"], 1),
        ("Which scientist proposed a temperature scale that was later modified into the modern Celsius scale after his death?",
         ["Daniel Fahrenheit", "Anders Celsius", "Lord Kelvin", "Galileo Galilei"], 1),
        ("Which scientist's original heat engine theory remained largely correct even though its underlying assumption—that heat was a conserved fluid—was incorrect?",
         ["James Joule", "Sadi Carnot", "James Clerk Maxwell", "Walther Nernst"], 1),
        ("Arrange these historical developments from earliest to latest:",
         ["Kelvin scale → Carnot cycle → Entropy",
          "Carnot cycle → Joule's mechanical equivalent of heat → Entropy",
          "Entropy → Carnot cycle → Kelvin scale",
          "Mechanical equivalent of heat → Carnot cycle → Entropy"], 1),
        # === NEW FROM BINDER ===
        ("""A solid metal sphere of radius 2.5 cm, density 7800 kg m^-3, and specific heat capacity c = 450 J kg^-1 K^-1 is suspended in a large evacuated
        chamber whose walls are held at a constant temperature T_a = 300 K. The sphere’s surface has emissivity ε = 0.80. In addition to thermal radiation,
        a weak convective cooling term is present that follows Newton’s Law of Cooling with heat-transfer coefficient h = 4.5 W m^-2 K^-1. The sphere is initially at 900 K.
        Find the approximate time needed for the sphere's temperature to fall under 450 K.""",
         ["1250 s", "1775 s", "1945 s", "2305 s"], 1),
        ("For an ideal gas undergoing a polytropic process PV^n = constant, the molar heat capacity is:",
         ["Cv + R/(1−n)", "Cv + R/(n−1)", "Cp − R", "Cv only"], 0),
        ("The efficiency of an ideal Otto cycle with compression ratio r is:",
         ["1 − 1/r", "1 − 1/r^{γ−1}", "1 − r^{γ−1}", "1 − (γ−1)/r"], 1),
        ("The efficiency of an ideal Brayton cycle with pressure ratio rp is:",
         ["1 − 1/rp", "1 − 1/rp^{(γ−1)/γ}", "1 − rp^{(γ−1)/γ}", "1 − (γ−1)/rp"], 1),
        ("In the expression for reversible adiabatic work of an ideal gas, W = (P1V1 − P2V2)/(γ−1) is equivalent to:",
         ["nR(T1 − T2)", "nCv(T1 − T2)", "nCp(T1 − T2)", "PΔV"], 1),
        ("When two objects at different temperatures are placed in contact inside an otherwise isolated system, the final common temperature is reached when:",
         ["Their internal energies become equal", "The entropy of the universe is maximized", "Their heat capacities become equal", "No more energy is available"], 1),
        ("The change in entropy of the universe for any real (irreversible) process is:",
         ["Zero", "Negative", "Positive", "Equal to ΔS_system"], 2),
        ("A system’s entropy can decrease only if:",
         ["The process is adiabatic", "The surroundings increase in entropy by at least as much", "The process is isothermal", "Absolute zero is approached"], 1),
        ("For radiation, a surface with low emissivity is most effective at reducing heat transfer when it faces:",
         ["A solid conductor", "An air gap or vacuum", "A high-conductivity metal", "A phase-change material"], 1),
        ("In the derivation of Carnot efficiency, the key step that produces η = 1 − TC/TH is the recognition that for the reversible cycle:",
         ["QH/TH = QC/TC", "QH = QC", "W = QH", "ΔS_universe > 0"], 0),
        ("The Gibbs phase rule F = C − P + 2 implies that at a triple point of a pure substance the system is:",
         ["Bivariant", "Univariant", "Invariant", "Trivariant"], 2),
        ("When using the Clausius-Clapeyron equation, the approximation that ΔH is constant is most reasonable over:",
         ["Very large temperature ranges", "Narrow temperature ranges", "Only at the critical point", "Only for solids"], 1),
        ("In Newton cooling analysis, a sudden increase in air speed over an object primarily increases:",
         ["Thermal conductivity k", "The convection coefficient h", "The specific heat c", "The latent heat"], 1),
        ("If a calorimeter’s heat capacity is ignored when calculating the specific heat of a hot object, the calculated value is usually:",
         ["Too high", "Too low", "Unaffected", "Randomly wrong"], 1),
        ("The statement “an adiabatic process is isentropic” is true only when the process is also:",
         ["Isothermal", "Reversible", "Isobaric", "Irreversible"], 1),
        ("For a cyclic device operating between two reservoirs, the equality ΔS_reservoirs = 0 holds only for:",
         ["Any real engine", "A reversible engine", "A refrigerator", "A heat pump with COP > 1"], 1),
        # === NEW ADDITIONS ===
        ("An ideal gas follows TV^x = constant. If the molar heat capacity for the process is 3R and γ = 5/3, the value of x is:",
         ["0.5", "1", "1.5", "2"], 0),
        ("A heat engine operates with two Carnot engines in series. The first operates between T and T/2, the second between T/2 and T/4. The overall efficiency is:",
         ["1/2", "3/4", "7/8", "15/16"], 1),
        ("For a van der Waals gas, the inversion temperature (where μ_JT = 0) is given by:",
         ["2a/Rb", "a/Rb", "a/(2Rb)", "2a/(Rb)"], 0),
        ("The natural variables of the Gibbs free energy G are:",
         ["S, V", "T, V", "T, P", "S, P"], 2),
        ("In a reversible polytropic process with n = γ, the heat transfer Q is:",
         ["nCv(T2 − T1)", "nCp(T2 − T1)", "0", "nR(T2 − T1)/(γ − 1)"], 2),
        ("The efficiency of a Carnot engine working between temperatures T and T − ΔT (ΔT ≪ T) is approximately:",
         ["ΔT/T", "2ΔT/T", "ΔT/(2T)", "(ΔT/T)²"], 0),
        ("For blackbody radiation, the entropy S is related to internal energy U and temperature by:",
         ["S = U/T", "S = (4/3)U/T", "S = (3/4)U/T", "S = U/(3T)"], 1),
        ("A system absorbs heat Q from a reservoir at T_h and rejects heat to a reservoir at T_c while producing work W. The entropy production of the universe is:",
         ["Q/T_h − (Q − W)/T_c", "(Q − W)/T_c − Q/T_h", "W/T_h", "0"], 1),
        ("The Helmholtz free energy F satisfies the relation (∂F/∂T)_V =:",
         ["−S", "S", "−P", "P"], 0),
        ("In the limit of a reversible isothermal free expansion of an ideal gas, the entropy change of the system approaches:",
         ["0", "nR ln(V2/V1)", "Infinity", "−nR ln(V2/V1)"], 1),
    ]
}

# ====================== ANATOMY & PHYSIOLOGY (SciOly-focused) ======================
QUESTIONS_ANATPHY = {
    "Novice": [
        ("Which type of tissue covers body surfaces and lines internal cavities?",
         ["Connective tissue", "Muscle tissue", "Nervous tissue", "Epithelial tissue"], 3),
        ("The basic functional unit of the nervous system is the:",
         ["Nephron", "Neuron", "Osteocyte", "Myofibril"], 1),
        ("Which organelle is known as the powerhouse of the cell?",
         ["Ribosome", "Golgi apparatus", "Mitochondrion", "Lysosome"], 2),
        ("Bones are connected to other bones by:",
         ["Tendons", "Ligaments", "Cartilage only", "Fascia"], 1),
        ("The primary function of red blood cells is to:",
         ["Fight infection", "Clot blood", "Transport oxygen", "Produce antibodies"], 2),
        ("Which system is responsible for the exchange of oxygen and carbon dioxide?",
         ["Circulatory", "Respiratory", "Digestive", "Endocrine"], 1),
        ("The pacemaker of the heart is the:",
         ["AV node", "SA node", "Bundle of His", "Purkinje fibers"], 1),
        ("Which hormone lowers blood glucose levels?",
         ["Glucagon", "Insulin", "Cortisol", "Epinephrine"], 1),
        ("The functional unit of the kidney is the:",
         ["Neuron", "Alveolus", "Nephron", "Hepatocyte"], 2),
        ("Which type of muscle is voluntary?",
         ["Cardiac", "Smooth", "Skeletal", "All of the above"], 2),
        ("The largest organ of the human body is the:",
         ["Liver", "Brain", "Skin", "Small intestine"], 2),
        ("Which blood vessels carry blood away from the heart?",
         ["Veins", "Arteries", "Capillaries", "Venules"], 1),
        ("The process of bone formation is called:",
         ["Ossification", "Hematopoiesis", "Calcification only", "Resorption"], 0),
        ("Which part of the brain controls balance and coordination?",
         ["Cerebrum", "Cerebellum", "Medulla oblongata", "Hypothalamus"], 1),
        ("Bile is produced by the:",
         ["Gallbladder", "Pancreas", "Liver", "Stomach"], 2),
        ("The voice box is also known as the:",
         ["Pharynx", "Larynx", "Trachea", "Epiglottis"], 1),
        ("Which vitamin is essential for blood clotting?",
         ["Vitamin C", "Vitamin D", "Vitamin K", "Vitamin B12"], 2),
        ("White blood cells are also called:",
         ["Erythrocytes", "Leukocytes", "Thrombocytes", "Platelets"], 1),
        ("The smallest blood vessels are:",
         ["Arteries", "Veins", "Capillaries", "Arterioles"], 2),
        ("Homeostasis means the body maintains:",
         ["Constant growth", "Stable internal conditions", "Only external responses", "Maximum energy production"], 1),
    ],
    "Intermediate": [
        ("Which structure prevents food from entering the larynx during swallowing?",
         ["Uvula", "Epiglottis", "Soft palate", "Glottis"], 1),
        ("The hormone TSH is produced by the:",
         ["Thyroid gland", "Anterior pituitary", "Posterior pituitary", "Hypothalamus only"], 1),
        ("In the sliding filament theory, calcium binds to which protein?",
         ["Myosin", "Actin", "Troponin", "Tropomyosin"], 2),
        ("Which cranial nerve is responsible for the sense of smell?",
         ["Optic (II)", "Olfactory (I)", "Trigeminal (V)", "Facial (VII)"], 1),
        ("The renal corpuscle is made of the glomerulus and:",
         ["Loop of Henle", "Bowman’s capsule", "Collecting duct", "Proximal tubule only"], 1),
        ("Oxygenated blood returns to the heart from the lungs via the:",
         ["Pulmonary arteries", "Pulmonary veins", "Aorta", "Superior vena cava"], 1),
        ("Surfactant in the lungs functions to:",
         ["Increase surface tension", "Decrease surface tension in alveoli", "Produce mucus", "Kill pathogens"], 1),
        ("Most nutrient absorption occurs in the:",
         ["Stomach", "Duodenum", "Jejunum", "Large intestine"], 2),
        ("The shoulder joint is an example of a:",
         ["Hinge joint", "Pivot joint", "Ball-and-socket joint", "Saddle joint"], 2),
        ("Aldosterone causes the kidneys to:",
         ["Excrete more sodium", "Reabsorb more sodium", "Reabsorb more potassium", "Decrease blood volume"], 1),
        ("Myelin in the peripheral nervous system is produced by:",
         ["Oligodendrocytes", "Schwann cells", "Astrocytes", "Microglia"], 1),
        ("The two cerebral hemispheres are connected by the:",
         ["Corpus callosum", "Thalamus", "Pons", "Medulla"], 0),
        ("Pepsin is an enzyme that digests:",
         ["Carbohydrates", "Lipids", "Proteins", "Nucleic acids"], 2),
        ("Which leukocyte is most involved in allergic reactions?",
         ["Neutrophil", "Eosinophil", "Monocyte", "Lymphocyte"], 1),
        ("Thyroid hormones require which element for synthesis?",
         ["Iron", "Iodine", "Calcium", "Zinc"], 1),
        ("During depolarization of a neuron, the main ion entering the cell is:",
         ["Potassium", "Sodium", "Calcium", "Chloride"], 1),
        ("Functional residual capacity equals:",
         ["Tidal volume + inspiratory reserve", "Expiratory reserve volume + residual volume", "Vital capacity only", "Inspiratory capacity"], 1),
        ("Oxytocin is released from the:",
         ["Anterior pituitary", "Posterior pituitary", "Thyroid", "Adrenal cortex"], 1),
        ("The spleen’s primary functions include:",
         ["Producing digestive enzymes", "Filtering blood and immune surveillance", "Storing bile", "Producing urine"], 1),
        ("Elastic cartilage is found in the:",
         ["Nose", "Intervertebral discs", "External ear", "Tracheal rings"], 2),
    ],
    "Hard": [
        ("The sodium-potassium pump moves:",
         ["3 Na⁺ in and 2 K⁺ out", "3 Na⁺ out and 2 K⁺ in", "2 Na⁺ out and 3 K⁺ in", "Equal numbers of both ions"], 1),
        ("The juxtaglomerular apparatus helps regulate:",
         ["Blood glucose", "Blood pressure through renin release", "Body temperature", "Blood pH directly"], 1),
        ("In a sarcomere, the H zone contains:",
         ["Only thin filaments", "Only thick filaments", "Both overlapping filaments", "No filaments"], 1),
        ("Which cranial nerve carries parasympathetic innervation to the heart?",
         ["Glossopharyngeal (IX)", "Vagus (X)", "Facial (VII)", "Trigeminal (V)"], 1),
        ("The Bohr effect refers to:",
         ["Increased O₂ affinity at higher pH", "Decreased O₂ affinity of hemoglobin when pH drops or CO₂ rises", "Increased CO₂ binding only", "A left shift of the dissociation curve"], 1),
        ("Keratohyalin granules are found in which epidermal layer?",
         ["Stratum basale", "Stratum spinosum", "Stratum granulosum", "Stratum corneum"], 2),
        ("Macula densa cells sense changes in:",
         ["Blood pressure in the afferent arteriole", "NaCl concentration in the distal tubule", "Oxygen levels", "Hormone levels"], 1),
        ("Type I muscle fibers are characterized as:",
         ["Fast-twitch glycolytic", "Slow-twitch oxidative and fatigue-resistant", "Fast oxidative-glycolytic", "Primarily anaerobic"], 1),
        ("The portal triad of the liver contains branches of the:",
         ["Hepatic artery, hepatic vein, and bile duct", "Hepatic artery, portal vein, and bile duct", "Portal vein, hepatic vein, and lymph vessel", "Hepatic artery, portal vein, and hepatic vein"], 1),
        ("During the absolute refractory period:",
         ["A strong stimulus can still trigger an action potential", "No stimulus can trigger another action potential", "Only potassium channels are open", "The membrane is hyperpolarized"], 1),
        ("Hepcidin regulates iron by:",
         ["Increasing iron absorption when levels are high", "Decreasing iron absorption and release when iron is high", "Only affecting hemoglobin synthesis", "Stimulating erythropoietin"], 1),
        ("The countercurrent multiplier is located in the:",
         ["Proximal convoluted tubule", "Loop of Henle", "Distal convoluted tubule", "Collecting duct"], 1),
        ("The sarcoplasmic reticulum’s main role in skeletal muscle is to:",
         ["Store and release calcium ions", "Generate ATP", "Synthesize contractile proteins", "Conduct action potentials"], 0),
        ("In fetal circulation, the foramen ovale allows blood to flow from:",
         ["Right atrium to left atrium", "Right ventricle to left ventricle", "Pulmonary artery to aorta", "Superior to inferior vena cava"], 0),
        ("Which is NOT a major function of the hypothalamus?",
         ["Temperature regulation", "Control of the autonomic nervous system", "Production of ADH and oxytocin", "Direct voluntary motor control"], 3),
        ("The common pathway of the clotting cascade begins with activation of:",
         ["Factor XII", "Factor VII", "Factor X", "Factor VIII"], 2),
        ("The major intracellular anion is:",
         ["Sodium", "Chloride", "Potassium", "Phosphate / organic phosphates"], 3),
        ("Linear acceleration and head position are detected by the:",
         ["Cochlea", "Semicircular canals", "Utricle and saccule", "Tympanic membrane"], 2),
        ("Starling’s law of the heart states that:",
         ["Heart rate is controlled only by the SA node", "Stroke volume increases with increased end-diastolic volume (within physiological limits)", "Cardiac output is independent of venous return", "Blood pressure depends only on resistance"], 1),
        ("Testosterone is produced primarily by which cells in the testes?",
         ["Sertoli cells", "Leydig (interstitial) cells", "Spermatogonia", "Principal cells"], 1),
    ],
    "Very Hard": [
        ("The approximate Nernst potential for potassium in a typical neuron is:",
         ["+60 mV", "0 mV", "−90 mV", "−70 mV"], 2),
        ("During exercise the oxygen-hemoglobin dissociation curve shifts right mainly because of:",
         ["Decreased temperature and 2,3-BPG", "Increased CO₂, H⁺, temperature, and 2,3-BPG", "Increased pH only", "Decreased PCO₂"], 1),
        ("Most bicarbonate reabsorption in the kidney occurs in the:",
         ["Proximal convoluted tubule", "Thick ascending limb", "Distal convoluted tubule", "Collecting duct"], 0),
        ("The length-tension relationship in skeletal muscle is largely due to:",
         ["Optimal overlap of actin and myosin filaments", "Availability of ATP only", "Frequency of stimulation only", "Elasticity of titin alone"], 0),
        ("The blood-brain barrier is formed primarily by:",
         ["Tight junctions between capillary endothelial cells", "Astrocytes alone", "The meninges", "Absence of capillaries in the brain"], 0),
        ("The second heart sound (S2) is caused by:",
         ["Closure of the atrioventricular valves", "Closure of the semilunar valves", "Opening of the AV valves", "Rapid ventricular filling"], 1),
        ("The Henderson-Hasselbalch equation for the bicarbonate system is:",
         ["pH = pKa + log([H₂CO₃]/[HCO₃⁻])", "pH = pKa + log([HCO₃⁻]/[H₂CO₃])", "pH = pKa − log([HCO₃⁻]/[CO₂])", "pH = 6.1 + log([CO₂]/[HCO₃⁻])"], 1),
        ("Which change would increase glomerular filtration rate?",
         ["Constriction of the afferent arteriole", "Dilation of the afferent arteriole", "Increased plasma oncotic pressure", "Severe volume depletion"], 1),
        ("Calcium-induced calcium release in cardiac muscle involves:",
         ["L-type Ca²⁺ channels triggering ryanodine receptors", "Only T-type calcium channels", "Voltage-gated sodium channels releasing Ca²⁺", "No involvement of the sarcoplasmic reticulum"], 0),
        ("Water reabsorption in the proximal tubule is driven mainly by:",
         ["Active transport of water", "The osmotic gradient created by solute reabsorption", "Hydrostatic pressure", "ADH"], 1),
        ("A key feature of smooth muscle is:",
         ["It always requires an action potential to contract", "It can maintain contraction with low ATP use (latch state)", "It uses troponin as its main regulatory protein", "It has an extensive T-tubule system"], 1),
        ("The Hering-Breuer reflex is mediated by:",
         ["Carotid body chemoreceptors", "Pulmonary stretch receptors via the vagus nerve", "Central chemoreceptors", "Joint proprioceptors"], 1),
        ("The enzyme responsible for organification and coupling of thyroid hormones is:",
         ["Thyroid peroxidase", "Deiodinase", "Thyroglobulin synthase", "TSH receptor"], 0),
        ("Atrial natriuretic peptide (ANP) primarily:",
         ["Increases renin release", "Causes sodium retention", "Promotes natriuresis and lowers blood volume/pressure", "Stimulates ADH release"], 2),
        ("The plateau phase of the cardiac action potential is mainly due to:",
         ["Rapid opening of delayed rectifier K⁺ channels", "Inward Ca²⁺ current balancing outward K⁺ current", "Prolonged opening of Na⁺ channels", "Inactivity of the Na⁺/K⁺ pump"], 1),
        ("Cerebrospinal fluid is produced by the:",
         ["Arachnoid villi", "Choroid plexus", "Ependymal cells of the central canal only", "Pia mater"], 1),
        ("Factor VIII acts as a cofactor for:",
         ["Activation of Factor X by Factor IXa", "Conversion of prothrombin to thrombin", "Activation of Factor VII", "Cross-linking of fibrin"], 0),
        ("At rest the membrane is more permeable to:",
         ["Sodium than potassium", "Potassium than sodium", "Calcium than either", "Chloride only"], 1),
        ("In severe emphysema one would expect:",
         ["Increased elastic recoil", "Decreased residual volume", "Air trapping and increased residual volume", "Increased FEV1/FVC ratio"], 2),
        ("The zona glomerulosa of the adrenal cortex mainly secretes:",
         ["Cortisol", "Aldosterone", "Androgens", "Epinephrine"], 1),
    ],
    "Impossible": [
        ("Using the Nernst equation at 37 °C, with [K⁺]in = 140 mM and [K⁺]out = 5 mM, the potassium equilibrium potential is closest to:",
         ["−90 mV", "−70 mV", "−60 mV", "+60 mV"], 0),
        ("In chronic metabolic acidosis the expected respiratory compensation is:",
         ["Hypoventilation", "Hyperventilation that lowers PCO₂", "Increased renal bicarbonate excretion", "Decreased ammonia production"], 1),
        ("The Goldman-Hodgkin-Katz equation takes into account:",
         ["Only potassium permeability", "Relative permeabilities of Na⁺, K⁺, and Cl⁻", "Only the contribution of the Na⁺/K⁺ pump", "The peak of the action potential"], 1),
        ("In healthy individuals during maximal exercise, the main limit to oxygen delivery is usually:",
         ["Pulmonary diffusion", "Cardiac output", "Mitochondrial capacity", "Hemoglobin concentration"], 1),
        ("Glucose reabsorption in the proximal tubule occurs primarily via:",
         ["SGLT cotransporters driven by the sodium gradient", "GLUT transporters only", "Paracellular diffusion", "Primary active transport independent of sodium"], 0),
        ("The Frank-Starling mechanism is best explained by:",
         ["Increased sympathetic drive", "Optimal sarcomere length improving actin-myosin overlap and calcium sensitivity", "It only works in heart failure", "Decreased stroke volume with increased preload"], 1),
        ("The chloride shift in red blood cells involves:",
         ["Cl⁻ entering in exchange for HCO₃⁻ leaving", "Cl⁻ leaving in exchange for HCO₃⁻ entering", "Active pumping of chloride out", "No role for band 3 protein"], 0),
        ("According to the size principle of motor unit recruitment:",
         ["Large motor units are recruited first", "Small, fatigue-resistant motor units are recruited first", "Recruitment is random", "Fast-twitch fibers are always first"], 1),
        ("A lesion of the left optic tract produces:",
         ["Left homonymous hemianopia", "Right homonymous hemianopia", "Bitemporal hemianopia", "Blindness in the left eye only"], 1),
        ("The plateau of the ventricular action potential is caused mainly by:",
         ["Delayed rectifier potassium channels opening quickly", "Inward calcium current through L-type channels balancing potassium efflux", "Sodium channels staying open", "Temporary stop of the Na⁺/K⁺ pump"], 1),
        ("Correct sequence in skeletal muscle excitation-contraction coupling:",
         ["AP → T-tubule → DHPR conformational change → RyR opens → Ca²⁺ release", "AP → direct Ca²⁺ entry from ECF → troponin binding", "AP → IP₃ production → SR release", "AP → Na⁺ entry → direct myosin activation"], 0),
        ("The key active transport step of the countercurrent multiplier is:",
         ["Na⁺-K⁺-2Cl⁻ cotransport in the thick ascending limb", "Water reabsorption in the descending limb", "Urea recycling alone", "Active Na⁺ transport in the collecting duct"], 0),
        ("Blocking the Na⁺/Ca²⁺ exchanger (NCX) in cardiac myocytes would tend to:",
         ["Decrease intracellular calcium and weaken contraction", "Increase intracellular calcium and strengthen contraction", "Have no effect on contractility", "Affect only pacemaker cells"], 1),
        ("The respiratory quotient for pure carbohydrate oxidation is:",
         ["0.7", "0.8", "1.0", "1.2"], 2),
        ("The final hydroxylation step in the formation of active vitamin D (calcitriol) occurs mainly in the:",
         ["Liver", "Kidney (proximal tubule)", "Skin", "Intestine"], 1),
        ("The pre-Bötzinger complex is best described as:",
         ["The primary rhythm generator for respiration", "A peripheral chemoreceptor", "Located in the cerebral cortex", "Active only during exercise"], 0),
        ("Hypoproteinemia would be expected to:",
         ["Decrease GFR", "Increase GFR because of lower glomerular capillary oncotic pressure", "Have no effect on GFR", "Increase afferent arteriolar resistance"], 1),
        ("The tenase complex consists of:",
         ["Factors VIIIa and IXa (with Ca²⁺ and phospholipid)", "Factors Va and Xa", "Tissue factor and Factor VIIa", "Factors XIa and XIIa"], 0),
        ("The major intracellular buffers are:",
         ["Bicarbonate", "Phosphate and proteins (including hemoglobin)", "Ammonia", "Sulfate"], 1),
        ("A left shift of the oxygen-hemoglobin dissociation curve is caused by:",
         ["Increased 2,3-BPG", "Decreased pH", "Increased temperature", "Fetal hemoglobin or decreased 2,3-BPG"], 3),
    ]
}

# ====================== UI CLASSES ======================
class AnswerButton(Button):
    def __init__(self, label: str, index: int, correct_index: int, options: list):
        super().__init__(label=label, style=discord.ButtonStyle.secondary)
        self.index = index
        self.correct_index = correct_index
        self.options = options

    async def callback(self, interaction: discord.Interaction):
        view: QuestionView = self.view
        if view.answered:
            await interaction.response.send_message("This question has already been answered.", ephemeral=True)
            return
        view.answered = True
        selected = chr(65 + self.index)
        correct = chr(65 + self.correct_index)

        for item in view.children:
            item.disabled = True
            if isinstance(item, AnswerButton):
                if item.index == self.correct_index:
                    item.style = discord.ButtonStyle.success
                elif item.index == self.index:
                    item.style = discord.ButtonStyle.danger

        if self.index == self.correct_index:
            msg = f"✅ **Correct!**\nYou selected **{selected}) {self.options[self.index]}**"
        else:
            msg = (f"❌ **Wrong.**\n"
                   f"You selected **{selected}) {self.options[self.index]}**\n"
                   f"Correct answer: **{correct}) {self.options[self.correct_index]}**")
        await interaction.response.send_message(msg, ephemeral=True)

        embed = interaction.message.embeds[0]
        embed.set_footer(text=f"Answered by {interaction.user.display_name}")
        await interaction.message.edit(view=view)


class QuestionView(View):
    def __init__(self, correct_index: int, options: list, owner_id: int):
        super().__init__(timeout=120)
        self.correct_index = correct_index
        self.options = options
        self.owner_id = owner_id
        self.answered = False
        for i, letter in enumerate(["A", "B", "C", "D"]):
            self.add_item(AnswerButton(letter, i, correct_index, options))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who requested this question can answer it.", ephemeral=True
            )
            return False
        return True


class DifficultySelect(Select):
    def __init__(self, owner_id: int, questions_dict: dict, color: int, title_prefix: str):
        self.owner_id = owner_id
        self.questions_dict = questions_dict
        self.color = color
        self.title_prefix = title_prefix
        options = [
            discord.SelectOption(label="Novice", description="Fundamentals", emoji="🟢"),
            discord.SelectOption(label="Intermediate", description="Solid intermediate", emoji="🟡"),
            discord.SelectOption(label="Hard", description="Advanced", emoji="🟠"),
            discord.SelectOption(label="Very Hard", description="Very challenging", emoji="🔴"),
            discord.SelectOption(label="Impossible", description="Brutal", emoji="🟣"),
        ]
        super().__init__(placeholder="Choose difficulty...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who ran the command can choose the difficulty.", ephemeral=True
            )
            return

        difficulty = self.values[0]
        q_text, options, correct = random.choice(self.questions_dict[difficulty])

        embed = discord.Embed(
            title=f"{self.title_prefix} — {difficulty}",
            description=q_text,
            color=self.color
        )
        option_text = "\n".join(f"**{chr(65+i)})** {opt}" for i, opt in enumerate(options))
        embed.add_field(name="Options", value=option_text, inline=False)
        embed.set_footer(text="(Only the user who requested the question can answer this question)")

        view = QuestionView(correct, options, interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)


class DifficultyView(View):
    def __init__(self, owner_id: int, questions_dict: dict, color: int, title_prefix: str):
        super().__init__(timeout=60)
        self.owner_id = owner_id
        self.add_item(DifficultySelect(owner_id, questions_dict, color, title_prefix))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who used the command can select a difficulty.", ephemeral=True
            )
            return False
        return True


# ====================== BOT ======================
class ThermoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


client = ThermoBot()


@client.tree.command(name="thermo", description="Get a thermodynamics question")
async def thermo(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 HeatSO Thermodynamics",
        description="Select a difficulty:",
        color=0xE85D04
    )
    await interaction.response.send_message(
        embed=embed,
        view=DifficultyView(
            interaction.user.id,
            questions_dict=QUESTIONS,
            color=0xE85D04,
            title_prefix="🔥 HeatSO Thermodynamics"
        )
    )


@client.tree.command(name="random", description="Alias for /thermo")
async def random_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 HeatSO Thermodynamics",
        description="Select a difficulty:",
        color=0xE85D04
    )
    await interaction.response.send_message(
        embed=embed,
        view=DifficultyView(
            interaction.user.id,
            questions_dict=QUESTIONS,
            color=0xE85D04,
            title_prefix="🔥 HeatSO Thermodynamics"
        )
    )


@client.tree.command(name="anatphy", description="Get an Anatomy & Physiology question (SciOly style)")
async def anatphy(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🧬 Anatomy & Physiology",
        description="Select a difficulty:",
        color=0x0D9488
    )
    await interaction.response.send_message(
        embed=embed,
        view=DifficultyView(
            interaction.user.id,
            questions_dict=QUESTIONS_ANATPHY,
            color=0x0D9488,
            title_prefix="🧬 Anatomy & Physiology"
        )
    )


@client.tree.command(name="coinflip", description="Flip a coin")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"🪙 The coin landed on **{result}**!")


client.run(os.getenv("DISCORD_TOKEN"))
