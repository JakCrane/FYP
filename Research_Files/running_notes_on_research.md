To reference a PDF in Markdown, you can use a link. Here is an example:


[1](/Research_Files/October/cold_spray_additive_manufacturing_and_repair.pdf)

high pressure cold spray > 1MPa, low pressure < 1MPa

greater than 100um and smaller than 10um are hard to deposit

most frequently used size is 20um - 60um

[2](/Research_Files/October/Experimental_Investigation_on_mass_flow_rate_measurements_and_feeding_characteristics_of_powder_at_high_pressure.pdf)

mass flow rate for powder. uses cyclone seperator to measure powder

[3](/Research_Files/October/progress_and_challenges_in_exploration_of_powder_fueled_ramjets.pdf)

A fluidized bed-type powder feed system can achieve stable
delivery of powder propellant, but due to the complex structure of the
system, it is not conducive to the integration of powder engine systems
and lightweight applications. 

![alt text](/Research_Files/October/fluidised_design.png)

The powder feed system of motor driven piston has obvious advantages for piston motion stability regulation, but the system putsforward high requirements for motor power. Especially when the pressure in the storage tank is high, it is difficult for the motor to push thepiston and thus the piston motion speed is difficult to regulate if an equalpressure balance is not taken. At the same time, since the piston isdirectly connected to the motor rod, it will increase the length of thepowder feed system accordingly, which is not beneficial to system integration.
Although the powder feed system of the pneumatic drive piston ismore complex in terms of gas circuit design, it can achieve piston speedregulation by adjusting the amount of driving gas and fluidizing gas. Thedriving gas and fluidizing gas can share a common gas source, withoutthe need for an additional piston drive device. When the pressure difference between the drive chamber and the fluidization chamber isgreater than the combined resistance, the piston could be motivated.Moreover, the piston guide rod can be removed in this way, and thesystem is more integrated. It can be seen that the powder feeding systemof the pneumatic drive piston is more suitable for powder fueled ramjets,and further research needs to focus on the accurate regulation of thepressure of fluidized gas and drive gas. 


[5](/Research_Files/October/Powder_feeding_enhancement_of_powder_propellant_supply_system_by_using_gas_permeable_piston.pdf)




had a meeting with ajit and he suggested taking research in a different direction


![alt text](/Research_Files/October/feedback_notes.jpg)
![alt text](/Research_Files/October/feedback_notes_1.jpg)


take a more smad style approach. look at what is currently available in terms of cold spray systems, what feed systems are commerically available and think more about the wider context in which they will be used to give ideas of flow rates and powder sizes



current proposed in-space manufacturing literature

[6](/Research_Files/October/in-space_additive_manufacturing_a_review.pdf)

general considerations:
    where is manufacturing taking place?
        inside a pressurised vehicle - high atmosphere low gravity
        outside a vehicle in transit - low atmosphere low gravity
        planetary manufacturing - high or low atmosphere and high or low gravity

    where is cold spray good?!!!!!!!!!!!!!!!!

[7](/Research_Files/October/an_overview_of_cold_spray_coatings_in_additive_manufacturing_component_repair_and_other_engineering_applications.pdf)

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

[8](/Research_Files/October/cold_spray_forming_a_novel_approach_in_cold_spray_additive_manufacturing_of_complex_parts_using_3d_printed_polymer_molds.pdf)

states higher deposition rates than PBF-LB/M and DED-LB
compared to those CS is lower resolution

The process offers material deposition rates of typical 2–7 kg/h [need to validate this]

87.6 g/s of Cu powder
300 standard liters per minute
8.94 g/mL at 25 °C [8.1](https://www.sigmaaldrich.com/GB/en/product/aldrich/266086?srsltid=AfmBOorlnBo-7y7D9ZJpWqgP9Rl2erRRW8rduaXeQcGV3pTplybTiREa)
roughly 10mL/s of copper
vs 5L/s of gas
0.2% volume
[9](/Research_Files/October/influence_of_feedstock_pwoder_and_cold_spray_processing_parameters_on_microstructure_and_mechanical_properties.pdf)


parameter comparison but its at 300°c so hotter than ours
The powder feed rate for atomized powders and hydride de-hydride powder were 5.7 g/min and 3.5 g/min, respectively. 

Hydride de-hydride means [idk will find out soon hopefully]

[9.2](https://www.google.com/search?q=plasma+atomisation&oq=plasma+atomisation&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCggCEAAYDxgWGB4yDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyCggFEAAYgAQYogTSAQgyNjk0ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:fd3ef46b,vid:vouCR6bhCt0,st:0)plasma atomization

[9.3](/Research_Files/October/ch5_Atomization_and_Granulation.pdf) gas atomisation 

[10](/Research_Files/October/cold_gas_dynamic_manufacturing_a_non_thermal_approach_to_freeform_fabrication.pdf)

helium MPa printing system with deposition rates of 100g/min

[11](https://impact-innovations.com/en/portfolio-item/impact-powder-feeder-cold-spray/)

interesting link

[12](/Research_Files/October/powder_feeder_redesign_for_laser_assisted_cold_spray.pdf)

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

![alt text](/Research_Files/October/16x9_Fluidized.jpg)


[14](/Research_Files/October/Development_of_a_generalized_parameter_window.pdf)

Fig. 7. Critical impact velocity for a 25 lm particle calculated for different
materials with Eq. (8). The dark grey levels indicate a range of uncertainty
with respect to the range of available materials data



[15](/Research_Files/October/A_Review_of_Advances_in_Cold_Spray_Additive_Manufacturing.pdf)
AM trl tech maturity graph
has info on parameter correlation with DE and stuff like that

Table 1 lists the Vcr and Ver for the most CSAM-ed materials

Table 2. Correlation behavior among the different input/output for CS 
[!alt text](/Research_Files/October/empirical_relations_of_cold_spray_parameters.png)

[16](/Research_Files/October/Cold_spray_deposition_for_additive_manufacturing_of_freeform_structural.pdf)

300 - 400 cm^3/hr but quoted at 5-20% porosity so probably low mass (p sure not the 2kg/hr seen)

[17](https://www.nottingham.ac.uk/research/groups/cse/facilities/processing-equipment.aspx)

nottingham cold spray set up


[18](/Research_Files/October/Establishing_a_Cold_Spray_Particle_Deposition_Window_on_Polymer_Substrate.pdf)

thought it had info on hardness wrt particle diameter but keeping cos maybe useful?


[19](/Research_Files/October/Experimental_and_Numerical_Investigations_of_Titanium.pdf)

thought it had info on hardness wrt particle diameter but keeping cos maybe useful?


[20](/Research_Files/October/Cold_Spraying_of_Titanium_A_Review_of_Bonding_Mechanisms.pdf)

The cooling rate of the material decreases with increasing particle size. 
The cooling rate has to be “low enough” to promote shear instability and on the other hand, “high enough” to let the interface solidify and finish the bonding process.

The shear loading under critical conditions leads to what is termed as adiabatic shear instability where thermal softening is locally dominant over strain and strain rate hardening, which leads to a discontinuous jump in strain and temperature and breakdown of flow stresses [6]. This adiabatic shear instability phenomenon results in viscous flow of material in an outward flowing direction at temperatures close to the melting temperature of the material.


[21](/Research_Files/October/Cold_Spraying_a_materials_perspective.pdf)

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

[22](/Research_Files/October/Performance_Metric_for_Powder_Feeder_Systems_in_Additive_Manufacturing.pdf)

![alt text](/Research_Files/October/screw_feed.png)
![alt text](/Research_Files/October/wheel_feed.png)
![alt text](/Research_Files/October/disk_feed.png)

[23](/Research_Files/October/Vibratory_Powder_Feeding_for_Powder_Bed_Additive_Manufacturing_Using_Water_and_Gas_Atomized_Metal_Powders.pdf)

![alt text](/Research_Files/October/vibrational_feed.png)
![alt text](/Research_Files/October/feed_rate_with_vibrational.png)

[24](/Research_Files/October/Powder_feeding_in_a_powder_engine_under_different_gas_solid_ratios.pdf)

![alt text](/Research_Files/October/fluidising_feed_system.png)

[25](https://www.parkerionics.com/powder-coating-equipment/powder-handling-equipment/auger-feed--ace-feed--system_pt30.html)

![alt text](/Research_Files/October/auger.jpg)

[26](/Research_Files/November/A_gravity-independent_powder-based_additive_manufacturing_process.pdf)




not convinced that screw feeding could work in microgravity so simulated a storage cavity coming off from the nozzle line and images are in /Research_Files/November/Starccm_images

chris cantwell ask about how to simulate it (24/11/24 email sent)

looked at some papers to figure out how the simulations are done

[27](/Research_Files/November/CFD_modelling_of_powder_flow_in_a_continuous_horizontal_mixer.pdf)

[27](/Research_Files/November/CFD-DEM_model_of_a_cold_plasma_assisted_fluidized_bed_powder_coating_process.pdf)



this was acc useful
[28](/Research_Files/November/discrete-particle-simulation-of-particle-fluid-flow-model-formulations-and-their-applicability.pdf)


to start i want to simulate a geometry using ansys as it claims to be able to do this

to get the geometry i want to use nominal sizes to reduce cost
found pipe that seems close or atleast a good start that is OuterDiamter = 152.4mm and thickness 3.5mm
this link has thickness 6.25mm which is larger than simulated but idk where the 3.5mm was found and can only find 3.25
https://www.aluminium-online.co.uk/product-category/aluminium-tube/aluminium-round-tube/?filter_diameter=152-4mm-6&srsltid=AfmBOooBOb9tkRpl-M447nQHUXg1aj7u2ifmwgI266YiS4VFWTNPvhYZ 
ran sims to see if this is safe in the 2 load cases 0bar inside, 1bar outside and 10bar inside and 0bar outside

the results can be seen of 0bar inside here
![alt text](/Research_Files/November/Capture4.PNG)
this was buckling using
    YoungsModulus = 68900
    PoissonsRatio = 0.033
    Height = 500
    pressure on outside going in = 0.1

    greatest deflection is 1mm from the results suggesting with end caps we wouldnt expect buckling
![alt text](/Research_Files/November/Capture8.PNG)
pressure of 1bar is put on the outside
highest stress is 0.01 of yield stress so also looks good

results of 10bar inside
![alt text](/Research_Files/November/Capture7.PNG)
the load case where we are filling the hopper even to 10 bar it is 0.1 of yield

all look good if not a little low (maybe did something wrong)

moving on to cadding up a geometry taking heavy inspiration from the permiable piston/image below source [3]

[29](https://www.youtube.com/watch?v=7cW08f7ugkU)
different types of behaviour you can get in fluidised powder bed

started ansys analysis of system. wanted to begin with /Research_Files/December/fluidising_bed_simulation but doing it 3d for the first time using ansys was too complex

rolled back the complexity to the /Research_Files/December/2D_fluidisation_simulation

this is a cross section of the assembly, first want to start with the piston face as an outlet for the gas and the powder inlet as an inlet for gas ( with the walls and the actual gas inlet and outlet parts of the funnel being modelled as walls )

the simulation is all settings default besides 
    transient time for the solver, 
    multiphase is on using eulerian model 
    fluid is default air and a second fluid is generated called al_powder rho = 2700 nu = 1.7894e-05
    secondary phase was set to granular with 40um size
    granular viscosity was set to syamlal-obrien
    all bcs were set to wall besides
    piston_face was set to pressure outlet at 0Pa and operating condition of gravity in the -y direction
    powder_outlet was velocity inlet of 0.31m/s for the gas only
    transient formula is second order implicit


    this simulation gave a result that seems reasonable, had difficulty saving the sim as a video but think the anumation on ansys works

next is trying to get the 3d version working

want to do some investigation through simulation as to what sensors i would need where when trying to build the control system for it
then validate that the simulations are atleast somewhaty representative of the real system through a certain set of tests to be prescribed

going to run with pneumatic actuation of the piston and then at a later date look at permiable

need to look into vacuum grease for o-ring 
need to look into outgassing of material for an o-ring


for 3d sim most is the same besides
    gas_inlet and gas_outlet are pressure inlet and outlet respectively where inlet pressure is 6bar and outlet is 0
    powder_outlet is pressure outlet at 3bar
    powder to gas volume ratio im taking at 0.5% from [8]


have two directions, 
    compare and contrast through simulations the current design and the old design and try and show how it wouldnt work
    start with current design, assume it works and then run with it and make it
        downfall for this approach is why this architecture specifically and the project doesnt care about what is testable. (it isnt a valid reason to chose this device solely based on testability)

old design thoughts
    im microgravity can the powder floating be controlled well enough, thing w fuel where it floats somewhere
    does it work well or at all in microgravity and prove exactly why not


got image of old design, bottom inlet is for gas to fluidise, top inlet touching the mesh is for fluidised powder to flow out of and higher inlet is for venting

to try and see if the simulations are valid im going to try and match what the final experiment was with the current hopper geometry

[30](https://met3dp.com/product/ti6al4v-powder/)
apparent density of ti64 powder is 60% of its regular density given as 4.43 g/cc in the above reference so 2.66 will be used

the simulation is all settings default besides 
    transient time for the solver, 
    multiphase is on using eulerian model 
    fluid is default air and a second fluid is generated called ti-64-powder rho = 2660 nu = 1.7894e-05
    secondary phase was set to granular with 40um size
    granular viscosity was set to syamlal-obrien
    all bcs were set to wall besides
    gas inlet was set to 5bar
    wire_mesh was set to a wall and had specified shear of 0,0 for air and no-slip for the powder 
    powder_outlet was set to pressure outlet at 0Pa and operating condition of gravity in the -y direction
    transient formula is second order implicit

hitting negative value of d1 for symalia-param for drag for particles so going to investigate
syamlal-obrien model is for estimating drag between phases, syamlal-obrien-para is to be able to finetune the parameters to avoid the tendency to over/underestimate bed expansion [https://ansyshelp.ansys.com/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug_sec_mphase_using_steps_eulerian.html%23flu_ug_sec_eulermp_using_drag]

ran at 5 bar pressure differential trying to use the mesh, mesh didnt allow gas through so changed the mesh to be just the bottom of the mesh is the filter that the powder would sit on
ran again with a 5 bar pressure differential with roughly 8000 cells, very weird result and saved as 5_bar_pressure_differential.mpeg
changed to 5bar in and 4bar at the pressure outlet but still had a weird animation so trying 4.5bar one end 5 bar another and then after finer mesh
the other change is the previous 2 animations use a 1 in 5 frames saved so the first 0.005s are very fast. I will change the time step to 0.0005 instead of 0.001 and then save every 2 frames not five to check time influence

getting much more standard results with 0.5bar pressure differential and smaller time step. changing to 0.1bar differential to see if i can get something representative in 2D

realised i was initialising at 0bar in the chambar and that initial rush of pressure coming in lead to the strange result

multiphase flow, decided maybe we dont understand the fundamental mechanism for fludiising besides
journals to look at is
    journal of fluids
    multiphase flow
    chemeng fluidising

whole point is looking for how powder control rate change
does rampinig add additional functionality
does it have start stop capabilities
does duration of simulation match what we have seen

follow up with ruth to check if the powder was disposed (phd student )


trying to do 3d sim now
running into some issues and the sim is much much slower than the 2d which is to be expected.
![alt text](/Research_Files/January/scaled_residuals_showing_data_before_crash.png)
initial guess is that with the increase in dimension the numerical stability of the sim has decreased, i will drop the time step from 0.001 to 0.0001 and if still unstable i will look into learning how to refine a mesh. current sim is with 499000pa on one side and 500000pa on the mesh

while using pressure inlet i am getting weird behaviour where the powder seemingly falls out of the bottom bc. Seen in (/Research_Files/January/0p01_diff_3d_w_mesh_refinement.mpeg) so am trying to switch to mass flow rate boundary condition

assuming the chokepoint is the pipe at the outlet and using that to size the mass flow rate of gas
using a 10mm diameter pipe and incompressibility assumptions
(taking density as 1.225kg/m^3 as thats what is being used at the moment in the sim)
    V = root(2 * pressure_diff / rho) = root(2 * 0.01*10^5 / 1.225) = 1632

since V is super sonic for previous calculations I will increase inlet pressure to 499900 (from 499000) as this may have been causing strange behaviour

from the incompressibility calculations (i know M>0.3 but will review this later) I will assume that a mass flow rate of 0.01 * 0.01 * π * 163 * 1.225 = 0.0627kg/s

this mass flow rate caused it to reach millions of bar in the chamber therefore i will retry the calculation guessing values of mass flow rate and then trying to reach a chamber pressure of 5 bar

upon looking back and to make sure i dont forget
the ###fixed_0p01_bar_pressure### simulations were the 2d ones still and seemed to show different behaviour than the most recent. this could be because they still didnt have mass flow rate bc at the bottom so the powder could leak out
the ###0p01 diff 3d w mesh refinement### was done as the large mesh was too slow especially at the time steps required for numerical stability being 0.001s
the next sim produced in the investigation were the ###pressure/powder of 3d working sim###. these had normal gravity and accounted for the fact i wanted the bottom bc to not let powder through. this looks close to what we would expect other than the mass flow rate of the powder looks considerably higher than i would expect
the most recent set of simulations were ###0 grav 5bar initial pressure### and ###0 grav 4bar initial pressure###. I expected that the starting pressure within the tank would affect the initial velocity of the powder and push it upwards in the tank away from the powder outlet pipe. this didnt seem to happen which could be because the powder doesnt have enough time to accellerate the particles before it normalises the pressure in the tank as from the pressure plots after 0.005s it looked like the pressure had reached the 5.05ish bar it remained at for the rest of the sim. however this could also be because there isnt enough coupling behaviour between the powder and particles. if the particles dont cause the pressure gradient we would expect to see over a fluidising bed then there will be no buoyancy force which is very important in the calculations for particle suspension.

a final simulation is running where the powder starts at the middle to verify that this would even be a problem in the first place but has not yet finished




going onto research again. I am looking at propellant management devices as they are analogous to this situation. 
(https://en.wikipedia.org/wiki/Propellant_management_device)
[31](/Research_Files/January/A_Detailed_Historical_Review_of_Propellant_Management.pdf)
this also outlines the different usecases. it seems that all pmd that do not use surface tension use some kind of piston, bladder or diaphragms.


talk to caitlin and get access to workstation with good fluent and has cpu and gpu 4070 12th gen cpu
research software for fluent

ajit seems convinced that a new design is needed so realistically should start with that ASAP and wrap up the other things at another date
things to wrap up
    mesh convergence on the specific study
    investigate if the gas is being adequately affected by the powder as l.g. gibilaro says there should always be a pressure drop across the fluid but this isnt seen in current simulations
    simulate powder dropping then being fluidised and dispensed (from /jan/configuration that demands pms.png)


for designing the tank

https://www.halfcatrocketry.com/
useful link on rocketry and a little on piston tanks


from meeting with ajit

    what modifications to make to the old set up could be somethign i outline as future work but right now i should follow the avenue that has the most promising results, that being the 2 new designs

    currently have cadded a possible solution following [!alt text](/Research_Files/October/gas_permeable_piston.png) 
    other possible solution follows [!alt text](/Research_Files/October/fluidised_design.png)

    in the meeting we discovered that i dont really understand the underlying physics behind it. my working theory is:
        powder bed will expand with the flow of air through the powder.
        the piston will push down on this expanded powder to contain it but not compact it
        this will give a regime of reliably fluidised powder that will be close to fully entrained into the flow and therefore easy to control

    next steps are then
        figure out how much the bed expands,
        figure out how much force the piston should put on it,
        figure out what geometry will get a pressure drop across the piston faces of that force value
        figure out if this is a valid model

in trying to find info about fluidisation i found [32](/Research_Files/February/Operation_of_magnetically_assisted_fluidized_beds_in_microgravity.pdf)
maybe i could think of the other restoring force as magnetic

do deep dive into Powder_feeding_enhancement_of_powder_propellant_supply_system_by_using_gas_permeable_piston and maybe look at their experimental results

try simulate what they got

reading through the paper, first thing to check is that a gear piston does cause a drop in pressure across the two faces of the piston and try and generate some kind of inlet pressure vs outlet pressure vs drop across the faces relation


[33](/Research_Files/February/Experimental_investigation_on_mass_flow_rate_measurements_and_feeding_characteristics_of_powder_at_high_pressure.pdf)
while doing these sims i am finding more information about the empriical relations. [33] suggests that mass flow rate is a linear scale of equations (5), (6) & (7)

also martin reviewed my cad. the width of the tank is way too large. start with mass i aim to be able to move and atleast half the width smaller. for subtractive manufacturing dont worry about making things thin.
push fit to 1/4bsp 
6mm nylon tubing
shop air and sand
for output 1/4in swagelock

https://www.metals4u.co.uk/materials/aluminium/aluminium-tube/728-p 
38.1mm radius - 1.6 thickness pi r^2  gives 0.00419 m^3/m
with ti being 2.66 g/cc => 2660kg/m
therefore 11.1454kg/m
500mm length then gives 5.6kg total but with plunger and stuff aiming for 5kg

pricing

600mm tie rods * 6 = £4.4 * 6

101.6mm cylinder * 90mm = £42.55
    50mm funnel
    10mm endcap
    20mm piston


76.2mm tube * 500mm = £9.42

1m of 6mm nylon tubing = £1.74

6mm x 1/4 bspt connector ~= £2 * 4 or 5?
https://www.advancedfluidsolutions.co.uk/6mm-x-14-bspt-male-stud-push-in-fitting-nylon-pipetube-connector-1661-p.asp 
[34](/Research_Files/February/High_Rate_Deposition_in_Cold_Spray.pdf)


post ajit meeting. looks good ajit is happy with me starting to gather experimental data

https://www.ebay.co.uk/itm/133562315642?_skw=90mm+ABS+plastic+stock&itmmeta=01JKXVFSZH8FJRBW3DSSMFHF5P&hash=item1f18ef337a%3Ag%3AmKsAAOSwuE9fnYyi&itmprp=enc%3AAQAKAAAA0FkggFvd1GGDu0w3yXCmi1elfp7ZQxan4zsUIe2pUSrFE8AAyr0deIR3xPgV1xMguzO3QZQWfHg2JJ1cqbGfN8IBjNuHPq33ilxgXZ6bObwU16URZm2fD75Kf5U65uE8TE2Q%2BYe3Sqvr3sKehyniGLlIgJS3a8XohUgfuo%2FjYnN9TOYl2mC%2B41NNvOyz7XqInCuf4%2BC9GGmCVI10vTUiY1Ja53xBLAngECdbe%2Fq1o3Bnq78r6CyCWBPIx7ydiW6hqRY%2Bg2Y%2FSGtmZB37GEZj5B0%3D%7Ctkp%3ABk9SR_Sfv7ufZQ&var=433021669627

https://www.ebay.co.uk/itm/166173980495?_skw=500mm+acrylic+tube&itmmeta=01JKXV09S24BYWGYRMQGF6NTCW&hash=item26b0bdb74f:g:ce4AAOSwDpxnq4tu&itmprp=enc%3AAQAKAAAA8FkggFvd1GGDu0w3yXCmi1fcstDfwDPvY30ozRAruwSvMRBpIKcgUPmXtkpDNmJ4T5dq8Vr9NVdnWQCc5j1IW3B49WUAKP6fugMSQTPn0OBTi1HPNJYo9PEhaDhyncE%2BUsf5BuOPJAhb4J4FiOpYOztmWych5JFCwF9Qcr%2BY3knSLDpkEdFxiUTVrRkHICENBujmqTyP1kbo1t6GUkJn0dNpJIODRRj7%2Bo6%2Bz%2BzIWj3kryPO%2BGLsupIg%2Fc0BCtWMpcXjkKJcHDYE%2BBJBOolkL4w%2FpMvY3LLgt7IRWGVxO1KmvmDRdc8LI7vAcCb1JfkEPA%3D%3D%7Ctkp%3ABk9SR9ycgbufZQ


when designing the prototype i was advised to do radial bolts.
the stress on the bolt holes was at the limit of damaging the plastic under 7 bar of presure 
/Research_Files/February/acrylic_tube_4mm_sim.png

to remedy this I will make the wholes larger decreasing the concentration of stress and epoxying in threaded inserts to make the distribution of force more uniform across the whole not just at the top edge

before testing the prototype for my report i want to see if i can get valid simulation results.
The first thing was verifying a test size for the chokepoint. 4.5mm chokepoint choked with a 1 bar pressure differential.
This is shown in
![alt text](/Research_Files/March/choke_point_investigation.png)
This was a 1 bar pressure differential from 1 bar above atmospheric to atmospheric

had a meeting with the technicians, they pointed out that 4.5mm is wider than the pipes so the choke point was changed to 3.5mm. We also discussed that the sand will sandblast the geometry so either a very hard material or replacable materials should be used like 3d printed ones

They also mentioned for a risk assessment i should either enclose the tank in a case for safety or have pressurised it to double the operating for safety. This leads me to investigate the safety factor for a 10bar pressure.

10 bar across the face of the delrin piece with the o ring results in 4289.2N
1,000,000*pi*0.0739*0.0739/4


Tank has been pressurised to 7bar absolute and sustained no damage. In the interest of getting some data and going from there, 3bar has been chosen as the operating pressure for the device.

Testing was done with the shop air line and regulating the pressure down to 3 bar. This didnt produce enough force to move the piston and the pressure reg could only maintain the 3 bar with a ball valve just after it and almost entirely closed. This shows that for the mass flow of the line, it will not choke at 3.5mm.

The set up is now going to use a 300 bar nitrogen tank to achieve the mass flow rate required to actually choke the flow through the choke point.

From the choked flow calculator (https://engineeringamp.com/piping/choked_flow) with nitrogen : {
    MW: 14.0067,
    T_c: 20 deg c,
    P_g: 300 kPa,
    P_atm: 101.325 kPa,
    z: 1,
    C_d: 0.61,
    k: 1.4,
    d_0: 3.5
}
The Mass flow rate is 13.919 kg/h of nitrogen
nitrogen is 1.205 g/L on wikipedia at 0 degrees C
This is almost 0.8 L/g so 800 L/kg
This means 11135.2 L/h or 185.6 L/m

if the chokepoint width is 3mm then the mass flow rate required is 10.226 kg/h or 136.35 L/m
2.5mm = 7.101kg/h = 94.68 L/m
2mm = 4.545 kg/h = 60.6 L/m
1.5mm = 2.556 kg/h = 34.08 L/m
1mm = 1.136 kg/h = 15.15 L/m

a wild guess using a mass flow meter that went up to 5 L/m suggests maybe the line does up to 20 L/m but this isnt enough for the application.

next steps are get access to the nitrogen bottle to test the cyclone seperator and if it is the right size for the application


Fig. 3.4 Comparison of metallic additive manufacturing processes
in May/Innovations_In Additive Manufacturing



/home/jack/Documents/FYP/Research_Files/May/in-space_manufacturing:_technologies.pdf
California-based private company Varda specializes in manufacturing pharmaceuticals in space. One of their groundbreaking advancements involves developing
single-use manufacturing satellites equipped with onboard reentry capsules. Collaborating with Rocket Lab, Varda launched their first test satellite in June 2024. These
automated manufacturing satellites aim to revolutionize pharmaceutical production,




i can control mass flow rate of powder using the force on the piston
i can control the force on the piston with the mass flow rate of air
what is the relationship between force on piston and mass flow rate?
    is it linear or dependent on something?

Is it possible to assume they are two seperate phenomenon, that being the pushing of the piston and the fluidisation of the powder? !important!!!!!!!
https://ntrs.nasa.gov/api/citations/19940017287/downloads/19940017287.pdf seems to suggest no relation between piston head pressure differential and mass flow rate







https://catalogimages.wiley.com/images/db/pdf/9780632064564.excerpt.pdf could read this to understand fluidised beds better

![alt text](./May/image.png) 4.581kg/hr from airline

loftus has some equ on flow rate and fluidisation

2 phase sim
sand as solid w density 2650kg/m^3 diameter of 0.25mm 0.6 packing density


crazy direction change after first test

(y-0.037)^2 + x^2 = 0.037^2 is the equation for the cirlce

integrate that where z = (0.074-y)*2650 will give the pressure that the sand exerts on the piston

P = rho * g * h

calculate it as though its a cylinder being 0.00430m^2 * 2650kg/m^3 = 11.4kg/m

density of the sand (as is, with packing efficincy != 1)

density of tap water at 20c = 998.23kg/m^3 (https://www.simetric.co.uk/si_water.htm)

775.4g empty
4335.5g sand
3100.0g water

3560.1g sand w/o bowl
2324.6g water w/o bowl
vol of bowl = 0.0023287m^3
density of sand = 1529kg/m^3



from tests with fixed piston, it appears that the device is only fluidising the particles close to the piston as they have a high enough velocity to do so, this causes the fluidised particles to move through a preexisting path and not fluidise the rest of the device


giving up on remeshing so mesh will just warp. Gonna try initialisation of 55% and 80mm piston vel
vel of the fluid of 0.01m/s
0.0001 ts
40 iter
2000 no ts