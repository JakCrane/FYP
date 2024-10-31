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

Fig. 7. Critical impact velocity for a 25 lm particle calculated for different
materials with Eq. (8). The dark grey levels indicate a range of uncertainty
with respect to the range of available materials data



[15](/Research_FIles/October/A_Review_of_Advances_in_Cold_Spray_Additive_Manufacturing.pdf)

has info on parameter correlation with DE and stuff like that

Table 1 lists the Vcr and Ver for the most CSAM-ed materials

Table 2. Correlation behavior among the different input/output for CS 
[!alt text](/Research_FIles/October/empirical_relations_of_cold_spray_parameters.png)

[16](/Research_FIles/October/Cold_spray_deposition_for_additive_manufacturing_of_freeform_structural.pdf)

300 - 400 cm^3/hr but quoted at 5-20% porosity so probably low mass (p sure not the 2kg/hr seen)

[17](https://www.nottingham.ac.uk/research/groups/cse/facilities/processing-equipment.aspx)

nottingham cold spray set up


[18](/Research_FIles/October/Establishing_a_Cold_Spray_Particle_Deposition_Window_on_Polymer_Substrate.pdf)

thought it had info on hardness wrt particle diameter but keeping cos maybe useful?


[19](/Research_FIles/October/Experimental_and_Numerical_Investigations_of_Titanium.pdf)

thought it had info on hardness wrt particle diameter but keeping cos maybe useful?


[20](/Research_FIles/October/Cold_Spraying_of_Titanium_A_Review_of_Bonding_Mechanisms.pdf)

The cooling rate of the material decreases with increasing particle size. 
The cooling rate has to be “low enough” to promote shear instability and on the other hand, “high enough” to let the interface solidify and finish the bonding process.

The shear loading under critical conditions leads to what is termed as adiabatic shear instability where thermal softening is locally dominant over strain and strain rate hardening, which leads to a discontinuous jump in strain and temperature and breakdown of flow stresses [6]. This adiabatic shear instability phenomenon results in viscous flow of material in an outward flowing direction at temperatures close to the melting temperature of the material.


[21](/Research_FIles/October/Cold_Spraying_a_materials_perspective.pdf)

The particle impact is associated with viscoplastic deformation of the interacting bodies, leading to (1) sequential compaction of the feedstock powder into a deposit, and (2) metallurgical bonding over a significant fraction of the particle-particle interfaces. Both of these processes are central to obtaining a dense and strong deposit.

incomplete compaction results in high porosity, whereas poor bonding results in low strength of the deposit.

Particles of cold spray powders are typically 10-50 µm in diameter, and the process of particle impact – from the time of initial contact to total dissipation of kinetic energy – takes about 100 ns. 

There are several physical phenomena that play a role in the process of deposition in CS of deformable materials. The most important of these is viscoplastic deformation, which occurs under dynamic shear loading.

[elastic deformation isnt important]

(wikipedia) - Viscoplasticity is a theory in continuum mechanics that describes the rate-dependent inelastic behavior of solids.

This means that for the same impact velocity, larger particles deform more adiabatically, and vice versa. 

The heat generation during plastic deformation, especially under high-strain rates, may lead to strain localisation and shear instability. This condition is normally manifested as shear banding and failure in bulk materials [46].

 During strain softening, the material becomes inherently unstable with respect to plastic deformation, so that localization and shear banding may occur at a critical strain, gamma_cr. Beyond this point, the local strain at the shear band increases sharply to high values, while the overall strain remains almost unchanged up to the point of rupture. As will be discussed later in more detail, this phenomenon is considered to be closely related to particle bonding in CS [40].

Generally, bonding takes place as soon as atomically-flat clean surfaces of two components are brought into contact. In principle, this can occur without a need for heating, fusion or mechanical interlocking. In practice, however, surfaces of metallic components are rarely flat and are usually covered by an oxide layer.

[22](/Research_FIles/October/Performance_Metric_for_Powder_Feeder_Systems_in_Additive_Manufacturing.pdf)

![alt text](/Research_FIles/October/screw_feed.png)
![alt text](/Research_FIles/October/wheel_feed.png)
![alt text](/Research_FIles/October/disk_feed.png)

[23](/Research_FIles/October/Vibratory_Powder_Feeding_for_Powder_Bed_Additive_Manufacturing_Using_Water_and_Gas_Atomized_Metal_Powders.pdf)

![alt text](/Research_FIles/October/vibrational_feed.png)
![alt text](/Research_FIles/October/feed_rate_with_vibrational.png)

[24](/Research_FIles/October/Powder_feeding_in_a_powder_engine_under_different_gas_solid_ratios.pdf)

![alt text](/Research_FIles/October/fluidising_feed_system.png)

[25](https://www.parkerionics.com/powder-coating-equipment/powder-handling-equipment/auger-feed--ace-feed--system_pt30.html)

![alt text](/Research_FIles/October/auger.jpg)
