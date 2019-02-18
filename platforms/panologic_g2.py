from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform


_io = [
    ("clk125", 0, Pins("Y13"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("B8"), IOStandard("LVCMOS33"),
                  Misc("SLEW=FAST")),
        Subsignal("rx", Pins("A8"), IOStandard("LVCMOS33"),
                  Misc("SLEW=FAST"))),

    ("spiflash", 0,
        #Subsignal("cs_n", Pins("V3")),
        #Subsignal("clk", Pins("R15")),
        #Subsignal("mosi", Pins("T13")),
        #Subsignal("miso", Pins("R13"), Misc("PULLUP")),
        Subsignal("cs_n", Pins("T5")), #IO_L65N_CSO_B_2
        Subsignal("clk", Pins("Y21")), #IO_L1P_CCLK_2
        Subsignal("mosi", Pins("AB20")), #IO_L3N_MOSI_CSI_B_MISO0_2
        Subsignal("miso", Pins("AA20"), Misc("PULLUP")), #IO_L3P_D0_DIN_MISO_MISO1_2
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")),





## DDR2
    # 128Mbyte DDR2 16-bit wide data @ 800MHz
    # Older boards - MT47H64M16HR-25E - DDR2 - 2.5ns @ CL = 5 (DDR2-800)
    # Newer boards - MIRA P3R1GE3EGF G8E DDR2 -
    #
    # The interface supports SSTL18 signaling. Address and control signals
    # are terminated through 47-ohm resistors to a 0.9V VTT, and data
    # signals use the On-Die-Termination (ODT) feature of the DDR2 chip.
    #
    # When generating a MIG core for the MIRA part, selecting the
    # “EDE1116AXXX-8E” device will result in the correct timing parameters
    # being set. When generating a component for the Micron part, it can be
    # selected by name within the wizard. The part loaded on your Atlys can
    # be determined by examining the print on the DDR2 component (IC13).
    #
    # NET "DDR2CLK0"   LOC = "G3"; # Bank = 3, Pin name = IO_L46P_M3CLK,               Sch name = DDR-CK_P
    # NET "DDR2CLK1"   LOC = "G1"; # Bank = 3, Pin name = IO_L46N_M3CLKN,              Sch name = DDR-CK_N
    ("ddram_clock", 0,
        #Subsignal("p", Pins("G3")),
        #Subsignal("n", Pins("G1")),
        #IOStandard("DIFF_SSTL18_II"), Misc("IN_TERM=NONE")
        #NET "DDR2A_CK_P" LOC = H20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_CK_N" LOC = J19 | IOSTANDARD = LVCMOS18;
        Subsignal("p", Pins("H20")),
        Subsignal("n", Pins("J19")),
        IOStandard("DIFF_SSTL18_II"), Misc("IN_TERM=NONE")
    ),
    ("ddram", 0,
        # NET "DDR2CKE"    LOC = "H7"; # Bank = 3, Pin name = IO_L53P_M3CKE,           Sch name = DDR-CKE
        #Subsignal("cke", Pins("H7"), IOStandard("SSTL18_II")),
        #NET "DDR2A_CKE" LOC = D21 | IOSTANDARD = LVCMOS18;
        Subsignal("cke", Pins("D21"), IOStandard("SSTL18_II")),
        
        # NET "DDR2RASN"   LOC = "L5"; # Bank = 3, Pin name = IO_L43P_GCLK23_M3RASN,   Sch name = DDR-RAS
        #Subsignal("ras_n", Pins("L5"), IOStandard("SSTL18_II")),
        #NET "DDR2A_RAS_L" LOC = H21 | IOSTANDARD = LVCMOS18;
        Subsignal("ras_n", Pins("H21"), IOStandard("SSTL18_II")),
        
        # NET "DDR2CASN"   LOC = "K5"; # Bank = 3, Pin name = IO_L43N_GCLK22_IRDY2_M3CASN, Sch name = DDR-CAS
        #Subsignal("cas_n", Pins("K5"), IOStandard("SSTL18_II")),
        #NET "DDR2A_CAS_L" LOC = H22 | IOSTANDARD = LVCMOS18;
        Subsignal("cas_n", Pins("H22"), IOStandard("SSTL18_II")),
        
        # NET "DDR2WEN"    LOC = "E3"; # Bank = 3, Pin name = IO_L50P_M3WE,         Sch name = DDR-WE
        #Subsignal("we_n", Pins("E3"), IOStandard("SSTL18_II")),
        #NET "DDR2A_WE_L" LOC = H19 | IOSTANDARD = LVCMOS18;
        Subsignal("we_n", Pins("H19"), IOStandard("SSTL18_II")),
        

        # NET "DDR2BA0"    LOC = "F2"; # Bank = 3, Pin name = IO_L48P_M3BA0,        Sch name = DDR-BA0
        # NET "DDR2BA1"    LOC = "F1"; # Bank = 3, Pin name = IO_L48N_M3BA1,        Sch name = DDR-BA1
        # NET "DDR2BA2"    LOC = "E1"; # Bank = 3, Pin name = IO_L50N_M3BA2,        Sch name = DDR-BA2

        #Subsignal("ba", Pins("F2 F1 E1"), IOStandard("SSTL18_II")),
       
        #NET "DDR2A_BA[2]" LOC = H18 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_BA[1]" LOC = K17 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_BA[0]" LOC = J17 | IOSTANDARD = LVCMOS18;
        
        Subsignal("ba", Pins("H18 K17 J17"), IOStandard("SSTL18_II")),

        # NET "DDR2A0"     LOC = "J7"; # Bank = 3, Pin name = IO_L47P_M3A0,         Sch name = DDR-A0
        # NET "DDR2A1"     LOC = "J6"; # Bank = 3, Pin name = IO_L47N_M3A1,         Sch name = DDR-A1
        # NET "DDR2A2"     LOC = "H5"; # Bank = 3, Pin name = IO_L49N_M3A2,         Sch name = DDR-A2
        # NET "DDR2A3"     LOC = "L7"; # Bank = 3, Pin name = IO_L45P_M3A3,         Sch name = DDR-A3
        # NET "DDR2A4"     LOC = "F3"; # Bank = 3, Pin name = IO_L51N_M3A4,         Sch name = DDR-A4
        # NET "DDR2A5"     LOC = "H4"; # Bank = 3, Pin name = IO_L44P_GCLK21_M3A5,  Sch name = DDR-A5
        # NET "DDR2A6"     LOC = "H3"; # Bank = 3, Pin name = IO_L44N_GCLK20_M3A6,  Sch name = DDR-A6
        # NET "DDR2A7"     LOC = "H6"; # Bank = 3, Pin name = IO_L49P_M3A7,         Sch name = DDR-A7
        # NET "DDR2A8"     LOC = "D2"; # Bank = 3, Pin name = IO_L52P_M3A8,         Sch name = DDR-A8
        # NET "DDR2A9"     LOC = "D1"; # Bank = 3, Pin name = IO_L52N_M3A9,         Sch name = DDR-A9
        # NET "DDR2A10"    LOC = "F4"; # Bank = 3, Pin name = IO_L51P_M3A10,        Sch name = DDR-A10
        # NET "DDR2A11"    LOC = "D3"; # Bank = 3, Pin name = IO_L54N_M3A11,        Sch name = DDR-A11
        # NET "DDR2A12"    LOC = "G6"; # Bank = 3, Pin name = IO_L53N_M3A12,        Sch name = DDR-A12
        #Subsignal("a", Pins("J7 J6 H5 L7 F3 H4 H3 H6 D2 D1 F4 D3 G6"), IOStandard("SSTL18_II")),
        
        #NET "DDR2A_A[12]" LOC = D22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[11]" LOC = F19 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[10]" LOC = G19 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[9]" LOC = C22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[8]" LOC = C20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[7]" LOC = E20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[6]" LOC = K19 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[5]" LOC = K20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[4]" LOC = F20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[3]" LOC = G20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[2]" LOC = E22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[1]" LOC = F22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_A[0]" LOC = F21 | IOSTANDARD = LVCMOS18;
        Subsignal("a", Pins("F21 F22 E22 G20 F20 K20 K19 E20 C20 C22 G19 F19 D2"), IOStandard("SSTL18_II")),

        # NET "DDR2DQ0"    LOC = "L2"; # Bank = 3, Pin name = IO_L37P_M3DQ0,        Sch name = DDR-DQ0
        # NET "DDR2DQ1"    LOC = "L1"; # Bank = 3, Pin name = IO_L37N_M3DQ1,        Sch name = DDR-DQ1
        # NET "DDR2DQ2"    LOC = "K2"; # Bank = 3, Pin name = IO_L38P_M3DQ2,        Sch name = DDR-DQ2
        # NET "DDR2DQ3"    LOC = "K1"; # Bank = 3, Pin name = IO_L38N_M3DQ3,        Sch name = DDR-DQ3
        # NET "DDR2DQ4"    LOC = "H2"; # Bank = 3, Pin name = IO_L41P_GCLK27_M3DQ4, Sch name = DDR-DQ4
        # NET "DDR2DQ5"    LOC = "H1"; # Bank = 3, Pin name = IO_L41N_GCLK26_M3DQ5, Sch name = DDR-DQ5
        # NET "DDR2DQ6"    LOC = "J3"; # Bank = 3, Pin name = IO_L40P_M3DQ6,        Sch name = DDR-DQ6
        # NET "DDR2DQ7"    LOC = "J1"; # Bank = 3, Pin name = IO_L40N_M3DQ7,        Sch name = DDR-DQ7
        # NET "DDR2DQ8"    LOC = "M3"; # Bank = 3, Pin name = IO_L36P_M3DQ8,        Sch name = DDR-DQ8
        # NET "DDR2DQ9"    LOC = "M1"; # Bank = 3, Pin name = IO_L36N_M3DQ9,        Sch name = DDR-DQ9
        # NET "DDR2DQ10"   LOC = "N2"; # Bank = 3, Pin name = IO_L35P_M3DQ10,       Sch name = DDR-DQ10
        # NET "DDR2DQ11"   LOC = "N1"; # Bank = 3, Pin name = IO_L35N_M3DQ11,       Sch name = DDR-DQ11
        # NET "DDR2DQ12"   LOC = "T2"; # Bank = 3, Pin name = IO_L33P_M3DQ12,       Sch name = DDR-DQ12
        # NET "DDR2DQ13"   LOC = "T1"; # Bank = 3, Pin name = IO_L33N_M3DQ13,       Sch name = DDR-DQ13
        # NET "DDR2DQ14"   LOC = "U2"; # Bank = 3, Pin name = IO_L32P_M3DQ14,       Sch name = DDR-DQ14
        # NET "DDR2DQ15"   LOC = "U1"; # Bank = 3, Pin name = IO_L32N_M3DQ15,       Sch name = DDR-DQ15
        #Subsignal("dq", Pins(
        #            "L2 L1 K2 K1 H2 H1 J3 J1",
        #            "M3 M1 N2 N1 T2 T1 U2 U1"), IOStandard("SSTL18_II")),
        #NET "DDR2A_D[0]" LOC = N20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[1]" LOC = N22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[2]" LOC = M21 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[3]" LOC = M22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[4]" LOC = J20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[5]" LOC = J22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[6]" LOC = K21 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[7]" LOC = K22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[8]" LOC = P21 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[9]" LOC = P22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[10]" LOC = R20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[11]" LOC = R22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[12]" LOC = U20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[13]" LOC = U22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[14]" LOC = V21 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_D[15]" LOC = V22 | IOSTANDARD = LVCMOS18;
        
        Subsignal("dq", Pins(
                    "N20 N22 M21 M22 J20 J22 K21 K22",
                    "P21 P22 R20 R22 U20 U22 V21 V22"), IOStandard("SSTL18_II")),
        # U == Upper, L == Lower
        # NET "DDR2UDQS"   LOC="P2"; # Bank = 3, Pin name = IO_L34P_M3UDQS,         Sch name = DDR-UDQS_P
        # NET "DDR2UDQSN"  LOC="P1"; # Bank = 3, Pin name = IO_L34N_M3UDQSN,        Sch name = DDR-UDQS_N
        # NET "DDR2LDQS"   LOC="L4"; # Bank = 3, Pin name = IO_L39P_M3LDQS,         Sch name = DDR-LDQS_P
        # NET "DDR2LDQSN"  LOC="L3"; # Bank = 3, Pin name = IO_L39N_M3LDQSN,        Sch name = DDR-LDQS_N
        #Subsignal("dqs", Pins("P2 L4"), IOStandard("DIFF_SSTL18_II")),
        #Subsignal("dqs_n", Pins("P1 L3"), IOStandard("DIFF_SSTL18_II")),
        
        #NET "DDR2A_LDQS_P" LOC = L20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_LDQS_N" LOC = L22 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_UDQS_P" LOC = T21 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_UDQS_N" LOC = T22 | IOSTANDARD = LVCMOS18;
        Subsignal("dqs", Pins("T21 L20"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("T22 L22"), IOStandard("DIFF_SSTL18_II")),
        
        # NET "DDR2UDM"    LOC="K4"; # Bank = 3, Pin name = IO_L42P_GCLK25_TRDY2_M3UDM, Sch name = DDR-UDM
        # NET "DDR2LDM"    LOC="K3"; # Bank = 3, Pin name = IO_L42N_GCLK24_M3LDM,   Sch name = DDR-LDM
        #Subsignal("dm", Pins("K4 K3"), IOStandard("SSTL18_II")),
        #NET "DDR2A_UDM" LOC = M20 | IOSTANDARD = LVCMOS18;
        #NET "DDR2A_LDM" LOC = L19 | IOSTANDARD = LVCMOS18;
        Subsignal("dm", Pins("M20 L19"), IOStandard("SSTL18_II")),
        
        #Subsignal("clk_p", Pins("H20"), IOStandard("DIFF_SSTL18_II")),
        #Subsignal("clk_n", Pins("J19"), IOStandard("DIFF_SSTL18_II")),
        
        # NET "DDR2ODT"    LOC="K6"; # Bank = 3, Pin name = IO_L45N_M3ODT,          Sch name = DDR-ODT
        #Subsignal("odt", Pins("K6"), IOStandard("SSTL18_II"))
        #NET "DDR2A_ODT" LOC = G22 | IOSTANDARD = LVCMOS18;
        Subsignal("odt", Pins("G22"), IOStandard("SSTL18_II"))
        

    ),

      
    ("ddram_clock", 1,
        #Subsignal("p", Pins("G3")),
        #Subsignal("n", Pins("G1")),
        #IOStandard("DIFF_SSTL18_II"), Misc("IN_TERM=NONE")
        #NET "DDR2B_CK_P" LOC = H4 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_CK_N" LOC = H3 | IOSTANDARD = LVCMOS18;
        Subsignal("p", Pins("H4")),
        Subsignal("n", Pins("H3")),
        IOStandard("DIFF_SSTL18_II"), Misc("IN_TERM=NONE")
    ),
    ("ddram", 1,
        # NET "DDR2CKE"    LOC = "H7"; # Bank = 3, Pin name = IO_L53P_M3CKE,           Sch name = DDR-CKE
        #Subsignal("cke", Pins("H7"), IOStandard("SSTL18_II")),
        #NET "DDR2B_CKE" LOC = D2 | IOSTANDARD = LVCMOS18;
        Subsignal("cke", Pins("D2"), IOStandard("SSTL18_II")),
        
        # NET "DDR2RASN"   LOC = "L5"; # Bank = 3, Pin name = IO_L43P_GCLK23_M3RASN,   Sch name = DDR-RAS
        #Subsignal("ras_n", Pins("L5"), IOStandard("SSTL18_II")),
        #NET "DDR2B_RAS_L" LOC = K5 | IOSTANDARD = LVCMOS18;
        Subsignal("ras_n", Pins("K5"), IOStandard("SSTL18_II")),
        
        # NET "DDR2CASN"   LOC = "K5"; # Bank = 3, Pin name = IO_L43N_GCLK22_IRDY2_M3CASN, Sch name = DDR-CAS
        #Subsignal("cas_n", Pins("K5"), IOStandard("SSTL18_II")),
        #NET "DDR2B_CAS_L" LOC = K4 | IOSTANDARD = LVCMOS18;
        Subsignal("cas_n", Pins("K4"), IOStandard("SSTL18_II")),
        
        # NET "DDR2WEN"    LOC = "E3"; # Bank = 3, Pin name = IO_L50P_M3WE,         Sch name = DDR-WE
        #Subsignal("we_n", Pins("E3"), IOStandard("SSTL18_II")),
        #NET "DDR2B_WE_L" LOC = F2 | IOSTANDARD = LVCMOS18; 
        Subsignal("we_n", Pins("F2"), IOStandard("SSTL18_II")),
        

        # NET "DDR2BA0"    LOC = "F2"; # Bank = 3, Pin name = IO_L48P_M3BA0,        Sch name = DDR-BA0
        # NET "DDR2BA1"    LOC = "F1"; # Bank = 3, Pin name = IO_L48N_M3BA1,        Sch name = DDR-BA1
        # NET "DDR2BA2"    LOC = "E1"; # Bank = 3, Pin name = IO_L50N_M3BA2,        Sch name = DDR-BA2

        #Subsignal("ba", Pins("F2 F1 E1"), IOStandard("SSTL18_II")),
       
        #NET "DDR2B_BA[2]" LOC = F1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_BA[1]" LOC = G1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_BA[0]" LOC = G3 | IOSTANDARD = LVCMOS18;
            
        Subsignal("ba", Pins("F1 G1 G3"), IOStandard("SSTL18_II")),

        # NET "DDR2A0"     LOC = "J7"; # Bank = 3, Pin name = IO_L47P_M3A0,         Sch name = DDR-A0
        # NET "DDR2A1"     LOC = "J6"; # Bank = 3, Pin name = IO_L47N_M3A1,         Sch name = DDR-A1
        # NET "DDR2A2"     LOC = "H5"; # Bank = 3, Pin name = IO_L49N_M3A2,         Sch name = DDR-A2
        # NET "DDR2A3"     LOC = "L7"; # Bank = 3, Pin name = IO_L45P_M3A3,         Sch name = DDR-A3
        # NET "DDR2A4"     LOC = "F3"; # Bank = 3, Pin name = IO_L51N_M3A4,         Sch name = DDR-A4
        # NET "DDR2A5"     LOC = "H4"; # Bank = 3, Pin name = IO_L44P_GCLK21_M3A5,  Sch name = DDR-A5
        # NET "DDR2A6"     LOC = "H3"; # Bank = 3, Pin name = IO_L44N_GCLK20_M3A6,  Sch name = DDR-A6
        # NET "DDR2A7"     LOC = "H6"; # Bank = 3, Pin name = IO_L49P_M3A7,         Sch name = DDR-A7
        # NET "DDR2A8"     LOC = "D2"; # Bank = 3, Pin name = IO_L52P_M3A8,         Sch name = DDR-A8
        # NET "DDR2A9"     LOC = "D1"; # Bank = 3, Pin name = IO_L52N_M3A9,         Sch name = DDR-A9
        # NET "DDR2A10"    LOC = "F4"; # Bank = 3, Pin name = IO_L51P_M3A10,        Sch name = DDR-A10
        # NET "DDR2A11"    LOC = "D3"; # Bank = 3, Pin name = IO_L54N_M3A11,        Sch name = DDR-A11
        # NET "DDR2A12"    LOC = "G6"; # Bank = 3, Pin name = IO_L53N_M3A12,        Sch name = DDR-A12
        #Subsignal("a", Pins("J7 J6 H5 L7 F3 H4 H3 H6 D2 D1 F4 D3 G6"), IOStandard("SSTL18_II")),
        
        #NET "DDR2B_A[12]" LOC = D1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[11]" LOC = C1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[10]" LOC = G4 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[9]" LOC = E1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[8]" LOC = E3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[7]" LOC = H6 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[6]" LOC = J4 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[5]" LOC = K3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[4]" LOC = F3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[3]" LOC = K6 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[2]" LOC = H5 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[1]" LOC = H1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_A[0]" LOC = H2 | IOSTANDARD = LVCMOS18;
        Subsignal("a", Pins("H2 H1 H5 K6 F3 K3 J4 H6 E3 E1 G4 C1 D1"), IOStandard("SSTL18_II")),

        # NET "DDR2DQ0"    LOC = "L2"; # Bank = 3, Pin name = IO_L37P_M3DQ0,        Sch name = DDR-DQ0
        # NET "DDR2DQ1"    LOC = "L1"; # Bank = 3, Pin name = IO_L37N_M3DQ1,        Sch name = DDR-DQ1
        # NET "DDR2DQ2"    LOC = "K2"; # Bank = 3, Pin name = IO_L38P_M3DQ2,        Sch name = DDR-DQ2
        # NET "DDR2DQ3"    LOC = "K1"; # Bank = 3, Pin name = IO_L38N_M3DQ3,        Sch name = DDR-DQ3
        # NET "DDR2DQ4"    LOC = "H2"; # Bank = 3, Pin name = IO_L41P_GCLK27_M3DQ4, Sch name = DDR-DQ4
        # NET "DDR2DQ5"    LOC = "H1"; # Bank = 3, Pin name = IO_L41N_GCLK26_M3DQ5, Sch name = DDR-DQ5
        # NET "DDR2DQ6"    LOC = "J3"; # Bank = 3, Pin name = IO_L40P_M3DQ6,        Sch name = DDR-DQ6
        # NET "DDR2DQ7"    LOC = "J1"; # Bank = 3, Pin name = IO_L40N_M3DQ7,        Sch name = DDR-DQ7
        # NET "DDR2DQ8"    LOC = "M3"; # Bank = 3, Pin name = IO_L36P_M3DQ8,        Sch name = DDR-DQ8
        # NET "DDR2DQ9"    LOC = "M1"; # Bank = 3, Pin name = IO_L36N_M3DQ9,        Sch name = DDR-DQ9
        # NET "DDR2DQ10"   LOC = "N2"; # Bank = 3, Pin name = IO_L35P_M3DQ10,       Sch name = DDR-DQ10
        # NET "DDR2DQ11"   LOC = "N1"; # Bank = 3, Pin name = IO_L35N_M3DQ11,       Sch name = DDR-DQ11
        # NET "DDR2DQ12"   LOC = "T2"; # Bank = 3, Pin name = IO_L33P_M3DQ12,       Sch name = DDR-DQ12
        # NET "DDR2DQ13"   LOC = "T1"; # Bank = 3, Pin name = IO_L33N_M3DQ13,       Sch name = DDR-DQ13
        # NET "DDR2DQ14"   LOC = "U2"; # Bank = 3, Pin name = IO_L32P_M3DQ14,       Sch name = DDR-DQ14
        # NET "DDR2DQ15"   LOC = "U1"; # Bank = 3, Pin name = IO_L32N_M3DQ15,       Sch name = DDR-DQ15
        #Subsignal("dq", Pins(
        #            "L2 L1 K2 K1 H2 H1 J3 J1",
        #            "M3 M1 N2 N1 T2 T1 U2 U1"), IOStandard("SSTL18_II")),
        #NET "DDR2B_D[15]" LOC = V1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[14]" LOC = V2 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[13]" LOC = U1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[12]" LOC = U3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[11]" LOC = R1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[10]" LOC = R3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[9]" LOC = P1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[8]" LOC = P2 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[7]" LOC = K1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[6]" LOC = K2 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[5]" LOC = J1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[4]" LOC = J3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[3]" LOC = M1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[2]" LOC = M2 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[1]" LOC = N1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_D[0]" LOC = N3 | IOSTANDARD = LVCMOS18;
        
        Subsignal("dq", Pins(
                    "N3 N1 M2 M1 J3 J1 K2 K1",
                    "P2 P1 R3 R1 U3 U1 V2 V1"), IOStandard("SSTL18_II")),
        # U == Upper, L == Lower
        # NET "DDR2UDQS"   LOC="P2"; # Bank = 3, Pin name = IO_L34P_M3UDQS,         Sch name = DDR-UDQS_P
        # NET "DDR2UDQSN"  LOC="P1"; # Bank = 3, Pin name = IO_L34N_M3UDQSN,        Sch name = DDR-UDQS_N
        # NET "DDR2LDQS"   LOC="L4"; # Bank = 3, Pin name = IO_L39P_M3LDQS,         Sch name = DDR-LDQS_P
        # NET "DDR2LDQSN"  LOC="L3"; # Bank = 3, Pin name = IO_L39N_M3LDQSN,        Sch name = DDR-LDQS_N
        #Subsignal("dqs", Pins("P2 L4"), IOStandard("DIFF_SSTL18_II")),
        #Subsignal("dqs_n", Pins("P1 L3"), IOStandard("DIFF_SSTL18_II")),
        
        #NET "DDR2B_LDQS_P" LOC = L3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_LDQS_N" LOC = L1 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_UDQS_P" LOC = T2 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_UDQS_N" LOC = T1 | IOSTANDARD = LVCMOS18;
        Subsignal("dqs", Pins("T2 L3"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("T1 L1"), IOStandard("DIFF_SSTL18_II")),
        
        #Subsignal("clk_p", Pins("H4"), IOStandard("DIFF_SSTL18_II")),
        #Subsignal("clk_n", Pins("H3"), IOStandard("DIFF_SSTL18_II")),
        
        # NET "DDR2UDM"    LOC="K4"; # Bank = 3, Pin name = IO_L42P_GCLK25_TRDY2_M3UDM, Sch name = DDR-UDM
        # NET "DDR2LDM"    LOC="K3"; # Bank = 3, Pin name = IO_L42N_GCLK24_M3LDM,   Sch name = DDR-LDM
        #Subsignal("dm", Pins("K4 K3"), IOStandard("SSTL18_II")),
        #NET "DDR2B_UDM" LOC = M3 | IOSTANDARD = LVCMOS18;
        #NET "DDR2B_LDM" LOC = L4 | IOSTANDARD = LVCMOS18;
        Subsignal("dm", Pins("M3 L4"), IOStandard("SSTL18_II")),

        # NET "DDR2ODT"    LOC="K6"; # Bank = 3, Pin name = IO_L45N_M3ODT,          Sch name = DDR-ODT
        #Subsignal("odt", Pins("K6"), IOStandard("SSTL18_II"))
        #NET "DDR2B_ODT" LOC = J6 | IOSTANDARD = LVCMOS18;
        Subsignal("odt", Pins("J6"), IOStandard("SSTL18_II"))
    ),

# Pano Button LED Output, Active High
#NET "led_red"               LOC = E12 | IOSTANDARD = LVCMOS33;
#NET "led_blue"              LOC = H13 | IOSTANDARD = LVCMOS33;
#NET "led_green"             LOC = F13 | IOSTANDARD = LVCMOS33;

# Pano Button Input, Active Low
#NET "pano_button"           LOC = H12 | IOSTANDARD = LVCMOS33;

    # Despite being marked as "sw" these are actually buttons which need
    # debouncing.
    # sw1 (user_btn:0) through sw6 (user_btn:5)
    ("user_btn", 0, Pins("H12"), IOStandard("LVCMOS33"), Misc("PULLUP")),


    # LEDs 1 through 8
    ("user_led", 0, Pins("E12"), IOStandard("LVCMOS33"), Drive(8)),
    ("user_led", 1, Pins("H13"), IOStandard("LVCMOS33"), Drive(8)),
    ("user_led", 2, Pins("F13"), IOStandard("LVCMOS33"), Drive(8)),


    #("audio", 0,
    #    Subsignal("channel1", Pins("B16"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")),
    #    Subsignal("channel2", Pins("A16"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST"))),

    #("vga_out", 0,
    #    Subsignal("hsync_n", Pins("B12"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")),
    #    Subsignal("vsync_n", Pins("A12"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")),
    #    Subsignal("r", Pins("A9 B9 C9"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")),
    #    Subsignal("g", Pins("C10 A10 C11"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")),
    #    Subsignal("b", Pins("B11 A11"), IOStandard("LVCMOS33"),
    #              Misc("SLEW=FAST")))
]

_connectors = [
]

class Platform(XilinxPlatform):
    name = "mimasv2"
    default_clk_name = "clk125"
    default_clk_period = 8

    # The MimasV2 has a XC6SLX9 which bitstream takes up ~2.6Mbit (1484472 bytes)
    # 0x80000 offset (4Mbit) gives plenty of space
    gateware_size = 0x80000

    # M25P16 - component U1
    # 16Mb - 75 MHz clock frequency
    # FIXME: Create a "spi flash module" object in the same way we have SDRAM
    # module objects.
    #	/*             name,  erase_cmd, chip_erase_cmd, device_id, pagesize, sectorsize, size_in_bytes */
    #	FLASH_ID("st m25p16",      0xd8,           0xc7, 0x00152020,   0x100,    0x10000,      0x200000),
    spiflash_model = "m25p128"
    spiflash_read_dummy_bits = 8
    spiflash_clock_div = 8
    spiflash_total_size = int((128/8)*1024*1024) # 128Mbit
    spiflash_page_size = 256
    #spiflash_sector_size = 0x10000
    spiflash_sector_size = 0x40000

    def __init__(self):
        #XC6SLX150 FGG484 speed grade 2
        XilinxPlatform.__init__(self, "xc6slx150-fgg484-2", _io, _connectors)

    def create_programmer(self):
        raise NotImplementedError
