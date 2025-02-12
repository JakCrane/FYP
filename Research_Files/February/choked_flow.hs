module Main where

main :: IO ()
main = do
  -- file to find values for choked flow pressure differential
  -- assuming uniform mixture of gas and powder

  let density_of_gas       = 1.225   -- air
      gas_constant         = 287.05  -- air
      
      -- 1442 kg/m^3 https://blog.certifiedmtp.com/density-of-sand-a-guide...
      density_of_powder    = 1442    -- sand

      -- from [34] 45g/min powder mass flow rate with loading rate of 0.05
      pressure_of_tank     = 500000  -- p_fc
      choke_area           = 0.0001  -- A (assumed 1 square cm for now)

      -- Define mass_ratio_of_powder_to_gas before the fractions:
      mass_ratio_of_powder_to_gas = 0.05  -- n (mass flow rate ratio, "loading rate")

      density_ratio_of_powder_to_gas =
        density_of_powder / density_of_gas  -- m

      mass_fraction_of_particle =
        mass_ratio_of_powder_to_gas / (1 + mass_ratio_of_powder_to_gas)  -- phi

      volume_fraction_of_particle =
        mass_ratio_of_powder_to_gas
          / (mass_ratio_of_powder_to_gas + density_ratio_of_powder_to_gas)  -- epsilon_p

      mixing_constant =
        gas_constant
          * (1 - mass_fraction_of_particle)
          / (1 - volume_fraction_of_particle)  -- R_mix

      temperature = 288.2  -- T (assuming Kelvin)
      k           = 1      -- "const"?

      -- m_dot_mixture calculation using sqrt from Prelude
      m_dot_mixture =
        k
          * pressure_of_tank
          * choke_area
          / sqrt (mixing_constant * temperature)

  -- Print the result
  print m_dot_mixture
