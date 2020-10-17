class MMU {
    ram = [];
    constructor(ram) {
        this.ram = ram;
    }

    readByte(addr) {
        return this.ram[addr] || 0;
    }

    writeByte(addr, val) {
        this.ram[addr] = val & 0xff;
    }
}

class Regs {
    regs = [0, 0, 0, 0, 0, 0, 0, 0];

    readReg(idx) {
        if(idx < 0 || idx > 7) {
            throw "invalid register index";
        }
        return this.regs[idx];
    }

    writeReg(idx, val) {
        if(idx < 0 || idx > 7) {
            throw "invalid register index";
        }
        this.regs[idx] = val & 0xffff;
    }
}

class CPU {
    regs = new Regs();

    get ip() {
        return this.regs.readReg(7);
    }
    set ip(newIp){
        this.regs.writeReg(7, newIp);
    }

    constructor(mmu) {
        this.mmu = mmu;
    }
    
    evalInstr() {
        switch(this.mmu.readByte(this.ip)){
        case 0x00:
            this.ip++;
            break;
        case 0x01: { //load immediate word
            const regIdx = this.mmu.readByte(this.ip + 1);
            const val = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            this.regs.writeReg(regIdx, val);
            this.ip += 4;
            break;
        }
        case 0x02: { //add word
            const regIdx = this.mmu.readByte(this.ip + 1);
            const val = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            this.regs.writeReg(regIdx, val + this.regs.readReg(regIdx));
            this.ip += 4;
            break;
        }
        case 0x03: { //sub word
            const regIdx = this.mmu.readByte(this.ip + 1);
            const val = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            this.regs.writeReg(regIdx, val - this.regs.readReg(regIdx));
            this.ip += 4;
            break;
        }
        case 0x04: {//mult word
            const regIdx = this.mmu.readByte(this.ip + 1);
            const val = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            this.regs.writeReg(regIdx, val * this.regs.readReg(regIdx));
            this.ip += 4;
            break;
        }
        case 0x05: {//mod word
            const regIdx = this.mmu.readByte(this.ip + 1);
            const val = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            this.regs.writeReg(regIdx, val % this.regs.readReg(regIdx));
            this.ip += 4;
            break;
        }
        case 0x06: {//write word at imm addr
            const regIdx = this.mmu.readByte(this.ip + 1);
            const addr = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            const regVal = this.regs.readReg(redIdx);
            this.mmu.writeByte(addr, regVal & 0xff);
            this.mmu.writeByte(addr, (regVal >> 8) & 0xff);
            this.ip += 4;
            break;
        }
        case 0x07: {//read word at imm addr
            const regIdx = this.mmu.readByte(this.ip + 1);
            const addr = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8); 
            const memVal = this.mmu.readByte(addr) | (this.mmu.readByte(addr + 1) << 8); 
            this.regs.readReg(memVal);
            this.ip += 4;
            break;
        }
        case 0x08: {//unconditional branch
            const offset = this.mmu.readByte(this.ip + 1) | (this.mmu.readByte(this.ip + 2)) << 8;
            this.ip += offset;
            this.ip += 3;
            break;
        }
        case 0x09: {//b.eq imm
            const regIdx = this.mmu.readByte(this.ip + 1);
            const offset = this.mmu.readByte(this.ip + 2) | (this.mmu.readByte(this.ip + 3) << 8);
            const val = this.mmu.readByte(this.ip + 4) | (this.mmu.readByte(this.ip + 5) << 8);
            if(this.regs.readReg(regIdx) == val) {
                this.ip += offset;
            }
            this.ip += 6;
            break;
        }
        case 0x0a: {//mov
            const destIdx = this.mmu.readByte(this.ip + 1);
            const srcIdx = this.mmu.readByte(this.ip + 2);
            this.regs.writeReg(destIdx, this.regs.readReg(srcIdx));
            this.ip += 3;
            break;
        }
        case 0x0b: {//read from reg addr
            const destIdx = this.mmu.readByte(this.ip + 1);
            const srcIdx = this.mmu.readByte(this.ip + 2);
            const srcAddr = this.regs.readReg(srcIdx);
            this.regs.writeReg(destIdx, this.mmu.readByte(srcAddr) | (this.mmu.readByte(srcAddr + 1) << 8));
            this.ip += 3;
            break;
        }
        case 0x0c: {//write word from reg to memory
            const destIdx = this.mmu.readByte(this.ip + 1);
            const srcIdx = this.mmu.readByte(this.ip + 2);
            const srcVal = this.regs.readReg(srcIdx);
            const destAddr = this.regs.readReg(destIdx);
            this.mmu.writeByte(destAddr, srcVal & 0xff);
            this.mmu.writeByte(destAddr + 1, (srcVal >> 8) & 0xff);
            this.ip += 3;
            break;
        }
        case 0x0d: {//b.eq regs
            const aIdx = this.mmu.readByte(this.ip + 1);
            const bIdx = this.mmu.readByte(this.ip + 2);
            const offset = this.mmu.readByte(this.ip + 3) | (this.mmu.readByte(this.ip + 4) << 8);
            if(this.regs.readReg(aIdx) === this.regs.readReg(bIdx)) {
                this.ip += offset;
            }
            this.ip += 5;
            break;
        }
        default:
            throw "invalid opcode: " + this.mmu.readByte(this.ip).toString(16);
        }
    }
}

