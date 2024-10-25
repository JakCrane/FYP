To reference a PDF in Markdown, you can use a link. Here is an example:


[1](/Research_FIles/October/cold_spray_additive_manufacturing_and_repair.pdf)

high pressure cold spray > 1MPa, low pressure < 1MPa

greater than 100um and smaller than 10um are hard to deposit

most frequently used size is 20um - 60um

[2](/Research_FIles/October/Experimental_Investigation_on_mass_flow_rate_measurements_and_feeding_characteristics_of_powder_at_high_pressure.pdf)

mass flow rate for powder. uses cyclone seperator to measure powder

[3](/Research_FIles/October/progress_and_challenges_in_exploration_of_powder_fueled_ramjets.pdf)

A fluidized bed-type powder feed system can achieve stable
delivery of powder propellant, but due to the complex structure of the
system, it is not conducive to the integration of powder engine systems
and lightweight applications. 

![alt text](/Research_FIles/October/fluidised_design.png)

The powder feed system of motor driven piston has obvious advantages for piston motion stability regulation, but the system putsforward high requirements for motor power. Especially when the pressure in the storage tank is high, it is difficult for the motor to push thepiston and thus the piston motion speed is difficult to regulate if an equalpressure balance is not taken. At the same time, since the piston isdirectly connected to the motor rod, it will increase the length of thepowder feed system accordingly, which is not beneficial to system integration.
Although the powder feed system of the pneumatic drive piston ismore complex in terms of gas circuit design, it can achieve piston speedregulation by adjusting the amount of driving gas and fluidizing gas. Thedriving gas and fluidizing gas can share a common gas source, withoutthe need for an additional piston drive device. When the pressure difference between the drive chamber and the fluidization chamber isgreater than the combined resistance, the piston could be motivated.Moreover, the piston guide rod can be removed in this way, and thesystem is more integrated. It can be seen that the powder feeding systemof the pneumatic drive piston is more suitable for powder fueled ramjets,and further research needs to focus on the accurate regulation of thepressure of fluidized gas and drive gas. 


[5](/Research_FIles/October/Powder_feeding_enhancement_of_powder_propellant_supply_system_by_using_gas_permeable_piston.pdf)




had a meeting with ajit and he suggested taking research in a different direction


![alt text](/Research_FIles/October/feedback_notes.jpg)
![alt text](/Research_FIles/October/feedback_notes_1.jpg)


take a more smad style approach. look at what is currently available in terms of cold spray systems, what feed systems are commerically available and think more about the wider context in which they will be used to give ideas of flow rates and powder sizes



current proposed in-space manufacturing literature

[6](/Research_FIles/October/in-space_additive_manufacturing_a_review.pdf)

general considerations:
    where is manufacturing taking place?
        inside a pressurised vehicle - high atmosphere low gravity
        outside a vehicle in transit - low atmosphere low gravity
        planetary manufacturing - high or low atmosphere and high or low gravity

    where is cold spray good?!!!!!!!!!!!!!!!!

[7](/Research_FIles/October/an_overview_of_cold_spray_coatings_in_additive_manufacturing_component_repair_and_other_engineering_applications.pdf)

seems to suggest that it is especially useful for coatings (maybe less useful for other stuff)

rate of coating quoted at 
```
    The CS beam’s spray footprint is small and clearly defined. A typical spray beam has a diameter of around 10 mm with sharp edges. A narrow spray beam combined with a high powder input rate results in extremely high deposition rates. In most cases, a 1–2-mm-thick coating may be applied in a single pass to most materials
```

```
Although post-spray heat treatment can provide mechanical property values similar to bulk values, the coldsprayed coating has near-zero ductility in its as-sprayed state.
Pure ceramics and certain work-hardening alloys cannot be sprayed and necessitate the substrate to have at least some ductility to generate well-bonded coatings. As a result, cold-sprayed coatings on ceramic substrates have a low bond strength. 
To attain the velocities required for deposition, highquality coating, such as MCrAlYs, Inconel, and others, is manufactured with pricey helium as the processing gas. 
Spraying complicated and interior surfaces is problematic [34].
```

figure 14 suggests you can print 3d objects with it

interesting 
n LPCSP, the processing gas is air. The premixing of feedstock powder and carrier gas does not take place because the powder feeder is placed at the convergence region of the CD nozzle. It develops coating with better adhesion. However, the cohesive properties are poor compared to HPCSP coating.

[8](/Research_FIles/October/cold_spray_forming_a_novel_approach_in_cold_spray_additive_manufacturing_of_complex_parts_using_3d_printed_polymer_molds.pdf)

states higher deposition rates than PBF-LB/M and DED-LB
compared to those CS is lower resolution

The process offers material deposition rates of typical 2–7 kg/h [need to validate this]


[9](/Research_FIles/October/influence_of_feedstock_pwoder_and_cold_spray_processing_parameters_on_microstructure_and_mechanical_properties.pdf)


parameter comparison but its at 300°c so hotter than ours
The powder feed rate for atomized powders and hydride de-hydride powder were 5.7 g/min and 3.5 g/min, respectively. 

Hydride de-hydride means [idk will find out soon hopefully]

[9.2](https://www.google.com/search?q=plasma+atomisation&oq=plasma+atomisation&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCggCEAAYDxgWGB4yDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyCggFEAAYgAQYogTSAQgyNjk0ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:fd3ef46b,vid:vouCR6bhCt0,st:0)plasma atomization

[9.3](/Research_FIles/October/ch5_Atomization_and_Granulation.pdf) gas atomisation 

[10](/Research_FIles/October/cold_gas_dynamic_manufacturing_a_non_thermal_approach_to_freeform_fabrication.pdf)

helium MPa printing system with deposition rates of 100g/min

[11](https://impact-innovations.com/en/portfolio-item/impact-powder-feeder-cold-spray/)

interesting link

[12](/Research_FIles/October/powder_feeder_redesign_for_laser_assisted_cold_spray.pdf)

Section 2.3 Commercially Available Cold Spray Systems
The aim of this section is to discuss commercially available cold spray systems and how they are sold

A majority of the powder feeders used for thermal 
spray  rely  on  the  rotating  disk  method  while  the  screw  fed  design  seemed  to  be  in  industries  
outside of thermal spray. 

The first was powder calibration ability as powders of different densities needed 
to  be  fed  with  different  volume  flowrates.

[13](https://www.oerlikon.com/metco/en/products-services/thermal-spray-equipment/thermal-spray-components/feeders/?tab=fluidized_bed)

3 types of feeders
oerlikon uses gravimetric control for fluidised and volumetric feed system
volumetric has a circular channel filled with powder that spins based on the mass of the powder on the plate

![alt text](/Research_FIles/October/16x9_Fluidized.jpg)


[14](/Research_FIles/October/Development_of_a_generalized_parameter_window.pdf)

has a lot of info on size and speed 

[15](/Research_FIles/October/A_Review_of_Advances_in_Cold_Spray_Additive_Manufacturing.pdf)

has info on parameter correlation with DE and stuff like that

[16](/Research_FIles/October/Cold_spray_deposition_for_additive_manufacturing_of_freeform_structural.pdf)

300 - 400 cm^3/hr but quoted at 5-20% porosity so probably low mass (p sure not the 2kg/hr seen)

