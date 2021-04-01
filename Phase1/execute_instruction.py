from five_stage_execution import *
from instruction_encoding import *
from execute_instruction import *



#Function to identify the type of instruction
def identify_instruction_and_run(instruction_dict,PC) :

	opc_code = instruction_dict['opc_code']
	funct3 = instruction_dict['funct3']
	funct7 = instruction_dict['funct7']

	if opc_code == '0110011' :
		if funct3 == '000' and funct7 == '0000000' :
			PC, branch = run_add(instruction_dict,PC)
			return PC, branch



# Functions to directly run the Instruction

# R Type
def run_add(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'addition')

	write_back(rd,output)

	return PC, False



# R Type
def run_and(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'and_bitwise')

	write_back(rd,output)

	return PC, False



# R Type
def run_or(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'or_bitwise')

	write_back(rd,output)

	return PC, False
 


# R Type
def run_sll(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_left_logical')

	write_back(rd,output)

	return PC, False 


# R Type
def run_slt(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_less than')

	if output == True :
		output = '0x00000001'
	else :
		output = '0x00000000'

	write_back(rd,output)

	return PC, False


# R Type
def run_sra(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_right_arithmetic')

	write_back(rd,output)

	return PC, False



# R Type
def run_srl(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_right_logical')

	write_back(rd,output)

	return PC, False
	


# R Type
def run_sub(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'subtract')

	write_back(rd,output)

	return PC, False


# R Type
def run_xor(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'xor_bitwise')

	write_back(rd,output)

	return PC, False


# R Type
def run_mul(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'multiply')

	write_back(rd,output)
	
	return PC, False


# R Type
def run_div(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'divide')

	write_back(rd,output)

	return PC, False


# R Type
def run_rem(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'remainder')

	write_back(rd,output)

	return PC, False


# I Type
def run_addi(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	write_back(rd,output)

	return PC, False 


# I Type
def run_andi(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'and_bitwise')

	write_back(rd,output)

	return PC, False  


# I Type
def run_ori(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'or_bitwise')

	write_back(rd,output)

	return PC, False  


# I Type
def run_lw(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	MDR = memory_access(output,None,4)

	write_back(rd,MDR)

	return PC, False   


# I Type
def run_lh(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	MDR = memory_access(output,None,2)

	write_back(rd,MDR)

	return PC, False


# I Type
def run_lb(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	MDR = memory_access(output,None,1)

	write_back(rd,MDR)

	return PC, False 


# I Type
def run_jalr(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	val_imm = hex(int(instruction_dict['imm'],2))

	rd = int(instruction_dict['rd'],2)

	new_PC = execute(val_rs1, val_imm, 32, 12, 'addition')

	PC = iag(PC, None, None, 1, 0)

	write_back(rd,PC)
		
	return new_PC, True 


# S Type
def run_sw(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	none_value = memory_access(output,val_rs2,4)

	return PC, False


# S Type
def run_sh(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	none_value = memory_access(output,val_rs2,2)

	return PC, False


# S Type
def run_sb(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_imm, 32, 12, 'addition')

	none_value = memory_access(output,val_rs2,1)

	return PC, False 


# SB Type
def run_beq(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_equal')

	if output == True :
		PC = execute(PC, val_imm, 32, 12, 'addition')
		return PC, True

	return PC, False



# SB Type
def run_bne(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_equal')

	if output == False :
		PC = execute(PC, val_imm, 32, 12, 'addition')
		return PC, True

	return PC, False 


# SB Type
def run_bge(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_greater_than_equal_to')

	if output == True :
		PC = execute(PC, val_imm, 32, 12, 'addition')
		return PC, True

	return PC, False 


# SB Type
def run_blt(instruction_dict,PC) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_less_than')

	if output == True :
		PC = execute(PC, val_imm, 32, 12, 'addition')
		return PC, True

	return PC, False 


# UJ Type
def run_jal(instruction_dict,PC) :

	rd = int(instruction_dict['rd'],2)

	val_imm = hex(int(instruction_dict['imm'],2))

	new_PC = execute(PC, val_imm, 32, 20, 'addition')

	PC = iag(PC, None, None, 1, 0)

	write_back(rd,PC)
		
	return new_PC, True


# U Type
def run_auipc(instruction_dict,PC) :

	rd = int(instruction_dict['rd'],2)

	val_imm = hex(int(instruction_dict['imm'],2))

	output = execute(PC, val_imm, 32, 20, 'addition')

	write_back(rd,output)
		
	return PC, False


# U Type
def run_lui(instruction_dict,PC) :

	rd = int(instruction_dict['rd'],2)

	val_imm = hex(int(instruction_dict['imm'],2))

	write_back(rd,val_imm)
		
	return PC, False 









