import gmsh
import meshio
import pyvista as pv
import numpy as np
import subprocess
import sys
import configparser


def create_channel_mesh(fileName, modelName="Channel"):
    gmsh.initialize()
    
    # Add a model
    gmsh.model.add(modelName)

    # Define points 
    p1 = gmsh.model.geo.addPoint(0, 0, 0, 1) # x y z mesh_element_size
    p2 = gmsh.model.geo.addPoint(10, 0, 0, 1)
    p3 = gmsh.model.geo.addPoint(10, 1, 0, 1)
    p4 = gmsh.model.geo.addPoint(8, 1, 0, 1)
    p5 = gmsh.model.geo.addPoint(8, 5, 0, 1) 
    p6 = gmsh.model.geo.addPoint(6, 5, 0, 1)
    p7 = gmsh.model.geo.addPoint(6, 7, 0, 1)
    p8 = gmsh.model.geo.addPoint(0, 7, 0, 1)
    p9 = gmsh.model.geo.addPoint(0, 3, 0, 1) 
    p10 = gmsh.model.geo.addPoint(6, 3, 0, 1)
    p11 = gmsh.model.geo.addPoint(6, 4, 0, 1)
    p12 = gmsh.model.geo.addPoint(7, 4, 0, 1)
    p13 = gmsh.model.geo.addPoint(7, 1, 0, 1) 
    p14 = gmsh.model.geo.addPoint(0, 1, 0, 1)

    # Define lines
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p5)
    l5 = gmsh.model.geo.addLine(p5, p6)
    l6 = gmsh.model.geo.addLine(p6, p7)
    l7 = gmsh.model.geo.addLine(p7, p8)
    l8 = gmsh.model.geo.addLine(p8, p9)
    l9 = gmsh.model.geo.addLine(p9, p10)
    l10 = gmsh.model.geo.addLine(p10, p11)
    l11 = gmsh.model.geo.addLine(p11, p12)
    l12 = gmsh.model.geo.addLine(p12, p13)
    l13 = gmsh.model.geo.addLine(p13, p14) 
    l14 = gmsh.model.geo.addLine(p14, p1) 

    # Create a line loop and a plane surface
    loop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14])
    surface = gmsh.model.geo.addPlaneSurface([loop])

    # Synchronize to reflect the changes
    gmsh.model.geo.synchronize()

    # Define physical groups for inlet, outlet, and wall
    gmsh.model.addPhysicalGroup(1, [l14], tag=1, name="inlet")  # Inlet: bottom edge (l1)
    gmsh.model.addPhysicalGroup(1, [l2], tag=2, name="outlet")  # Outlet: top edge (l3)
    gmsh.model.addPhysicalGroup(1, [l1, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13], tag=3, name="wall")  # Wall: left and right edges (l2 and l4)

    # Add physical groups for the surface if needed
    gmsh.model.addPhysicalGroup(2, [surface], tag=4, name="fluid")  # Surface group (for reference)

    # Generate the 2D triangular mesh
    gmsh.model.mesh.generate(2)

    # Set output format to ASCII (Version 2)
    gmsh.option.setNumber("Mesh.Binary", 0)  # Ensures ASCII output
    gmsh.option.setNumber("Mesh.MshFileVersion", 2.0)  # Use Version 2

    # Save the mesh
    gmsh.write(fileName)

    # Finalize Gmsh
    gmsh.finalize()

def display_mesh(fileName):
    # Read the mesh
    mesh = meshio.read(fileName)

    # Extract points and triangle cells for 2D visualization
    points = mesh.points
    cells = mesh.cells_dict.get("triangle")
    
    if cells is None:
        raise ValueError("No triangle cells found in the mesh.")

    # Convert the triangle cells to PyVista's UnstructuredGrid format
    num_cells = cells.shape[0]
    cell_types = [5] * num_cells  # '5' is the VTK cell type for triangles
    cell_data = np.hstack([[3, *cell] for cell in cells])  # '3' for 3 nodes per triangle

    # Create UnstructuredGrid object in PyVista
    pv_mesh = pv.UnstructuredGrid(cell_data, cell_types, points)

    # Plot the mesh
    plotter = pv.Plotter()
    plotter.add_mesh(pv_mesh, show_edges=True, color="lightblue")
    plotter.show()

def convert_mesh_to_pyfr(msh_file, pyfr_file):
    # msh_file = "./Research_Files/November/" + msh_file
    # pyfr_file = "./Research_Files/November/" + pyfr_file
    command = ["pyfr", "import", msh_file, pyfr_file]
    subprocess.run(command, check=True)

def write_config_to_ini(input_file, output_file):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Set the configuration options for PyFR
    config['Mesh'] = {
        'meshfile': input_file  # The mesh file (.pyfrm)
    }
    
    config['BoundaryConditions'] = {
        'inlet_type': 'pressure-inlet',  # Example boundary condition type for inlet
        'inlet_value': '6.0',            # Example boundary condition value for inlet
        'outlet_type': 'pressure-outlet', # Example boundary condition type for outlet
        'outlet_value': '0.0',           # Example boundary condition value for outlet
        'wall_type': 'no-slip',          # Example boundary condition for walls
        'wall_value': '0.0'              # No-slip condition value for walls
    }
    
    config['TimeStepping'] = {
        'method': 'RK4',                # Runge-Kutta time-stepping method
        'timestep': '1e-3',             # Time step size
        'total_steps': '10000'          # Total number of time steps
    }
    
    config['Solver'] = {
        'linear_solver': 'GMRES',       # Linear solver to use
        'preconditioner': 'ILU'        # Preconditioner for the solver
    }

    # Write the configuration to the specified .ini file
    with open(output_file, 'w') as configfile:
        config.write(configfile)

    print(f"Configuration written to {output_file}")

def run_pyfr_simulation(msh_file, cfg_dir, backend="openmp"):
    # Define the pyfr solve command
    command = ["pyfr", "run", "--backend", backend, msh_file, cfg_dir]
    
    # Run the command using subprocess
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Simulation completed successfully!\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print("Error occurred during simulation:")
        print("Standard Output:")
        print(e.stdout)  # This captures any output that was printed to stdout
        print("Standard Error:")
        print(e.stderr)  # This captures any error messages that were printed to stderr

        # Add more context about the failure
        print(f"Command that failed: {' '.join(command)}")
        print(f"Exit code: {e.returncode}")
        
        # Optionally, you can log the complete output (for debugging purposes)
        with open('simulation_error.log', 'w') as log_file:
            log_file.write(f"Command: {' '.join(command)}\n")
            log_file.write(f"Exit code: {e.returncode}\n")
            log_file.write("Standard Output:\n")
            log_file.write(e.stdout)
            log_file.write("Standard Error:\n")
            log_file.write(e.stderr)

        # Re-raise the error if you want to stop execution
        raise
    
fileNameMsh = "./Research_Files/November/channel.msh"
fileNamePyfrm = "./Research_Files/November/channel.pyfrm"
fileNameCfg = "./Research_Files/November/config.ini"

create_channel_mesh(fileNameMsh)
display_mesh(fileNameMsh)
convert_mesh_to_pyfr(fileNameMsh, fileNamePyfrm)
        
write_config_to_ini(fileNamePyfrm, fileNameCfg)
# run_pyfr_simulation(fileNamePyfrm, fileNameCfg)

